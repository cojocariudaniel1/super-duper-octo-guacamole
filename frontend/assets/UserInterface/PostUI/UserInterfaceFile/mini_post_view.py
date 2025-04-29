# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mini_post_view.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MiniViewPost(object):
    def setupUi(self, MiniViewPost):
        if not MiniViewPost.objectName():
            MiniViewPost.setObjectName(u"MiniViewPost")
        MiniViewPost.resize(1206, 235)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MiniViewPost.sizePolicy().hasHeightForWidth())
        MiniViewPost.setSizePolicy(sizePolicy)
        MiniViewPost.setMinimumSize(QSize(0, 150))
        MiniViewPost.setMaximumSize(QSize(16777215, 16777215))
        MiniViewPost.setStyleSheet(u"background: #252526; border-radius: 8px; padding: 10px; margin: 5px; color: white;")
        self.postLayout = QVBoxLayout(MiniViewPost)
        self.postLayout.setObjectName(u"postLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.frame_2 = QFrame(MiniViewPost)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(400, 75))
        self.frame_2.setStyleSheet(u"background: #1A1A1B;\n"
"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.profileIcon = QLabel(self.frame_2)
        self.profileIcon.setObjectName(u"profileIcon")
        self.profileIcon.setGeometry(QRect(10, 10, 61, 51))
        self.profileIcon.setStyleSheet(u"background-color: rgb(255, 85, 255);")
        self.horizontalLayoutWidget = QWidget(self.frame_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(79, 10, 311, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 12pt \"Raleway\";")

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 12pt \"Raleway\";")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_2)

        self.title_label = QLabel(MiniViewPost)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setStyleSheet(u"font: 800 18pt \"Raleway\";")

        self.verticalLayout.addWidget(self.title_label)

        self.browserContent = QTextBrowser(MiniViewPost)
        self.browserContent.setObjectName(u"browserContent")
        self.browserContent.setStyleSheet(u"font: 14pt \"Raleway\";")

        self.verticalLayout.addWidget(self.browserContent)


        self.postLayout.addLayout(self.verticalLayout)


        self.retranslateUi(MiniViewPost)

        QMetaObject.connectSlotsByName(MiniViewPost)
    # setupUi

    def retranslateUi(self, MiniViewPost):
        self.profileIcon.setText("")
        self.label_2.setText(QCoreApplication.translate("MiniViewPost", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MiniViewPost", u"16 min. ago", None))
        self.title_label.setText(QCoreApplication.translate("MiniViewPost", u"TextLabel", None))
        self.browserContent.setHtml(QCoreApplication.translate("MiniViewPost", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Raleway'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt;\">Text</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        pass
    # retranslateUi

