from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLineEdit, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt, Signal
from frontend.assets.customWidget.CommentCW import CommentWidget


class CommentSection(QWidget):
    new_comment_submitted = Signal(str, str)  # text, parent_comment_id
    like_comment = Signal(str)  # comment_id

    def __init__(self, post_id, user_id, parent=None):
        super().__init__(parent)
        self.post_id = post_id
        self.user_id = user_id
        self.replying_to = None

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(10)

        # Comment input area
        self.comment_input = QLineEdit()
        self.comment_input.setPlaceholderText("Add a comment...")
        self.comment_input.setStyleSheet("""
             QLineEdit {
                 background-color: #2E2E2E;
                 color: white;
                 border-radius: 15px;
                 padding: 8px;
                 font: 12pt "Raleway";
             }
         """)

        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("""
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
        self.submit_button.clicked.connect(self._submit_comment)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.comment_input)
        input_layout.addWidget(self.submit_button)

        self.layout.addLayout(input_layout)
        # Comments container
        self.comments_container = QFrame()
        self.comments_container.setFrameShape(QFrame.Shape.NoFrame)
        self.comments_layout = QVBoxLayout(self.comments_container)
        self.comments_layout.setContentsMargins(0, 0, 0, 0)
        self.comments_layout.setSpacing(10)

        self.layout.addWidget(self.comments_container)

        # Load comments
        self.load_comments()

    def load_comments(self):
        """Load and display comments for the post"""
        # Clear existing comments
        while self.comments_layout.count():
            item = self.comments_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Get comments from repository
        from neo4j_data.Repository.CommentRepository import CommentRepository
        from neo4j_data.database_connect import Neo4jDriverSingleton

        driver = Neo4jDriverSingleton.get_driver()
        comment_repo = CommentRepository(driver)
        comments = comment_repo.get_comments_for_post(self.post_id)

        # Display comments in hierarchy
        self._display_comments(comments)

    def _display_comments(self, comments, depth=0):
        """Recursively display comments and their replies"""
        for comment in comments:
            if depth == 0:
                # Adaugă delimiter doar între comentarii principale
                delimiter = QFrame()
                delimiter.setFrameShape(QFrame.Shape.HLine)
                delimiter.setFrameShadow(QFrame.Shadow.Sunken)
                delimiter.setStyleSheet("color: #333; background-color: #333; height: 1px;")
                self.comments_layout.addWidget(delimiter)

            comment_widget = CommentWidget(comment, depth=depth)
            comment_widget.like_clicked.connect(self._on_comment_liked)
            comment_widget.reply_clicked.connect(self._set_replying_to)

            self.comments_layout.addWidget(comment_widget)

            # Recursiv pentru reply-uri
            if comment.get("replies"):
                self._display_comments(comment["replies"], depth + 1)

    def _submit_comment(self):
        """Handle submission of a new comment"""
        text = self.comment_input.text().strip()
        if not text:
            return

        # Emit signal with comment text and parent comment ID if replying
        parent_id = self.replying_to if self.replying_to else None
        self.new_comment_submitted.emit(text, parent_id)

        # Reset input
        self.comment_input.clear()
        self.replying_to = None
        self.comment_input.setPlaceholderText("Add a comment...")

    def _on_comment_liked(self, comment_id):
        """Handle like action on a comment"""
        self.like_comment.emit(comment_id)

    def _set_replying_to(self, comment_id, text):
        self.new_comment_submitted.emit(text, comment_id)

    def add_new_comment(self, comment_data, parent_id=None):
        """Add a newly created comment to the display"""
        if parent_id:
            # Find the parent comment widget
            for i in range(self.comments_layout.count()):
                widget = self.comments_layout.itemAt(i).widget()
                if isinstance(widget, CommentWidget) and widget.comment_id == parent_id:
                    # Hide the reply input if it's visible
                    widget.reply_container.setVisible(False)

                    # Create a container for replies if it doesn't exist
                    if not hasattr(widget, 'replies_container'):
                        widget.replies_container = QWidget()
                        widget.replies_layout = QVBoxLayout(widget.replies_container)
                        widget.replies_layout.setContentsMargins(0, 0, 0, 0)
                        widget.replies_layout.setSpacing(10)
                        self.comments_layout.insertWidget(i + 1, widget.replies_container)

                    # Add the reply
                    reply_widget = CommentWidget(comment_data, depth=widget.depth + 1)
                    reply_widget.like_clicked.connect(self._on_comment_liked)
                    reply_widget.reply_clicked.connect(self._set_replying_to)
                    widget.replies_layout.addWidget(reply_widget)
                    break
        else:
            # Add as top-level comment
            comment_widget = CommentWidget(comment_data)
            comment_widget.like_clicked.connect(self._on_comment_liked)
            comment_widget.reply_clicked.connect(self._set_replying_to)
            self.comments_layout.addWidget(comment_widget)