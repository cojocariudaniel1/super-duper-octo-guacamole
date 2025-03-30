import os

from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QScrollArea, QPushButton
from PySide6.QtCore import QTimer, Qt, Signal, Slot, QThread, QObject

from backend.global_path import get_absolute_file_path
from frontend.PySide6_GUI.customWidget.LoadingBar import LoadingBar
from frontend.assets.ui_files.HomePageUI.UserInterfaceFile.dashboard import Ui_DashBoardView
from frontend.assets.ui_files.HomePageUI.controller.createPostWidget import CreatePostWidget
from frontend.assets.ui_files.PostUI.PythonUI.DetaliedPostWidget import DetailedPostWidget
from frontend.assets.ui_files.PostUI.PythonUI.FeedPostWidget import FeedPostWidget

from neo4j_data.database_connect import Neo4jDriverSingleton
from neo4j_data.Repository.PostRepository import PostRepository


class PostWorker(QObject):
    finished = Signal(list)
    error = Signal(str)

    def __init__(self, repository, user_id=None, community_name=None, limit=10, offset=0):
        super().__init__()
        self.repository = repository
        self.user_id = user_id
        self.community_name = community_name
        self.limit = limit
        self.offset = offset

    @Slot()
    def load_posts(self):
        """Load posts based on current configuration"""
        try:
            if self.user_id:
                posts = self.repository.get_posts_by_user(self.user_id)
            elif self.community_name:
                posts = self.repository.get_posts_by_community(self.community_name)
            else:
                posts = self.repository.get_all_posts(limit=self.limit, offset=self.offset)
            self.finished.emit(posts)
        except Exception as e:
            self.error.emit(str(e))


