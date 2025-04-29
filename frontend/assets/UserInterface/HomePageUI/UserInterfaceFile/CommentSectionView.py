from PySide6.QtGui import QTextDocument, QPainter, QColor, QPen
from PySide6.QtWidgets import (
    QWidget, QLabel, QTextBrowser, QPushButton, QHBoxLayout, QLineEdit, QButtonGroup, QSizePolicy, QTextEdit
)
from PySide6.QtCore import Qt

from datetime import datetime, timezone


from neo4j_data.Repository.CommentRepository import CommentRepository
from neo4j_data.database_connect import Neo4jDriverSingleton


def format_relative_time(timestamp_str):
    """Convert timestamp string to relative time (e.g., '5 min ago')"""
    try:
        # Handle both string timestamps and neo4j DateTime objects
        if isinstance(timestamp_str, str):
            dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
        else:
            # For neo4j DateTime objects
            dt = datetime(
                timestamp_str.year, timestamp_str.month, timestamp_str.day,
                timestamp_str.hour, timestamp_str.minute, timestamp_str.second,
                tzinfo=timezone.utc
            )

        now = datetime.now(timezone.utc)
        diff = now - dt

        # Calculate time differences
        seconds = diff.total_seconds()
        if seconds < 60:
            return "just now"
        minutes = seconds / 60
        if minutes < 60:
            return f"{int(minutes)} min ago"
        hours = minutes / 60
        if hours < 24:
            return f"{int(hours)} hour{'s' if hours >= 2 else ''} ago"
        days = hours / 24
        if days < 30:
            return f"{int(days)} day{'s' if days >= 2 else ''} ago"
        months = days / 30
        if months < 12:
            return f"{int(months)} month{'s' if months >= 2 else ''} ago"
        years = days / 365
        return f"{int(years)} year{'s' if years >= 2 else ''} ago"

    except Exception as e:
        print(f"Error formatting timestamp: {e}")
        return "some time ago"

