import random
from PySide6.QtWidgets import QApplication, QWidget, QFrame, QVBoxLayout, QLabel, QSizePolicy
from frontend.assets.ui_files.HomePageUI.UserInterfaceFile.dashboard import Ui_ForumAppUI
from frontend.assets.ui_files.PostUI.UserInterfaceFile.mini_post_view import Ui_MiniViewPost
import sys

class ForumApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ForumAppUI()
        self.ui.setupUi(self)  # Set up the UI

        # Set ScrollArea properties
        self.ui.ContentPosts_ScrollArea.setWidgetResizable(True)
        self.ui.ContentPosts_ScrollArea.setStyleSheet("""
            QScrollBar:vertical {
                background: #2e2e2e;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background: #5a5a5a;
                border-radius: 6px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: #3a3a3a;
            }
        """)

        # Get post layout container
        self.posts_layout = self.ui.postsLayout
        self.posts_layout.setSpacing(10)  # Add spacing between posts
        self.posts_layout.setContentsMargins(0, 0, 0, 0)  # Remove layout margins

        # Set a fixed height for the scroll area widget
        # Add test posts
        for i in range(50):
            self.add_post(f"Post {i+1}", f"Acesta este conținutul postării {i+1}.")

        # Set max width for side panels
        self.ui.communityList.setMaximumWidth(300)
        self.ui.recentPostsList.setMaximumWidth(300)

    def add_post(self, title, content):
        """Adds a new post to the layout."""
        post_widget = MiniPostWidget(title, content)  # Create a new post widget
        self.posts_layout.addWidget(post_widget)  # Add it to the layout


class MiniPostWidget(QFrame):
    def __init__(self, title, content, parent=None):
        super().__init__(parent)

        # Set up the UI from the generated class
        self.ui = Ui_MiniViewPost()
        self.ui.setupUi(self)

        # Customize the post content
        self.ui.label_2.setText(title)  # Set the title
        self.ui.label.setText(content)  # Set the content (or timestamp)
        self.add_random_text()

    def add_random_text(self):
        # Generate a random number of rows (between 2 and 550)
        num_rows = random.randint(2, 50)
        label_text = self.ui.content_label  # Ensure this matches the name in your .ui file

        # Add random text to the content (or any other QLabel)
        text = "\n".join(f"Random text line {i + 1}" for i in range(num_rows))
        label_text.setText(text)

        # Enable word wrapping
        label_text.setWordWrap(True)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ForumApp()
    window.show()
    sys.exit(app.exec())
