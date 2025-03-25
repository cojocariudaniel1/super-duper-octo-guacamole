import sys
from PySide6.QtWidgets import QApplication, QMainWindow


from frontend.assets.ui_files.loginUI.controller.noLoginWindow import NoLoginWindow
from neo4j_data.database_connect import Neo4jDriverSingleton

if __name__ == "__main__":
    # Inițializează conexiunea globală o singură dată
    Neo4jDriverSingleton(uri="bolt://localhost:7687", user="neo4j", password="12345678")

    app = QApplication(sys.argv)
    window = NoLoginWindow()
    window.show()
    sys.exit(app.exec())




