# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashBoardView.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

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
        self.mainVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainWindowScrollArea = QScrollArea(DashBoardView)
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
        self.mainWindowScrollAreaWidget.setGeometry(QRect(0, 0, 1424, 955))
        self.postsLayout = QVBoxLayout(self.mainWindowScrollAreaWidget)
        self.postsLayout.setSpacing(0)
        self.postsLayout.setObjectName(u"postsLayout")
        self.postsLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.postsLayout.setContentsMargins(0, 0, 0, 0)
        self.HeaderBar = QHBoxLayout()
        self.HeaderBar.setObjectName(u"HeaderBar")
        self.HeaderBar.setContentsMargins(35, -1, 15, 10)
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


        self.postsLayout.addLayout(self.HeaderBar)

        self.HeaderDelimiter = QFrame(self.mainWindowScrollAreaWidget)
        self.HeaderDelimiter.setObjectName(u"HeaderDelimiter")
        sizePolicy2.setHeightForWidth(self.HeaderDelimiter.sizePolicy().hasHeightForWidth())
        self.HeaderDelimiter.setSizePolicy(sizePolicy2)
        self.HeaderDelimiter.setMinimumSize(QSize(0, 1))
        self.HeaderDelimiter.setStyleSheet(u"background-color: rgb(116, 116, 116);")
        self.HeaderDelimiter.setFrameShape(QFrame.Shape.StyledPanel)
        self.HeaderDelimiter.setFrameShadow(QFrame.Shadow.Raised)

        self.postsLayout.addWidget(self.HeaderDelimiter)

        self.topFeedContent = QHBoxLayout()
        self.topFeedContent.setSpacing(0)
        self.topFeedContent.setObjectName(u"topFeedContent")
        self.topFeedContent.setContentsMargins(-1, -1, 0, 0)
        self.accesLinksLayout = QVBoxLayout()
        self.accesLinksLayout.setSpacing(12)
        self.accesLinksLayout.setObjectName(u"accesLinksLayout")
        self.accesLinksLayout.setContentsMargins(-1, 0, 0, 0)
        self.acessLinkSpacingFrame = QFrame(self.mainWindowScrollAreaWidget)
        self.acessLinkSpacingFrame.setObjectName(u"acessLinkSpacingFrame")
        self.acessLinkSpacingFrame.setMinimumSize(QSize(245, 1))
        self.acessLinkSpacingFrame.setMaximumSize(QSize(245, 16777215))
        self.acessLinkSpacingFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.acessLinkSpacingFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.accesLinksLayout.addWidget(self.acessLinkSpacingFrame)

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


        self.topFeedContent.addLayout(self.accesLinksLayout)

        self.accesLinkRightDelimiteer = QFrame(self.mainWindowScrollAreaWidget)
        self.accesLinkRightDelimiteer.setObjectName(u"accesLinkRightDelimiteer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.accesLinkRightDelimiteer.sizePolicy().hasHeightForWidth())
        self.accesLinkRightDelimiteer.setSizePolicy(sizePolicy3)
        self.accesLinkRightDelimiteer.setMinimumSize(QSize(2, 0))
        self.accesLinkRightDelimiteer.setMaximumSize(QSize(2, 16777215))
        self.accesLinkRightDelimiteer.setStyleSheet(u"background-color: rgb(116, 116, 116);")
        self.accesLinkRightDelimiteer.setFrameShape(QFrame.Shape.StyledPanel)
        self.accesLinkRightDelimiteer.setFrameShadow(QFrame.Shadow.Raised)

        self.topFeedContent.addWidget(self.accesLinkRightDelimiteer)

        self.TopFeedWidgetParent = QWidget(self.mainWindowScrollAreaWidget)
        self.TopFeedWidgetParent.setObjectName(u"TopFeedWidgetParent")
        sizePolicy2.setHeightForWidth(self.TopFeedWidgetParent.sizePolicy().hasHeightForWidth())
        self.TopFeedWidgetParent.setSizePolicy(sizePolicy2)
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
        self.verticalLayout_2 = QVBoxLayout(self.topCommunitiesGridWidget)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.CommRow_1 = QHBoxLayout()
        self.CommRow_1.setObjectName(u"CommRow_1")
        self.CommRow_1.setContentsMargins(-1, -1, -1, 0)

        self.verticalLayout_2.addLayout(self.CommRow_1)

        self.CommRow_2 = QHBoxLayout()
        self.CommRow_2.setObjectName(u"CommRow_2")

        self.verticalLayout_2.addLayout(self.CommRow_2)

        self.CommRow_3 = QHBoxLayout()
        self.CommRow_3.setObjectName(u"CommRow_3")

        self.verticalLayout_2.addLayout(self.CommRow_3)

        self.CommRow_4 = QHBoxLayout()
        self.CommRow_4.setObjectName(u"CommRow_4")

        self.verticalLayout_2.addLayout(self.CommRow_4)

        self.CommRow_5 = QHBoxLayout()
        self.CommRow_5.setObjectName(u"CommRow_5")

        self.verticalLayout_2.addLayout(self.CommRow_5)


        self.topCommunnitiesPopularHashTagLayout_2.addWidget(self.topCommunitiesGridWidget)

        self.delimiterTopCommunitiesPopularTags = QFrame(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.delimiterTopCommunitiesPopularTags.setObjectName(u"delimiterTopCommunitiesPopularTags")
        sizePolicy2.setHeightForWidth(self.delimiterTopCommunitiesPopularTags.sizePolicy().hasHeightForWidth())
        self.delimiterTopCommunitiesPopularTags.setSizePolicy(sizePolicy2)
        self.delimiterTopCommunitiesPopularTags.setMinimumSize(QSize(0, 2))
        self.delimiterTopCommunitiesPopularTags.setMaximumSize(QSize(16777215, 2))
        self.delimiterTopCommunitiesPopularTags.setStyleSheet(u"background-color: rgb(116, 116, 116);")
        self.delimiterTopCommunitiesPopularTags.setFrameShape(QFrame.Shape.StyledPanel)
        self.delimiterTopCommunitiesPopularTags.setFrameShadow(QFrame.Shadow.Raised)

        self.topCommunnitiesPopularHashTagLayout_2.addWidget(self.delimiterTopCommunitiesPopularTags)

        self.PopularHashtagsLabel = QLabel(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.PopularHashtagsLabel.setObjectName(u"PopularHashtagsLabel")
        sizePolicy2.setHeightForWidth(self.PopularHashtagsLabel.sizePolicy().hasHeightForWidth())
        self.PopularHashtagsLabel.setSizePolicy(sizePolicy2)
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

        self.popularHashtagsLayoutWidget = QVBoxLayout()
        self.popularHashtagsLayoutWidget.setSpacing(9)
        self.popularHashtagsLayoutWidget.setObjectName(u"popularHashtagsLayoutWidget")
        self.popularHashtagsLayoutWidget.setContentsMargins(9, 0, 9, 9)
        self.popularHashtagsLayoutWidgetFirstRow = QHBoxLayout()
        self.popularHashtagsLayoutWidgetFirstRow.setSpacing(6)
        self.popularHashtagsLayoutWidgetFirstRow.setObjectName(u"popularHashtagsLayoutWidgetFirstRow")
        self.label = QLabel(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setMinimumSize(QSize(0, 37))
        self.label.setMaximumSize(QSize(16777215, 60))
        self.label.setStyleSheet(u"font: 500 12pt \"Raleway\";\n"
"background-color: rgb(58, 58, 58);\n"
"border-radius:18px;\n"
"color:white;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label.setScaledContents(False)

        self.popularHashtagsLayoutWidgetFirstRow.addWidget(self.label)

        self.firstRowSpacer = QFrame(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.firstRowSpacer.setObjectName(u"firstRowSpacer")
        sizePolicy2.setHeightForWidth(self.firstRowSpacer.sizePolicy().hasHeightForWidth())
        self.firstRowSpacer.setSizePolicy(sizePolicy2)
        self.firstRowSpacer.setMaximumSize(QSize(16777215, 20))
        self.firstRowSpacer.setStyleSheet(u"border:none;")
        self.firstRowSpacer.setFrameShape(QFrame.Shape.StyledPanel)
        self.firstRowSpacer.setFrameShadow(QFrame.Shadow.Raised)

        self.popularHashtagsLayoutWidgetFirstRow.addWidget(self.firstRowSpacer)


        self.popularHashtagsLayoutWidget.addLayout(self.popularHashtagsLayoutWidgetFirstRow)

        self.popularHashtagsLayoutWidgetSecondRow = QHBoxLayout()
        self.popularHashtagsLayoutWidgetSecondRow.setSpacing(6)
        self.popularHashtagsLayoutWidgetSecondRow.setObjectName(u"popularHashtagsLayoutWidgetSecondRow")
        self.popularHashtagsLayoutWidgetSecondRow.setContentsMargins(-1, -1, -1, 0)
        self.label_5 = QLabel(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setMinimumSize(QSize(0, 37))
        self.label_5.setMaximumSize(QSize(16777215, 60))
        self.label_5.setStyleSheet(u"font: 500 12pt \"Raleway\";\n"
"background-color: rgb(58, 58, 58);\n"
"border-radius:18px;\n"
"color:white;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label_5.setScaledContents(False)

        self.popularHashtagsLayoutWidgetSecondRow.addWidget(self.label_5)

        self.firstRowSpacer_2 = QFrame(self.topCommunnitiesPopularHashTagLayoutWidget)
        self.firstRowSpacer_2.setObjectName(u"firstRowSpacer_2")
        sizePolicy2.setHeightForWidth(self.firstRowSpacer_2.sizePolicy().hasHeightForWidth())
        self.firstRowSpacer_2.setSizePolicy(sizePolicy2)
        self.firstRowSpacer_2.setMaximumSize(QSize(16777215, 20))
        self.firstRowSpacer_2.setStyleSheet(u"border:none;")
        self.firstRowSpacer_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.firstRowSpacer_2.setFrameShadow(QFrame.Shadow.Raised)

        self.popularHashtagsLayoutWidgetSecondRow.addWidget(self.firstRowSpacer_2)


        self.popularHashtagsLayoutWidget.addLayout(self.popularHashtagsLayoutWidgetSecondRow)


        self.topCommunnitiesPopularHashTagLayout_2.addLayout(self.popularHashtagsLayoutWidget)


        self.RecommendFeedLayout_2.addWidget(self.topCommunnitiesPopularHashTagLayoutWidget)

        self.accesLinkRightDelimiter = QFrame(self.TopFeedWidgetParent)
        self.accesLinkRightDelimiter.setObjectName(u"accesLinkRightDelimiter")
        sizePolicy3.setHeightForWidth(self.accesLinkRightDelimiter.sizePolicy().hasHeightForWidth())
        self.accesLinkRightDelimiter.setSizePolicy(sizePolicy3)
        self.accesLinkRightDelimiter.setMinimumSize(QSize(2, 0))
        self.accesLinkRightDelimiter.setMaximumSize(QSize(2, 16777215))
        self.accesLinkRightDelimiter.setStyleSheet(u"background-color: rgb(116, 116, 116);")
        self.accesLinkRightDelimiter.setFrameShape(QFrame.Shape.StyledPanel)
        self.accesLinkRightDelimiter.setFrameShadow(QFrame.Shadow.Raised)

        self.RecommendFeedLayout_2.addWidget(self.accesLinkRightDelimiter)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, 30)
        self.recommendedPostsLabel = QLabel(self.TopFeedWidgetParent)
        self.recommendedPostsLabel.setObjectName(u"recommendedPostsLabel")
        sizePolicy2.setHeightForWidth(self.recommendedPostsLabel.sizePolicy().hasHeightForWidth())
        self.recommendedPostsLabel.setSizePolicy(sizePolicy2)
        self.recommendedPostsLabel.setMinimumSize(QSize(400, 0))
        self.recommendedPostsLabel.setMaximumSize(QSize(16777215, 40))
        self.recommendedPostsLabel.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"margin-left: 30px;\n"
"border:0px;\n"
"color: rgb(160, 160, 160);\n"
"margin-top:5px;")

        self.verticalLayout.addWidget(self.recommendedPostsLabel)

        self.RecommendedFeedScrollArea = QScrollArea(self.TopFeedWidgetParent)
        self.RecommendedFeedScrollArea.setObjectName(u"RecommendedFeedScrollArea")
        sizePolicy.setHeightForWidth(self.RecommendedFeedScrollArea.sizePolicy().hasHeightForWidth())
        self.RecommendedFeedScrollArea.setSizePolicy(sizePolicy)
        self.RecommendedFeedScrollArea.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"")
        self.RecommendedFeedScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.RecommendedFeedScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.RecommendedFeedScrollArea.setWidgetResizable(True)
        self.RecommendedFeedScrollArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.recommendFeedScrollAreaWidget = QWidget()
        self.recommendFeedScrollAreaWidget.setObjectName(u"recommendFeedScrollAreaWidget")
        self.recommendFeedScrollAreaWidget.setGeometry(QRect(0, 0, 579, 176))
        self.postsLayout_2 = QHBoxLayout(self.recommendFeedScrollAreaWidget)
        self.postsLayout_2.setSpacing(0)
        self.postsLayout_2.setObjectName(u"postsLayout_2")
        self.postsLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.postsLayout_2.setContentsMargins(0, 0, 0, 0)
        self.recommendFeedHWidget = QHBoxLayout()
        self.recommendFeedHWidget.setSpacing(12)
        self.recommendFeedHWidget.setObjectName(u"recommendFeedHWidget")
        self.recommendFeedHWidget.setContentsMargins(9, 9, 9, 9)

        self.postsLayout_2.addLayout(self.recommendFeedHWidget)

        self.RecommendedFeedScrollArea.setWidget(self.recommendFeedScrollAreaWidget)

        self.verticalLayout.addWidget(self.RecommendedFeedScrollArea)


        self.RecommendFeedLayout_2.addLayout(self.verticalLayout)


        self.topFeedContent.addWidget(self.TopFeedWidgetParent)


        self.postsLayout.addLayout(self.topFeedContent)

        self.topContentDelmiter = QFrame(self.mainWindowScrollAreaWidget)
        self.topContentDelmiter.setObjectName(u"topContentDelmiter")
        sizePolicy2.setHeightForWidth(self.topContentDelmiter.sizePolicy().hasHeightForWidth())
        self.topContentDelmiter.setSizePolicy(sizePolicy2)
        self.topContentDelmiter.setMinimumSize(QSize(0, 1))
        self.topContentDelmiter.setStyleSheet(u"background-color: rgb(116, 116, 116);")
        self.topContentDelmiter.setFrameShape(QFrame.Shape.StyledPanel)
        self.topContentDelmiter.setFrameShadow(QFrame.Shadow.Raised)

        self.postsLayout.addWidget(self.topContentDelmiter)

        self.BottomContentLayout = QHBoxLayout()
        self.BottomContentLayout.setObjectName(u"BottomContentLayout")
        self.BottomContentLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.BottomContentLayout.setContentsMargins(-1, 0, 0, -1)
        self.FriendsLayout = QVBoxLayout()
        self.FriendsLayout.setSpacing(12)
        self.FriendsLayout.setObjectName(u"FriendsLayout")
        self.FriendsLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.FriendsLayout.setContentsMargins(-1, -1, -1, 30)
        self.friendsWidhtDelimiter = QFrame(self.mainWindowScrollAreaWidget)
        self.friendsWidhtDelimiter.setObjectName(u"friendsWidhtDelimiter")
        sizePolicy2.setHeightForWidth(self.friendsWidhtDelimiter.sizePolicy().hasHeightForWidth())
        self.friendsWidhtDelimiter.setSizePolicy(sizePolicy2)
        self.friendsWidhtDelimiter.setMinimumSize(QSize(245, 20))
        self.friendsWidhtDelimiter.setMaximumSize(QSize(16777215, 20))
        self.friendsWidhtDelimiter.setFrameShape(QFrame.Shape.StyledPanel)
        self.friendsWidhtDelimiter.setFrameShadow(QFrame.Shadow.Raised)

        self.FriendsLayout.addWidget(self.friendsWidhtDelimiter)

        self.titleFriendsLayout = QFrame(self.mainWindowScrollAreaWidget)
        self.titleFriendsLayout.setObjectName(u"titleFriendsLayout")
        self.titleFriendsLayout.setMinimumSize(QSize(0, 40))
        self.titleFriendsLayout.setMaximumSize(QSize(16777215, 40))
        self.titleFriendsLayout.setStyleSheet(u"")
        self.titleFriendsLayout.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleFriendsLayout.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.titleFriendsLayout)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.friendsTitleLabel = QLabel(self.titleFriendsLayout)
        self.friendsTitleLabel.setObjectName(u"friendsTitleLabel")
        self.friendsTitleLabel.setMinimumSize(QSize(0, 0))
        self.friendsTitleLabel.setMaximumSize(QSize(400, 40))
        self.friendsTitleLabel.setStyleSheet(u"font: 700 12pt \"Raleway\";\n"
"color: rgb(160, 160, 160);\n"
"margin-left:13px;")

        self.horizontalLayout.addWidget(self.friendsTitleLabel)

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

        self.horizontalLayout.addWidget(self.searchBarFriends)


        self.FriendsLayout.addWidget(self.titleFriendsLayout)

        self.label_myFeed_3 = QLabel(self.mainWindowScrollAreaWidget)
        self.label_myFeed_3.setObjectName(u"label_myFeed_3")
        self.label_myFeed_3.setMinimumSize(QSize(0, 0))
        self.label_myFeed_3.setMaximumSize(QSize(400, 40))
        self.label_myFeed_3.setStyleSheet(u"font: 700 12pt \"Raleway\";\n"
"color: rgb(160, 160, 160);\n"
"margin-left:13px;")

        self.FriendsLayout.addWidget(self.label_myFeed_3)

        self.onlineFriendsLayout = QVBoxLayout()
        self.onlineFriendsLayout.setSpacing(6)
        self.onlineFriendsLayout.setObjectName(u"onlineFriendsLayout")
        self.onlineFriendsLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.onlineFriendsLayout.setContentsMargins(9, 10, -1, -1)

        self.FriendsLayout.addLayout(self.onlineFriendsLayout)

        self.label_myFeed_4 = QLabel(self.mainWindowScrollAreaWidget)
        self.label_myFeed_4.setObjectName(u"label_myFeed_4")
        self.label_myFeed_4.setMinimumSize(QSize(0, 0))
        self.label_myFeed_4.setMaximumSize(QSize(400, 40))
        self.label_myFeed_4.setStyleSheet(u"font: 700 12pt \"Raleway\";\n"
"color: rgb(160, 160, 160);\n"
"margin-left:13px;")

        self.FriendsLayout.addWidget(self.label_myFeed_4)

        self.offlineFriendsLayout = QVBoxLayout()
        self.offlineFriendsLayout.setSpacing(0)
        self.offlineFriendsLayout.setObjectName(u"offlineFriendsLayout")
        self.offlineFriendsLayout.setContentsMargins(-1, -1, -1, 40)

        self.FriendsLayout.addLayout(self.offlineFriendsLayout)

        self.frame_4 = QFrame(self.mainWindowScrollAreaWidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)

        self.FriendsLayout.addWidget(self.frame_4)


        self.BottomContentLayout.addLayout(self.FriendsLayout)

        self.friendsPostsDelimiteer = QFrame(self.mainWindowScrollAreaWidget)
        self.friendsPostsDelimiteer.setObjectName(u"friendsPostsDelimiteer")
        sizePolicy3.setHeightForWidth(self.friendsPostsDelimiteer.sizePolicy().hasHeightForWidth())
        self.friendsPostsDelimiteer.setSizePolicy(sizePolicy3)
        self.friendsPostsDelimiteer.setMinimumSize(QSize(2, 0))
        self.friendsPostsDelimiteer.setMaximumSize(QSize(2, 16777215))
        self.friendsPostsDelimiteer.setStyleSheet(u"background-color: rgb(116, 116, 116);")
        self.friendsPostsDelimiteer.setFrameShape(QFrame.Shape.StyledPanel)
        self.friendsPostsDelimiteer.setFrameShadow(QFrame.Shadow.Raised)

        self.BottomContentLayout.addWidget(self.friendsPostsDelimiteer)

        self.postAreea = QVBoxLayout()
        self.postAreea.setObjectName(u"postAreea")
        self.postAreea.setContentsMargins(-1, 20, 20, -1)

        self.BottomContentLayout.addLayout(self.postAreea)

        self.BottomContentLayout.setStretch(2, 1)

        self.postsLayout.addLayout(self.BottomContentLayout)

        self.frame_2 = QFrame(self.mainWindowScrollAreaWidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.postsLayout.addWidget(self.frame_2)

        self.MainWindowScrollArea.setWidget(self.mainWindowScrollAreaWidget)

        self.mainVerticalLayout.addWidget(self.MainWindowScrollArea)


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
        self.TopCommunitiesLabel.setText(QCoreApplication.translate("DashBoardView", u"TOP COMMUNITIES", None))
        self.PopularHashtagsLabel.setText(QCoreApplication.translate("DashBoardView", u"POPUlAR HASHTAGS", None))
        self.label.setText(QCoreApplication.translate("DashBoardView", u"#Exemplu Tag 1", None))
        self.label_5.setText(QCoreApplication.translate("DashBoardView", u"#Exemplu Tag 2", None))
        self.recommendedPostsLabel.setText(QCoreApplication.translate("DashBoardView", u"RECOMMENDED POSTS", None))
        self.friendsTitleLabel.setText(QCoreApplication.translate("DashBoardView", u"Friends", None))
        self.searchBarFriends.setInputMask("")
        self.searchBarFriends.setText("")
        self.searchBarFriends.setPlaceholderText(QCoreApplication.translate("DashBoardView", u"Search", None))
        self.label_myFeed_3.setText(QCoreApplication.translate("DashBoardView", u"Online", None))
        self.label_myFeed_4.setText(QCoreApplication.translate("DashBoardView", u"Offline", None))
        pass
    # retranslateUi

