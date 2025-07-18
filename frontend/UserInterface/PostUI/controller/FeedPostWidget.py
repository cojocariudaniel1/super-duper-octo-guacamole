import logging

from PySide6.QtWidgets import QFrame, QSizePolicy
from PySide6.QtCore import Signal, Qt, QSize
from PySide6.QtGui import QTextOption

from frontend.UserInterface.PostUI.UserInterfaceFile.FeedPostWidget import Ui_FeedPostWidget


import image_utils
from image_config import ImageType
from backend.Repository.PostRepository import PostRepository
from backend.database_connect import Neo4jDriverSingleton


class FeedPostWidget(QFrame):
    post_clicked = Signal(str)
    like_clicked = Signal(str)
    comment_clicked = Signal(str)
    reply_clicked = Signal(str)

    def __init__(self, post_data, user_id, parent=None):
        super().__init__(parent)
        self.ui = Ui_FeedPostWidget()
        self.ui.setupUi(self)
        self.user_id = user_id
        self.driver = Neo4jDriverSingleton.get_driver()
        self.post_repo = PostRepository(self.driver)
        self.post_data = post_data
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self._initialize_post_data(post_data)
        self._setup_ui_styles()
        self._connect_signals()
        self._setup_images(post_data)

    def _setup_images(self, post_data):
        """Configure all images in the post widget"""
        # User avatar
        image_utils.set_configured_image(
            item=self.ui.userAvatar,
            image_name=post_data.get("author_avatar", "default_user.png"),
            image_type=ImageType.POST_AVATAR,
            item_type="label"
        )

        # Community icon if available

        if "community_icon" in post_data:
            image_utils.set_configured_image(
                item=self.ui.communityIcon,
                image_name=post_data["community_icon"],
                image_type=ImageType.COMMUNITY_AVATAR_MINI,
            item_type="label"
            )
        else:
            image_utils.set_configured_image(
                item=self.ui.communityIcon,
                image_name="communityIcon1.png",
                image_type=ImageType.COMMUNITY_AVATAR_MINI,
                item_type="label"
            )

        # Button icons
        image_utils.set_configured_image(
            item=self.ui.likeButtonIcon,
            image_name="like_icon.png",
            image_type=ImageType.BUTTON_ICON,
            item_type="button"
        )

        image_utils.set_configured_image(
            item=self.ui.commentButtonIcon,
            image_name="comment_icon.png",
            image_type=ImageType.BUTTON_ICON,
            item_type="button"
        )

        # Status indicator if needed
        image_utils.set_configured_image(
            item=self.ui.replyCommentButtonIcon,
            image_name="replyButtonIcon.png",
            image_type=ImageType.BUTTON_ICON,
            item_type="button"
        )



    def _setup_ui_styles(self):
        """Configure UI styling and behavior"""
        for browser in [self.ui.textBrowserContent]:
            browser.setWordWrapMode(QTextOption.WrapMode.WordWrap)
            browser.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            browser.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            browser.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            browser.setMinimumHeight(browser.height() + 20)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)


    def _initialize_post_data(self, post_data):
        """Initialize widget with post data"""
        self.post_id = post_data["id"]
        self.title = post_data["title"]
        self.content = post_data["content"]
        self.author = post_data["author_name"]
        self.timestamp = post_data["timestamp"]

        likes = post_data.get("likes", 0)
        dislikes = post_data.get("dislikes", 0)
        self.points = likes - dislikes

        community = post_data.get("community_name", "")
        self.tags = f"#{community.replace(' ', '')}" if community else ""

        self.ui.communityName.setText(community if community else "General")
        self.ui.postTime.setText(self._format_timestamp(self.timestamp))
        self.ui.username.setText(self.author)
        self.ui.usernamePoints.setText(f"{self.points} points")
        self.ui.postTitle.setText(self.title)
        self.ui.textBrowserContent.setHtml(self.content)

        if "likes" in post_data:
            self.ui.likeCount.setText(str(post_data["likes"]))
        if "comments" in post_data:
            self.ui.commentCount.setText(str(post_data["comments"]))

    def _formatTags(self, tags):
        tags_string = ""
        if len(tags) > 0:
            for tag in tags:
                tags_string += tag
        else:
            tags_string = "No tags"

        return tags_string

    def _format_timestamp(self, timestamp):
        """Format timestamp to relative time"""
        # Implement your timestamp formatting logic here
        return timestamp  # Return formatted string

    def _connect_signals(self):
        """Connect all widget signals"""
        self.ui.likeButtonIcon.clicked.connect(self._on_like_clicked)
        self.ui.commentButtonIcon.clicked.connect(self._on_comment_clicked)

    def _on_post_clicked(self):
        """Handle post click event"""
        logging.critical("_on_post_clicked")
        self.post_clicked.emit(self.post_id)

    def _on_like_clicked(self):
        try:
            print(self.user_id)
            user_id = self.user_id
            new_points = self.post_repo.increment_post_points(
                post_id=self.post_id,
                increment=1,
                is_like=True,
                user_id=user_id
            )
            self.update_points(new_points)
        except Exception as e:
            logging.error(f"Failed to like post {self.post_id}: {str(e)}")

    def _on_comment_clicked(self):
        """Handle comment button click"""
        self.comment_clicked.emit(self.post_id)

    def update_points(self, points):
        """Update the points display for this post"""
        self.points = points
        self.ui.usernamePoints.setText(f"{points} points")
        self.ui.likeCount.setText(str(points))

    def mouseDoubleClickEvent(self, event):
        """Emit post_clicked signal on double click"""

        if event.button() == Qt.MouseButton.LeftButton:
            self._on_post_clicked()
        super().mouseDoubleClickEvent(event)

    def update_comments_count(self, count):
        """Update the comments count display"""
        self.ui.commentCount.setText(str(count))

    def sizeHint(self):
        """Provide a size hint based on content"""
        # Calculate the height based on content
        height = (
                self.ui.headerLayout.sizeHint().height() +
                self.ui.authorLayout.sizeHint().height() +
                self.ui.postTitle.sizeHint().height() +
                self.ui.textBrowserContent.document().size().height() +
                self.ui.footerLayout.sizeHint().height() +
                40  # Additional padding
        )
        return QSize(super().sizeHint().width(), height)