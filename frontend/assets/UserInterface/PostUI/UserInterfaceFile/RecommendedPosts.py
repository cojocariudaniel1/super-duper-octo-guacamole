# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RecommendedPosts.ui'
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
    QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_RecommendedPostsWidget(object):
    def setupUi(self, RecommendedPostsWidget):
        if not RecommendedPostsWidget.objectName():
            RecommendedPostsWidget.setObjectName(u"RecommendedPostsWidget")
        RecommendedPostsWidget.resize(350, 346)
        RecommendedPostsWidget.setMinimumSize(QSize(350, 0))
        RecommendedPostsWidget.setMaximumSize(QSize(350, 346))
        RecommendedPostsWidget.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border-radius: 18px;\n"
"")
        RecommendedPostsWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout = QVBoxLayout(RecommendedPostsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.contentWidget = QWidget(RecommendedPostsWidget)
        self.contentWidget.setObjectName(u"contentWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contentWidget.sizePolicy().hasHeightForWidth())
        self.contentWidget.setSizePolicy(sizePolicy)
        self.contentWidget.setMinimumSize(QSize(0, 0))
        self.contentWidget.setMaximumSize(QSize(16777215, 16777215))
        self.contentWidget.setStyleSheet(u"background: transparent;")
        self.horizontalLayout = QHBoxLayout(self.contentWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 0, 0, 0)
        self.postContentWidget = QWidget(self.contentWidget)
        self.postContentWidget.setObjectName(u"postContentWidget")
        sizePolicy.setHeightForWidth(self.postContentWidget.sizePolicy().hasHeightForWidth())
        self.postContentWidget.setSizePolicy(sizePolicy)
        self.postContentWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.postContentWidget)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setSpacing(6)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(9, -1, -1, -1)
        self.communityIcon = QLabel(self.postContentWidget)
        self.communityIcon.setObjectName(u"communityIcon")
        self.communityIcon.setMinimumSize(QSize(16, 16))
        self.communityIcon.setMaximumSize(QSize(16, 16))
        self.communityIcon.setStyleSheet(u"")

        self.headerLayout.addWidget(self.communityIcon)

        self.communityName = QLabel(self.postContentWidget)
        self.communityName.setObjectName(u"communityName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.communityName.sizePolicy().hasHeightForWidth())
        self.communityName.setSizePolicy(sizePolicy1)
        self.communityName.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 10px;\n"
"line-height: 12px;\n"
"color: white;\n"
"margin:5px;\n"
"")

        self.headerLayout.addWidget(self.communityName)

        self.postTime = QLabel(self.postContentWidget)
        self.postTime.setObjectName(u"postTime")
        self.postTime.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 10px;\n"
"line-height: 12px;\n"
"color:white;\n"
"margin:5px;")

        self.headerLayout.addWidget(self.postTime)

        self.frame = QFrame(self.postContentWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.headerLayout.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.headerLayout)

        self.authorLayout = QHBoxLayout()
        self.authorLayout.setSpacing(0)
        self.authorLayout.setObjectName(u"authorLayout")
        self.userAvatar = QLabel(self.postContentWidget)
        self.userAvatar.setObjectName(u"userAvatar")
        self.userAvatar.setMinimumSize(QSize(34, 34))
        self.userAvatar.setMaximumSize(QSize(34, 34))
        self.userAvatar.setStyleSheet(u"border-radius: 17px;\n"
"")

        self.authorLayout.addWidget(self.userAvatar)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.username = QLabel(self.postContentWidget)
        self.username.setObjectName(u"username")
        self.username.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 12px;\n"
"line-height: 14px;\n"
"color:white;\n"
"margin-left:2px;\n"
"margin-top:3px;\n"
"margin-bottom:3px;")

        self.verticalLayout_3.addWidget(self.username)

        self.usernamePoints = QLabel(self.postContentWidget)
        self.usernamePoints.setObjectName(u"usernamePoints")
        self.usernamePoints.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 10px;\n"
"line-height: 12px;\n"
"color:white;\n"
"margin-left:5px;\n"
"")

        self.verticalLayout_3.addWidget(self.usernamePoints)


        self.authorLayout.addLayout(self.verticalLayout_3)

        self.frame_2 = QFrame(self.postContentWidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.authorLayout.addWidget(self.frame_2)


        self.verticalLayout_2.addLayout(self.authorLayout)

        self.postTitle = QLabel(self.postContentWidget)
        self.postTitle.setObjectName(u"postTitle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.postTitle.sizePolicy().hasHeightForWidth())
        self.postTitle.setSizePolicy(sizePolicy2)
        self.postTitle.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"color:white;\n"
"margin:5px;\n"
"margin-top:10px;\n"
"")
        self.postTitle.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.postTitle)

        self.textBrowserContent = QTextBrowser(self.postContentWidget)
        self.textBrowserContent.setObjectName(u"textBrowserContent")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.textBrowserContent.sizePolicy().hasHeightForWidth())
        self.textBrowserContent.setSizePolicy(sizePolicy3)
        self.textBrowserContent.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 14px;\n"
