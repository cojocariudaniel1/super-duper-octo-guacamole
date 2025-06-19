import os
from PySide6.QtWidgets import QWidget

import image_utils
from frontend.UserInterface.HomePageUI.UserInterfaceFile.OfflineFriendsWidget import Ui_offlineFriendsWidget
from image_config import ImageType


def get_absolute_file_path(relative_path):
    """Returnează calea absolută către un fișier relativ la proiect."""
    base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class OfflineFriendWidget(QWidget):
    def __init__(self, username, points, img, parent=None):
        super().__init__(parent)
        self.ui = Ui_offlineFriendsWidget()
        self.ui.setupUi(self)
        self.status = None
        # Exemple de folosire (poți elimina dacă nu ai nevoie aici)
        self.ui.username.setText(username)
        self.ui.pointsLabel.setText(  "points: " + str(points))

        if img:
            image_utils.set_configured_image(item=self.ui.icon, image_name=img, image_type=ImageType.USER_AVATAR,
                                             item_type="label")
        image_utils.set_image_default(self.ui.circle, "redEclipse.png", True)
        self.ui.username.adjustSize()


