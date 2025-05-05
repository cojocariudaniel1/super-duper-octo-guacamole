import logging
import sys
from PySide6.QtWidgets import QApplication, QMainWindow



from frontend.assets.UserInterface.loginUI.controller.login_window import LoginWindow
from neo4j_data.database_connect import Neo4jDriverSingleton

logging.basicConfig(
    level=logging.DEBUG,  # Afișează toate nivelurile de logging
    format='[%(levelname)s] %(asctime)s - %(name)s - %(message)s',
    datefmt='%H:%M:%S'
)
if __name__ == "__main__":
    # Inițializează conexiunea globală o singură dată
    Neo4jDriverSingleton(uri="bolt://localhost:7687", user="neo4j", password="12345678")

    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())




