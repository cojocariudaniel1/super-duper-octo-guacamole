# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DetaliedPostView.ui'
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
    QLayout, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_DetaliedPostView(object):
    def setupUi(self, DetaliedPostView):
        if not DetaliedPostView.objectName():
            DetaliedPostView.setObjectName(u"DetaliedPostView")
        DetaliedPostView.resize(1424, 955)
        DetaliedPostView.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        DetaliedPostView.setStyleSheet(u"background-color: #1A1A1B;\n"
"")
        self.verticalLayout_3 = QVBoxLayout(DetaliedPostView)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 40)
        self.MainWindowScrollArea = QScrollArea(DetaliedPostView)
        self.MainWindowScrollArea.setObjectName(u"MainWindowScrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainWindowScrollArea.sizePolicy().hasHeightForWidth())
        self.MainWindowScrollArea.setSizePolicy(sizePolicy)
        self.MainWindowScrollArea.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"")
        self.MainWindowScrollArea.setWidgetResizable(True)
        self.MainWindowScrollArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainWindowScrollAreaWidget = QWidget()
        self.mainWindowScrollAreaWidget.setObjectName(u"mainWindowScrollAreaWidget")
        self.mainWindowScrollAreaWidget.setGeometry(QRect(0, 0, 1424, 915))
        self.MainWindowLayout = QVBoxLayout(self.mainWindowScrollAreaWidget)
        self.MainWindowLayout.setSpacing(0)
        self.MainWindowLayout.setObjectName(u"MainWindowLayout")
        self.MainWindowLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.MainWindowLayout.setContentsMargins(0, 0, 0, 0)
        self.HeaderBar = QHBoxLayout()
        self.HeaderBar.setObjectName(u"HeaderBar")
        self.HeaderBar.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.HeaderBar.setContentsMargins(35, -1, 15, 0)
        self.logoLabel = QLabel(self.mainWindowScrollAreaWidget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMinimumSize(QSize(0, 50))
        self.logoLabel.setStyleSheet(u"color:white;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.logoLabel.setPixmap(QPixmap(u"C:/Users/images/logo.png"))
        self.logoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.HeaderBar.addWidget(self.logoLabel)

        self.searchBar = QLineEdit(self.mainWindowScrollAreaWidget)
        self.searchBar.setObjectName(u"searchBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy1)
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

        self.profileButton = QPushButton(self.mainWindowScrollAreaWidget)
        self.profileButton.setObjectName(u"profileButton")
        self.profileButton.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 6px;\n"
"border:none;")
        icon = QIcon()
        icon.addFile(u"C:/Users/images/UserSettings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileButton.setIcon(icon)
        self.profileButton.setIconSize(QSize(43, 43))

        self.HeaderBar.addWidget(self.profileButton)

        self.frameSpacingHeader = QFrame(self.mainWindowScrollAreaWidget)
        self.frameSpacingHeader.setObjectName(u"frameSpacingHeader")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frameSpacingHeader.sizePolicy().hasHeightForWidth())
        self.frameSpacingHeader.setSizePolicy(sizePolicy2)
        self.frameSpacingHeader.setMaximumSize(QSize(16777215, 20))
        self.frameSpacingHeader.setStyleSheet(u"border:none;")
        self.frameSpacingHeader.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameSpacingHeader.setFrameShadow(QFrame.Shadow.Raised)

        self.HeaderBar.addWidget(self.frameSpacingHeader)

        self.notificationButton = QPushButton(self.mainWindowScrollAreaWidget)
        self.notificationButton.setObjectName(u"notificationButton")
        self.notificationButton.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 6px;\n"
"border:none;")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/images/ButtonNotificationImage.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notificationButton.setIcon(icon1)
        self.notificationButton.setIconSize(QSize(35, 35))

        self.HeaderBar.addWidget(self.notificationButton)

        self.shortcutSettingsButton = QPushButton(self.mainWindowScrollAreaWidget)
        self.shortcutSettingsButton.setObjectName(u"shortcutSettingsButton")
        self.shortcutSettingsButton.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 6px;\n"
"border:none;")
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/images/ProfileSettingsShortcut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.shortcutSettingsButton.setIcon(icon2)
        self.shortcutSettingsButton.setIconSize(QSize(10, 25))

        self.HeaderBar.addWidget(self.shortcutSettingsButton)


        self.MainWindowLayout.addLayout(self.HeaderBar)

        self.HeaderDelimiter = QFrame(self.mainWindowScrollAreaWidget)
        self.HeaderDelimiter.setObjectName(u"HeaderDelimiter")
        sizePolicy2.setHeightForWidth(self.HeaderDelimiter.sizePolicy().hasHeightForWidth())
        self.HeaderDelimiter.setSizePolicy(sizePolicy2)
        self.HeaderDelimiter.setMinimumSize(QSize(0, 1))
        self.HeaderDelimiter.setMaximumSize(QSize(16777215, 1))
        self.HeaderDelimiter.setStyleSheet(u"background-color: rgb(116, 116, 116);")
        self.HeaderDelimiter.setFrameShape(QFrame.Shape.StyledPanel)
        self.HeaderDelimiter.setFrameShadow(QFrame.Shadow.Raised)

        self.MainWindowLayout.addWidget(self.HeaderDelimiter)

        self.MainLayout = QHBoxLayout()
        self.MainLayout.setObjectName(u"MainLayout")
        self.MainLayout.setContentsMargins(-1, -1, 40, 40)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.accesLinksLayout = QVBoxLayout()
        self.accesLinksLayout.setSpacing(12)
        self.accesLinksLayout.setObjectName(u"accesLinksLayout")
        self.accesLinksLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.accesLinksLayout.setContentsMargins(-1, 0, 0, 0)
        self.homeBtn = QPushButton(self.mainWindowScrollAreaWidget)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setStyleSheet(u"background:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 700 14pt \"Raleway\";\n"
"color: rgb(192, 192, 192);\n"
"margin-top:6px;\n"
"text-align: left;\n"
"padding-left:30px;")

        self.accesLinksLayout.addWidget(self.homeBtn)

        self.recommendedBtn = QPushButton(self.mainWindowScrollAreaWidget)
        self.recommendedBtn.setObjectName(u"recommendedBtn")
        self.recommendedBtn.setStyleSheet(u"background:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 700 14pt \"Raleway\";\n"
"color: rgb(192, 192, 192);\n"
"text-align: left;\n"
"padding-left:30px;")

        self.accesLinksLayout.addWidget(self.recommendedBtn)

        self.communitiesBtn = QPushButton(self.mainWindowScrollAreaWidget)
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
        self.communitiesWidgetLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.communitiesWidgetLayout.setContentsMargins(28, 6, 12, 0)

        self.accesLinksLayout.addLayout(self.communitiesWidgetLayout)

        self.myProfileBtn = QPushButton(self.mainWindowScrollAreaWidget)
        self.myProfileBtn.setObjectName(u"myProfileBtn")
        self.myProfileBtn.setStyleSheet(u"background:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 700 14pt \"Raleway\";\n"
"color: rgb(192, 192, 192);\n"
"text-align: left;\n"
"padding-left:30px;")

        self.accesLinksLayout.addWidget(self.myProfileBtn)

        self.settingsBtn = QPushButton(self.mainWindowScrollAreaWidget)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setStyleSheet(u"background:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 700 14pt \"Raleway\";\n"
"color: rgb(192, 192, 192);\n"
"text-align: left;\n"
"padding-left:30px;")

        self.accesLinksLayout.addWidget(self.settingsBtn)

        self.disconnectBtn = QPushButton(self.mainWindowScrollAreaWidget)
        self.disconnectBtn.setObjectName(u"disconnectBtn")
        self.disconnectBtn.setStyleSheet(u"background:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 700 14pt \"Raleway\";\n"
"color: rgb(192, 192, 192);\n"
"margin-bottom:14px;\n"
"text-align: left;\n"
"padding-left:30px;")

        self.accesLinksLayout.addWidget(self.disconnectBtn)


        self.verticalLayout.addLayout(self.accesLinksLayout)

        self.HeaderDelimiter_2 = QFrame(self.mainWindowScrollAreaWidget)
        self.HeaderDelimiter_2.setObjectName(u"HeaderDelimiter_2")
        sizePolicy2.setHeightForWidth(self.HeaderDelimiter_2.sizePolicy().hasHeightForWidth())
        self.HeaderDelimiter_2.setSizePolicy(sizePolicy2)
        self.HeaderDelimiter_2.setMinimumSize(QSize(0, 1))
        self.HeaderDelimiter_2.setMaximumSize(QSize(16777215, 1))
        self.HeaderDelimiter_2.setStyleSheet(u"background-color: rgb(116, 116, 116);")
        self.HeaderDelimiter_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.HeaderDelimiter_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.HeaderDelimiter_2)

        self.FriendsLayout = QVBoxLayout()
        self.FriendsLayout.setSpacing(12)
        self.FriendsLayout.setObjectName(u"FriendsLayout")
        self.FriendsLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.FriendsLayout.setContentsMargins(-1, -1, -1, 30)
        self.friendsWidhtDelimiter_2 = QFrame(self.mainWindowScrollAreaWidget)
        self.friendsWidhtDelimiter_2.setObjectName(u"friendsWidhtDelimiter_2")
        sizePolicy2.setHeightForWidth(self.friendsWidhtDelimiter_2.sizePolicy().hasHeightForWidth())
        self.friendsWidhtDelimiter_2.setSizePolicy(sizePolicy2)
        self.friendsWidhtDelimiter_2.setMinimumSize(QSize(245, 20))
        self.friendsWidhtDelimiter_2.setMaximumSize(QSize(16777215, 20))
        self.friendsWidhtDelimiter_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.friendsWidhtDelimiter_2.setFrameShadow(QFrame.Shadow.Raised)

        self.FriendsLayout.addWidget(self.friendsWidhtDelimiter_2)

        self.titleFriendsLayout = QFrame(self.mainWindowScrollAreaWidget)
        self.titleFriendsLayout.setObjectName(u"titleFriendsLayout")
        self.titleFriendsLayout.setMinimumSize(QSize(0, 40))
        self.titleFriendsLayout.setMaximumSize(QSize(16777215, 40))
        self.titleFriendsLayout.setStyleSheet(u"")
        self.titleFriendsLayout.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleFriendsLayout.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.titleFriendsLayout)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.friendsTitleLabel = QLabel(self.titleFriendsLayout)
        self.friendsTitleLabel.setObjectName(u"friendsTitleLabel")
        self.friendsTitleLabel.setMinimumSize(QSize(0, 0))
        self.friendsTitleLabel.setMaximumSize(QSize(400, 40))
        self.friendsTitleLabel.setStyleSheet(u"font: 700 12pt \"Raleway\";\n"
"color: rgb(160, 160, 160);\n"
"margin-left:13px;")

        self.horizontalLayout_4.addWidget(self.friendsTitleLabel)

        self.searchBarFriends = QLineEdit(self.titleFriendsLayout)
        self.searchBarFriends.setObjectName(u"searchBarFriends")
        self.searchBarFriends.setMinimumSize(QSize(0, 25))
        self.searchBarFriends.setAutoFillBackground(False)
        self.searchBarFriends.setStyleSheet(u"border:none;\n"
"background-color:#3A3A3A;\n"
"padding-left:6px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Raleway\";\n"
"border-radius:10px;")
        self.searchBarFriends.setFrame(False)

        self.horizontalLayout_4.addWidget(self.searchBarFriends)


        self.FriendsLayout.addWidget(self.titleFriendsLayout)

        self.label_myFeed_5 = QLabel(self.mainWindowScrollAreaWidget)
        self.label_myFeed_5.setObjectName(u"label_myFeed_5")
        self.label_myFeed_5.setMinimumSize(QSize(0, 0))
        self.label_myFeed_5.setMaximumSize(QSize(400, 40))
        self.label_myFeed_5.setStyleSheet(u"font: 700 12pt \"Raleway\";\n"
"color: rgb(160, 160, 160);\n"
"margin-left:13px;")

        self.FriendsLayout.addWidget(self.label_myFeed_5)

        self.label_myFeed_6 = QLabel(self.mainWindowScrollAreaWidget)
        self.label_myFeed_6.setObjectName(u"label_myFeed_6")
        self.label_myFeed_6.setMinimumSize(QSize(0, 0))
        self.label_myFeed_6.setMaximumSize(QSize(400, 40))
        self.label_myFeed_6.setStyleSheet(u"font: 700 12pt \"Raleway\";\n"
"color: rgb(160, 160, 160);\n"
"margin-left:13px;")

        self.FriendsLayout.addWidget(self.label_myFeed_6)

        self.onlineFriendsLayout = QVBoxLayout()
        self.onlineFriendsLayout.setSpacing(6)
        self.onlineFriendsLayout.setObjectName(u"onlineFriendsLayout")
        self.onlineFriendsLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.onlineFriendsLayout.setContentsMargins(9, 10, -1, -1)

        self.FriendsLayout.addLayout(self.onlineFriendsLayout)

        self.offlineFriendsLayout = QVBoxLayout()
        self.offlineFriendsLayout.setSpacing(0)
        self.offlineFriendsLayout.setObjectName(u"offlineFriendsLayout")
        self.offlineFriendsLayout.setContentsMargins(-1, -1, -1, 40)

        self.FriendsLayout.addLayout(self.offlineFriendsLayout)

        self.frame_5 = QFrame(self.mainWindowScrollAreaWidget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)

        self.FriendsLayout.addWidget(self.frame_5)


        self.verticalLayout.addLayout(self.FriendsLayout)

        self.verticalLayout.setStretch(2, 1)

        self.MainLayout.addLayout(self.verticalLayout)

        self.friendsPostsDelimiteer = QFrame(self.mainWindowScrollAreaWidget)
        self.friendsPostsDelimiteer.setObjectName(u"friendsPostsDelimiteer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.friendsPostsDelimiteer.sizePolicy().hasHeightForWidth())
        self.friendsPostsDelimiteer.setSizePolicy(sizePolicy4)
        self.friendsPostsDelimiteer.setMinimumSize(QSize(2, 0))
        self.friendsPostsDelimiteer.setMaximumSize(QSize(2, 16777215))
        self.friendsPostsDelimiteer.setStyleSheet(u"background-color: rgb(116, 116, 116);")
        self.friendsPostsDelimiteer.setFrameShape(QFrame.Shape.StyledPanel)
        self.friendsPostsDelimiteer.setFrameShadow(QFrame.Shadow.Raised)

        self.MainLayout.addWidget(self.friendsPostsDelimiteer)

        self.postAreea = QVBoxLayout()
        self.postAreea.setObjectName(u"postAreea")
        self.postAreea.setContentsMargins(-1, 20, 20, -1)

        self.MainLayout.addLayout(self.postAreea)

        self.postAreaRecommendPostsDelimiter = QFrame(self.mainWindowScrollAreaWidget)
        self.postAreaRecommendPostsDelimiter.setObjectName(u"postAreaRecommendPostsDelimiter")
        sizePolicy4.setHeightForWidth(self.postAreaRecommendPostsDelimiter.sizePolicy().hasHeightForWidth())
        self.postAreaRecommendPostsDelimiter.setSizePolicy(sizePolicy4)
        self.postAreaRecommendPostsDelimiter.setMinimumSize(QSize(2, 0))
        self.postAreaRecommendPostsDelimiter.setMaximumSize(QSize(2, 16777215))
        self.postAreaRecommendPostsDelimiter.setStyleSheet(u"background-color: rgb(116, 116, 116);")
        self.postAreaRecommendPostsDelimiter.setFrameShape(QFrame.Shape.StyledPanel)
        self.postAreaRecommendPostsDelimiter.setFrameShadow(QFrame.Shadow.Raised)

        self.MainLayout.addWidget(self.postAreaRecommendPostsDelimiter)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, -1, 15, -1)

        self.MainLayout.addLayout(self.verticalLayout_2)

        self.MainLayout.setStretch(2, 1)

        self.MainWindowLayout.addLayout(self.MainLayout)

        self.MainWindowScrollArea.setWidget(self.mainWindowScrollAreaWidget)

        self.verticalLayout_3.addWidget(self.MainWindowScrollArea)


        self.retranslateUi(DetaliedPostView)

        QMetaObject.connectSlotsByName(DetaliedPostView)
    # setupUi

    def retranslateUi(self, DetaliedPostView):
        self.logoLabel.setText("")
        self.searchBar.setPlaceholderText(QCoreApplication.translate("DetaliedPostView", u"Search...", None))
        self.profileButton.setText("")
        self.notificationButton.setText("")
        self.shortcutSettingsButton.setText("")
        self.homeBtn.setText(QCoreApplication.translate("DetaliedPostView", u"Home", None))
        self.recommendedBtn.setText(QCoreApplication.translate("DetaliedPostView", u"Recommended", None))
        self.communitiesBtn.setText(QCoreApplication.translate("DetaliedPostView", u"Communities", None))
        self.myProfileBtn.setText(QCoreApplication.translate("DetaliedPostView", u"My Profile", None))
        self.settingsBtn.setText(QCoreApplication.translate("DetaliedPostView", u"Settings", None))
        self.disconnectBtn.setText(QCoreApplication.translate("DetaliedPostView", u"Disconnect", None))
        self.friendsTitleLabel.setText(QCoreApplication.translate("DetaliedPostView", u"Friends", None))
        self.searchBarFriends.setInputMask("")
        self.searchBarFriends.setText("")
        self.searchBarFriends.setPlaceholderText(QCoreApplication.translate("DetaliedPostView", u"Search", None))
        self.label_myFeed_5.setText(QCoreApplication.translate("DetaliedPostView", u"Online", None))
        self.label_myFeed_6.setText(QCoreApplication.translate("DetaliedPostView", u"Offline", None))
        pass
    # retranslateUi

