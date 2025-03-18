from PySide6.QtWidgets import QWidget, QMessageBox
from frontend.assets.ui_files.HomePageUI.controller.dashboardWIndow import DashboardWindow
from frontend.assets.ui_files.loginUI.UserInterfaceFile.login import Ui_Form
from neo4j_data.Repository.UserRepository import UserRepository
from neo4j_data.database_connect import Neo4jDriverSingleton

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.new_window = None
        self.ui.loginButton.clicked.connect(self.login)

        # Use the singleton instance of the Neo4j driver
        self.driver = Neo4jDriverSingleton.get_instance()
        self.user_repo = UserRepository(self.driver)

        self.show()

    def login(self):
        username = self.ui.userNameInput.text().strip()
        password = self.ui.passwordInput.text().strip()

        # Retrieve the user from the database
        user = self.user_repo.read(username)

        if user:
            stored_password = user['password']
            print(f"Debug: Stored password from DB: {stored_password}")

            if self.user_repo.check_password(stored_password, password):
                self.hide()
                self.new_window = DashboardWindow()
                self.new_window.show()
            else:
                QMessageBox.warning(self, "Login", "Invalid password!")
                print(f"Debug: Entered password does not match stored password.")
        else:
            QMessageBox.warning(self, "Login", "User not found!")
            print(f"Debug: User not found in DB.")