# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard2.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_DashBoardView(object):
    def setupUi(self, DashBoardView):
        if not DashBoardView.objectName():
            DashBoardView.setObjectName(u"DashBoardView")
        DashBoardView.resize(1424, 955)
        DashBoardView.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        DashBoardView.setStyleSheet(u"background-color: #1A1A1B;\n"
"")
        self.mainVerticalLayout = QVBoxLayout(DashBoardView)
        self.mainVerticalLayout.setSpacing(0)
        self.mainVerticalLayout.setObjectName(u"mainVerticalLayout")
        self.mainVerticalLayout.setContentsMargins(0, 20, 0, 0)
        self.HeaderBar = QHBoxLayout()
        self.HeaderBar.setObjectName(u"HeaderBar")
        self.HeaderBar.setContentsMargins(35, -1, 15, 10)
        self.logoLabel = QLabel(DashBoardView)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMinimumSize(QSize(0, 50))
        self.logoLabel.setStyleSheet(u"color:white;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.logoLabel.setPixmap(QPixmap(u"C:/Users/images/logo.png"))
        self.logoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HeaderBar.addWidget(self.logoLabel)

        self.searchBar = QLineEdit(DashBoardView)
        self.searchBar.setObjectName(u"searchBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy)
        self.searchBar.setMinimumSize(QSize(600, 0))
        self.searchBar.setMaximumSize(QSize(16777215, 42))
        self.searchBar.setStyleSheet(u"\n"
"border-radius: 21px;\n"
"background-color: rgb(85, 85, 85);\n"
"color:white;\n"
"margin-left:60px;\n"
"margin-right:10px;\n"
"border:none;\n"
"padding:15px;\n"
"")
        self.searchBar.setFrame(False)

        self.HeaderBar.addWidget(self.searchBar)

        self.profileButton = QPushButton(DashBoardView)
        self.profileButton.setObjectName(u"profileButton")
        self.profileButton.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 6px;\n"
"border:none;")
        icon = QIcon()
        icon.addFile(u"C:/Users/images/UserSettings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileButton.setIcon(icon)
        self.profileButton.setIconSize(QSize(43, 43))

        self.HeaderBar.addWidget(self.profileButton)

        self.frameSpacingHeader = QFrame(DashBoardView)
        self.frameSpacingHeader.setObjectName(u"frameSpacingHeader")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameSpacingHeader.sizePolicy().hasHeightForWidth())
        self.frameSpacingHeader.setSizePolicy(sizePolicy1)
        self.frameSpacingHeader.setMaximumSize(QSize(16777215, 20))
        self.frameSpacingHeader.setStyleSheet(u"border:none;")
        self.frameSpacingHeader.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameSpacingHeader.setFrameShadow(QFrame.Shadow.Raised)

        self.HeaderBar.addWidget(self.frameSpacingHeader)

        self.notificationButton = QPushButton(DashBoardView)
        self.notificationButton.setObjectName(u"notificationButton")
        self.notificationButton.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 6px;\n"
"border:none;")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/images/ButtonNotificationImage.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notificationButton.setIcon(icon1)
        self.notificationButton.setIconSize(QSize(35, 35))

        self.HeaderBar.addWidget(self.notificationButton)

        self.shortcutSettingsButton = QPushButton(DashBoardView)
        self.shortcutSettingsButton.setObjectName(u"shortcutSettingsButton")
        self.shortcutSettingsButton.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 6px;\n"
