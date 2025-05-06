import logging

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame, QLineEdit
from PySide6.QtCore import Qt, Signal

import image_utils
from image_config import ImageType
from frontend.assets.UserInterface.PostUI.UserInterfaceFile.CommentWidget import Ui_CommentWidget


class CommentWidget(QFrame):
    like_clicked = Signal(str)  # comment_id
    reply_clicked = Signal(str, str)  # comment_id, text

    def __init__(self, comment_data, parent=None, depth=0):
        super().__init__(parent)
        self.ui = Ui_CommentWidget()
        self.ui.setupUi(self)

        # Initialize frame properties
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setStyleSheet("""
                 QFrame {
                     background-color: #1A1A1B;
                     border-radius: 18px;
                 }
             """)

        self.comment_id = comment_data["id"]
        self.depth = depth

        # Set comment data
        self.ui.username.setText(comment_data["author_name"])
        points = comment_data.get("likes", 0) - comment_data.get("dislikes", 0)
        self.ui.usernamePoints.setText(f"{points} points")
        self.ui.authorLabel.setText(comment_data["timestamp"])
        self.ui.textBrowserContent.setText(comment_data["text"])
        self.ui.likeCount.setText(str(comment_data.get("likes", 0)))

        self.ui.depthIconLabel.setPixmap(QPixmap())

        # Set indentation based on depth
        self.set_indentation(depth)

        # Set up images
        self._setup_images(comment_data)


        self.reply_container = QWidget()
        self.reply_container.setVisible(False)
        self.reply_layout = QVBoxLayout(self.reply_container)
        self.reply_input = QLineEdit()
        self.reply_input.setPlaceholderText("Write your reply...")
        self.reply_input.setStyleSheet("""
             QLineEdit {
                 background-color: #2E2E2E;
                 color: white;
                 border-radius: 15px;
                 padding: 8px;
                 font: 12pt "Raleway";
             }
         """)

        self.reply_submit = QPushButton("Submit Reply")
        self.reply_submit.setStyleSheet("""
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
        self.reply_layout.addWidget(self.reply_input)
        self.reply_layout.addWidget(self.reply_submit)

        # Add reply container to main layout
        self.ui.verticalLayout.addWidget(self.reply_container)

        # Connect signals
        self.ui.likeButtonIcon.clicked.connect(self._on_like_clicked)
        self.ui.replyCommentButtonIcon.clicked.connect(self._on_reply_clicked)
        self.ui.replyCommentButtonIcon.clicked.connect(self._toggle_reply_input)
        self.reply_submit.clicked.connect(self._submit_reply)

    def _toggle_reply_input(self):
        """Toggle visibility of reply input field"""
        self.reply_container.setVisible(not self.reply_container.isVisible())
        if self.reply_container.isVisible():
            self.reply_input.setFocus()

    def _submit_reply(self):
        """Handle reply submission"""
        text = self.reply_input.text().strip()
        if text:
            self.reply_clicked.emit(self.comment_id, text)
            self.reply_input.clear()
            self.reply_container.setVisible(False)

    def set_indentation(self, depth):
        """Add left margin based on comment depth in hierarchy"""
        if depth > 0:
            margin = depth * 40  # 20px per level of nesting
            self.ui.contentWidget.layout().setContentsMargins(margin, 0, 0, 0)
            image_utils.set_image_default(
                label=self.ui.depthIconLabel,
                image_name="commentDepthIcon.png",
                scaling=False
            )

    def _setup_images(self, comment_data):
        """Configure all images in the comment widget"""
        # User avatar
        image_utils.set_configured_image(
            item=self.ui.userAvatar,
            image_name=comment_data.get("author_avatar", "default_user.png"),
            image_type=ImageType.USER_AVATAR,
            item_type="label"
        )

        # Button icons
        image_utils.set_configured_image(
            item=self.ui.likeButtonIcon,
            image_name="like_icon.png",
            image_type=ImageType.BUTTON_ICON,
            item_type="button"
        )

        # Button icons
        image_utils.set_configured_image(
            item=self.ui.commentButtonIcon,
            image_name="comment_icon.png",
            image_type=ImageType.BUTTON_ICON,
            item_type="button"
        )

        image_utils.set_configured_image(
            item=self.ui.replyCommentButtonIcon,
            image_name="replyButtonIcon.png",
            image_type=ImageType.BUTTON_ICON,
            item_type="button"
        )

    def _on_like_clicked(self):
        """Handle like button click"""
        self.like_clicked.emit(self.comment_id)

    def _on_reply_clicked(self):
        """Handle reply button click"""
        self.reply_clicked.emit(self.comment_id)

