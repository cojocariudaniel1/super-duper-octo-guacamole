import logging

from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from frontend.assets.UserInterface.HomePageUI.controller.dashboardWIndow import DashboardWindow
from frontend.assets.UserInterface.PostUI.PythonUI.DetaliedPostWidget import DetailedPostWidget
from neo4j_data.Repository.PostRepository import PostRepository
from neo4j_data.database_connect import Neo4jDriverSingleton


class MainWindow(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.setObjectName("mainWindow")
        # Create the main stacked widget
        self.stack = QStackedWidget(self)
        self.setStyleSheet("#mainWindow { background-color: #1A1A1B; }")
        self.setGeometry(100,100, 1440,1024)
        self.dashboard = DashboardWindow(self.user_id)
        print(f"Dashboard signal exists: {hasattr(self.dashboard, 'dashboard_post_clicked')}")

        # Connect the signal with debugging
        self.dashboard.dashboard_post_clicked.connect(lambda post_id: self.handle_post_click(post_id))

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