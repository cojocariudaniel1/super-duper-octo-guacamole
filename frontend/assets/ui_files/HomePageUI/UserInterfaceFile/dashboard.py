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
"border-radius: 6px;")
        icon1 = QIcon()
        icon1.addFile(u"../../../images/UserSettings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileButton.setIcon(icon1)
        self.profileButton.setIconSize(QSize(43, 43))

        self.topNavLayout.addWidget(self.profileButton)

        self.pushButton = QPushButton(self.topNavBar)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background: #1A1A1B;\n"
"border-radius: 6px;")
        icon2 = QIcon()
        icon2.addFile(u"../../../images/ProfileSettingsShortcut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(10, 25))

        self.topNavLayout.addWidget(self.pushButton)


        self.mainVerticalLayout.addWidget(self.topNavBar)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.leftSideBar = QWidget(DashBoardView)
        self.leftSideBar.setObjectName(u"leftSideBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leftSideBar.sizePolicy().hasHeightForWidth())
        self.leftSideBar.setSizePolicy(sizePolicy3)
        self.leftSideBar.setMinimumSize(QSize(300, 0))
        self.leftSideBar.setMaximumSize(QSize(300, 16777215))
        self.leftSideBar.setStyleSheet(u"border-color: rgb(195, 195, 195);\n"
"border-top:1px solid white;\n"
"border-right:1px solid white;")
        self.sidebarLayout = QVBoxLayout(self.leftSideBar)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.logoLabel = QLabel(self.leftSideBar)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setStyleSheet(u"color:white;")
        self.logoLabel.setPixmap(QPixmap(u"../../../images/logo.png"))

        self.sidebarLayout.addWidget(self.logoLabel)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 12)
        self.label = QLabel(self.leftSideBar)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"margin-left: 30px;\n"
"border:0px;\n"
"color: #C0C0C0;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.leftSideBar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"margin-left: 30px;\n"
"border-color: rgb(195, 195, 195);\n"
"border:0px;;\n"
"color: #C0C0C0;")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.leftSideBar)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"margin-left: 30px;\n"
"border:0px;;\n"
"color: #C0C0C0;")

        self.verticalLayout.addWidget(self.label_4)


        self.sidebarLayout.addLayout(self.verticalLayout)

        self.label_2 = QLabel(self.leftSideBar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(256, 0))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 600 14pt \"Segoe UI\";\n"
"border:0px;;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sidebarLayout.addWidget(self.label_2)

        self.frame_2 = QFrame(self.leftSideBar)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setStyleSheet(u"border:0px;;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.sidebarLayout.addWidget(self.frame_2)


        self.mainLayout.addWidget(self.leftSideBar)

        self.middleBar = QWidget(DashBoardView)
        self.middleBar.setObjectName(u"middleBar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.middleBar.sizePolicy().hasHeightForWidth())
        self.middleBar.setSizePolicy(sizePolicy5)
        self.middleBar.setStyleSheet(u"background: transparent;")
        self.middleBarLayout = QVBoxLayout(self.middleBar)
        self.middleBarLayout.setSpacing(0)
        self.middleBarLayout.setObjectName(u"middleBarLayout")
        self.ContentPosts_ScrollArea = QScrollArea(self.middleBar)
        self.ContentPosts_ScrollArea.setObjectName(u"ContentPosts_ScrollArea")
        self.ContentPosts_ScrollArea.setStyleSheet(u"border: none; background: transparent;")
        self.ContentPosts_ScrollArea.setWidgetResizable(True)
        self.ContentPosts_ScrollArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 758, 835))
        self.postsLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.postsLayout.setSpacing(20)
        self.postsLayout.setObjectName(u"postsLayout")
        self.postsLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.ContentPosts_ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.middleBarLayout.addWidget(self.ContentPosts_ScrollArea)


        self.mainLayout.addWidget(self.middleBar)

        self.rightSideBar = QWidget(DashBoardView)
        self.rightSideBar.setObjectName(u"rightSideBar")
        sizePolicy3.setHeightForWidth(self.rightSideBar.sizePolicy().hasHeightForWidth())
        self.rightSideBar.setSizePolicy(sizePolicy3)
        self.rightSideBar.setMinimumSize(QSize(300, 0))
        self.rightSideBar.setMaximumSize(QSize(300, 16777215))
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
        self.searchBar.setPlaceholderText(QCoreApplication.translate("DashBoardView", u"Search...", None))
        self.pushButton_2.setText("")
        self.profileButton.setText("")
        self.pushButton.setText("")
        self.logoLabel.setText("")
        self.label.setText(QCoreApplication.translate("DashBoardView", u"Home", None))
        self.label_3.setText(QCoreApplication.translate("DashBoardView", u"Recent Posts", None))
        self.label_4.setText(QCoreApplication.translate("DashBoardView", u"Communities", None))
        self.label_2.setText(QCoreApplication.translate("DashBoardView", u"Frieends", None))
        pass
    # retranslateUi

