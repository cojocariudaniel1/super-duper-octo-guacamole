# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OnlineFriendsWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(244, 90)
        Form.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 261, 121))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.icon = QLabel(self.frame)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(0, 0, 31, 31))
        self.icon.setPixmap(QPixmap(u"../../../images/userIcon1.png"))
        self.icon.setScaledContents(False)
        self.username = QLabel(self.frame)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(42, 5, 91, 21))
        self.username.setStyleSheet(u"/* Gaudy3!p */\n"
"\n"
"position: absolute;\n"
"width: 44px;\n"
"height: 15px;\n"
"left: 70px;\n"
"top: 576.64px;\n"
"\n"
"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"line-height: 8px;\n"
"\n"
"color: #D9D9D9;\n"
"\n"
"")
        self.circle = QLabel(self.frame)
        self.circle.setObjectName(u"circle")
        self.circle.setGeometry(QRect(117, 9, 15, 15))
        self.circle.setMaximumSize(QSize(16777215, 16777215))
        self.circle.setStyleSheet(u"")
        self.circle.setFrameShadow(QFrame.Shadow.Plain)
        self.circle.setPixmap(QPixmap(u"../../../images/greenCircle.png"))
        self.circle.setScaledContents(True)
        self.reply_icon = QLabel(self.frame)
        self.reply_icon.setObjectName(u"reply_icon")
        self.reply_icon.setGeometry(QRect(10, 42, 41, 31))
        self.reply_icon.setPixmap(QPixmap(u"../../../images/icon_arrow.png"))
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 50, 161, 22))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"/* Send a chat */\n"
"\n"
"position: absolute;\n"
"width: 43.73px;\n"
"height: 7px;\n"
"left: 75.19px;\n"
"top: 608px;\n"
"\n"
"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"line-height: 6px;\n"
"\n"
"color: #C0C0C0;\n"
"\n"
"")
        self.lineEdit.setFrame(False)
        self.inputBackground = QLabel(self.frame)
        self.inputBackground.setObjectName(u"inputBackground")
        self.inputBackground.setGeometry(QRect(55, 50, 181, 24))
        self.inputBackground.setStyleSheet(u"min-width: 106;\n"
"min-height: 24;\n"
"max-height:24;")
        self.inputBackground.setPixmap(QPixmap(u"../../../images/Rectangle 25.png"))
        self.inputBackground.setScaledContents(True)
        self.pointsLabel = QLabel(self.frame)
        self.pointsLabel.setObjectName(u"pointsLabel")
        self.pointsLabel.setGeometry(QRect(41, 21, 101, 21))
        self.pointsLabel.setStyleSheet(u"/* 102 points */\n"
"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"position: absolute;\n"
"width: 33px;\n"
"height: 14px;\n"
"left: 70px;\n"
"top: 706.64px;\n"
"\n"
"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 12px;\n"
"line-height: 6px;\n"
"\n"
"color: #D9D9D9;\n"
"\n"
"")
        self.icon.raise_()
        self.username.raise_()
        self.circle.raise_()
        self.reply_icon.raise_()
        self.inputBackground.raise_()
        self.lineEdit.raise_()
        self.pointsLabel.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.icon.setText("")
        self.username.setText(QCoreApplication.translate("Form", u"Gaudy3!p", None))
        self.circle.setText("")
        self.reply_icon.setText("")
        self.inputBackground.setText("")
        self.pointsLabel.setText(QCoreApplication.translate("Form", u"102 points", None))
    # retranslateUi

