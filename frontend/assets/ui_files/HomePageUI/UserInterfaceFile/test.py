import sys

from PySide6.QtWidgets import QApplication

from frontend.assets.ui_files.loginUI.controller.noLoginWindow import NoLoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NoLoginWindow()
    window.show()
    sys.exit(app.exec())