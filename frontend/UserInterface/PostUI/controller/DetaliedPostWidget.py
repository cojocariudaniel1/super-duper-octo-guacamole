import os

from backend.Repository.UserRepository import get_friends_with_status
from frontend.UserInterface.HomePageUI.UserInterfaceFile.CommentSectionView import CommentSection
from frontend.assets.customWidget.CommentCW import CommentWidget
from frontend.assets.customWidget.communitiesWidgetCW import CommunityWidget

from PySide6.QtGui import Qt, QPixmap, QIcon
from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QWidget, QSizePolicy
from PySide6.QtCore import Signal
from frontend.UserInterface.PostUI.controller.FeedPostWidget import FeedPostWidget
from frontend.UserInterface.PostUI.UserInterfaceFile.DetaliedPostView import Ui_DetaliedPostView
from backend.Repository.CommunityRepository import CommunityRepository
from backend.database_connect import Neo4jDriverSingleton
from backend.Repository.PostRepository import PostRepository
from backend.Repository.CommentRepository import CommentRepository
import logging
import image_utils
from frontend.assets.customWidget.offlineFriendsCW import OfflineFriendWidget
from frontend.assets.customWidget.onlineFriendsCW import OnlineFriendWidget
from image_config import ImageType
from backend.global_path import get_absolute_file_path

