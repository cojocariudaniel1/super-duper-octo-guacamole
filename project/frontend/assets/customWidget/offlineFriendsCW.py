import logging
import os
from PySide6.QtWidgets import QWidget, QPushButton, QLabel
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QFile

from frontend.assets.UserInterface.HomePageUI.UserInterfaceFile.OfflineFriendsWidget import Ui_offlineFriendsWidget


def get_absolute_file_path(relative_path):
    """Returnează calea absolută către un fișier relativ la proiect."""
    base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class OfflineFriendWidget(QWidget):
    def __init__(self, username, parent=None):
        super().__init__(parent)
        self.ui = Ui_offlineFriendsWidget()
        self.ui.setupUi(self)
        self.status = None
        # Exemple de folosire (poți elimina dacă nu ai nevoie aici)
        self.ui.username.setText(username)

        self.set_image(self.ui.icon, "userIcon1.png", False)
        self.set_image(self.ui.circle, "redEclipse.png", True)

        self.ui.username.adjustSize()


    def set_image(self, label: QLabel, image_name: str, scalling):
        """
        Setează o imagine pe un QLabel din folderul de assets.

        Args:
            label (QLabel): Label-ul țintă.
            image_name (str): Numele imaginii (ex: "avatar.png").
            :param scalling (bool): Imaginea va fi scalata
               """
        try:
            logging.debug("set_image in offlineFriendsCW")
            image_path = get_absolute_file_path(f"frontend/assets/images/{image_name}")

            if os.path.exists(image_path):
                pixmap = QPixmap(image_path)
                if not pixmap.isNull():
                    label.setPixmap(pixmap)
                    label.setScaledContents(scalling)
                    return

            print(f"[WARN] Image not found: {image_path}")
            label.setPixmap(QPixmap(label.size()))  # fallback blank
        except Exception as e:
            logging.critical(f"Unexpected error: {e}")