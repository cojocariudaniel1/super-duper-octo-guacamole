from xml.etree.ElementTree import tostring

from PySide6.QtGui import QTextOption
from PySide6.QtWidgets import QFrame, QTextBrowser
from PySide6.QtCore import Signal, Qt
from frontend.assets.ui_files.PostUI.UserInterfaceFile.mini_post_view import Ui_MiniViewPost


class MiniPostWidget(QFrame):
    post_clicked = Signal()  # Define a custom signal

    def __init__(self, id, title, content, author, timestamp, parent=None):
        super().__init__(parent)

        # Set up the UI from the generated class
        self.ui = Ui_MiniViewPost()
        self.ui.setupUi(self)

        self.id = id
        self.title = title
        self.content = content
        self.author = author

        # Customize the post content
        self.ui.label_2.setText(author)  # Set the author name
        # self.ui.label.setText((timestamp.to))  # Set the timestamp

        # Use a QTextBrowser for HTML content rendering
        self.content_browser = QTextBrowser(self)
        self.ui.content_label = self.content_browser  # Replace content_label with QTextBrowser for HTML rendering
        self.ui.content_label.setOpenExternalLinks(True)  # Allow opening external links (like images) in the content

        # Set the HTML content (assuming 'content' is an HTML string)
        self.ui.content_label.setHtml(content)  # Set HTML content in QTextBrowser

        self.ui.content_label.setWordWrapMode(QTextOption.WrapMode.WordWrap)

        # Set the title text (add a label for the title in the UI if it doesn't exist)
        self.ui.title_label.setText(title)  # Assuming there's a title_label in the UI file

    def mouseDoubleClickEvent(self, e):
        """Emit signal when the post is clicked."""
        self.post_clicked.emit()  # Emit signal to notify the DashboardWindow
        print(f"{self.id}, {self.title}, {self.author}")  # Print post info for debugging

    def set_post(self, id, title, content, author, timestamp):
        """Update the post content."""
        self.id = id
        self.title = title
        self.content = content
        self.author = author

        # Update UI elements
        self.ui.title_label.setText(title)  # Update title
        self.ui.label_2.setText(author)  # Update author
        self.ui.label.setText(timestamp)  # Update timestamp

        # Set the HTML content in QTextBrowser
        self.ui.content_label.setHtml(content)  # Set HTML content in QTextBrowser
