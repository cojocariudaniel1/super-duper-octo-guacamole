# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_DashBoardView(object):
    def setupUi(self, DashBoardView):
        if not DashBoardView.objectName():
            DashBoardView.setObjectName(u"DashBoardView")
        DashBoardView.resize(1440, 955)
        DashBoardView.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        DashBoardView.setStyleSheet(u"background: #1E1E1E;")
        self.mainVerticalLayout = QVBoxLayout(DashBoardView)
        self.mainVerticalLayout.setSpacing(0)
        self.mainVerticalLayout.setObjectName(u"mainVerticalLayout")
        self.mainVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout = QHBoxLayout()
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(-1, -1, -1, 0)
        self.leftSideBar = QWidget(DashBoardView)
        self.leftSideBar.setObjectName(u"leftSideBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftSideBar.sizePolicy().hasHeightForWidth())
        self.leftSideBar.setSizePolicy(sizePolicy)
        self.leftSideBar.setMinimumSize(QSize(300, 0))
        self.leftSideBar.setMaximumSize(QSize(300, 16777215))
        self.leftSideBar.setStyleSheet(u"background-color: transparent;\n"
"border-right: 1px solid #3a3a3a;")
        self.sidebarLayout = QVBoxLayout(self.leftSideBar)
        self.sidebarLayout.setSpacing(0)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.sidebarLayout.setContentsMargins(0, 0, 0, 0)
        self.logoLabel = QLabel(self.leftSideBar)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMinimumSize(QSize(0, 50))
        self.logoLabel.setStyleSheet(u"color:white;\n"
"border-bottom:1px solid #3a3a3a;")
        self.logoLabel.setPixmap(QPixmap(u"../../../images/logo.png"))
        self.logoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sidebarLayout.addWidget(self.logoLabel)

        self.label_2 = QLabel(self.leftSideBar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(256, 0))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 600 14pt \"Segoe UI\";\n"
"border:0px;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sidebarLayout.addWidget(self.label_2)

        self.frame_2 = QFrame(self.leftSideBar)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setStyleSheet(u"border:0px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.sidebarLayout.addWidget(self.frame_2)


        self.mainLayout.addWidget(self.leftSideBar)

        self.middleBar = QWidget(DashBoardView)
        self.middleBar.setObjectName(u"middleBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.middleBar.sizePolicy().hasHeightForWidth())
        self.middleBar.setSizePolicy(sizePolicy2)
        self.middleBar.setStyleSheet(u"background-color: transparent;\n"
"border-left: 1px solid #3a3a3a;")
        self.verticalLayout_3 = QVBoxLayout(self.middleBar)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topNavBar = QWidget(self.middleBar)
        self.topNavBar.setObjectName(u"topNavBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.topNavBar.sizePolicy().hasHeightForWidth())
        self.topNavBar.setSizePolicy(sizePolicy3)
        self.topNavBar.setMinimumSize(QSize(0, 50))
        self.topNavBar.setBaseSize(QSize(0, 100))
        self.topNavBar.setStyleSheet(u"background-color: transparent;\n"
"border-bottom:1px solid #3a3a3a;")
        self.topNavLayout = QHBoxLayout(self.topNavBar)
        self.topNavLayout.setSpacing(0)
        self.topNavLayout.setObjectName(u"topNavLayout")
        self.topNavLayout.setContentsMargins(0, 0, 0, 0)
        self.searchBar = QLineEdit(self.topNavBar)
        self.searchBar.setObjectName(u"searchBar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy4)
        self.searchBar.setMinimumSize(QSize(600, 0))
        self.searchBar.setMaximumSize(QSize(16777215, 38))
        self.searchBar.setStyleSheet(u"\n"
"border-radius: 6px;\n"
"background-color: rgb(85, 85, 85);\n"
"color:white;\n"
"margin-left:10px;\n"
"margin-right:10px;\n"
"border:none;")
        self.searchBar.setFrame(False)

        self.topNavLayout.addWidget(self.searchBar)

        self.notificationButton = QPushButton(self.topNavBar)
        self.notificationButton.setObjectName(u"notificationButton")
        self.notificationButton.setStyleSheet(u"background: #1A1A1B;\n"
"border-radius: 6px;\n"
"border:none;")
        icon = QIcon()
        icon.addFile(u"../../../images/ButtonNotificationImage.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notificationButton.setIcon(icon)
        self.notificationButton.setIconSize(QSize(35, 35))

        self.topNavLayout.addWidget(self.notificationButton)

        self.frame = QFrame(self.topNavBar)
        self.frame.setObjectName(u"frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy5)
        self.frame.setMaximumSize(QSize(16777215, 20))
        self.frame.setStyleSheet(u"border:none;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.topNavLayout.addWidget(self.frame)

        self.profileButton = QPushButton(self.topNavBar)
        self.profileButton.setObjectName(u"profileButton")
        self.profileButton.setStyleSheet(u"background: #1A1A1B;\n"
"border-radius: 6px;\n"
"border:none;")
        icon1 = QIcon()
        icon1.addFile(u"../../../images/UserSettings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileButton.setIcon(icon1)
        self.profileButton.setIconSize(QSize(43, 43))

        self.topNavLayout.addWidget(self.profileButton)

        self.shortcutSettingsButton = QPushButton(self.topNavBar)
        self.shortcutSettingsButton.setObjectName(u"shortcutSettingsButton")
        self.shortcutSettingsButton.setStyleSheet(u"background: #1A1A1B;\n"
"border-radius: 6px;\n"
"border:none;")
        icon2 = QIcon()
        icon2.addFile(u"../../../images/ProfileSettingsShortcut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.shortcutSettingsButton.setIcon(icon2)
        self.shortcutSettingsButton.setIconSize(QSize(10, 25))

        self.topNavLayout.addWidget(self.shortcutSettingsButton)


        self.verticalLayout_3.addWidget(self.topNavBar)

        self.TopFeedWidgetParent = QWidget(self.middleBar)
        self.TopFeedWidgetParent.setObjectName(u"TopFeedWidgetParent")
        self.TopFeedWidgetParent.setStyleSheet(u"background: transparent;")
        self.RecommendFeedLayout = QHBoxLayout(self.TopFeedWidgetParent)
        self.RecommendFeedLayout.setSpacing(0)
        self.RecommendFeedLayout.setObjectName(u"RecommendFeedLayout")
        self.RecommendFeedLayout.setContentsMargins(0, 0, 0, 0)
        self.topCommunnitiesPopularHashTagLayoutWidget = QWidget(self.TopFeedWidgetParent)
        self.topCommunnitiesPopularHashTagLayoutWidget.setObjectName(u"topCommunnitiesPopularHashTagLayoutWidget")
        self.topCommunnitiesPopularHashTagLayout = QVBoxLayout(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.topCommunnitiesPopularHashTagLayout.setSpacing(6)
        self.topCommunnitiesPopularHashTagLayout.setObjectName(u"topCommunnitiesPopularHashTagLayout")
        self.topCommunnitiesPopularHashTagLayout.setContentsMargins(0, 0, 0, 0)
        self.TopCommunitiesLabel = QLabel(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.TopCommunitiesLabel.setObjectName(u"TopCommunitiesLabel")
        self.TopCommunitiesLabel.setMinimumSize(QSize(400, 0))
        self.TopCommunitiesLabel.setMaximumSize(QSize(400, 16777215))
        self.TopCommunitiesLabel.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"margin-left: 30px;\n"
"border:0px;\n"
"color: #C0C0C0;")

        self.topCommunnitiesPopularHashTagLayout.addWidget(self.TopCommunitiesLabel)

        self.topCommunitiesGridWidget = QWidget(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.topCommunitiesGridWidget.setObjectName(u"topCommunitiesGridWidget")
        self.topCommunitiesGridLayout = QGridLayout(self.topCommunitiesGridWidget)
        self.topCommunitiesGridLayout.setSpacing(0)
        self.topCommunitiesGridLayout.setObjectName(u"topCommunitiesGridLayout")
        self.topCommunitiesGridLayout.setContentsMargins(0, 40, 0, 0)
        self.label = QLabel(self.topCommunitiesGridWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color:yellow;")

        self.topCommunitiesGridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.topCommunnitiesPopularHashTagLayout.addWidget(self.topCommunitiesGridWidget)

        self.delimiter2 = QFrame(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.delimiter2.setObjectName(u"delimiter2")
        self.delimiter2.setMinimumSize(QSize(0, 1))
        self.delimiter2.setStyleSheet(u"background-color: transparent;\n"
"border-bottom:1px solid #3a3a3a;")
        self.delimiter2.setFrameShape(QFrame.Shape.StyledPanel)
        self.delimiter2.setFrameShadow(QFrame.Shadow.Raised)

        self.topCommunnitiesPopularHashTagLayout.addWidget(self.delimiter2)

        self.PopularHashtagsLabel = QLabel(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.PopularHashtagsLabel.setObjectName(u"PopularHashtagsLabel")
        sizePolicy5.setHeightForWidth(self.PopularHashtagsLabel.sizePolicy().hasHeightForWidth())
        self.PopularHashtagsLabel.setSizePolicy(sizePolicy5)
        self.PopularHashtagsLabel.setMinimumSize(QSize(400, 0))
        self.PopularHashtagsLabel.setMaximumSize(QSize(16777215, 16777215))
        self.PopularHashtagsLabel.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"margin-left: 30px;\n"
"border:none;\n"
"color: #C0C0C0;")

        self.topCommunnitiesPopularHashTagLayout.addWidget(self.PopularHashtagsLabel)

        self.popularHashtagsLayoutWidget = QWidget(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.popularHashtagsLayoutWidget.setObjectName(u"popularHashtagsLayoutWidget")
        self.popularHashtagsLayout = QGridLayout(self.popularHashtagsLayoutWidget)
        self.popularHashtagsLayout.setSpacing(0)
        self.popularHashtagsLayout.setObjectName(u"popularHashtagsLayout")
        self.popularHashtagsLayout.setContentsMargins(0, 40, 0, 0)
        self.label_3 = QLabel(self.popularHashtagsLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color:yellow;")

        self.popularHashtagsLayout.addWidget(self.label_3, 0, 0, 1, 1)


        self.topCommunnitiesPopularHashTagLayout.addWidget(self.popularHashtagsLayoutWidget)


        self.RecommendFeedLayout.addWidget(self.topCommunnitiesPopularHashTagLayoutWidget)

        self.delimiter1 = QFrame(self.TopFeedWidgetParent)
        self.delimiter1.setObjectName(u"delimiter1")
        sizePolicy1.setHeightForWidth(self.delimiter1.sizePolicy().hasHeightForWidth())
        self.delimiter1.setSizePolicy(sizePolicy1)
        self.delimiter1.setMaximumSize(QSize(1, 16777215))
        self.delimiter1.setStyleSheet(u"background-color: transparent;\n"
"border-left:1px solid #3a3a3a;")
        self.delimiter1.setFrameShape(QFrame.Shape.StyledPanel)
        self.delimiter1.setFrameShadow(QFrame.Shadow.Raised)

        self.RecommendFeedLayout.addWidget(self.delimiter1)

        self.recommendFeedHWidget = QWidget(self.TopFeedWidgetParent)
        self.recommendFeedHWidget.setObjectName(u"recommendFeedHWidget")
        self.recommendFeedHWidget.setStyleSheet(u"background: transparent;")
        self.recommendFeedHLayout = QHBoxLayout(self.recommendFeedHWidget)
        self.recommendFeedHLayout.setSpacing(0)
        self.recommendFeedHLayout.setObjectName(u"recommendFeedHLayout")
        self.recommendFeedHLayout.setContentsMargins(0, 0, 0, 0)

        self.RecommendFeedLayout.addWidget(self.recommendFeedHWidget)


        self.verticalLayout_3.addWidget(self.TopFeedWidgetParent)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.ContentPosts_ScrollArea = QScrollArea(self.middleBar)
        self.ContentPosts_ScrollArea.setObjectName(u"ContentPosts_ScrollArea")
        self.ContentPosts_ScrollArea.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"border-top:1px solid #3a3a3a;")
        self.ContentPosts_ScrollArea.setWidgetResizable(True)
        self.ContentPosts_ScrollArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(1, 1, 1136, 719))
        self.postsLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.postsLayout.setSpacing(20)
        self.postsLayout.setObjectName(u"postsLayout")
        self.postsLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.ContentPosts_ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.ContentPosts_ScrollArea)


        self.mainLayout.addWidget(self.middleBar)


        self.mainVerticalLayout.addLayout(self.mainLayout)


        self.retranslateUi(DashBoardView)

        QMetaObject.connectSlotsByName(DashBoardView)
    # setupUi

    def retranslateUi(self, DashBoardView):
        self.logoLabel.setText("")
        self.label_2.setText(QCoreApplication.translate("DashBoardView", u"Frieends", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("DashBoardView", u"Search...", None))
        self.notificationButton.setText("")
        self.profileButton.setText("")
        self.shortcutSettingsButton.setText("")
        self.TopCommunitiesLabel.setText(QCoreApplication.translate("DashBoardView", u"Top communities", None))
        self.label.setText(QCoreApplication.translate("DashBoardView", u"TextLabel", None))
        self.PopularHashtagsLabel.setText(QCoreApplication.translate("DashBoardView", u"POPUlAR HASHTAGS", None))
        self.label_3.setText(QCoreApplication.translate("DashBoardView", u"TextLabel", None))
        pass
    # retranslateUi

