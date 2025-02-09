from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QScrollArea, QFrame
from PySide6.QtUiTools import QUiLoader
from backend.global_path import get_absolute_file_path
from frontend.assets.prefabs_ui.prefab_postsLabel import PostWidget
import sys

class ForumApp(QWidget):
    def __init__(self):
        super().__init__()

        # Încarcă fișierul .ui
        loader = QUiLoader()
        self.ui = loader.load(get_absolute_file_path(r"frontend\assets\ui_files\test.ui"), self)

        # Obține referința către ScrollArea
        self.scroll_area = self.ui.findChild(QScrollArea, "ContentPosts_ScrollArea")
        self.scroll_area.setWidgetResizable(True)  # Permite ajustarea conținutului
        self.scroll_area.setStyleSheet("""
            QScrollBar:vertical {
                background: #2e2e2e;  /* Fundalul barei de scroll */
                width: 12px;  /* Lățimea barei */
                border-radius: 6px;  /* Colțuri rotunjite */
            }

            QScrollBar::handle:vertical {
                background: #5a5a5a;  /* Culoarea mânerului (partea care se mișcă) */
                border-radius: 6px;
            }

            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: #2e2e2e;  /* Liniile de la capetele barei */
                height: 0px;
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: #3a3a3a;  /* Zona de fundal care nu este selectată */
            }
        """)

        # Obține widget-ul care conține postările
        self.scroll_content = self.ui.findChild(QWidget, "scrollAreaWidgetContents")
        self.posts_layout = self.ui.findChild(QVBoxLayout, "postsLayout")

        # Asigură-te că layout-ul este corect setat pe scroll_content
        self.scroll_content.setLayout(self.posts_layout)

        # **Setează o dimensiune inițială mai mare pentru scroll content**
        self.scroll_content.setMinimumHeight(0)  # Crește înălțimea ca să forțeze scroll

        # Adaugă postări de test
        for i in range(20):  # Adaugă mai multe postări pentru a verifica scroll-ul
            title = f"Post {i + 1}"
            # Verificăm dacă indexul postării (i+1) este impar
            if (i + 1) % 2 != 0:
                # Dacă postarea are număr impar, adăugăm o imagine
                image_path = get_absolute_file_path("frontend/assets/images/img2.png")
                self.add_post(title, image_path)
            else:
                # Dacă numărul este par, adăugăm postarea fără imagine
                self.add_post(title, None)

        self.show()

    def add_post(self, title,  image_path=None):
        """Adaugă o postare nouă în layout."""
        post_widget = PostWidget(title,image_path)
        self.posts_layout.addWidget(post_widget)
        self.posts_layout.update()  # Actualizează layout-ul

if __name__ == "__main__":
    app = QApplication(sys.argv)
    forum = ForumApp()
    sys.exit(app.exec())
