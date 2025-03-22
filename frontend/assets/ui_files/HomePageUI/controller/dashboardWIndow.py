from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QScrollArea, QPushButton
from PySide6.QtCore import QTimer, Qt, Signal, Slot

# Assuming your CreatePostWidget is defined elsewhere
from frontend.PySide6_GUI.customWidget.LoadingBar import LoadingBar
from frontend.assets.ui_files.HomePageUI.UserInterfaceFile.dashboard import Ui_DashBoardView
from frontend.assets.ui_files.HomePageUI.controller.createPostWidget import CreatePostWidget
from frontend.assets.ui_files.PostUI.PythonUI.DetaliedPostWidget import DetailedPostWidget
from frontend.assets.ui_files.PostUI.PythonUI.minipost_view import MiniPostWidget

from neo4j_data.database_connect import Neo4jDriverSingleton
from neo4j_data.Repository.PostRepository import PostRepository

class DashboardWindow(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.ui = Ui_DashBoardView()
        self.ui.setupUi(self)

        # Initialize database
        self.driver = Neo4jDriverSingleton.get_instance()
        self.post_repo = PostRepository(self.driver)

        # Set ScrollArea properties
        self.setup_scroll_area()

        # Create stacked widget for view switching
        self.stack = QStackedWidget(self)

        # -------------------- FEED CONTAINER --------------------
        self.feed_container = self.create_feed_container()

        # -------------------- DETAILED POST CONTAINER --------------------
        self.post_container = self.create_post_container()

        # -------------------- CREATE POST CONTAINER --------------------
        self.create_post_container = self.create_create_post_container()

        # Connect back button to show feed
        self.post_detail.back_to_feed.connect(self.show_feed)

        # Add containers to stack and set in scroll area
        self.stack.addWidget(self.feed_container)
        self.stack.addWidget(self.post_container)
        self.stack.addWidget(self.create_post_container)  # Add the Create Post container

        self.ui.ContentPosts_ScrollArea.setWidget(self.stack)

        # -------------------- LOADING BAR --------------------
        self.loading_bar = LoadingBar(self)
        self.loading_bar.setGeometry(0, 0, self.width(), 4)
        self.loading_bar.hide()

        # Set max width for side panels
        self.ui.communityList.setMaximumWidth(300)
        self.ui.recentPostsList.setMaximumWidth(300)

        # Variables for pagination
        self.current_offset = 0
        self.posts_per_page = 10

        # Load posts (initial batch)
        self.load_posts()

        # Create a button to show the Create Post page (you can add this button in your dashboard UI)
        self.create_post_button = QPushButton("Create Post")
        self.create_post_button.clicked.connect(self.show_create_post)
        self.ui.topNavLayout.addWidget(self.create_post_button)  # Add button to layout or toolbar

    def setup_scroll_area(self):
        """Set up scroll area properties."""
        self.ui.ContentPosts_ScrollArea.setWidgetResizable(True)
        self.ui.ContentPosts_ScrollArea.setStyleSheet("""
            QScrollBar:vertical {
                background: #2e2e2e;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background: #5a5a5a;
                border-radius: 6px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: #3a3a3a;
            }
        """)

    def create_feed_container(self):
        """Create and return the feed container."""
        feed_container = QWidget()
        feed_layout = QVBoxLayout(feed_container)
        self.posts_layout = QVBoxLayout()
        feed_layout.addLayout(self.posts_layout)
        feed_layout.addStretch(1)
        return feed_container

    def create_post_container(self):
        """Create and return the post detail container."""
        post_container = QWidget()
        post_layout = QVBoxLayout(post_container)
        self.post_detail = DetailedPostWidget(post_container)
        post_layout.addWidget(self.post_detail)
        post_layout.addStretch(1)
        return post_container

    def create_create_post_container(self):
        """Create and return the create post container (from CreatePostWidget)."""
        create_post_container = QWidget()
        create_post_layout = QVBoxLayout(create_post_container)
        self.create_post_widget = CreatePostWidget(self.user_id,self.post_repo)  # Initialize your CreatePostWidget here
        create_post_layout.addWidget(self.create_post_widget)
        create_post_layout.addStretch(1)
        return create_post_container

    def show_create_post(self):
        """Switch to the Create Post view."""
        self.stack.setCurrentIndex(2)  # Switch to Create Post view

    def load_posts(self):
        """Fetch posts from the database and add them to the layout."""
        self.loading_bar.start_loading()
        posts = self.post_repo.get_all_posts(limit=self.posts_per_page, offset=self.current_offset)
        for post in posts:
            self.add_post(post["id"], post["title"], post["content"], post["author_name"], post["timestamp"])

        # Increment the offset for the next batch
        self.current_offset += self.posts_per_page
        self.loading_bar.stop_loading()

    def add_post(self, id, title, content, author, timestamp):
        """Add a new post to the feed layout."""
        if len(content) > 1000:
            minipost_content = content[:1000] + " ..."
        else:
            minipost_content = content
        post_widget = MiniPostWidget(id, title, minipost_content, author, timestamp)
        self.posts_layout.addWidget(post_widget)


    def show_post_detail(self, id, title, content, author, timestamp):
        """Switch to the detailed post view."""
        self.loading_bar.start_loading()
        QTimer.singleShot(2000, self.loading_bar.stop_loading)  # Simulate loading delay

        # Set the post content as HTML (rich text)
        self.post_detail.set_post(id, title, content, author, timestamp)
        self.stack.setCurrentIndex(1)  # Switch to detailed post view

    def show_feed(self):
        """Switch back to the feed view."""
        self.stack.setCurrentIndex(0)
