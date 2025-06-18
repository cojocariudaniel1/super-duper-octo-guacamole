import logging
import os
from PySide6.QtWidgets import QWidget, QPushButton, QLabel
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QFile

from frontend.assets.UserInterface.HomePageUI.UserInterfaceFile.OnlineFriendsWidget import Ui_onlineFriendsWidget
import image_utils
from image_config import ImageType

def get_absolute_file_path(relative_path):
    """Returnează calea absolută către un fișier relativ la proiect."""
    base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class OnlineFriendWidget(QWidget):
    def __init__(self, username,img=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_onlineFriendsWidget()
        self.ui.setupUi(self)
        self.status = None
        # Exemple de folosire (poți elimina dacă nu ai nevoie aici)
        self.ui.username.setText(username)
        if img:
            image_utils.set_configured_image(item=self.ui.icon, image_name=img, image_type=ImageType.USER_AVATAR, item_type="label")

        image_utils.set_image_default(self.ui.circle, "greenCircle.png", True)
        image_utils.set_image_default(self.ui.reply_icon, "icon_arrow.png", False)
        image_utils.set_image_default(self.ui.inputBackground, "Rectangle 25.png", False)
        self.ui.username.adjustSize()

