import logging
import os
from PySide6.QtWidgets import QWidget, QPushButton, QLabel
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QFile


import image_utils
from frontend.assets.UserInterface.HomePageUI.UserInterfaceFile.PopularHashTags import Ui_PopularHashTagsWidget
from image_config import ImageType


class PopularHashTagsWidget(QWidget):
    def __init__(self, tagName,parent=None):
        super().__init__(parent)
        self.ui = Ui_PopularHashTagsWidget()
        self.ui.setupUi(self)
        # Exemple de folosire (poți elimina dacă nu ai nevoie aici)
        self.ui.tagName.setText(tagName)

