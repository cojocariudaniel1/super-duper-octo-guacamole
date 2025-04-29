# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OfflineFriendsWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(244, 41)
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
        self.circle.setPixmap(QPixmap(u"../../../images/redEclipse.png"))
        self.circle.setScaledContents(True)
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.icon.setText("")
        self.username.setText(QCoreApplication.translate("Form", u"Gaudy3!p", None))
        self.circle.setText("")
        self.pointsLabel.setText(QCoreApplication.translate("Form", u"102 points", None))
    # retranslateUi

