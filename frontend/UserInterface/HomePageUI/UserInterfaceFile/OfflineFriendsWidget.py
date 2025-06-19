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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_offlineFriendsWidget(object):
    def setupUi(self, offlineFriendsWidget):
        if not offlineFriendsWidget.objectName():
            offlineFriendsWidget.setObjectName(u"offlineFriendsWidget")
        offlineFriendsWidget.resize(204, 63)
        offlineFriendsWidget.setMinimumSize(QSize(204, 0))
        offlineFriendsWidget.setMaximumSize(QSize(204, 16777215))
        offlineFriendsWidget.setStyleSheet(u"background-color: rgb(30, 30, 30,0);")
        self.verticalLayout = QVBoxLayout(offlineFriendsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(offlineFriendsWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(204, 45))
        self.frame.setMaximumSize(QSize(204, 45))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
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
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 191, 33))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon = QLabel(self.widget)
        self.icon.setObjectName(u"icon")
        self.icon.setMaximumSize(QSize(32, 31))
        self.icon.setPixmap(QPixmap(u"../../../assets/images/userIcon1.png"))
        self.icon.setScaledContents(False)

        self.horizontalLayout.addWidget(self.icon)

        self.username = QLabel(self.widget)
        self.username.setObjectName(u"username")
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

        self.horizontalLayout.addWidget(self.username)

        self.circle = QLabel(self.widget)
        self.circle.setObjectName(u"circle")
        self.circle.setMaximumSize(QSize(15, 15))
        self.circle.setStyleSheet(u"")
        self.circle.setFrameShadow(QFrame.Shadow.Plain)
        self.circle.setPixmap(QPixmap(u"../../../assets/images/redEclipse.png"))
        self.circle.setScaledContents(True)
        self.circle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.circle)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(offlineFriendsWidget)

        QMetaObject.connectSlotsByName(offlineFriendsWidget)
    # setupUi

    def retranslateUi(self, offlineFriendsWidget):
        offlineFriendsWidget.setWindowTitle(QCoreApplication.translate("offlineFriendsWidget", u"Form", None))
        self.pointsLabel.setText(QCoreApplication.translate("offlineFriendsWidget", u"102 points", None))
        self.icon.setText("")
        self.username.setText(QCoreApplication.translate("offlineFriendsWidget", u"Gaudy3!p", None))
        self.circle.setText("")
    # retranslateUi