class CommentWidget(QWidget):
    def __init__(self, comment, parent_widget=None, add_reply_callback=None, comment_repo=None, depth=0):
        super().__init__()
        self.comment = comment
        self.add_reply_callback = add_reply_callback
        self.comment_repo = comment_repo
        self.depth = depth  # Track nesting level

        # Main layout with indentation based on depth
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Connector widget for hierarchy lines
        self.connector_widget = QWidget()
        self.connector_widget.setFixedWidth(30)
        self.connector_widget.setStyleSheet("background: transparent;")
        self.main_layout.addWidget(self.connector_widget)

        # The actual comment content container
        self.content_container = QWidget()
        self.content_container.setStyleSheet("background: transparent;")
        self.layout = QVBoxLayout(self.content_container)
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(0, 0, 10, 10)
        self.main_layout.addWidget(self.content_container)

        # Custom paint event for connectors
        self.connector_widget.paintEvent = self.paint_connectors

        # Header with relative timestamp
        relative_time = format_relative_time(comment['timestamp'])
        self.header = QLabel(f"{comment.get('author_name', 'Unknown')} · {relative_time}")
        self.header.setStyleSheet("""
            font-weight: bold; 
            color: white;
            margin-left: 5px;
        """)
        self.layout.addWidget(self.header)

        # Content (text)
        self.content = QTextBrowser()
        self.content.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.content.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.content.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.content.setOpenExternalLinks(True)
        self.content.setHtml(self.comment['text'])
        self.content.setStyleSheet("""
            QTextBrowser {
                background: #333;
                color: white;
                border: none;
                padding: 10px;
                margin: 5px 5px 5px 0;
                border-radius: 4px;
            }
        """)
        self.adjust_content_height()
        self.layout.addWidget(self.content)

        # Vote buttons (unchanged from your original)
        self.vote_layout = QHBoxLayout()
        self.vote_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.upvote_button = QPushButton("▲")
        self.upvote_button.setFixedSize(30, 30)
        self.upvote_button.setStyleSheet("""
            background: #444; 
            color: white; 
            border-radius: 4px;
            font-size: 16px;
        """)
        self.upvote_button.clicked.connect(self.upvote)
        self.vote_layout.addWidget(self.upvote_button)

        self.downvote_button = QPushButton("▼")
        self.downvote_button.setFixedSize(30, 30)
        self.downvote_button.setStyleSheet("""
            background: #444; 
            color: white; 
            border-radius: 4px;
            font-size: 16px;
        """)
        self.downvote_button.clicked.connect(self.downvote)
        self.vote_layout.addWidget(self.downvote_button)

        self.vote_count = QLabel(f"{self.comment['upvotes']} votes")
        self.vote_count.setStyleSheet("color: white; font-size: 14px;")
        self.vote_layout.addWidget(self.vote_count)

        self.layout.addLayout(self.vote_layout)

        # Reply button and input (unchanged from your original)
        self.reply_button = QPushButton("Reply")
        self.reply_button.setStyleSheet("background: #444; color: white; padding: 2px; border-radius: 4px;")
        self.reply_button.clicked.connect(self.show_reply_box)
        self.layout.addWidget(self.reply_button)

        self.reply_input = QTextEdit()
        self.reply_input.setPlaceholderText("Write a reply...")
        self.reply_input.setStyleSheet("background: #444; color: white; padding: 5px; border-radius: 4px;")

        self.reply_input.setVisible(False)
        self.layout.addWidget(self.reply_input)

        self.send_button = QPushButton("Post")
        self.send_button.setStyleSheet("background: #444; color: white; padding: 5px; border-radius: 4px;")
        self.send_button.setVisible(False)
        self.send_button.clicked.connect(self.post_reply)
        self.layout.addWidget(self.send_button)

        # Replies layout
        self.replies_layout = QVBoxLayout()
        self.replies_layout.setContentsMargins(0, 5, 0, 0)
        self.replies_layout.setSpacing(15)
        self.layout.addLayout(self.replies_layout)

    def paint_connectors(self, event):
        """Draw the hierarchy connector lines"""
        painter = QPainter(self.connector_widget)
        pen = QPen(QColor("#FFFFFF"))  # Light gray color
        pen.setWidth(2)
        painter.setPen(pen)

        width = self.connector_widget.width()
        height = self.connector_widget.height()

        # Vertical line (full height)
        painter.drawLine(width - 10, 0, width - 10, height)



        painter.end()

    def show_reply_box(self):
        self.reply_input.setVisible(True)
        self.send_button.setVisible(True)

    def post_reply(self):
        reply_text = self.reply_input.toPlainText().strip()
        if reply_text and self.add_reply_callback:
            self.add_reply_callback(self.comment['id'], reply_text)
        self.reply_input.clear()
        self.reply_input.setVisible(False)
        self.send_button.setVisible(False)

    def upvote(self):
        try:
            # Update database first
            new_upvotes = self.comment_repo.upvote_comment(self.comment['id'])
            # Then update UI
            self.comment['upvotes'] = new_upvotes
            self.update_vote_count()
        except Exception as e:
            print(f"Error upvoting comment: {e}")

    def downvote(self):
        try:
            # Update database first
            new_upvotes = self.comment_repo.downvote_comment(self.comment['id'])
            # Then update UI
            self.comment['upvotes'] = new_upvotes
            self.update_vote_count()
        except Exception as e:
            print(f"Error downvoting comment: {e}")

    def update_vote_count(self):
        self.vote_count.setText(f"{self.comment['upvotes']} votes")

    def resizeEvent(self, event):
        """Handle window resize events"""
        super().resizeEvent(event)
        self.adjust_content_height()

        # Ensure parent widgets know about our size change
        if self.parent():
            self.parent().updateGeometry()

    def adjust_content_height(self):
        """Adjust height to show all content without scrolling"""
        doc = self.content.document()
        doc.setDocumentMargin(5)  # Set small document margin instead of 0

        # Set text width accounting for widget padding (10px each side in stylesheet)
        content_width = self.content.width() - 27  # 10px padding each side

        # Ensure minimum width for very narrow windows
        content_width = max(content_width, 100)
        doc.setTextWidth(content_width)

        # Calculate height including padding (10px top + 10px bottom from stylesheet)
        required_height = doc.size().height() + 30

        # Set fixed height
        self.content.setFixedHeight(int(required_height))

        # Force immediate update
        self.content.updateGeometry()
        self.updateGeometry()

