from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QTextEdit, QPushButton, QScrollArea, QWidget, QTextBrowser
from PySide6.QtCore import Signal

from frontend.assets.ui_files.PostUI.UserInterfaceFile.DetaliedPostView import Ui_DetailedPostView


class DetailedPostWidget(QFrame):
    back_to_feed = Signal()  # Signal to return to the feed

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DetailedPostView()
        self.ui.setupUi(self)

        self.id = None
        self.content = None
        self.author = None
        self.timestamp = None

        # Create and configure the back button
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.on_back_button_click)
        self.ui.verticalLayout.addWidget(self.back_button)  # Add the button to the layout

        # Create a QTextBrowser for rendering HTML content
        self.content_browser = QTextBrowser(self)
        self.ui.content_label = self.content_browser  # Replace content_label with QTextBrowser for HTML rendering
        self.ui.content_label.setOpenExternalLinks(True)  # Allow opening external links (like images) in the content

    def set_post(self, id, title, content, author, timestamp):
        """Update the post content with the title."""
        self.id = id
        self.content = content
        self.author = author
        self.timestamp = timestamp

        self.ui.author_label.setText(f"By: {author}")
        self.ui.timestamp_label.setText(timestamp)
        self.ui.post_title_label.setText(title)  # Set the post title

        # Set the HTML content (assuming 'content' is an HTML string)
        self.ui.content_label.setHtml(content)  # Set HTML content in QTextBrowser

    def on_back_button_click(self):
        """Emit the signal to go back to the feed."""
        self.back_to_feed.emit()  # Emit the signal when the back button is clicked
