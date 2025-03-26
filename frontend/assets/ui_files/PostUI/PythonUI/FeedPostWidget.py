import os
from PySide6.QtWidgets import QFrame, QSizePolicy
from PySide6.QtCore import Signal, Qt, QSize
from PySide6.QtGui import QTextOption, QPixmap, QIcon

from frontend.assets.ui_files.PostUI.UserInterfaceFile.FeedPostWidget import Ui_FeedPostWidget


class FeedPostWidget(QFrame):
    post_clicked = Signal(str)  # Emits post ID
    like_clicked = Signal(str)  # Emits post ID
    comment_clicked = Signal(str)  # Emits post ID
    reply_clicked = Signal(str)  # Emits post ID

    def __init__(self, post_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_FeedPostWidget()
        self.ui.setupUi(self)

        # Set size constraints - fixed width, flexible height
        self.setMinimumSize(QSize(1167, 0))  # Minimum width 1167px, height can vary
        self.setMaximumSize(QSize(1167, 16777215))  # Max width 1167px, flexible height
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)

        # Configure widget properties
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        # Initialize with post data
        self._initialize_post_data(post_data)
        self._setup_ui_styles()
        self._connect_signals()

    def _setup_ui_styles(self):
        """Configure UI styling and behavior"""
        # Configure text browsers
        for browser in [self.ui.textBrowserContent, self.ui.tagsBrowser, self.ui.commentContent]:
            browser.setWordWrapMode(QTextOption.WrapMode.WordWrap)
            browser.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            browser.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            browser.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)

        # Adjust content text browser dimensions
        self.ui.textBrowserContent.setMinimumSize(150, 0)  # Minimum width 150px, flexible height
        self.ui.textBrowserContent.setMaximumSize(700, 16777215)  # Max width 700px, flexible height

        # Make buttons transparent
        for button in [self.ui.likeButton, self.ui.commentButton]:
            button.setStyleSheet("background: transparent; border: none;")

    def _initialize_post_data(self, post_data):
        """Initialize widget with post data"""
        self.post_id = post_data["id"]
        self.title = post_data["title"]
        self.content = post_data["content"]
        self.author = post_data["author_name"]
        self.timestamp = post_data["timestamp"]

        # Calculate points (likes - dislikes)
        likes = post_data.get("likes", 0)
        dislikes = post_data.get("dislikes", 0)
        self.points = likes - dislikes

        # Format community tags
        community = post_data.get("community_name", "")
        self.tags = f"#{community.replace(' ', '')}" if community else ""

        # Set UI elements
        self.ui.communityName.setText(community if community else "General")
        self.ui.postTime.setText(self._format_timestamp(self.timestamp))
        self.ui.username.setText(self.author)
        self.ui.usernamePoints.setText(f"{self.points} points")
        self.ui.postTitle.setText(self.title)

        # Check if content has images
        has_images = '<img' in self.content.lower()

        # Set content with HTML formatting
        content_style = """
            <style>
                img {
                    max-width: 100%;
                    height: auto;
                }
                div.content {
                    font-family: Raleway; 
                    font-weight: 500; 
                    font-size: 14px; 
                    line-height: 16px; 
                    color: #1A1A1B;
                }
            </style>
        """
        self.ui.textBrowserContent.setHtml(f"""
            {content_style}
            <div class="content">
                {self.content}
            </div>
        """)

        # Adjust size based on content
        if has_images:
            self.ui.textBrowserContent.setMinimumSize(700, 0)  # Wider for images
        else:
            self.ui.textBrowserContent.setMinimumSize(150, 0)  # Narrower for text-only

        # Set tags with HTML formatting
        self.ui.tagsBrowser.setHtml(f"""
            <div style='font-family: Raleway; font-weight: 500; font-size: 10px; line-height: 12px; color: rgba(85, 85, 85, 0.7);'>
                {self.tags}
            </div>
        """)

        # Set counts if available
        if "likes" in post_data:
            self.ui.likeCount.setText(str(post_data["likes"]))
        if "comments" in post_data:
            self.ui.commentCount.setText(str(post_data["comments"]))

        # Adjust widget height based on content
        self.adjustSize()

    def _format_timestamp(self, timestamp):
        """Format timestamp to relative time"""
        # Implement your timestamp formatting logic here
        return timestamp  # Return formatted string

    def _connect_signals(self):
        """Connect all widget signals"""
        self.ui.likeButton.clicked.connect(self._on_like_clicked)
        self.ui.commentButton.clicked.connect(self._on_comment_clicked)
        # self.doubleClicked.connect(self._on_post_clicked)

    def _on_post_clicked(self):
        """Handle post click event"""
        self.post_clicked.emit(self.post_id)

    def _on_like_clicked(self):
        """Handle like button click"""
        self.like_clicked.emit(self.post_id)

    def _on_comment_clicked(self):
        """Handle comment button click"""
        self.comment_clicked.emit(self.post_id)

    def update_points(self, points):
        """Update the points display for this post"""
        self.points = points
        self.ui.usernamePoints.setText(f"{points} points")
        self.ui.likeCount.setText(str(points))

    def update_comments_count(self, count):
        """Update the comments count display"""
        self.ui.commentCount.setText(str(count))

    def sizeHint(self):
        """Provide a size hint based on content"""
        # Calculate required height based on content
        doc = self.ui.textBrowserContent.document()
        content_height = doc.size().height()

        # Add heights of other fixed elements
        fixed_elements_height = 150  # Approximate height of header, title, footer

        return QSize(1167, content_height + fixed_elements_height)