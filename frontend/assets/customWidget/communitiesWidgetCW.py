import os
from PySide6.QtWidgets import QWidget

import image_utils
from image_config import ImageType
from frontend.UserInterface.HomePageUI.UserInterfaceFile.CommunitiesWidgetView import Ui_CommunitiesWidget


def get_absolute_file_path(relative_path):
    """Returns the absolute path to a file relative to the project."""
    base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class CommunityWidget(QWidget):
    def __init__(self, communityName, icon=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_CommunitiesWidget()
        self.ui.setupUi(self)
        self.ui.communityName.setText(communityName)

        if icon :
            image_utils.set_configured_image(
                item=self.ui.icon,
                image_name=icon,
                image_type=ImageType.COMMUNITY_AVATAR,
                item_type="label"
            )