"line-height: 16px;\n"
"color:white;\n"
"background: transparent;\n"
"border: none;\n"
"margin-left:6px;\n"
"padding-bottom:30x;")
        self.textBrowserContent.setFrameShape(QFrame.Shape.NoFrame)
        self.textBrowserContent.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textBrowserContent.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout_2.addWidget(self.textBrowserContent)

        self.footerLayout = QHBoxLayout()
        self.footerLayout.setSpacing(6)
        self.footerLayout.setObjectName(u"footerLayout")
        self.footerLayout.setContentsMargins(6, 0, 6, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.likeButtonIcon = QPushButton(self.postContentWidget)
        self.likeButtonIcon.setObjectName(u"likeButtonIcon")
        self.likeButtonIcon.setMinimumSize(QSize(25, 25))
        self.likeButtonIcon.setMaximumSize(QSize(25, 25))
        self.likeButtonIcon.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.likeButtonIcon)

        self.likeCount = QLabel(self.postContentWidget)
        self.likeCount.setObjectName(u"likeCount")
        self.likeCount.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 10px;\n"
"line-height: 12px;\n"
"color:white;\n"
"margin-left:5px;")

        self.verticalLayout_4.addWidget(self.likeCount)


        self.footerLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.commentButtonIcon = QPushButton(self.postContentWidget)
        self.commentButtonIcon.setObjectName(u"commentButtonIcon")
        self.commentButtonIcon.setMinimumSize(QSize(25, 25))
        self.commentButtonIcon.setMaximumSize(QSize(25, 25))
        self.commentButtonIcon.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.commentButtonIcon)

        self.commentCount = QLabel(self.postContentWidget)
        self.commentCount.setObjectName(u"commentCount")
        self.commentCount.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 10px;\n"
"line-height: 12px;\n"
"color:white;\n"
"margin-left:5px;\n"
"margin-right:10px;")

        self.verticalLayout_5.addWidget(self.commentCount)


        self.footerLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.replyCommentButtonIcon = QPushButton(self.postContentWidget)
        self.replyCommentButtonIcon.setObjectName(u"replyCommentButtonIcon")
        self.replyCommentButtonIcon.setMinimumSize(QSize(25, 25))
        self.replyCommentButtonIcon.setMaximumSize(QSize(25, 25))
        self.replyCommentButtonIcon.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.replyCommentButtonIcon)

        self.mockLabel1 = QLabel(self.postContentWidget)
        self.mockLabel1.setObjectName(u"mockLabel1")
        self.mockLabel1.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 10px;\n"
"line-height: 12px;\n"
"color:white;\n"
"margin-left:5px;\n"
"margin-right:10px;")

        self.verticalLayout_6.addWidget(self.mockLabel1)


        self.footerLayout.addLayout(self.verticalLayout_6)

        self.frame_3 = QFrame(self.postContentWidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.footerLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addLayout(self.footerLayout)


        self.horizontalLayout.addWidget(self.postContentWidget)

        self.divider = QFrame(self.contentWidget)
        self.divider.setObjectName(u"divider")
        self.divider.setMinimumSize(QSize(1, 0))
        self.divider.setStyleSheet(u"border: 1px solid rgba(85, 85, 85, 0.7);")
        self.divider.setFrameShape(QFrame.Shape.VLine)
        self.divider.setFrameShadow(QFrame.Shadow.Plain)

        self.horizontalLayout.addWidget(self.divider)


        self.verticalLayout.addWidget(self.contentWidget)


        self.retranslateUi(RecommendedPostsWidget)

        QMetaObject.connectSlotsByName(RecommendedPostsWidget)
    # setupUi

    def retranslateUi(self, RecommendedPostsWidget):
        self.communityName.setText(QCoreApplication.translate("RecommendedPostsWidget", u"RoadAccidents", None))
        self.postTime.setText(QCoreApplication.translate("RecommendedPostsWidget", u"1h ago", None))
        self.username.setText(QCoreApplication.translate("RecommendedPostsWidget", u"Gaudy3!p", None))
        self.usernamePoints.setText(QCoreApplication.translate("RecommendedPostsWidget", u"190 points", None))
        self.postTitle.setText(QCoreApplication.translate("RecommendedPostsWidget", u"Had a car accident, could use some advice", None))
        self.likeButtonIcon.setText("")
        self.likeCount.setText(QCoreApplication.translate("RecommendedPostsWidget", u"103", None))
        self.commentButtonIcon.setText("")
        self.commentCount.setText(QCoreApplication.translate("RecommendedPostsWidget", u"25", None))
        self.replyCommentButtonIcon.setText("")
        self.mockLabel1.setText("")
        pass
    # retranslateUi

