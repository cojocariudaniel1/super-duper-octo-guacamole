# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreatePostView.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFontComboBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QToolBar, QVBoxLayout, QWidget)

class Ui_CreatePostView(object):
    def setupUi(self, CreatePostView):
        if not CreatePostView.objectName():
            CreatePostView.setObjectName(u"CreatePostView")
        CreatePostView.resize(800, 600)
        self.boldAction = QAction(CreatePostView)
        self.boldAction.setObjectName(u"boldAction")
        self.boldAction.setCheckable(True)
        font = QFont()
        font.setFamilies([u"Raleway"])
        font.setPointSize(11)
        font.setBold(True)
        self.boldAction.setFont(font)
        self.italicAction = QAction(CreatePostView)
        self.italicAction.setObjectName(u"italicAction")
        self.italicAction.setCheckable(True)
        self.italicAction.setFont(font)
        self.underlineAction = QAction(CreatePostView)
        self.underlineAction.setObjectName(u"underlineAction")
        self.underlineAction.setCheckable(True)
        self.underlineAction.setFont(font)
        self.strikeAction = QAction(CreatePostView)
        self.strikeAction.setObjectName(u"strikeAction")
        self.strikeAction.setCheckable(True)
        self.strikeAction.setFont(font)
        self.verticalLayout = QVBoxLayout(CreatePostView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleInput = QLineEdit(CreatePostView)
        self.titleInput.setObjectName(u"titleInput")
        self.titleInput.setStyleSheet(u"font: 14pt \"Raleway\"; padding: 10px; border-radius: 5px; border: 1px solid #ccc; color:white;")

        self.verticalLayout.addWidget(self.titleInput)

        self.fontSizeComboBox = QComboBox(CreatePostView)
        self.fontSizeComboBox.setObjectName(u"fontSizeComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontSizeComboBox.sizePolicy().hasHeightForWidth())
        self.fontSizeComboBox.setSizePolicy(sizePolicy)
        self.fontSizeComboBox.setMinimumSize(QSize(100, 0))
        self.fontSizeComboBox.setStyleSheet(u"    font: 500 11pt \"Raleway\";\n"
"    border: 2px solid rgb(85, 170, 255);  /* Border color */\n"
"    background-color: transparent;  /* Remove background */\n"
"    color: white;  /* Text color */")

        self.verticalLayout.addWidget(self.fontSizeComboBox)

        self.fontComboBox = QFontComboBox(CreatePostView)
        self.fontComboBox.setObjectName(u"fontComboBox")
        sizePolicy.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())
        self.fontComboBox.setSizePolicy(sizePolicy)
        self.fontComboBox.setMinimumSize(QSize(0, 30))
        self.fontComboBox.setStyleSheet(u"font: 500 11pt \"Raleway\"; color:white;")

        self.verticalLayout.addWidget(self.fontComboBox)

        self.formattingToolbar = QToolBar(CreatePostView)
        self.formattingToolbar.setObjectName(u"formattingToolbar")
        self.formattingToolbar.setStyleSheet(u"\n"
"       QToolBar {\n"
"           background: #f5f5f5;\n"
"           border-radius: 5px;\n"
"           padding: 5px;\n"
"           spacing: 5px;\n"
"       }\n"
"       QToolButton {\n"
"           background: transparent;\n"
"           border: 1px solid #ccc;\n"
"           border-radius: 3px;\n"
"           padding: 5px;\n"
"       }\n"
"       QToolButton:hover {\n"
"           background: #e0e0e0;\n"
"       }\n"
"       QToolButton:pressed {\n"
"           background: #d0d0d0;\n"
"       }\n"
"      ")

        self.verticalLayout.addWidget(self.formattingToolbar)

        self.bodyInput = QTextEdit(CreatePostView)
        self.bodyInput.setObjectName(u"bodyInput")
        self.bodyInput.setStyleSheet(u"font: 12pt \"Raleway\"; padding: 10px; border-radius: 5px; border: 1px solid #ccc; color:white;")

        self.verticalLayout.addWidget(self.bodyInput)

        self.uploadImageButton = QPushButton(CreatePostView)
        self.uploadImageButton.setObjectName(u"uploadImageButton")
        self.uploadImageButton.setStyleSheet(u"font: 12pt \"Raleway\"; padding: 10px; border-radius: 5px; background-color: #0079D3; color: white;")

        self.verticalLayout.addWidget(self.uploadImageButton)

        self.imagePreview = QLabel(CreatePostView)
        self.imagePreview.setObjectName(u"imagePreview")
        self.imagePreview.setStyleSheet(u"border: 2px dashed #ccc; padding: 10px; border-radius: 5px;")
        self.imagePreview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.imagePreview)

        self.submitButton = QPushButton(CreatePostView)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setStyleSheet(u"font: 12pt \"Raleway\"; padding: 10px; border-radius: 5px; background-color: #0079D3; color: white;")

        self.verticalLayout.addWidget(self.submitButton)


        self.formattingToolbar.addAction(self.boldAction)
        self.formattingToolbar.addAction(self.italicAction)
        self.formattingToolbar.addAction(self.underlineAction)
        self.formattingToolbar.addAction(self.strikeAction)

        self.retranslateUi(CreatePostView)

        QMetaObject.connectSlotsByName(CreatePostView)
    # setupUi

    def retranslateUi(self, CreatePostView):
        CreatePostView.setWindowTitle(QCoreApplication.translate("CreatePostView", u"Create Post", None))
        self.boldAction.setText(QCoreApplication.translate("CreatePostView", u"Bold", None))
        self.boldAction.setIconText(QCoreApplication.translate("CreatePostView", u"B", None))
#if QT_CONFIG(tooltip)
        self.boldAction.setToolTip(QCoreApplication.translate("CreatePostView", u"Bold", None))
#endif // QT_CONFIG(tooltip)
        self.italicAction.setText(QCoreApplication.translate("CreatePostView", u"Italic", None))
        self.italicAction.setIconText(QCoreApplication.translate("CreatePostView", u"I", None))
#if QT_CONFIG(tooltip)
        self.italicAction.setToolTip(QCoreApplication.translate("CreatePostView", u"Italic", None))
#endif // QT_CONFIG(tooltip)
        self.underlineAction.setText(QCoreApplication.translate("CreatePostView", u"Underline", None))
        self.underlineAction.setIconText(QCoreApplication.translate("CreatePostView", u"U", None))
#if QT_CONFIG(tooltip)
        self.underlineAction.setToolTip(QCoreApplication.translate("CreatePostView", u"Underline", None))
#endif // QT_CONFIG(tooltip)
        self.strikeAction.setText(QCoreApplication.translate("CreatePostView", u"Strike", None))
        self.strikeAction.setIconText(QCoreApplication.translate("CreatePostView", u"S", None))
#if QT_CONFIG(tooltip)
        self.strikeAction.setToolTip(QCoreApplication.translate("CreatePostView", u"Strikethrough", None))
#endif // QT_CONFIG(tooltip)
        self.titleInput.setPlaceholderText(QCoreApplication.translate("CreatePostView", u"Title", None))
        self.bodyInput.setPlaceholderText(QCoreApplication.translate("CreatePostView", u"Text (optional)", None))
        self.uploadImageButton.setText(QCoreApplication.translate("CreatePostView", u"Upload Image", None))
        self.submitButton.setText(QCoreApplication.translate("CreatePostView", u"Submit", None))
    # retranslateUi

