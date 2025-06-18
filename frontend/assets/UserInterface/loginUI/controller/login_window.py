from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import QThread, Signal
from frontend.assets.UserInterface.HomePageUI.controller.dashboardWIndow import DashboardWindow
from frontend.assets.UserInterface.HomePageUI.controller.mainwindow import MainWindow

from frontend.assets.UserInterface.loginUI.UserInterfaceFile.login import Ui_Form
from neo4j_data.Repository.UserRepository import UserRepository
from neo4j_data.database_connect import Neo4jDriverSingleton
from neo4j_data.Repository.SessionRepository import SessionRepository


class QueryThread(QThread):
    # Signal to return the query result back to the main thread
    finished = Signal(dict)

    def __init__(self, username, password, user_repo):
        super().__init__()
        self.username = username
        self.password = password
        self.user_repo = user_repo
        self.session_id = None  # Store active session ID

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
        self.session_repo = SessionRepository(self.driver)
        self.session_id = None  # Store active session ID

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
            password = self.ui.passwordInput.text().strip()

            if self.user_repo.check_password(stored_password, password):
                try:
                    # Create a new session
                    self.session_id = self.session_repo.create_session(user["id"])
                    print(f"Session started: {self.session_id}")
                except Exception as e:
                    QMessageBox.critical(self, "Session Error", f"Failed to create session: {str(e)}")
                    return

                self.hide()
                self.new_window = MainWindow(user["id"], self.session_id)
                self.new_window.show()
            else:
                QMessageBox.warning(self, "Login", "Invalid password!")
        else:
            QMessageBox.warning(self, "Login", "User not found!")
