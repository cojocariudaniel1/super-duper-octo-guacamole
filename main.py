import sys
from PySide6.QtWidgets import QApplication

from frontend.UserInterface.loginUI.controller.login_window import LoginWindow
from backend.database_connect import Neo4jDriverSingleton


if __name__ == "__main__":
    # Inițializează conexiunea globală o singură dată
    Neo4jDriverSingleton(uri="bolt://localhost:7687", user="neo4j", password="12345678")

    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())




