import sys

from PySide6.QtWidgets import QApplication

from frontend.PySide6_GUI.login_window import LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    forum = LoginWindow()
    sys.exit(app.exec())