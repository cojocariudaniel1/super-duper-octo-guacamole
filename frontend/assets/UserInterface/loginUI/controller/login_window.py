from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import QThread, Signal
from frontend.assets.UserInterface.HomePageUI.controller.dashboardWIndow import DashboardWindow
from frontend.assets.UserInterface.HomePageUI.controller.mainwindow import MainWindow

from frontend.assets.UserInterface.loginUI.UserInterfaceFile.login import Ui_Form
from neo4j_data.Repository.UserRepository import UserRepository
from neo4j_data.database_connect import Neo4jDriverSingleton


class QueryThread(QThread):
    # Signal to return the query result back to the main thread
    finished = Signal(dict)

    def __init__(self, username, password, user_repo):
        super().__init__()
        self.username = username
        self.password = password
        self.user_repo = user_repo

    def run(self):
        """Run the query in the background."""
        user = self.user_repo.read(self.username)  # Perform the query
        self.finished.emit(user)  # Emit the result to the main thread


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.new_window = None
        self.ui.loginButton.clicked.connect(self.start_login)

        # Use the singleton instance of the Neo4j driver
        self.driver = Neo4jDriverSingleton.get_driver()
        self.user_repo = UserRepository(self.driver)

        # Add the loading bar
        self.ui.usernameInput.setText("user38599@topikka.com")
        self.ui.passwordInput.setText("hashed_password")
        self.show()

    def start_login(self):
        """Start the login process with a loading animation."""

        # Get the username and password
        username = self.ui.usernameInput.text().strip()

        password = self.ui.passwordInput.text().strip()

        # Start the query in a separate thread
        self.query_thread = QueryThread(username, password, self.user_repo)
        self.query_thread.finished.connect(self.process_login)  # Connect the result to the handler
        self.query_thread.start()  # Start the query thread

    def process_login(self, user):
        """Perform the actual login process after the query is completed."""

        if user:
            stored_password = user['password']
            print(f"Debug: Stored password from DB: {stored_password}")

            # Check the password
            password = self.ui.passwordInput.text().strip()
            if self.user_repo.check_password(stored_password, password):

                self.hide()
                self.new_window = MainWindow(user["id"])
                self.new_window.show()
            else:
                QMessageBox.warning(self, "Login", "Invalid password!")
                print(f"Debug: Entered password does not match stored password.")
        else:
            QMessageBox.warning(self, "Login", "User not found!")
            print(f"Debug: User not found in DB.")
