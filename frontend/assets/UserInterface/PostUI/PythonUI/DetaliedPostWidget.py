from PySide6.QtGui import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QWidget, QSizePolicy
from PySide6.QtCore import Signal

from frontend.assets.UserInterface.HomePageUI.UserInterfaceFile.CommentSectionView import CommentSection
from frontend.assets.UserInterface.PostUI.UserInterfaceFile.DetaliedPostView import Ui_DetailedPostView
from neo4j_data.database_connect import Neo4jDriverSingleton

class DetailedPostWidget(QFrame):
    back_to_feed = Signal()  # Signal to notify parent to switch back to feed

    def __init__(self, parent=None):
        super().__init__(parent)
        # Load the compiled UI structure
        self.ui = Ui_DetailedPostView()
        self.ui.setupUi(self)

        # Initialize additional widgets
        self.initialize_widgets()

        # Placeholder attributes for post content
        self.post_id = None
        self.post_content = None
        self.post_author = None
        self.post_timestamp = None
        self.user_id = None

        # Initialize database
        # self.driver = Neo4jDriverSingleton.get_instance()

    def initialize_widgets(self):
        """Initialize extra components like buttons or sections."""
        # Create back button
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.on_back_button_click)
        self.ui.postLayout.addWidget(self.back_button)

        # Create comment section container
        self.comment_section_container = QWidget()
        # Changed to Expanding for both horizontal and vertical
        self.comment_section_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.comment_layout = QVBoxLayout(self.comment_section_container)
        self.comment_layout.setContentsMargins(0, 0, 0, 0)
        self.comment_layout.setSpacing(0)

        # Add to main layout with stretch
        self.ui.postLayout.addWidget(self.comment_section_container)
        self.ui.postLayout.addStretch()

    def set_post(self, post_id, title, content, author, timestamp, user_id):
        """
        Update the post details dynamically.
        :param post_id: ID of the post
        :param title: Post title
        :param content: Post content (HTML)
        :param author: Author name
        :param timestamp: Timestamp of the post
        :param user_id: Current user's ID
        """
        self.post_id = post_id
        self.post_content = content
        self.post_author = author
        self.post_timestamp = str(timestamp)
        self.user_id = user_id

        # Update the labels with post details
        self.ui.author_label.setText(f"By: {author}")
        self.ui.timestamp_label.setText(self.post_timestamp)
        self.ui.post_title_label.setText(title)
        self.ui.content_label.setText(content)

        # Clear previous comment section if exists
        for i in reversed(range(self.comment_layout.count())):
            self.comment_layout.itemAt(i).widget().setParent(None)

        # Create and add the full comment section
        self.comment_section = CommentSection(post_id, user_id)
        # Changed to Expanding for both horizontal and vertical
        self.comment_section.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.comment_layout.addWidget(self.comment_section)

    def on_back_button_click(self):
        """Emit the back_to_feed signal."""
        self.back_to_feed.emit()