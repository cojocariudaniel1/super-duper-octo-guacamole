# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OnlineFriendsWidget.ui'
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
    QLayout, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_onlineFriendsWidget(object):
    def setupUi(self, onlineFriendsWidget):
        if not onlineFriendsWidget.objectName():
            onlineFriendsWidget.setObjectName(u"onlineFriendsWidget")
        onlineFriendsWidget.resize(204, 75)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(onlineFriendsWidget.sizePolicy().hasHeightForWidth())
        onlineFriendsWidget.setSizePolicy(sizePolicy)
        onlineFriendsWidget.setMinimumSize(QSize(204, 75))
        onlineFriendsWidget.setMaximumSize(QSize(204, 16777215))
        onlineFriendsWidget.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.verticalLayout = QVBoxLayout(onlineFriendsWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(onlineFriendsWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(204, 75))
        self.frame.setMaximumSize(QSize(204, 75))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.reply_icon = QLabel(self.frame)
        self.reply_icon.setObjectName(u"reply_icon")
        self.reply_icon.setGeometry(QRect(10, 42, 41, 31))
        self.reply_icon.setPixmap(QPixmap(u"../../../images/icon_arrow.png"))
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 50, 121, 22))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(u"font: 500 12pt \"Raleway\";\n"
"\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.lineEdit.setFrame(False)
        self.inputBackground = QLabel(self.frame)
        self.inputBackground.setObjectName(u"inputBackground")
        self.inputBackground.setGeometry(QRect(55, 50, 141, 24))
        self.inputBackground.setStyleSheet(u"min-width: 106;\n"
"min-height: 24;\n"
"max-height:24;")
        self.inputBackground.setPixmap(QPixmap(u"../../../images/Rectangle 25.png"))
        self.inputBackground.setScaledContents(True)
        self.pointsLabel = QLabel(self.frame)
        self.pointsLabel.setObjectName(u"pointsLabel")
        self.pointsLabel.setGeometry(QRect(0, 30, 201, 21))
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
"padding-left:35px;\n"
"color: #D9D9D9;\n"
"\n"
"")
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 201, 33))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon = QLabel(self.layoutWidget)
        self.icon.setObjectName(u"icon")
        self.icon.setMaximumSize(QSize(32, 31))
        self.icon.setPixmap(QPixmap(u"../../../images/userIcon1.png"))
        self.icon.setScaledContents(False)

        self.horizontalLayout.addWidget(self.icon)

        self.username = QLabel(self.layoutWidget)
        self.username.setObjectName(u"username")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy1)
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
        self.username.setScaledContents(True)
        self.username.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout.addWidget(self.username)

        self.circle = QLabel(self.layoutWidget)
        self.circle.setObjectName(u"circle")
        self.circle.setMaximumSize(QSize(15, 15))
        self.circle.setStyleSheet(u"")
        self.circle.setFrameShadow(QFrame.Shadow.Plain)
        self.circle.setPixmap(QPixmap(u"../../../images/greenCircle.png"))
        self.circle.setScaledContents(True)

        self.horizontalLayout.addWidget(self.circle)

        self.frame_2 = QFrame(self.layoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        self.layoutWidget.raise_()
        self.reply_icon.raise_()
        self.inputBackground.raise_()
        self.lineEdit.raise_()
        self.pointsLabel.raise_()

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(onlineFriendsWidget)

        QMetaObject.connectSlotsByName(onlineFriendsWidget)
    # setupUi

    def retranslateUi(self, onlineFriendsWidget):
        onlineFriendsWidget.setWindowTitle(QCoreApplication.translate("onlineFriendsWidget", u"Form", None))
        self.reply_icon.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("onlineFriendsWidget", u"Send a chat", None))
        self.inputBackground.setText("")
        self.pointsLabel.setText(QCoreApplication.translate("onlineFriendsWidget", u"102 points", None))
        self.icon.setText("")
        self.username.setText(QCoreApplication.translate("onlineFriendsWidget", u"Gaudy3!p", None))
        self.circle.setText("")
    # retranslateUi

