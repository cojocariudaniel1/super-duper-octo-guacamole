from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QFont, QPixmap

# Assuming the generated UI file is named CreatePostView.py
from frontend.UserInterface.PostUI.UserInterfaceFile.CreatePostView import Ui_CreatePostView

class CreatePostWidget(QWidget, Ui_CreatePostView):
    def __init__(self, user_id,post_repo):
        super().__init__()
        self.setupUi(self)
        self.post_repo = post_repo
        self.user_id = user_id
        # Connect formatting actions
        self.boldAction.triggered.connect(self.format_bold)
        self.italicAction.triggered.connect(self.format_italic)
        self.underlineAction.triggered.connect(self.format_underline)
        self.strikeAction.triggered.connect(self.format_strike)

        # Connect font selection
        self.fontComboBox.currentFontChanged.connect(self.change_font_family)
        self.fontSizeComboBox.currentTextChanged.connect(self.change_font_size)

        # Populate font size combo box
        self.fontSizeComboBox.addItems(["8", "10", "12", "14", "16", "18", "20", "24", "28", "32", "36", "48", "72"])
        self.fontSizeComboBox.setCurrentText("12")  # Default font size

        # Connect image upload button
        self.uploadImageButton.clicked.connect(self.upload_image)

        # Connect submit button
        self.submitButton.clicked.connect(self.submit_post)

    def format_bold(self):
        cursor = self.bodyInput.textCursor()
        fmt = cursor.charFormat()
        fmt.setFontWeight(QFont.Weight.Bold if fmt.fontWeight() != QFont.Weight.Bold else QFont.Weight.Normal)
        cursor.mergeCharFormat(fmt)
        self.bodyInput.setCurrentCharFormat(fmt)

    def format_italic(self):
        cursor = self.bodyInput.textCursor()
        fmt = cursor.charFormat()
        fmt.setFontItalic(not fmt.fontItalic())
        cursor.mergeCharFormat(fmt)
        self.bodyInput.setCurrentCharFormat(fmt)

    def format_underline(self):
        cursor = self.bodyInput.textCursor()
        fmt = cursor.charFormat()
        fmt.setFontUnderline(not fmt.fontUnderline())
        cursor.mergeCharFormat(fmt)
        self.bodyInput.setCurrentCharFormat(fmt)

    def format_strike(self):
        cursor = self.bodyInput.textCursor()
        fmt = cursor.charFormat()
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
        cursor.mergeCharFormat(fmt)
        self.bodyInput.setCurrentCharFormat(fmt)

    def change_font_family(self, font):
        cursor = self.bodyInput.textCursor()
        fmt = cursor.charFormat()
        fmt.setFontFamily(font.family())
        cursor.mergeCharFormat(fmt)
        self.bodyInput.setCurrentCharFormat(fmt)

    def change_font_size(self, size):
        cursor = self.bodyInput.textCursor()
        fmt = cursor.charFormat()
        fmt.setFontPointSize(float(size))
        cursor.mergeCharFormat(fmt)
        self.bodyInput.setCurrentCharFormat(fmt)

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            pixmap = QPixmap(file_path)  # Convert file path to QPixmap
            if not pixmap.isNull():  # Check if the pixmap is valid
                self.imagePreview.setPixmap(pixmap)
                self.imagePreview.setScaledContents(True)

    def submit_post(self):
        # Get data from the form
        title = self.titleInput.text()
        body = self.bodyInput.toHtml()  # Get the HTML formatted content
        image_path = self.imagePreview.pixmap().cacheKey() if self.imagePreview.pixmap() else None

        # Replace image path in the HTML body if an image is selected
        if image_path:
            body += f'<img src="{image_path}" alt="Uploaded Image"/>'


        # Call the PostRepository's create_post method to save the post in Neo4j
        post = self.post_repo.create_post(self.user_id, title, body, visibility="PUBLIC")

        # Print or log the created post
        print("Post Created:")
        print("Title:", post["title"])
        print("Body:", post["content"])
        print("Image Path:", image_path)

        # Clear the form after submission
        self.titleInput.clear()
        self.bodyInput.clear()
        self.imagePreview.clear()

        # Optionally, show a confirmation to the user that the post was created
        # You can display a success message or redirect to another page/screen
