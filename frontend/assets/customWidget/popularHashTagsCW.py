from PySide6.QtWidgets import QWidget

from frontend.UserInterface.HomePageUI.UserInterfaceFile.PopularHashTags import Ui_PopularHashTagsWidget


class PopularHashTagsWidget(QWidget):
    def __init__(self, tagName,parent=None):
        super().__init__(parent)
        self.ui = Ui_PopularHashTagsWidget()
        self.ui.setupUi(self)
        # Exemple de folosire (poți elimina dacă nu ai nevoie aici)
        self.ui.tagName.setText(tagName)

