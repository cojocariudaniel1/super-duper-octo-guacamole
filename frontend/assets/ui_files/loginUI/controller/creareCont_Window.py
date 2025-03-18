from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from backend.global_path import get_absolute_file_path
import sys

from frontend.assets.ui_files.loginUI.UserInterfaceFile.registerPage import Ui_registerForm


class RegisterForm(QWidget):
    def __init__(self):
        super().__init__()

        # Încarcă fișierul .ui pentru RegisterForm
        loader = QUiLoader()
        self.ui = Ui_registerForm()
        self.ui.setupUi(self)

        # Inițializează conexiunea la Neo4j
        self.connector = Neo4jConnector("bolt://localhost:7687", "neo4j", "12345678")  # Modifică cu credențialele tale

        try:
            message = self.connector.test_connection()
            print(message)
        except Exception as e:
            QMessageBox.critical(self, "Connection Failed", str(e))
            sys.exit(1)

        # Conectează butonul de creare cont
        self.ui.registerButton.clicked.connect(self.create_account)

        # Conectează butonul de revenire la login
        # self.ui.backToLoginButton.clicked.connect(self.back_to_login)

        self.show()

    def create_account(self):
        """Creează un cont nou utilizator."""
        username = self.ui.userNameInput.text()
        email = self.ui.emailInput.text()
        password = self.ui.passwordInput.text()
        confirm_password = self.ui.repeatPasswordInput.text()

        if password != confirm_password:
            QMessageBox.warning(self, "Password Mismatch", "Passwords do not match. Please try again.")
            return

        # Verifică dacă utilizatorul există deja
        if self.connector.query_user_by_username(username):
            QMessageBox.warning(self, "Account Creation Failed", "Username already exists.")
        else:
            # Adaugă utilizatorul în baza de date
            self.connector.create_user(username, email, password)
            QMessageBox.information(self, "Account Created", "Your account has been created successfully!")
            self.back_to_login()

    def back_to_login(self):
        """Revine la fereastra de login."""
        # Logica pentru a închide acest formular și a reveni la login
        self.close()

    def closeEvent(self, event):
        """Închide conexiunea la Neo4j când fereastra este închisă."""
        self.connector.close()
        event.accept()


class Neo4jConnector:
    def __init__(self, uri, user, password):
        from neo4j import GraphDatabase
        self._uri = uri
        self._user = user
        self._password = password
        self._driver = GraphDatabase.driver(self._uri, auth=(self._user, self._password))

    def test_connection(self):
        """Testează conexiunea la baza de date Neo4j."""
        with self._driver.session() as session:
            result = session.run("RETURN 'Connection successful' AS message")
            return result.single()[0]

    def close(self):
        """Închide conexiunea la baza de date Neo4j."""
        self._driver.close()

    def query_user_by_username(self, username):
        """Căutăm un utilizator după username."""
        with self._driver.session() as session:
            query = "MATCH (u:User {username: $username}) RETURN u"
            result = session.run(query, username=username)
            return result.single()

    def create_user(self, username, email, password):
        """Creăm un nou utilizator în baza de date."""
        with self._driver.session() as session:
            query = """
            CREATE (u:User {username: $username, email: $email, password: $password})
            RETURN u
            """
            session.run(query, username=username, email=email, password=password)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    register_form = RegisterForm()
    sys.exit(app.exec())
