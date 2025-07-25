from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLineEdit, QPushButton, QHBoxLayout, QTextEdit
from PySide6.QtCore import Signal, Qt
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

        # Comment input area (QTextEdit in loc de QLineEdit)
        self.comment_input = QTextEdit()
        self.comment_input.setPlaceholderText("Add a comment...")
        self.comment_input.setFixedHeight(40)
        self.comment_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.comment_input.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.comment_input.setStyleSheet("""
            QTextEdit {
                background-color: #2E2E2E;
                color: white;
                border-radius: 15px;
                padding: 8px;
                font: 12pt "Raleway";
            }
            QTextEdit QScrollBar {
                width: 0px;
                height: 0px;
            }
        """)
        self.comment_input.textChanged.connect(self._auto_resize_input)

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

        self.load_comments()

    def _auto_resize_input(self):
        """Adjust height of QTextEdit based on content"""
        doc_height = self.comment_input.document().size().height()
        self.comment_input.setFixedHeight(min(150, max(40, int(doc_height + 10))))

    def load_comments(self):
        """Load and display comments for the post"""
        # Clear existing comments
        while self.comments_layout.count():
            item = self.comments_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Get comments from repository
        from backend.Repository.CommentRepository import CommentRepository
        from backend.database_connect import Neo4jDriverSingleton

        driver = Neo4jDriverSingleton.get_driver()
        comment_repo = CommentRepository(driver)
        comments = comment_repo.get_comments_for_post(self.post_id)
        print(comments)
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
            comment_widget.reply_clicked.connect(self._handle_reply_submission)

            self.comments_layout.addWidget(comment_widget)

            # Recursiv pentru reply-uri
            if comment.get("replies"):
                self._display_comments(comment["replies"], depth + 1)

    def _submit_comment(self):
        """Handle submission of a new comment"""
        text = self.comment_input.toPlainText().strip()

        if not text:
            return

        # Emit signal with comment text and parent comment ID if replying
        parent_id = self.replying_to if self.replying_to else None

        self.new_comment_submitted.emit(text, parent_id)

        # Reset input
        self.comment_input.clear()
        self.replying_to = None
        self.comment_input.setPlaceholderText("Add a comment...")

    def _handle_reply_submission(self, comment_id, text):
        self.new_comment_submitted.emit(text, comment_id)

    def _on_comment_liked(self, comment_id):
        """Handle like action on a comment"""
        self.like_comment.emit(comment_id)

    def _set_replying_to(self, comment_id):
        self.replying_to = comment_id
        self.comment_input.setFocus()
        self.comment_input.setPlaceholderText("Replying to comment...")

    def add_new_comment(self, comment_data, parent_id=None):
        """Add a newly created comment to the display"""
        comment_widget = CommentWidget(comment_data, depth=1 if parent_id else 0)
        comment_widget.like_clicked.connect(self._on_comment_liked)
        comment_widget.reply_clicked.connect(self._on_reply_submitted)

        if parent_id:
            # Insert under the parent comment
            inserted = False
            for i in range(self.comments_layout.count()):
                widget = self.comments_layout.itemAt(i).widget()
                if isinstance(widget, CommentWidget) and widget.comment_id == parent_id:
                    self.comments_layout.insertWidget(i + 1, comment_widget)
                    inserted = True
                    break
            if not inserted:
                self.comments_layout.addWidget(comment_widget)
        else:
            self.comments_layout.addWidget(comment_widget)

    def _on_reply_submitted(self, parent_comment_id, text):
        self.new_comment_submitted.emit(text, parent_comment_id)