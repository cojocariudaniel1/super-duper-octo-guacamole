# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_DashBoardView(object):
    def setupUi(self, DashBoardView):
        if not DashBoardView.objectName():
            DashBoardView.setObjectName(u"DashBoardView")
        DashBoardView.resize(1440, 1024)
        DashBoardView.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        DashBoardView.setStyleSheet(u"background: #1A1A1B;")
        self.mainVerticalLayout = QVBoxLayout(DashBoardView)
        self.mainVerticalLayout.setObjectName(u"mainVerticalLayout")
        self.topNavBar = QWidget(DashBoardView)
        self.topNavBar.setObjectName(u"topNavBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topNavBar.sizePolicy().hasHeightForWidth())
        self.topNavBar.setSizePolicy(sizePolicy)
        self.topNavLayout = QHBoxLayout(self.topNavBar)
        self.topNavLayout.setObjectName(u"topNavLayout")
        self.logoLabel = QLabel(self.topNavBar)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setStyleSheet(u"color:white;")
        self.logoLabel.setPixmap(QPixmap(u"../../../images/logo.png"))

        self.topNavLayout.addWidget(self.logoLabel)

        self.searchBar = QLineEdit(self.topNavBar)
        self.searchBar.setObjectName(u"searchBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy1)
        self.searchBar.setMinimumSize(QSize(700, 0))
        self.searchBar.setMaximumSize(QSize(16777215, 38))
        self.searchBar.setStyleSheet(u"\n"
"border-radius: 6px;\n"
"background-color: rgb(85, 85, 85);\n"
"color:white;\n"
"margin-left: 80px;\n"
"")
        self.searchBar.setFrame(False)

        self.topNavLayout.addWidget(self.searchBar)

        self.pushButton_2 = QPushButton(self.topNavBar)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background: #1A1A1B;\n"
"\n"
"border-radius: 6px;")
        icon = QIcon()
        icon.addFile(u"../../../images/ButtonNotificationImage.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(35, 35))

        self.topNavLayout.addWidget(self.pushButton_2)

        self.frame = QFrame(self.topNavBar)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.topNavLayout.addWidget(self.frame)

        self.profileButton = QPushButton(self.topNavBar)
        self.profileButton.setObjectName(u"profileButton")
        self.profileButton.setStyleSheet(u"background: #1A1A1B;\n"
"\n"
"border-radius: 6px;")
        icon1 = QIcon()
        icon1.addFile(u"../../../images/UserSettings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileButton.setIcon(icon1)
        self.profileButton.setIconSize(QSize(43, 43))

        self.topNavLayout.addWidget(self.profileButton)

        self.pushButton = QPushButton(self.topNavBar)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background: #1A1A1B;\n"
"\n"
"border-radius: 6px;")
        icon2 = QIcon()
        icon2.addFile(u"../../../images/ProfileSettingsShortcut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(10, 25))

        self.topNavLayout.addWidget(self.pushButton)


        self.mainVerticalLayout.addWidget(self.topNavBar)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.leftSideBar = QWidget(DashBoardView)
        self.leftSideBar.setObjectName(u"leftSideBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leftSideBar.sizePolicy().hasHeightForWidth())
        self.leftSideBar.setSizePolicy(sizePolicy3)
        self.sidebarLayout = QVBoxLayout(self.leftSideBar)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.label = QLabel(self.leftSideBar)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 600 14pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sidebarLayout.addWidget(self.label)

        self.communityList = QListWidget(self.leftSideBar)
        self.communityList.setObjectName(u"communityList")

        self.sidebarLayout.addWidget(self.communityList)

        self.label_2 = QLabel(self.leftSideBar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 600 14pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sidebarLayout.addWidget(self.label_2)

        self.friendsList = QListWidget(self.leftSideBar)
        self.friendsList.setObjectName(u"friendsList")

        self.sidebarLayout.addWidget(self.friendsList)


        self.mainLayout.addWidget(self.leftSideBar)

        self.ContentPosts_ScrollArea = QScrollArea(DashBoardView)
        self.ContentPosts_ScrollArea.setObjectName(u"ContentPosts_ScrollArea")
        self.ContentPosts_ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 858, 931))
        self.postsLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.postsLayout.setObjectName(u"postsLayout")
        self.postsLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.ContentPosts_ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.mainLayout.addWidget(self.ContentPosts_ScrollArea)

        self.rightSideBar = QWidget(DashBoardView)
        self.rightSideBar.setObjectName(u"rightSideBar")
        sizePolicy3.setHeightForWidth(self.rightSideBar.sizePolicy().hasHeightForWidth())
        self.rightSideBar.setSizePolicy(sizePolicy3)
        self.rightsidebarLayout = QVBoxLayout(self.rightSideBar)
        self.rightsidebarLayout.setObjectName(u"rightsidebarLayout")
        self.recentPostsList = QListWidget(self.rightSideBar)
        self.recentPostsList.setObjectName(u"recentPostsList")

        self.rightsidebarLayout.addWidget(self.recentPostsList)


        self.mainLayout.addWidget(self.rightSideBar)


        self.mainVerticalLayout.addLayout(self.mainLayout)


        self.retranslateUi(DashBoardView)

        QMetaObject.connectSlotsByName(DashBoardView)
    # setupUi

    def retranslateUi(self, DashBoardView):
        self.logoLabel.setText("")
        self.searchBar.setPlaceholderText(QCoreApplication.translate("DashBoardView", u"Search...", None))
        self.pushButton_2.setText("")
        self.profileButton.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("DashBoardView", u"Communities", None))
        self.label_2.setText(QCoreApplication.translate("DashBoardView", u"Frieends", None))
        pass
    # retranslateUi

