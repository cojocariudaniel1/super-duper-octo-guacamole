from PySide6.QtWidgets import QWidget, QMessageBox

from frontend.assets.ui_files.loginUI.UserInterfaceFile.noLoginPage import Ui_noLoginWindow
from frontend.assets.ui_files.loginUI.controller.creareCont_Window import RegisterForm
from frontend.assets.ui_files.loginUI.controller.login_window import LoginWindow


class NoLoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_noLoginWindow()
        self.ui.setupUi(self)
        self.new_window = None
        self.ui.loginButton.clicked.connect(self.goToLoginPage)
        self.ui.registerButton.clicked.connect(self.goToRegisterPage)

        self.show()


    def goToLoginPage(self):
        self.new_window = LoginWindow()
        self.close()
        self.new_window.show()

    def goToRegisterPage(self):
        self.new_window = RegisterForm()
        self.close()
        self.new_window.show()