class DashboardWindow(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.ui = Ui_DashBoardView()
        self.ui.setupUi(self)

        self.set_image(self.ui.logoLabel, "logo.png")
        self.set_button_icon(self.ui.notificationButton, "ButtonNotificationImage.png")
        self.set_button_icon(self.ui.profileButton, "UserSettings.png")
        self.set_button_icon(self.ui.shortcutSettingsButton, "ProfileSettingsShortcut.png")

        # Initialize database
        self.driver = Neo4jDriverSingleton.get_driver()
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
        self.stack.addWidget(self.create_post_container)

        self.ui.ContentPosts_ScrollArea.setWidget(self.stack)

        # -------------------- LOADING BAR --------------------
        self.loading_bar = LoadingBar(self)
        self.loading_bar.setGeometry(0, 0, self.width(), 4)
        self.loading_bar.hide()

        # Variables for pagination
        self.current_offset = 0
        self.posts_per_page = 10

        # Create a button to show the Create Post page
        self.create_post_button = QPushButton("Create Post")
        self.create_post_button.clicked.connect(self.show_create_post)
        self.ui.topNavLayout.addWidget(self.create_post_button)

        # Initialize worker thread
        self.worker_thread = None
        self.initialize_custom_style()
        # Load posts (initial batch)
        self.load_posts()

    def set_button_icon(self, button, icon_name, fallback_size=(32, 32)):
        """
        Sets an icon from the assets folder to a QPushButton

        Args:
            button (QPushButton): The button to set the icon to
            icon_name (str): Name of the icon file in assets/images/
            fallback_size (tuple): Size for fallback blank icon (width, height)
        """
        # Construct the full path
        icon_path = get_absolute_file_path(f"frontend/assets/images/{icon_name}")

        if os.path.exists(icon_path):
            icon = QIcon(icon_path)
            if not icon.isNull():
                button.setIcon(icon)
                return

        # Fallback if icon not found
        print(f"Icon not found: {icon_path}")
        blank_pixmap = QPixmap(fallback_size[0], fallback_size[1])
        button.setIcon(QIcon(blank_pixmap))

    def set_image(self, label, image_name):
        """
        Sets an image from the assets folder to a QLabel

        Args:
            label (QLabel): The label to set the image to
            image_name (str): Name of the image file in assets/images/
        """
        # Construct the full path
        image_path = get_absolute_file_path(f"frontend/assets/images/{image_name}")

        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                label.setPixmap(pixmap)
                return

        # Fallback if image not found
        print(f"Image not found: {image_path}")
        label.setPixmap(QPixmap(label.size()))  # Bla

    def setup_scroll_area(self):
        """Set up scroll area properties."""
        self.ui.ContentPosts_ScrollArea.setWidgetResizable(True)

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
        """Create and return the create post container."""
        create_post_container = QWidget()
        create_post_layout = QVBoxLayout(create_post_container)
        self.create_post_widget = CreatePostWidget(self.user_id, self.post_repo)
        create_post_layout.addWidget(self.create_post_widget)
        create_post_layout.addStretch(1)
        return create_post_container

    def show_create_post(self):
        """Switch to the Create Post view."""
        self.stack.setCurrentIndex(2)

    def load_posts(self):
        """Fetch posts from the database asynchronously."""
        self.loading_bar.start_loading()

        # Clear existing posts (except the first load)
        if self.current_offset == 0:
            while self.posts_layout.count():
                item = self.posts_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

        # Set up the worker thread
        self.worker_thread = QThread()
        self.worker = PostWorker(
            self.post_repo,
            limit=self.posts_per_page,
            offset=self.current_offset
        )
        self.worker.moveToThread(self.worker_thread)

        # Connect signals
        self.worker_thread.started.connect(self.worker.load_posts)
        self.worker.finished.connect(self.on_posts_loaded)
        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.error.connect(self.on_posts_error)
        self.worker.error.connect(self.worker_thread.quit)

        # Clean up thread when done
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)

        # Start the thread
        self.worker_thread.start()

        # Increment the offset for the next batch
        self.current_offset += self.posts_per_page

    def on_posts_loaded(self, posts):
        """Handle successfully loaded posts."""
        for post in posts:
            self.add_post(post)
        self.loading_bar.stop_loading()

    def on_posts_error(self, error_msg):
        """Handle post loading errors."""
        print(f"Error loading posts: {error_msg}")
        self.loading_bar.stop_loading()

    def add_post(self, post_data):
        """Add a new post to the feed layout."""
        post_widget = FeedPostWidget(post_data)
        # Remove any manual size constraints to respect the .ui file settings
        post_widget.post_clicked.connect(lambda post_id: self.show_post_detail(post_id))
        post_widget.like_clicked.connect(self.handle_like)
        post_widget.comment_clicked.connect(self.handle_comment)
        post_widget.reply_clicked.connect(self.handle_reply)

        # Add spacing between posts
        self.posts_layout.addWidget(post_widget)
        # Add delimiter line between posts
        delimiter = QWidget()
        delimiter.setFixedHeight(1)
        delimiter.setStyleSheet("background-color: #3a3a3a;")
        self.posts_layout.addWidget(delimiter)
        self.posts_layout.addSpacing(5)  # Reduced spacing since we have the delimiter

    def show_post_detail(self, post_id):
        """Switch to the detailed post view."""
        self.loading_bar.start_loading()

        # Fetch the full post details here (implementation needed)
        # For now, simulate loading
        QTimer.singleShot(1000, lambda: self.loading_bar.stop_loading())
        self.stack.setCurrentIndex(1)

    def handle_like(self, post_id):
        """Handle like button click."""
        print(f"Like clicked for post {post_id}")
        # Implement like functionality here

    def handle_comment(self, post_id):
        """Handle comment button click."""
        print(f"Comment clicked for post {post_id}")
        # Implement comment functionality here

    def handle_reply(self, post_id):
        """Handle reply button click."""
        print(f"Reply clicked for post {post_id}")
        # Implement reply functionality here

    def show_feed(self):
        """Switch back to the feed view."""
        self.stack.setCurrentIndex(0)

    def initialize_custom_style(self):
        """Apply custom styles with proper isolation"""
        # Base style for the entire application
        base_style = """
            QWidget {
                background: transparent;
                border: none;
            }
        """
        self.setStyleSheet(base_style)

        # Define border style with proper string formatting
        border_style = """
            QWidget#{name} {{
                border: 1px solid #3a3a3a;
                background: transparent;
            }}
        """

        # Apply to main containers
        containers = [
            "leftSideBar",
            "middleBar",
            "topNavBar",
            "ContentPosts_ScrollArea",
            "delimiter1",
            "delimiter2"
        ]

        for container in containers:
            widget = getattr(self.ui, container)
            # Use double braces for literal braces in the format string
            widget.setStyleSheet(border_style.format(name=container))

        # Special case for scroll area to prevent inner widget borders
        self.ui.ContentPosts_ScrollArea.setStyleSheet("""
            QScrollArea#ContentPosts_ScrollArea {
                border-top: 1px solid #3a3a3a;
            }
            QScrollArea#ContentPosts_ScrollArea > QWidget > QWidget {
                border: none;
            }
        """)

        # Post widget styling to prevent inheritance
        post_style = """
            FeedPostWidget {
                background: #2a2a2a;
                border-radius: 4px;
                border: none;
                margin: 5px 0;
            }
        """
        self.setStyleSheet(self.styleSheet() + post_style)
