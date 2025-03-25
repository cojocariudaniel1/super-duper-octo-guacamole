import os

from PySide6.QtWidgets import QFrame
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

        # Set fixed size constraints
        self.setFixedSize(1167, 259)
        self.setMinimumSize(1167, 259)
        self.setMaximumSize(1167, 259)

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
        print(f"Tags {self.tags}")
        # Set content with HTML formatting
        self.ui.textBrowserContent.setHtml(f"""
            <div style='font-family: Raleway; font-weight: 500; font-size: 14px; line-height: 16px; color: #1A1A1B;'>
                {self.content}
            </div>
        """)

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