class DetailedPostWidget(QFrame):
    back_to_feed = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DetaliedPostView()
        self.ui.setupUi(self)
        self.user_id = None
        # Initialize database
        self.driver = Neo4jDriverSingleton.get_driver()
        self.post_repo = PostRepository(self.driver)
        self.community_repo = CommunityRepository(self.driver)
        self.comment_repo = CommentRepository(self.driver)

        self.feed_post_widget = None
        self.post_content = None
        self.post_author = None
        self.post_timestamp = None

        self.initialize_widgets()
        self.set_image(self.ui.logoLabel, "logo.png")
        self.set_button_icon(self.ui.notificationButton, "ButtonNotificationImage.png")
        self.set_button_icon(self.ui.profileButton, "UserSettings.png")
        self.set_button_icon(self.ui.shortcutSettingsButton, "ProfileSettingsShortcut.png")


        self.load_communities_acces_link()



    def initialize_widgets(self):
        # Main container for the detailed view
        self.post_container = QWidget()
        self.post_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.post_layout = QVBoxLayout(self.post_container)
        self.post_layout.setContentsMargins(0, 0, 0, 0)
        self.post_layout.setSpacing(10)

        # Back button
        self.back_button = QPushButton("Back to Feed")
        self.back_button.setStyleSheet("""
            QPushButton {
                background-color: #3A3A3A;
                color: white;
                border-radius: 5px;
                padding: 8px;
                font: 12pt "Raleway";
            }
            QPushButton:hover {
                background-color: #4A4A4A;
            }
        """)
        self.back_button.clicked.connect(self.on_back_button_click)
        self.ui.HeaderBar.addWidget(self.back_button, alignment=Qt.AlignmentFlag.AlignLeft)

        # Placeholder for post (FeedPostWidget)
        self.feed_post_container = QWidget()
        self.feed_post_layout = QVBoxLayout(self.feed_post_container)
        self.feed_post_layout.setContentsMargins(0, 0, 0, 0)
        self.feed_post_layout.setSpacing(0)
        self.post_layout.addWidget(self.feed_post_container)
        print("online layout:", self.ui.onlineFriendsLayout)
        print("offline layout:", self.ui.offlineFriendsLayout)

        # Comment section - now using our updated CommentSection
        self.comment_section_container = QWidget()
        self.comment_layout = QVBoxLayout(self.comment_section_container)
        self.comment_layout.setContentsMargins(0, 0, 0, 0)
        self.comment_layout.setSpacing(0)
        self.post_layout.addWidget(self.comment_section_container)
        self.post_layout.addStretch()
        self.clear_layout(self.ui.postAreea)
        self.ui.postAreea.addWidget(self.post_container)


    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

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
        label.setPixmap(QPixmap(label.size()))

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
        blank_pixmap = QPixmap(fallback_size[0], fallback_size[1])
        button.setIcon(QIcon(blank_pixmap))

    def _handle_new_comment(self, text, parent_comment_id=None):
        try:

            if (self.user_id):
                new_comment = self.comment_repo.add_comment_to_post(
                    post_id=self.post_id,
                    user_id=self.user_id,
                    text=text,
                    parent_comment_id=parent_comment_id
                )

                if new_comment:
                    self.comment_section.add_new_comment(new_comment, parent_comment_id)
                else:
                    logging.error("Failed to create new comment")
        except Exception as e:
            logging.error(f"Error adding comment: {e}")

    def _handle_like_comment(self, comment_id):
        try:
            new_likes = self.comment_repo.increment_comment_points(comment_id)
            self._update_comment_likes(comment_id, new_likes)
        except Exception as e:
            logging.error(f"Error liking comment: {e}")

    def _update_comment_likes(self, comment_id, new_likes):
        for i in range(self.comment_section.comments_layout.count()):
            widget = self.comment_section.comments_layout.itemAt(i).widget()
            if isinstance(widget, CommentWidget) and widget.comment_id == comment_id:
                widget.ui.likeCount.setText(str(new_likes))
                widget.ui.usernamePoints.setText(f"{new_likes} points")
                break

    def load_friends_widgets(self):
        """Load and display a list of online and offline friends from the database."""
        try:
            friends_data = get_friends_with_status(self.driver, self.user_id)



            for layout in [self.ui.onlineFriendsLayout, self.ui.offlineFriendsLayout]:
                while layout.count():
                    item = layout.takeAt(0)
                    if item.widget():
                        item.widget().deleteLater()

            for friend in friends_data:
                if friend["status"] == "online":
                    widget = OnlineFriendWidget(friend["name"], friend["points"], friend["img"])
                    self.ui.onlineFriendsLayout.addWidget(widget)
                else:
                    widget = OfflineFriendWidget(friend["name"],friend["points"], friend["img"])
                    self.ui.offlineFriendsLayout.addWidget(widget)

            self.ui.onlineFriendsLayout.addStretch(1)
            self.ui.offlineFriendsLayout.addStretch(1)
            print(">> friends_data received:", friends_data)
            print(">> online layout count:", self.ui.onlineFriendsLayout.count())
            print(">> offline layout count:", self.ui.offlineFriendsLayout.count())
        except Exception as e:
            logging.error(f"Error loading friends: {e}")

    def set_post(self, post_data, user_id):
        self.user_id = user_id
        self.post_id = post_data["id"]

        self.clear_layout(self.feed_post_layout)
        self.feed_post_widget = FeedPostWidget(post_data, self.user_id)
        self.feed_post_layout.addWidget(self.feed_post_widget)

        self.clear_layout(self.comment_layout)
        self.comment_section = CommentSection(self.post_id, self.user_id)
        self.comment_section.new_comment_submitted.connect(self._handle_new_comment)
        self.comment_section.like_comment.connect(self._handle_like_comment)
        self.comment_layout.addWidget(self.comment_section)

        self.comment_section.load_comments()

        if 'author_avatar' in post_data:
            try:
                image_utils.set_configured_image(
                    item=self.feed_post_widget.ui.userAvatar,
                    image_name=post_data["author_avatar"],
                    image_type=ImageType.USER_AVATAR,
                    item_type="label"
                )
            except Exception as e:
                logging.error(f"Error setting author avatar: {e}")
        self.load_friends_widgets()

    def on_back_button_click(self):
        self.back_to_feed.emit(True)

    def load_communities_acces_link(self):
        try:
            while self.ui.communitiesWidgetLayout.count():
                item = self.ui.communitiesWidgetLayout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

            communities = self.community_repo.get_top_communities(limit=4)

            for community in communities:
                community_widget = CommunityWidget(
                    communityName=community["name"],
                    icon=community.get("icon")
                )
                self.ui.communitiesWidgetLayout.addWidget(community_widget)

            self.ui.communitiesWidgetLayout.addStretch(1)

        except Exception as e:
            logging.critical(f"Error loading communities: {e}")

    def _horizontal_spacer(self):
        spacer = QFrame()
        spacer.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )
        return spacer
