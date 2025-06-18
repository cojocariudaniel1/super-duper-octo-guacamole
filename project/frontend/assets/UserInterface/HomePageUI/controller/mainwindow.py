import logging

from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from frontend.assets.UserInterface.HomePageUI.controller.dashboardWIndow import DashboardWindow
from frontend.assets.UserInterface.PostUI.PythonUI.DetaliedPostWidget import DetailedPostWidget
from neo4j_data.Repository.PostRepository import PostRepository
from neo4j_data.Repository.SessionRepository import SessionRepository
from neo4j_data.database_connect import Neo4jDriverSingleton


class MainWindow(QWidget):
    def __init__(self, user_id, session_id=None):
        super().__init__()
        self.user_id = user_id
        self.session_id = session_id
        self.interacted_posts = []
        self.setObjectName("mainWindow")
        # Create the main stacked widget
        self.stack = QStackedWidget(self)
        self.setStyleSheet("#mainWindow { background-color: #1A1A1B; }")
        self.setGeometry(100,100, 1440,1024)
        self.dashboard = DashboardWindow(self.user_id)
        print(f"Dashboard signal exists: {hasattr(self.dashboard, 'dashboard_post_clicked')}")

        # Connect the signal with debugging
        self.dashboard.dashboard_post_clicked.connect(lambda post_id: self.handle_post_click(post_id))
        self.dashboard.handle_like = self.handle_like

        self.stack.addWidget(self.dashboard)
        self.stack.setStyleSheet("background-color: #1A1A1B")

        # Create detailed post view (initially empty)
        self.detailed_post = DetailedPostWidget()
        self.stack.addWidget(self.detailed_post)

        # Set the main layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)
        layout.setContentsMargins(0, 0, 0, 0)

        self.detailed_post.back_to_feed.connect(self.show_dashboard)

    def handle_post_click(self, post_id):
        """Switch to detailed post view"""
        logging.critical(f"MainWindow received post_click for post_id: {post_id}")
        print(f"Handling post click for {post_id}")

        # Get actual post data from database (you'll need to implement this)
        post_data = self.get_post_data(post_id)  # You need to implement this method
        self.interacted_posts.append({"post_id": post_id, "type": "view", "score": 1})

        if post_data:
            self.detailed_post.set_post(post_data, self.user_id)
            self.stack.setCurrentIndex(1)
            print("View switched to detailed post")
        else:
            print(f"Could not find post with id {post_id}")

    def show_dashboard(self):
        """Switch back to dashboard view"""
        self.stack.setCurrentIndex(0)

    def get_post_data(self, post_id):
        """Fetch post data from database"""
        try:
            driver = Neo4jDriverSingleton.get_driver()
            post_repo = PostRepository(driver)
            return post_repo.get_post_by_post_id(post_id)
        except Exception as e:
            print(f"Error fetching post data: {e}")
            return None

    def handle_like(self, post_id):
        self.interacted_posts.append({"post_id": post_id, "type": "like", "score": 3})


    def closeEvent(self, event):
        """Închide sesiunea la ieșirea din aplicație"""
        if self.session_id:
            try:
                driver = Neo4jDriverSingleton.get_driver()
                with driver.session() as session:
                    for interaction in self.interacted_posts:
                        session.run(
                            """
                            MATCH (u:User {id: $user_id}), (p:Post {id: $post_id})
                            MERGE (u)-[r:INTERACTED_WITH]->(p)
                            ON CREATE SET 
                                r.score = $score,
                                r.timestamp = datetime(),
                                r.view_count = CASE WHEN $type = 'view' THEN 1 ELSE 0 END,
                                r.like_count = CASE WHEN $type = 'like' THEN 1 ELSE 0 END
                            ON MATCH SET
                                r.score = r.score + $score,
                                r.timestamp = datetime(),
                                r.view_count = r.view_count + CASE WHEN $type = 'view' THEN 1 ELSE 0 END,
                                r.like_count = r.like_count + CASE WHEN $type = 'like' THEN 1 ELSE 0 END
                            """,
                            user_id=self.user_id,
                            post_id=interaction["post_id"],
                            type=interaction["type"],
                            score=interaction["score"]
                        )
                        
                session_repo = SessionRepository(Neo4jDriverSingleton.get_driver())
                session_repo.end_session(self.session_id)
                print(f"[INFO] Sesiunea {self.session_id} a fost încheiată.")


            except Exception as e:
                print(f"[ERROR] Nu s-a putut închide sesiunea: {str(e)}")
        event.accept()