class CommentSection(QWidget):
    def __init__(self, post_id, user_id):
        super().__init__()
        self.post_id = post_id
        self.user_id = user_id
        self.comment_widgets = {}
        self.driver = Neo4jDriverSingleton.get_instance()
        self.comment_repo = CommentRepository(self.driver)

        # Main layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(10, 10, 10, 10)

        self.create_comment_input_section()
        self.create_sorting_buttons()
        self.current_sort = "newest"
        self.create_comments_layout()
        self.load_comments()

    def load_comments(self):
        """Load comments with current sorting while maintaining hierarchy"""
        print(f"Loading comments sorted by: {self.current_sort}")
        comments = self.comment_repo.get_comments_by_post(
            self.post_id,
            sort_by="timestamp_desc" if self.current_sort == "newest" else
            "timestamp_asc" if self.current_sort == "oldest" else
            "upvotes_desc"
        )

        # Clear existing comments
        for i in reversed(range(self.comments_layout.count())):
            self.comments_layout.itemAt(i).widget().setParent(None)
        self.comment_widgets.clear()

        if not comments:
            print("No comments found for this post.")
            no_comments_label = QLabel("No comments found. Be the first to comment!")
            no_comments_label.setStyleSheet("color: white; font-size: 16px;")
            self.comments_layout.addWidget(no_comments_label)
            return

        # Create a dictionary to organize comments by their parent
        comment_dict = {}
        for comment in comments:
            parent_id = comment.get('reply_to_id')
            if parent_id not in comment_dict:
                comment_dict[parent_id] = []
            comment_dict[parent_id].append(comment)

        # First add all top-level comments (those replying to post)
        top_level_comments = comment_dict.get(None, [])

        # Sort top-level comments according to current sort
        if self.current_sort == "newest":
            top_level_comments.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        elif self.current_sort == "oldest":
            top_level_comments.sort(key=lambda x: x.get('timestamp', ''))
        elif self.current_sort == "top":
            top_level_comments.sort(key=lambda x: x.get('upvotes', 0), reverse=True)

        # Add them to the layout
        for comment in top_level_comments:
            self.add_comment_with_replies(comment, comment_dict)

    def create_comments_layout(self):
        """Create scrollable comments area"""
        self.comments_container = QWidget()
        self.comments_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.comments_layout = QVBoxLayout(self.comments_container)
        self.comments_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.comments_layout.setSpacing(15)
        self.comments_layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.comments_container)

    def add_comment(self, comment_data):
        """Add a comment widget to the layout."""
        print(f"Adding comment: {comment_data}")


        # Ensure all fields have values
        comment_data['author_name'] = comment_data.get('author_name', 'Unknown')
        comment_data['author_id'] = comment_data.get('author_id', '')
        comment_data['upvotes'] = comment_data.get('upvotes', 0)
        comment_data['timestamp'] = str(comment_data.get('timestamp', ''))
        comment_widget = CommentWidget(
            comment_data,
            add_reply_callback=self.add_reply,
            comment_repo=self.comment_repo
        )
        self.comment_widgets[comment_data['id']] = comment_widget



        if comment_data.get('reply_to_id') is None:
            # Add top-level comment to the scroll layout
            self.comments_layout.addWidget(comment_widget)
        else:
            # Add reply to its parent's replies layout
            parent_widget = self.comment_widgets.get(comment_data['reply_to_id'])
            if parent_widget:
                parent_widget.replies_layout.addWidget(comment_widget)
            else:
                # If parent not found, add as top-level (shouldn't happen with proper data)
                self.comments_layout.addWidget(comment_widget)

    def add_comment_with_replies(self, comment, comment_dict, depth=0):
        """Recursively add comments with proper depth"""
        comment_widget = CommentWidget(
            comment,
            add_reply_callback=self.add_reply,
            comment_repo=self.comment_repo,
            depth=depth
        )
        self.comment_widgets[comment['id']] = comment_widget

        # Add to layout if top-level
        if comment.get('reply_to_id') is None:
            self.comments_layout.addWidget(comment_widget)

        # Add replies with increased depth
        replies = comment_dict.get(comment['id'], [])
        if self.current_sort == "newest":
            replies.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        elif self.current_sort == "oldest":
            replies.sort(key=lambda x: x.get('timestamp', ''))
        elif self.current_sort == "top":
            replies.sort(key=lambda x: x.get('upvotes', 0), reverse=True)

        for reply in replies:
            self.add_comment_with_replies(reply, comment_dict, depth + 1)
            parent_widget = self.comment_widgets.get(reply['reply_to_id'])
            if parent_widget:
                parent_widget.replies_layout.addWidget(self.comment_widgets[reply['id']])

    def post_comment(self):
        """Handle posting a new comment."""
        comment_text = self.comment_input.toPlainText().strip()
        if comment_text:
            try:
                print(f"Creating comment for post_id: {self.post_id}")
                new_comment = self.comment_repo.create_comment(self.post_id, self.user_id, comment_text)
                self.add_comment(new_comment)
                self.comment_input.clear()
            except Exception as e:
                print(f"Error creating comment: {e}")

    def add_reply(self, parent_comment_id, reply_text):
        """Handle posting a reply to a comment."""
        if reply_text:
            try:
                print(f"Creating reply for comment_id: {parent_comment_id}")
                new_reply = self.comment_repo.create_comment(self.post_id, self.user_id, reply_text, parent_comment_id)
                self.add_comment(new_reply)
            except Exception as e:
                print(f"Error creating reply: {e}")

    def create_sorting_buttons(self):
        """Create toolbar with sorting buttons"""
        toolbar = QWidget()
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(0, 0, 0, 0)

        toolbar.setStyleSheet("""

            QWidget {
                  background: #444; 
                padding: 5px;
                border-radius: 4px;
            }
            QPushButton {
                background: #444;
                color: white;
                padding: 5px 10px;
                border: none;
                border-radius: 4px;
                margin-right: 5px;
            }
            QPushButton:hover {
                background: #555;
            }
            QPushButton:checked {
                background: #666;
                font-weight: bold;
            }
        """)

        # Create button group for exclusive selection
        self.sort_button_group = QButtonGroup()

        # Newest button
        self.newest_btn = QPushButton("Newest")
        self.newest_btn.setCheckable(True)
        self.newest_btn.setChecked(True)
        self.newest_btn.clicked.connect(lambda: self.sort_comments("newest"))
        toolbar_layout.addWidget(self.newest_btn)
        self.sort_button_group.addButton(self.newest_btn)

        # Oldest button
        self.oldest_btn = QPushButton("Oldest")
        self.oldest_btn.setCheckable(True)
        self.oldest_btn.clicked.connect(lambda: self.sort_comments("oldest"))
        toolbar_layout.addWidget(self.oldest_btn)
        self.sort_button_group.addButton(self.oldest_btn)

        # Top button
        self.top_btn = QPushButton("Top")
        self.top_btn.setCheckable(True)
        self.top_btn.clicked.connect(lambda: self.sort_comments("top"))
        toolbar_layout.addWidget(self.top_btn)
        self.sort_button_group.addButton(self.top_btn)

        # Add stretch to push buttons to the left
        toolbar_layout.addStretch()

        self.layout.addWidget(toolbar)

    def sort_comments(self, sort_option):
        """Handle sorting of comments"""
        self.current_sort = sort_option
        self.load_comments()


    def create_comment_input_section(self):
        """Create the widget for new comment input"""
        self.input_widget = QWidget()
        input_layout = QVBoxLayout(self.input_widget)

        # Comment input field
        self.comment_input = QTextEdit()
        self.comment_input.setPlaceholderText("Write a comment...")
        self.comment_input.setStyleSheet("""
            background: #444; 
            color: white; 
            padding: 5px; 
            border-radius: 4px;
        """)
        self.comment_input.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.comment_input.LineWrapMode(True)

        input_layout.addWidget(self.comment_input)

        # Post button
        self.comment_button = QPushButton("Post Comment")
        self.comment_button.setStyleSheet("""
            background: #555; 
            color: white; 
            padding: 5px; 
            border-radius: 4px;
        """)
        self.comment_button.clicked.connect(self.post_comment)
        input_layout.addWidget(self.comment_button)

        # Add some spacing
        input_layout.addSpacing(10)

        # Add the input widget to the main layout
        self.layout.addWidget(self.input_widget)


from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, post_id, user_id):
        super().__init__()
        self.post_id = post_id
        self.user_id = user_id

        # Set up the main window
        self.setWindowTitle("Reddit-like Comment Section")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("""
            background: #444; 
            color: white; 
            padding: 5px; 
            border-radius: 4px;
        """)
        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Set up a layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create the comment section and add it to the layout
        self.comment_section = CommentSection(self.post_id, self.user_id)
        layout.addWidget(self.comment_section)


if __name__ == "__main__":
    # Create the application
    app = QApplication([])

    # Example post ID and user ID
    post_id = "101"  # Use post1 from the database
    user_id = "1"    # Use user1 from the database

    # Debugging: Print post_id and user_id
    print(f"Using post_id: {post_id}, user_id: {user_id}")

    # Create and show the main window
    main_window = MainWindow(post_id, user_id)
    main_window.show()

    # Run the application
    app.exec()