"border:none;")
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/images/ProfileSettingsShortcut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.shortcutSettingsButton.setIcon(icon2)
        self.shortcutSettingsButton.setIconSize(QSize(10, 25))

        self.HeaderBar.addWidget(self.shortcutSettingsButton)


        self.mainVerticalLayout.addLayout(self.HeaderBar)

        self.HeaderDelimiter = QFrame(DashBoardView)
        self.HeaderDelimiter.setObjectName(u"HeaderDelimiter")
        sizePolicy1.setHeightForWidth(self.HeaderDelimiter.sizePolicy().hasHeightForWidth())
        self.HeaderDelimiter.setSizePolicy(sizePolicy1)
        self.HeaderDelimiter.setMinimumSize(QSize(0, 1))
        self.HeaderDelimiter.setStyleSheet(u"background-color: rgb(82, 255, 19);")
        self.HeaderDelimiter.setFrameShape(QFrame.Shape.StyledPanel)
        self.HeaderDelimiter.setFrameShadow(QFrame.Shadow.Raised)

        self.mainVerticalLayout.addWidget(self.HeaderDelimiter)

        self.topFeedContent = QHBoxLayout()
        self.topFeedContent.setSpacing(0)
        self.topFeedContent.setObjectName(u"topFeedContent")
        self.topFeedContent.setContentsMargins(-1, -1, 0, 0)
        self.accesLinksLayout = QVBoxLayout()
        self.accesLinksLayout.setSpacing(12)
        self.accesLinksLayout.setObjectName(u"accesLinksLayout")
        self.accesLinksLayout.setContentsMargins(-1, 0, 0, 0)
        self.acessLinkSpacingFrame = QFrame(DashBoardView)
        self.acessLinkSpacingFrame.setObjectName(u"acessLinkSpacingFrame")
        self.acessLinkSpacingFrame.setMinimumSize(QSize(245, 1))
        self.acessLinkSpacingFrame.setMaximumSize(QSize(245, 16777215))
        self.acessLinkSpacingFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.acessLinkSpacingFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.accesLinksLayout.addWidget(self.acessLinkSpacingFrame)

        self.homeBtn = QPushButton(DashBoardView)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setStyleSheet(u"background:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 700 14pt \"Raleway\";\n"
"color: rgb(192, 192, 192);\n"
"margin-top:6px;\n"
"text-align: left;\n"
"padding-left:30px;")

        self.accesLinksLayout.addWidget(self.homeBtn)

        self.recommendedBtn = QPushButton(DashBoardView)
        self.recommendedBtn.setObjectName(u"recommendedBtn")
        self.recommendedBtn.setStyleSheet(u"background:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 700 14pt \"Raleway\";\n"
"color: rgb(192, 192, 192);\n"
"text-align: left;\n"
"padding-left:30px;")

        self.accesLinksLayout.addWidget(self.recommendedBtn)

        self.communitiesBtn = QPushButton(DashBoardView)
        self.communitiesBtn.setObjectName(u"communitiesBtn")
        self.communitiesBtn.setStyleSheet(u"background:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 700 14pt \"Raleway\";\n"
"color: rgb(192, 192, 192);\n"
"text-align: left;\n"
"padding-left:30px;")

        self.accesLinksLayout.addWidget(self.communitiesBtn)

        self.communitiesWidgetLayout = QVBoxLayout()
        self.communitiesWidgetLayout.setSpacing(6)
        self.communitiesWidgetLayout.setObjectName(u"communitiesWidgetLayout")
        self.communitiesWidgetLayout.setContentsMargins(28, 6, 12, 0)

        self.accesLinksLayout.addLayout(self.communitiesWidgetLayout)

        self.myProfileBtn = QPushButton(DashBoardView)
        self.myProfileBtn.setObjectName(u"myProfileBtn")
        self.myProfileBtn.setStyleSheet(u"background:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 700 14pt \"Raleway\";\n"
"color: rgb(192, 192, 192);\n"
"text-align: left;\n"
"padding-left:30px;")

        self.accesLinksLayout.addWidget(self.myProfileBtn)

        self.settingsBtn = QPushButton(DashBoardView)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setStyleSheet(u"background:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 700 14pt \"Raleway\";\n"
"color: rgb(192, 192, 192);\n"
"text-align: left;\n"
"padding-left:30px;")

        self.accesLinksLayout.addWidget(self.settingsBtn)

        self.disconnectBtn = QPushButton(DashBoardView)
        self.disconnectBtn.setObjectName(u"disconnectBtn")
        self.disconnectBtn.setStyleSheet(u"background:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 700 14pt \"Raleway\";\n"
"color: rgb(192, 192, 192);\n"
"margin-bottom:14px;\n"
"text-align: left;\n"
"padding-left:30px;")

        self.accesLinksLayout.addWidget(self.disconnectBtn)


        self.topFeedContent.addLayout(self.accesLinksLayout)

        self.accesLinkRightDelimiteer = QFrame(DashBoardView)
        self.accesLinkRightDelimiteer.setObjectName(u"accesLinkRightDelimiteer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.accesLinkRightDelimiteer.sizePolicy().hasHeightForWidth())
        self.accesLinkRightDelimiteer.setSizePolicy(sizePolicy2)
        self.accesLinkRightDelimiteer.setMinimumSize(QSize(2, 0))
        self.accesLinkRightDelimiteer.setMaximumSize(QSize(2, 16777215))
        self.accesLinkRightDelimiteer.setStyleSheet(u"background-color: rgb(82, 255, 19);")
        self.accesLinkRightDelimiteer.setFrameShape(QFrame.Shape.StyledPanel)
        self.accesLinkRightDelimiteer.setFrameShadow(QFrame.Shadow.Raised)

        self.topFeedContent.addWidget(self.accesLinkRightDelimiteer)

        self.TopFeedWidgetParent = QWidget(DashBoardView)
        self.TopFeedWidgetParent.setObjectName(u"TopFeedWidgetParent")
        sizePolicy1.setHeightForWidth(self.TopFeedWidgetParent.sizePolicy().hasHeightForWidth())
        self.TopFeedWidgetParent.setSizePolicy(sizePolicy1)
        self.TopFeedWidgetParent.setStyleSheet(u"background: transparent;\n"
"border:none;")
        self.RecommendFeedLayout_2 = QHBoxLayout(self.TopFeedWidgetParent)
        self.RecommendFeedLayout_2.setSpacing(0)
        self.RecommendFeedLayout_2.setObjectName(u"RecommendFeedLayout_2")
        self.RecommendFeedLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topCommunnitiesPopularHashTagLayoutWidget = QWidget(self.TopFeedWidgetParent)
        self.topCommunnitiesPopularHashTagLayoutWidget.setObjectName(u"topCommunnitiesPopularHashTagLayoutWidget")
        self.topCommunnitiesPopularHashTagLayoutWidget.setStyleSheet(u"border:none;")
        self.topCommunnitiesPopularHashTagLayout_2 = QVBoxLayout(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.topCommunnitiesPopularHashTagLayout_2.setSpacing(0)
        self.topCommunnitiesPopularHashTagLayout_2.setObjectName(u"topCommunnitiesPopularHashTagLayout_2")
        self.topCommunnitiesPopularHashTagLayout_2.setContentsMargins(0, 0, 0, 0)
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
"color: rgb(160, 160, 160);")

        self.topCommunnitiesPopularHashTagLayout_2.addWidget(self.TopCommunitiesLabel)

        self.topCommunitiesGridWidget = QWidget(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.topCommunitiesGridWidget.setObjectName(u"topCommunitiesGridWidget")
        self.topCommunitiesGridLayout_2 = QGridLayout(self.topCommunitiesGridWidget)
        self.topCommunitiesGridLayout_2.setSpacing(0)
        self.topCommunitiesGridLayout_2.setObjectName(u"topCommunitiesGridLayout_2")
        self.topCommunitiesGridLayout_2.setContentsMargins(0, 40, 0, 0)
        self.label_2 = QLabel(self.topCommunitiesGridWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color:yellow;")

        self.topCommunitiesGridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)


        self.topCommunnitiesPopularHashTagLayout_2.addWidget(self.topCommunitiesGridWidget)

        self.delimiterTopCommunitiesPopularTags = QFrame(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.delimiterTopCommunitiesPopularTags.setObjectName(u"delimiterTopCommunitiesPopularTags")
        sizePolicy1.setHeightForWidth(self.delimiterTopCommunitiesPopularTags.sizePolicy().hasHeightForWidth())
        self.delimiterTopCommunitiesPopularTags.setSizePolicy(sizePolicy1)
        self.delimiterTopCommunitiesPopularTags.setMinimumSize(QSize(0, 2))
        self.delimiterTopCommunitiesPopularTags.setMaximumSize(QSize(16777215, 2))
        self.delimiterTopCommunitiesPopularTags.setStyleSheet(u"background-color: rgb(82, 255, 19);")
        self.delimiterTopCommunitiesPopularTags.setFrameShape(QFrame.Shape.StyledPanel)
        self.delimiterTopCommunitiesPopularTags.setFrameShadow(QFrame.Shadow.Raised)

        self.topCommunnitiesPopularHashTagLayout_2.addWidget(self.delimiterTopCommunitiesPopularTags)

        self.PopularHashtagsLabel = QLabel(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.PopularHashtagsLabel.setObjectName(u"PopularHashtagsLabel")
        sizePolicy1.setHeightForWidth(self.PopularHashtagsLabel.sizePolicy().hasHeightForWidth())
        self.PopularHashtagsLabel.setSizePolicy(sizePolicy1)
        self.PopularHashtagsLabel.setMinimumSize(QSize(400, 0))
        self.PopularHashtagsLabel.setMaximumSize(QSize(16777215, 16777215))
        self.PopularHashtagsLabel.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"margin-left: 30px;\n"
"border:none;\n"
"color: rgb(160, 160, 160);")

        self.topCommunnitiesPopularHashTagLayout_2.addWidget(self.PopularHashtagsLabel)

        self.popularHashtagsLayoutWidget = QWidget(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.popularHashtagsLayoutWidget.setObjectName(u"popularHashtagsLayoutWidget")
        self.popularHashtagsLayout_2 = QGridLayout(self.popularHashtagsLayoutWidget)
        self.popularHashtagsLayout_2.setSpacing(0)
        self.popularHashtagsLayout_2.setObjectName(u"popularHashtagsLayout_2")
        self.popularHashtagsLayout_2.setContentsMargins(0, 40, 0, 0)
        self.label_4 = QLabel(self.popularHashtagsLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color:yellow;")

        self.popularHashtagsLayout_2.addWidget(self.label_4, 0, 0, 1, 1)


        self.topCommunnitiesPopularHashTagLayout_2.addWidget(self.popularHashtagsLayoutWidget)


        self.RecommendFeedLayout_2.addWidget(self.topCommunnitiesPopularHashTagLayoutWidget)

        self.accesLinkRightDelimiter = QFrame(self.TopFeedWidgetParent)
        self.accesLinkRightDelimiter.setObjectName(u"accesLinkRightDelimiter")
        sizePolicy2.setHeightForWidth(self.accesLinkRightDelimiter.sizePolicy().hasHeightForWidth())
        self.accesLinkRightDelimiter.setSizePolicy(sizePolicy2)
        self.accesLinkRightDelimiter.setMinimumSize(QSize(2, 0))
        self.accesLinkRightDelimiter.setMaximumSize(QSize(2, 16777215))
        self.accesLinkRightDelimiter.setStyleSheet(u"background-color: rgb(82, 255, 19);")
        self.accesLinkRightDelimiter.setFrameShape(QFrame.Shape.StyledPanel)
        self.accesLinkRightDelimiter.setFrameShadow(QFrame.Shadow.Raised)

        self.RecommendFeedLayout_2.addWidget(self.accesLinkRightDelimiter)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 50, -1)
        self.recommendedPostsLabel = QLabel(self.TopFeedWidgetParent)
        self.recommendedPostsLabel.setObjectName(u"recommendedPostsLabel")
        sizePolicy1.setHeightForWidth(self.recommendedPostsLabel.sizePolicy().hasHeightForWidth())
        self.recommendedPostsLabel.setSizePolicy(sizePolicy1)
        self.recommendedPostsLabel.setMinimumSize(QSize(400, 0))
        self.recommendedPostsLabel.setMaximumSize(QSize(16777215, 40))
        self.recommendedPostsLabel.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"margin-left: 30px;\n"
"border:none;\n"
"color: rgb(160, 160, 160);")

        self.verticalLayout.addWidget(self.recommendedPostsLabel)

        self.recommendFeedHWidget = QWidget(self.TopFeedWidgetParent)
        self.recommendFeedHWidget.setObjectName(u"recommendFeedHWidget")
        sizePolicy1.setHeightForWidth(self.recommendFeedHWidget.sizePolicy().hasHeightForWidth())
        self.recommendFeedHWidget.setSizePolicy(sizePolicy1)
        self.recommendFeedHWidget.setStyleSheet(u"background: transparent;")
        self.recommendFeedHLayout_2 = QHBoxLayout(self.recommendFeedHWidget)
        self.recommendFeedHLayout_2.setSpacing(0)
        self.recommendFeedHLayout_2.setObjectName(u"recommendFeedHLayout_2")
        self.recommendFeedHLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.recommendFeedHWidget)


        self.RecommendFeedLayout_2.addLayout(self.verticalLayout)


        self.topFeedContent.addWidget(self.TopFeedWidgetParent)


        self.mainVerticalLayout.addLayout(self.topFeedContent)

        self.topContentDelmiter = QFrame(DashBoardView)
        self.topContentDelmiter.setObjectName(u"topContentDelmiter")
        sizePolicy1.setHeightForWidth(self.topContentDelmiter.sizePolicy().hasHeightForWidth())
        self.topContentDelmiter.setSizePolicy(sizePolicy1)
        self.topContentDelmiter.setMinimumSize(QSize(0, 1))
        self.topContentDelmiter.setStyleSheet(u"background-color: rgb(82, 255, 19);")
        self.topContentDelmiter.setFrameShape(QFrame.Shape.StyledPanel)
        self.topContentDelmiter.setFrameShadow(QFrame.Shadow.Raised)

        self.mainVerticalLayout.addWidget(self.topContentDelmiter)

        self.bottomContent = QHBoxLayout()
        self.bottomContent.setSpacing(0)
        self.bottomContent.setObjectName(u"bottomContent")
        self.bottomContent.setContentsMargins(0, -1, -1, 0)
        self.FriendsScrollArea = QScrollArea(DashBoardView)
        self.FriendsScrollArea.setObjectName(u"FriendsScrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.FriendsScrollArea.sizePolicy().hasHeightForWidth())
        self.FriendsScrollArea.setSizePolicy(sizePolicy3)
        self.FriendsScrollArea.setMinimumSize(QSize(245, 0))
        self.FriendsScrollArea.setMaximumSize(QSize(245, 16777215))
        self.FriendsScrollArea.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"")
        self.FriendsScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.FriendsScrollArea.setWidgetResizable(False)
        self.FriendsScrollArea.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.FriendsScrollAreaWidget = QWidget()
        self.FriendsScrollAreaWidget.setObjectName(u"FriendsScrollAreaWidget")
        self.FriendsScrollAreaWidget.setGeometry(QRect(20, 0, 204, 500))
        sizePolicy3.setHeightForWidth(self.FriendsScrollAreaWidget.sizePolicy().hasHeightForWidth())
        self.FriendsScrollAreaWidget.setSizePolicy(sizePolicy3)
        self.FriendsScrollAreaWidget.setMinimumSize(QSize(0, 0))
        self.FriendsScrollAreaWidget.setMaximumSize(QSize(16777215, 99999))
        self.FriendsScrollAreaWidget.setSizeIncrement(QSize(0, 100))
        self.FriendsScrollAreaWidget.setStyleSheet(u"border:none;")
        self.postsLayout_2 = QVBoxLayout(self.FriendsScrollAreaWidget)
        self.postsLayout_2.setSpacing(6)
        self.postsLayout_2.setObjectName(u"postsLayout_2")
        self.postsLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.postsLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.frame_3 = QFrame(self.FriendsScrollAreaWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_myFeed_9 = QLabel(self.frame_3)
        self.label_myFeed_9.setObjectName(u"label_myFeed_9")
        self.label_myFeed_9.setMinimumSize(QSize(0, 0))
        self.label_myFeed_9.setMaximumSize(QSize(400, 40))
        self.label_myFeed_9.setStyleSheet(u"font: 700 12pt \"Raleway\";\n"
"color: rgb(160, 160, 160);\n"
"margin-left:5px;")

        self.horizontalLayout.addWidget(self.label_myFeed_9)

        self.lineEdit_6 = QLineEdit(self.frame_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 25))
        self.lineEdit_6.setAutoFillBackground(False)
        self.lineEdit_6.setStyleSheet(u"border:none;\n"
"background-color:#3A3A3A;\n"
"padding-left:6px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Raleway\";\n"
"border-radius:10px;")
        self.lineEdit_6.setFrame(False)

        self.horizontalLayout.addWidget(self.lineEdit_6)


        self.postsLayout_2.addWidget(self.frame_3)

        self.label_myFeed_3 = QLabel(self.FriendsScrollAreaWidget)
        self.label_myFeed_3.setObjectName(u"label_myFeed_3")
        self.label_myFeed_3.setMinimumSize(QSize(0, 0))
        self.label_myFeed_3.setMaximumSize(QSize(400, 40))
        self.label_myFeed_3.setStyleSheet(u"font: 700 12pt \"Raleway\";\n"
"color: rgb(160, 160, 160);\n"
"margin-left:5px;")

        self.postsLayout_2.addWidget(self.label_myFeed_3)

        self.onlineFriendsLayout = QVBoxLayout()
        self.onlineFriendsLayout.setSpacing(6)
        self.onlineFriendsLayout.setObjectName(u"onlineFriendsLayout")
        self.onlineFriendsLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.onlineFriendsLayout.setContentsMargins(9, 10, -1, -1)

        self.postsLayout_2.addLayout(self.onlineFriendsLayout)

        self.label_myFeed_4 = QLabel(self.FriendsScrollAreaWidget)
        self.label_myFeed_4.setObjectName(u"label_myFeed_4")
        self.label_myFeed_4.setMinimumSize(QSize(0, 0))
        self.label_myFeed_4.setMaximumSize(QSize(400, 40))
        self.label_myFeed_4.setStyleSheet(u"font: 700 12pt \"Raleway\";\n"
"color: rgb(160, 160, 160);\n"
"margin-left:5px;")

        self.postsLayout_2.addWidget(self.label_myFeed_4)

        self.friendsWidhtDelimiter = QFrame(self.FriendsScrollAreaWidget)
        self.friendsWidhtDelimiter.setObjectName(u"friendsWidhtDelimiter")
        sizePolicy1.setHeightForWidth(self.friendsWidhtDelimiter.sizePolicy().hasHeightForWidth())
        self.friendsWidhtDelimiter.setSizePolicy(sizePolicy1)
        self.friendsWidhtDelimiter.setMinimumSize(QSize(204, 0))
        self.friendsWidhtDelimiter.setMaximumSize(QSize(16777215, 1))
        self.friendsWidhtDelimiter.setFrameShape(QFrame.Shape.StyledPanel)
        self.friendsWidhtDelimiter.setFrameShadow(QFrame.Shadow.Raised)

        self.postsLayout_2.addWidget(self.friendsWidhtDelimiter)

        self.offlineFriendsLayout = QVBoxLayout()
        self.offlineFriendsLayout.setSpacing(0)
        self.offlineFriendsLayout.setObjectName(u"offlineFriendsLayout")
        self.offlineFriendsLayout.setContentsMargins(-1, -1, -1, 40)

        self.postsLayout_2.addLayout(self.offlineFriendsLayout)

        self.postsLayout_2.setStretch(2, 1)
        self.postsLayout_2.setStretch(4, 1)
        self.postsLayout_2.setStretch(5, 1)
        self.FriendsScrollArea.setWidget(self.FriendsScrollAreaWidget)

        self.bottomContent.addWidget(self.FriendsScrollArea)

        self.friendsPostsDelimiteer = QFrame(DashBoardView)
        self.friendsPostsDelimiteer.setObjectName(u"friendsPostsDelimiteer")
        sizePolicy2.setHeightForWidth(self.friendsPostsDelimiteer.sizePolicy().hasHeightForWidth())
        self.friendsPostsDelimiteer.setSizePolicy(sizePolicy2)
        self.friendsPostsDelimiteer.setMinimumSize(QSize(2, 0))
        self.friendsPostsDelimiteer.setMaximumSize(QSize(2, 16777215))
        self.friendsPostsDelimiteer.setStyleSheet(u"background-color: rgb(82, 255, 19);")
        self.friendsPostsDelimiteer.setFrameShape(QFrame.Shape.StyledPanel)
        self.friendsPostsDelimiteer.setFrameShadow(QFrame.Shadow.Raised)

        self.bottomContent.addWidget(self.friendsPostsDelimiteer)

        self.middleBar = QWidget(DashBoardView)
        self.middleBar.setObjectName(u"middleBar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.middleBar.sizePolicy().hasHeightForWidth())
        self.middleBar.setSizePolicy(sizePolicy4)
        self.middleBar.setStyleSheet(u"background-color: transparent;\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.middleBar)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ContentPosts_ScrollArea = QScrollArea(self.middleBar)
        self.ContentPosts_ScrollArea.setObjectName(u"ContentPosts_ScrollArea")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ContentPosts_ScrollArea.sizePolicy().hasHeightForWidth())
        self.ContentPosts_ScrollArea.setSizePolicy(sizePolicy5)
        self.ContentPosts_ScrollArea.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"")
        self.ContentPosts_ScrollArea.setWidgetResizable(True)
        self.ContentPosts_ScrollArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1175, 592))
        self.postsLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.postsLayout.setSpacing(20)
        self.postsLayout.setObjectName(u"postsLayout")
        self.postsLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.label_myFeed = QLabel(self.scrollAreaWidgetContents)
        self.label_myFeed.setObjectName(u"label_myFeed")
        self.label_myFeed.setMinimumSize(QSize(400, 0))
        self.label_myFeed.setMaximumSize(QSize(400, 40))
        self.label_myFeed.setStyleSheet(u"font: 700 12pt \"Raleway\";\n"
"color: rgb(160, 160, 160);")

        self.postsLayout.addWidget(self.label_myFeed)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.postsLayout.addWidget(self.frame)

        self.ContentPosts_ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.ContentPosts_ScrollArea)


        self.bottomContent.addWidget(self.middleBar)


        self.mainVerticalLayout.addLayout(self.bottomContent)


        self.retranslateUi(DashBoardView)

        QMetaObject.connectSlotsByName(DashBoardView)
    # setupUi

    def retranslateUi(self, DashBoardView):
        self.logoLabel.setText("")
        self.searchBar.setPlaceholderText(QCoreApplication.translate("DashBoardView", u"Search...", None))
        self.profileButton.setText("")
        self.notificationButton.setText("")
        self.shortcutSettingsButton.setText("")
        self.homeBtn.setText(QCoreApplication.translate("DashBoardView", u"Home", None))
        self.recommendedBtn.setText(QCoreApplication.translate("DashBoardView", u"Recommended", None))
        self.communitiesBtn.setText(QCoreApplication.translate("DashBoardView", u"Communities", None))
        self.myProfileBtn.setText(QCoreApplication.translate("DashBoardView", u"My Profile", None))
        self.settingsBtn.setText(QCoreApplication.translate("DashBoardView", u"Settings", None))
        self.disconnectBtn.setText(QCoreApplication.translate("DashBoardView", u"Disconnect", None))
        self.TopCommunitiesLabel.setText(QCoreApplication.translate("DashBoardView", u"Top communities", None))
        self.label_2.setText(QCoreApplication.translate("DashBoardView", u"TextLabel", None))
        self.PopularHashtagsLabel.setText(QCoreApplication.translate("DashBoardView", u"POPUlAR HASHTAGS", None))
        self.label_4.setText(QCoreApplication.translate("DashBoardView", u"TextLabel", None))
        self.recommendedPostsLabel.setText(QCoreApplication.translate("DashBoardView", u"RECOMMENDED POSTS", None))
        self.label_myFeed_9.setText(QCoreApplication.translate("DashBoardView", u"Friends", None))
        self.lineEdit_6.setInputMask("")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("DashBoardView", u"Search", None))
        self.label_myFeed_3.setText(QCoreApplication.translate("DashBoardView", u"Online", None))
        self.label_myFeed_4.setText(QCoreApplication.translate("DashBoardView", u"Offline", None))
        self.label_myFeed.setText(QCoreApplication.translate("DashBoardView", u"MY FEED", None))
        pass
    # retranslateUi

