from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class PostWidget(QWidget):
    def __init__(self, title, image_path=None):
        super().__init__()
        self.title = title
        self.image_path = image_path
        self.set_ui_properties()
        self.create_layout()

    def set_ui_properties(self):
        """Setează proprietățile vizuale ale postării."""
        self.setStyleSheet("padding: 5px; margin: 5px; color: white;")
        # Asigurăm că widget-ul are o dimensiune flexibilă în scroll
        self.setFixedWidth(1000)  # Lățime fixă pentru postare, dar înălțimea va fi flexibilă

    def create_layout(self):
        """Creează layout-ul pentru postare folosind poziții absolute."""
        layout = QVBoxLayout(self)  # Folosim un layout vertical pentru widget-ul postării
        layout.setContentsMargins(0, 0, 0, 0)  # Eliminăm margini suplimentare pentru layout

        # Titlul postării
        title_label = QLabel(f"{self.title}", self)
        title_label.setStyleSheet("font-weight: bold; font-size: 20px;")  # Stilizare titlu: Bold și mărire font
        layout.addWidget(title_label)

        # Dacă există o imagine, o adăugăm
        if self.image_path:
            image_label = QLabel(self)
            pixmap = QPixmap(self.image_path)

            # Verificăm dacă pixmap-ul a fost încărcat corect
            if not pixmap.isNull():
                # Redimensionăm imaginea astfel încât să nu depășească dimensiunea maximă
                pixmap = pixmap.scaled(800, 600, Qt.AspectRatioMode.KeepAspectRatio)
                image_label.setPixmap(pixmap)
                layout.addWidget(image_label)
            else:
                print(f"Failed to load image from path: {self.image_path}")  # Verificăm dacă imaginea a fost încărcată corect

        # Aplicăm layout-ul
        self.setLayout(layout)

    def update_content(self, new_title):
        """Permite actualizarea titlului postării."""
        self.title = new_title
        self.create_layout()  # Re-creăm layout-ul pentru a include titlul actualizat
