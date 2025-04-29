# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'commentsView.ui'
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
    QLayout, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MiniViewPost(object):
    def setupUi(self, MiniViewPost):
        if not MiniViewPost.objectName():
            MiniViewPost.setObjectName(u"MiniViewPost")
        MiniViewPost.resize(1206, 568)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MiniViewPost.sizePolicy().hasHeightForWidth())
        MiniViewPost.setSizePolicy(sizePolicy)
        MiniViewPost.setMinimumSize(QSize(0, 200))
        MiniViewPost.setMaximumSize(QSize(16777215, 16777215))
        MiniViewPost.setStyleSheet(u"background: #252526; border-radius: 8px; padding: 10px; margin: 5px; color: white;")
        self.postLayout = QVBoxLayout(MiniViewPost)
        self.postLayout.setObjectName(u"postLayout")
        self.postLayout.setContentsMargins(0, 0, 0, 0)
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
        self.userNameLabel = QLabel(self.horizontalLayoutWidget)
        self.userNameLabel.setObjectName(u"userNameLabel")

        self.horizontalLayout.addWidget(self.userNameLabel)

        self.timeOfThePost = QLabel(self.horizontalLayoutWidget)
        self.timeOfThePost.setObjectName(u"timeOfThePost")

        self.horizontalLayout.addWidget(self.timeOfThePost)


        self.verticalLayout.addWidget(self.frame_2)

        self.contentFrame = QFrame(MiniViewPost)
        self.contentFrame.setObjectName(u"contentFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.contentFrame.sizePolicy().hasHeightForWidth())
        self.contentFrame.setSizePolicy(sizePolicy2)
        self.contentFrame.setMinimumSize(QSize(0, 400))
        self.contentFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.contentLayout = QVBoxLayout()
        self.contentLayout.setObjectName(u"contentLayout")

        self.verticalLayout_2.addLayout(self.contentLayout)


        self.verticalLayout.addWidget(self.contentFrame)

        self.buttonsBar = QFrame(MiniViewPost)
        self.buttonsBar.setObjectName(u"buttonsBar")
        self.buttonsBar.setMinimumSize(QSize(75, 75))
        self.buttonsBar.setMaximumSize(QSize(16777215, 75))
        self.buttonsBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.buttonsBar.setFrameShadow(QFrame.Shadow.Raised)
        self.button1 = QLabel(self.buttonsBar)
        self.button1.setObjectName(u"button1")
        self.button1.setGeometry(QRect(20, 15, 45, 45))
        sizePolicy1.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy1)
        self.button1.setMinimumSize(QSize(45, 45))
        self.button1.setMaximumSize(QSize(45, 45))
        self.button1.setStyleSheet(u"background-color: rgb(255, 85, 255);")
        self.button2 = QLabel(self.buttonsBar)
        self.button2.setObjectName(u"button2")
        self.button2.setGeometry(QRect(70, 15, 45, 45))
        sizePolicy1.setHeightForWidth(self.button2.sizePolicy().hasHeightForWidth())
        self.button2.setSizePolicy(sizePolicy1)
        self.button2.setMinimumSize(QSize(45, 45))
        self.button2.setMaximumSize(QSize(45, 45))
        self.button2.setStyleSheet(u"background-color: rgb(255, 85, 255);")
        self.button3 = QLabel(self.buttonsBar)
        self.button3.setObjectName(u"button3")
        self.button3.setGeometry(QRect(120, 15, 45, 45))
        sizePolicy1.setHeightForWidth(self.button3.sizePolicy().hasHeightForWidth())
        self.button3.setSizePolicy(sizePolicy1)
        self.button3.setMinimumSize(QSize(45, 45))
        self.button3.setMaximumSize(QSize(45, 45))
        self.button3.setStyleSheet(u"background-color: rgb(255, 85, 255);")
        self.button4 = QLabel(self.buttonsBar)
        self.button4.setObjectName(u"button4")
        self.button4.setGeometry(QRect(170, 15, 45, 45))
        sizePolicy1.setHeightForWidth(self.button4.sizePolicy().hasHeightForWidth())
        self.button4.setSizePolicy(sizePolicy1)
        self.button4.setMinimumSize(QSize(45, 45))
        self.button4.setMaximumSize(QSize(45, 45))
        self.button4.setStyleSheet(u"background-color: rgb(255, 85, 255);")

        self.verticalLayout.addWidget(self.buttonsBar)


        self.postLayout.addLayout(self.verticalLayout)


        self.retranslateUi(MiniViewPost)

        QMetaObject.connectSlotsByName(MiniViewPost)
    # setupUi

    def retranslateUi(self, MiniViewPost):
        self.profileIcon.setText("")
        self.userNameLabel.setText(QCoreApplication.translate("MiniViewPost", u"TextLabel", None))
        self.timeOfThePost.setText(QCoreApplication.translate("MiniViewPost", u"16 min. ago", None))
        self.button1.setText(QCoreApplication.translate("MiniViewPost", u"A", None))
        self.button2.setText(QCoreApplication.translate("MiniViewPost", u"B", None))
        self.button3.setText(QCoreApplication.translate("MiniViewPost", u"C", None))
        self.button4.setText(QCoreApplication.translate("MiniViewPost", u"D", None))
        pass
    # retranslateUi

