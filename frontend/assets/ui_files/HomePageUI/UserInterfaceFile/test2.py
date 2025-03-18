from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QFrame

class CommentWidget(QWidget):
    def __init__(self, comment, parent_widget=None, add_reply_callback=None):
        super().__init__()
        self.comment = comment
        self.add_reply_callback = add_reply_callback

        layout = QVBoxLayout(self)

        # Header (User + Time)
        header = QLabel(f"{comment['author']} - {comment['time']}")
        header.setStyleSheet("font-weight: bold; color: white;")

        # Comment Text
        text = QLabel(comment['text'])
        text.setWordWrap(True)

        # Reply Button
        reply_button = QPushButton("Reply")
        reply_button.setStyleSheet("background: #444; color: white; padding: 2px; border-radius: 4px;")
        reply_button.clicked.connect(self.show_reply_box)

        # Reply Box (Inițial ascuns)
        self.reply_box = QLineEdit()
        self.reply_box.setPlaceholderText("Write a reply...")
        self.reply_box.setVisible(False)

        send_button = QPushButton("Post")
        send_button.setVisible(False)
        send_button.clicked.connect(self.post_reply)

        # Layout pentru răspunsuri
        self.replies_layout = QVBoxLayout()
        self.replies_layout.setContentsMargins(20, 0, 0, 0)  # Indentare pentru răspunsuri

        # Adăugare în layout
        layout.addWidget(header)
        layout.addWidget(text)
        layout.addWidget(reply_button)
        layout.addWidget(self.reply_box)
        layout.addWidget(send_button)
        layout.addLayout(self.replies_layout)

        self.send_button = send_button  # Salvează referința

    def show_reply_box(self):
        self.reply_box.setVisible(True)
        self.send_button.setVisible(True)

    def post_reply(self):
        reply_text = self.reply_box.text().strip()
        if reply_text and self.add_reply_callback:
            self.add_reply_callback(self.comment['id'], reply_text)
        self.reply_box.clear()
        self.reply_box.setVisible(False)
        self.send_button.setVisible(False)

    def add_reply(self, reply_widget):
        self.replies_layout.addWidget(reply_widget)


from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea

class CommentSection(QWidget):
    def __init__(self, comments_data):
        super().__init__()

        # Scroll pentru comentarii
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("background: #252526; border-radius: 8px; padding: 10px;")

        # Widget pentru conținutul scrollului
        self.scroll_widget = QWidget()
        self.layout = QVBoxLayout(self.scroll_widget)

        # Dicționar pentru a mapa ID-urile comentariilor
        self.comment_widgets = {}

        # Inițializare comentarii
        self.load_comments(comments_data)

        scroll_area.setWidget(self.scroll_widget)

        # Layout principal
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

    def load_comments(self, comments_data):
        for comment in comments_data:
            self.add_comment(comment, parent_id=comment['parent_id'])

    def add_comment(self, comment_data, parent_id):
        comment_widget = CommentWidget(comment_data, add_reply_callback=self.add_reply)
        self.comment_widgets[comment_data['id']] = comment_widget

        if parent_id == 0:
            self.layout.addWidget(comment_widget)
        else:
            parent_widget = self.comment_widgets.get(parent_id)
            if parent_widget:
                parent_widget.add_reply(comment_widget)

    def add_reply(self, parent_id, text):
        new_comment = {
            'id': len(self.comment_widgets) + 1,
            'parent_id': parent_id,
            'text': text,
            'author': 'You',
            'time': 'Just now'
        }
        self.add_comment(new_comment, parent_id)


from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Date inițiale (pot fi citite dintr-o bază de date)
    comments_data = [
        {'id': 1, 'parent_id': 0, 'text': "This is the first comment!", 'author': "Alice", 'time': "10 min ago"},
        {'id': 2, 'parent_id': 1, 'text': "Reply to first comment", 'author': "Bob", 'time': "8 min ago"},
        {'id': 3, 'parent_id': 1, 'text': "Another reply", 'author': "Charlie", 'time': "5 min ago"},
        {'id': 4, 'parent_id': 2, 'text': "Reply to reply", 'author': "David", 'time': "2 min ago"},
    ]

    # Creare fereastră principală
    main_window = QWidget()
    layout = QVBoxLayout(main_window)

    comment_section = CommentSection(comments_data)
    layout.addWidget(comment_section)

    main_window.setWindowTitle("Nested Comments Example")
    main_window.show()
    sys.exit(app.exec())
