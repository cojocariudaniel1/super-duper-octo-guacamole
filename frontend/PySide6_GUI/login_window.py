from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit, QPushButton
import sys
from frontend.assets.ui_files.login_window import Ui_LoginPage
from neo4j_data.Repository.UserRepository import UserRepository
from neo4j_data.database_connect import Neo4jDriverSingleton

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginPage()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.createAccountButton.clicked.connect(self.create_account)

        self.driver = Neo4jDriverSingleton(uri="bolt://localhost:7687", user="neo4j", password="12345678")
        self.session = self.driver.session()
        self.user_repo = UserRepository(self.session)

        self.show()

    def login(self):
        username = self.ui.usernameInput.text().strip()  # Ensure no leading/trailing spaces
        password = self.ui.passwordInput.text().strip()  # Ensure no leading/trailing spaces

        user = self.user_repo.read(username)
        if user:
            stored_password = user['password']
            print(f"Debug: Stored password from DB: {stored_password}")

            if self.user_repo.check_password(stored_password, password):
                QMessageBox.information(self, "Login", "Login successful!")
            else:
                QMessageBox.warning(self, "Login", "Invalid password!")
                print(f"Debug: Entered password does not match stored password.")
        else:
            QMessageBox.warning(self, "Login", "User not found!")
            print(f"Debug: User not found in DB.")

    def create_account(self):
        """Create a new user account."""
        email = self.ui.usernameInput.text().strip()  # Assume you have an email input field
        password = self.ui.passwordInput.text().strip()  # Ensure no leading/trailing spaces

        # Check if the user already exists
        user = self.user_repo.read(email)
        if user:
            QMessageBox.warning(self, "Account", "Account already exists!")
        else:
            print(f"Debug: Storing plain text password: {password}")

            if self.user_repo.create(email, password):  # Store password as plain text
                QMessageBox.information(self, "Account", "Account created successfully!")
            else:
                QMessageBox.warning(self, "Account", "Error creating account!")
