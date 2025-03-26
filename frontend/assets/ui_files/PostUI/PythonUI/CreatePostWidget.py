from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide6.QtGui import QTextCursor, QTextCharFormat, QTextImageFormat, QImage, QTextDocument, QFont
from PySide6.QtCore import QByteArray, QBuffer, QIODevice

import base64

from frontend.assets.ui_files.PostUI.UserInterfaceFile.CreatePostView import Ui_CreatePostView


class CreatePostWidget(QWidget):
    def __init__(self, user_id, post_repository, parent=None):
        super().__init__(parent)
        self.user_id = user_id
        self.post_repository = post_repository
        self.community_id = None  # Will be set when creating post
        self.ui = Ui_CreatePostView()
        self.ui.setupUi(self)

        # Connect toolbar actions
        self.ui.boldAction.triggered.connect(self.toggle_bold)
        self.ui.italicAction.triggered.connect(self.toggle_italic)
        self.ui.underlineAction.triggered.connect(self.toggle_underline)
        self.ui.strikeAction.triggered.connect(self.toggle_strike)

        # Connect other buttons
        self.ui.uploadImageButton.clicked.connect(self.upload_image)
        self.ui.submitButton.clicked.connect(self.submit_post)

        # Setup font size combo box
        self.setup_font_sizes()

        # Connect font changes
        self.ui.fontComboBox.currentFontChanged.connect(self.change_font)
        self.ui.fontSizeComboBox.currentTextChanged.connect(self.change_font_size)

        # Store images with their positions
        self.images = {}  # {position: image_data}

    def setup_font_sizes(self):
        """Populate the font size combo box with common sizes"""
        sizes = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
        self.ui.fontSizeComboBox.addItems([str(size) for size in sizes])
        self.ui.fontSizeComboBox.setCurrentText("12")  # Default size

    def toggle_bold(self):
        """Toggle bold formatting for selected text"""
        fmt = QTextCharFormat()
        fmt.setFontWeight(QFont.Weight.Bold if not self.ui.boldAction.isChecked() else QFont.Weight.Normal)
        self.merge_format_on_selection(fmt)

    def toggle_italic(self):
        """Toggle italic formatting for selected text"""
        fmt = QTextCharFormat()
        fmt.setFontItalic(not self.ui.italicAction.isChecked())
        self.merge_format_on_selection(fmt)

    def toggle_underline(self):
        """Toggle underline formatting for selected text"""
        fmt = QTextCharFormat()
        fmt.setFontUnderline(not self.ui.underlineAction.isChecked())
        self.merge_format_on_selection(fmt)

    def toggle_strike(self):
        """Toggle strikeout formatting for selected text"""
        fmt = QTextCharFormat()
        fmt.setFontStrikeOut(not self.ui.strikeAction.isChecked())
        self.merge_format_on_selection(fmt)

    def merge_format_on_selection(self, format):
        """Apply formatting to selected text"""
        cursor = self.ui.bodyInput.textCursor()
        if not cursor.hasSelection():
            cursor.select(QTextCursor.SelectionType.WordUnderCursor)
        cursor.mergeCharFormat(format)
        self.ui.bodyInput.mergeCurrentCharFormat(format)

    def change_font(self, font):
        """Change font family for selected text"""
        fmt = QTextCharFormat()
        fmt.setFontFamily(font.family())
        self.merge_format_on_selection(fmt)

    def change_font_size(self, size):
        """Change font size for selected text"""
        fmt = QTextCharFormat()
        fmt.setFontPointSize(float(size))
        self.merge_format_on_selection(fmt)

    def upload_image(self):
        """Handle image upload and insertion into the post"""
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.gif *.bmp)")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            image = QImage(file_path)

            if image.isNull():
                QMessageBox.warning(self, "Error", "Could not load image")
                return

            # Scale image if too large
            max_width = 600  # Max width for images in posts
            if image.width() > max_width:
                image = image.scaledToWidth(max_width)

            # Insert image into document
            cursor = self.ui.bodyInput.textCursor()
            image_format = QTextImageFormat()
            image_format.setName(file_path)  # Temporary identifier

            # Store the image data with its position
            position = cursor.position()
            self.images[position] = self.image_to_bytes(image)

            # Insert the image
            cursor.insertImage(image_format)

    def image_to_bytes(self, image):
        """Convert QImage to bytes for database storage"""
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.OpenModeFlag.WriteOnly)
        image.save(buffer, "PNG")  # Save as PNG for lossless compression
        return base64.b64encode(byte_array.data()).decode('utf-8')

    def set_community(self, community_id):
        """Set the community this post belongs to"""
        self.community_id = community_id

    def submit_post(self):
        """Handle post submission to database"""
        title = self.ui.titleInput.text().strip()
        if not title:
            QMessageBox.warning(self, "Error", "Post title cannot be empty")
            return

        # Get HTML content with embedded images
        html_content = self.get_html_with_images()

        try:
            # Create post in database
            post_id = self.post_repository.create_post(
                user_id=self.user_id,
                community_name=self.community_id,
                title=title,
                content=html_content,
                visibility="PUBLIC"  # Could be made configurable
            )

            # Clear the form after successful submission
            self.ui.titleInput.clear()
            self.ui.bodyInput.clear()
            self.images.clear()

            QMessageBox.information(self, "Success", "Post created successfully!")
            # Emit signal or handle post-creation logic here

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to create post: {str(e)}")

    def get_html_with_images(self):
        """Convert the document to HTML with embedded images"""
        doc = self.ui.bodyInput.document()
        html = doc.toHtml()

        # Replace temporary image references with base64 data
        for position, image_data in self.images.items():
            # Find the image in the HTML and replace with base64
            placeholder = f'<img src="{position}"'  # Our temporary identifier
            if placeholder in html:
                html = html.replace(placeholder, f'<img src="data:image/png;base64,{image_data}"')

        return html

    def clear_form(self):
        """Clear the post creation form"""
        self.ui.titleInput.clear()
        self.ui.bodyInput.clear()
        self.images.clear()
        self.community_id = None


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    from PySide6.QtGui import QFontDatabase
    from neo4j_data.database_connect import Neo4jDriverSingleton
    from neo4j_data.Repository.PostRepository import PostRepository
    Neo4jDriverSingleton(uri="bolt://localhost:7687", user="neo4j", password="12345678")
    # Initialize the application
    app = QApplication([])

    # Initialize database connection (for testing)
    driver = Neo4jDriverSingleton.get_driver()
    post_repo = PostRepository(driver)

    # Test user and community IDs
    TEST_USER_ID = "45678"  # Replace with actual test user ID
    TEST_COMMUNITY_ID = "RoadAccidents"  # Replace with actual test community name

    # Create and show the widget
    widget = CreatePostWidget(user_id=TEST_USER_ID, post_repository=post_repo)
    widget.set_community(TEST_COMMUNITY_ID)
    widget.resize(800, 600)
    widget.setWindowTitle("Test Create Post Widget")
    widget.show()

    # Run the application
    app.exec()