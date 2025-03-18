from PySide6.QtWidgets import QWidget, QFrame
from frontend.assets.ui_files.HomePageUI.UserInterfaceFile.dashboard import Ui_DashBoardView
from frontend.assets.ui_files.PostUI.UserInterfaceFile.mini_post_view import Ui_MiniViewPost
from neo4j_data.database_connect import Neo4jDriverSingleton
from neo4j_data.Repository.PostRepository import PostRepository


class DashboardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DashBoardView()
        self.ui.setupUi(self)
        self.new_window = None

        # Set ScrollArea properties
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

        # Get post layout container
        self.posts_layout = self.ui.postsLayout

        # Initialize the PostRepository
        self.driver = Neo4jDriverSingleton.get_instance()
        self.post_repo = PostRepository(self.driver)

        # Fetch and display posts
        for x in range(1,15):
            self.load_posts()

        # Set max width for side panels
        self.ui.communityList.setMaximumWidth(300)
        self.ui.recentPostsList.setMaximumWidth(300)

    def load_posts(self):
        """Fetch posts from the database and add them to the layout."""
        posts = self.post_repo.get_all_posts()  # Fetch all posts
        for post in posts:
            self.add_post(post["content"], post["author_name"], post["timestamp"])
        print(posts)

    def add_post(self, content, author, timestamp):
        """Adds a new post to the layout."""
        post_widget = MiniPostWidget(content, author, timestamp)  # Create a new post widget
        self.posts_layout.addWidget(post_widget)  # Add it to the layout


class MiniPostWidget(QFrame):
    def __init__(self, content, author, timestamp, parent=None):
        super().__init__(parent)

        # Set up the UI from the generated class
        self.ui = Ui_MiniViewPost()
        self.ui.setupUi(self)

        # Customize the post content
        self.ui.label_2.setText(author)  # Set the author name
        self.ui.label.setText(timestamp)  # Set the timestamp
        self.ui.content_label.setText(content)  # Set the post content

        # Enable word wrapping
        self.ui.content_label.setWordWrap(True)