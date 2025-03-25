# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FeedPostWidget.ui'
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
    QLayout, QPushButton, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_FeedPostWidget(object):
    def setupUi(self, FeedPostWidget):
        if not FeedPostWidget.objectName():
            FeedPostWidget.setObjectName(u"FeedPostWidget")
        FeedPostWidget.resize(1167, 259)
        FeedPostWidget.setMinimumSize(QSize(1167, 259))
        FeedPostWidget.setMaximumSize(QSize(1167, 259))
        FeedPostWidget.setStyleSheet(u"background: #D9D9D9;\n"
"border-radius: 18px;\n"
"")
        FeedPostWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout = QVBoxLayout(FeedPostWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.contentWidget = QWidget(FeedPostWidget)
        self.contentWidget.setObjectName(u"contentWidget")
        self.contentWidget.setStyleSheet(u"background: transparent;")
        self.horizontalLayout = QHBoxLayout(self.contentWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.postContentWidget = QWidget(self.contentWidget)
        self.postContentWidget.setObjectName(u"postContentWidget")
        self.postContentWidget.setMinimumSize(QSize(700, 0))
        self.postContentWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.postContentWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setSpacing(4)
        self.headerLayout.setObjectName(u"headerLayout")
        self.communityIcon = QLabel(self.postContentWidget)
        self.communityIcon.setObjectName(u"communityIcon")
        self.communityIcon.setMinimumSize(QSize(13, 13))
        self.communityIcon.setMaximumSize(QSize(13, 13))
        self.communityIcon.setStyleSheet(u"background: #555555;\n"
"border-radius: 6px;")

        self.headerLayout.addWidget(self.communityIcon)

        self.communityName = QLabel(self.postContentWidget)
        self.communityName.setObjectName(u"communityName")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.communityName.sizePolicy().hasHeightForWidth())
        self.communityName.setSizePolicy(sizePolicy)
        self.communityName.setMaximumSize(QSize(9999, 9999))
        self.communityName.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 10px;\n"
"line-height: 12px;\n"
"color: #1A1A1B;\n"
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
"color: #555555;\n"
"margin:5px;")

        self.headerLayout.addWidget(self.postTime)

        self.frame = QFrame(self.postContentWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.headerLayout.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.headerLayout)

        self.authorLayout = QHBoxLayout()
        self.authorLayout.setSpacing(0)
        self.authorLayout.setObjectName(u"authorLayout")
        self.authorIcon = QLabel(self.postContentWidget)
        self.authorIcon.setObjectName(u"authorIcon")
        self.authorIcon.setMinimumSize(QSize(31, 30))
        self.authorIcon.setMaximumSize(QSize(31, 30))
        self.authorIcon.setStyleSheet(u"background: #1A1A1B;\n"
"border-radius: 15px;\n"
"")

        self.authorLayout.addWidget(self.authorIcon)

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
"color: #1A1A1B;\n"
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
"color: #1A1A1B;\n"
"margin-left:5px;\n"
"")

        self.verticalLayout_3.addWidget(self.usernamePoints)


        self.authorLayout.addLayout(self.verticalLayout_3)

        self.authorLabel = QLabel(self.postContentWidget)
        self.authorLabel.setObjectName(u"authorLabel")
        self.authorLabel.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 12px;\n"
"line-height: 14px;\n"
"color: #555555;\n"
"margin-bottom:11px;")

        self.authorLayout.addWidget(self.authorLabel)

        self.frame_2 = QFrame(self.postContentWidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.authorLayout.addWidget(self.frame_2)


        self.verticalLayout_2.addLayout(self.authorLayout)

        self.postTitle = QLabel(self.postContentWidget)
        self.postTitle.setObjectName(u"postTitle")
        self.postTitle.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"color: #1A1A1B;\n"
"margin:5px;\n"
"margin-top:10px;\n"
"")

        self.verticalLayout_2.addWidget(self.postTitle)

        self.textBrowserContent = QTextBrowser(self.postContentWidget)
        self.textBrowserContent.setObjectName(u"textBrowserContent")
        self.textBrowserContent.setMinimumSize(QSize(715, 95))
        self.textBrowserContent.setMaximumSize(QSize(715, 95))
        self.textBrowserContent.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 14px;\n"
"line-height: 16px;\n"
"color: #1A1A1B;\n"
"background: transparent;\n"
"border: none;\n"
"margin-left:6px;")
        self.textBrowserContent.setFrameShape(QFrame.Shape.NoFrame)
        self.textBrowserContent.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textBrowserContent.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout_2.addWidget(self.textBrowserContent)

        self.footerLayout = QHBoxLayout()
        self.footerLayout.setSpacing(0)
        self.footerLayout.setObjectName(u"footerLayout")
        self.likeButton = QPushButton(self.postContentWidget)
        self.likeButton.setObjectName(u"likeButton")
        self.likeButton.setMinimumSize(QSize(13, 13))
        self.likeButton.setMaximumSize(QSize(13, 13))
        self.likeButton.setStyleSheet(u"background: #1A1A1B;\n"
"border: 1.5px solid #D9D9D9;\n"
"border-radius: 6px;")

        self.footerLayout.addWidget(self.likeButton)

        self.likeCount = QLabel(self.postContentWidget)
        self.likeCount.setObjectName(u"likeCount")
        self.likeCount.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 10px;\n"
"line-height: 12px;\n"
"color: #1A1A1B;\n"
"margin-left:5px;")

        self.footerLayout.addWidget(self.likeCount)

        self.commentButton = QPushButton(self.postContentWidget)
        self.commentButton.setObjectName(u"commentButton")
        self.commentButton.setMinimumSize(QSize(13, 12))
        self.commentButton.setMaximumSize(QSize(13, 12))
        self.commentButton.setStyleSheet(u"background: #1A1A1B;\n"
"border: 1.5px solid #D9D9D9;\n"
"border-radius: 6px;")

        self.footerLayout.addWidget(self.commentButton)

        self.commentCount = QLabel(self.postContentWidget)
        self.commentCount.setObjectName(u"commentCount")
        self.commentCount.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 10px;\n"
"line-height: 12px;\n"
"color: #1A1A1B;\n"
"margin-left:5px;\n"
"margin-right:10px;")

        self.footerLayout.addWidget(self.commentCount)

        self.tagsBrowser = QTextBrowser(self.postContentWidget)
        self.tagsBrowser.setObjectName(u"tagsBrowser")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tagsBrowser.sizePolicy().hasHeightForWidth())
        self.tagsBrowser.setSizePolicy(sizePolicy2)
        self.tagsBrowser.setMinimumSize(QSize(645, 0))
        self.tagsBrowser.setMaximumSize(QSize(645, 50))
        self.tagsBrowser.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 10px;\n"
"line-height: 12px;\n"
"color: rgba(85, 85, 85, 0.7);\n"
"background: transparent;\n"
"border: none;")

        self.footerLayout.addWidget(self.tagsBrowser)

        self.frame_3 = QFrame(self.postContentWidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.footerLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addLayout(self.footerLayout)


        self.horizontalLayout.addWidget(self.postContentWidget)

        self.divider = QFrame(self.contentWidget)
        self.divider.setObjectName(u"divider")
        self.divider.setMinimumSize(QSize(1, 213))
        self.divider.setMaximumSize(QSize(1, 213))
        self.divider.setStyleSheet(u"border: 1px solid rgba(85, 85, 85, 0.7);")
        self.divider.setFrameShape(QFrame.Shape.VLine)
        self.divider.setFrameShadow(QFrame.Shadow.Plain)

        self.horizontalLayout.addWidget(self.divider)

        self.commentsWidget = QWidget(self.contentWidget)
        self.commentsWidget.setObjectName(u"commentsWidget")
        self.commentsWidget.setMinimumSize(QSize(330, 0))
        self.commentsWidget.setMaximumSize(QSize(348, 16777215))
        self.commentsWidget.setStyleSheet(u"margins-left:-20px;\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.commentsWidget)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.commentSectionLabel = QLabel(self.commentsWidget)
        self.commentSectionLabel.setObjectName(u"commentSectionLabel")
        self.commentSectionLabel.setMaximumSize(QSize(16777215, 20))
        self.commentSectionLabel.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 12px;\n"
"line-height: 14px;\n"
"color: #555555;")

        self.verticalLayout_4.addWidget(self.commentSectionLabel)

        self.widget = QWidget(self.commentsWidget)
        self.widget.setObjectName(u"widget")
        self.commentContent = QTextBrowser(self.widget)
        self.commentContent.setObjectName(u"commentContent")
        self.commentContent.setGeometry(QRect(0, 50, 291, 91))
        self.commentContent.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 14px;\n"
"line-height: 16px;\n"
"color: #1A1A1B;\n"
"background: transparent;\n"
"border: none;\n"
"margin-left:6px;")
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 8, 190, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.icon = QLabel(self.layoutWidget)
        self.icon.setObjectName(u"icon")
        self.icon.setPixmap(QPixmap(u"../../../images/userIcon1.png"))
        self.icon.setScaledContents(False)

        self.horizontalLayout_2.addWidget(self.icon)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.username_2 = QLabel(self.layoutWidget)
        self.username_2.setObjectName(u"username_2")
        self.username_2.setStyleSheet(u"/* Gaudy3!p */\n"
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
"color:black;\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.username_2)

        self.pointsLabel = QLabel(self.layoutWidget)
        self.pointsLabel.setObjectName(u"pointsLabel")
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
"color: black;\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.pointsLabel)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.postTime_2 = QLabel(self.layoutWidget)
        self.postTime_2.setObjectName(u"postTime_2")
        self.postTime_2.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 10px;\n"
"line-height: 12px;\n"
"color: #555555;\n"
"margin-bottom:20px;")

        self.horizontalLayout_2.addWidget(self.postTime_2)

        self.commentCount_2 = QLabel(self.widget)
        self.commentCount_2.setObjectName(u"commentCount_2")
        self.commentCount_2.setGeometry(QRect(53, 101, 30, 50))
        self.commentCount_2.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 10px;\n"
"line-height: 12px;\n"
"color: #1A1A1B;\n"
"margin-left:5px;\n"
"margin-right:10px;")
        self.commentButton_2 = QPushButton(self.widget)
        self.commentButton_2.setObjectName(u"commentButton_2")
        self.commentButton_2.setGeometry(QRect(40, 120, 13, 12))
        self.commentButton_2.setMinimumSize(QSize(13, 12))
        self.commentButton_2.setMaximumSize(QSize(13, 12))
        self.commentButton_2.setStyleSheet(u"background: #1A1A1B;\n"
"border: 1.5px solid #D9D9D9;\n"
"border-radius: 6px;")
        self.likeButton_2 = QPushButton(self.widget)
        self.likeButton_2.setObjectName(u"likeButton_2")
        self.likeButton_2.setGeometry(QRect(7, 118, 13, 13))
        self.likeButton_2.setMinimumSize(QSize(13, 13))
        self.likeButton_2.setMaximumSize(QSize(13, 13))
        self.likeButton_2.setStyleSheet(u"background: #1A1A1B;\n"
"border: 1.5px solid #D9D9D9;\n"
"border-radius: 6px;")
        self.likeCount_2 = QLabel(self.widget)
        self.likeCount_2.setObjectName(u"likeCount_2")
        self.likeCount_2.setGeometry(QRect(20, 100, 25, 50))
        self.likeCount_2.setStyleSheet(u"font-family: 'Raleway';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 10px;\n"
"line-height: 12px;\n"
"color: #1A1A1B;\n"
"margin-left:5px;")

        self.verticalLayout_4.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.commentsWidget)


        self.verticalLayout.addWidget(self.contentWidget)


        self.retranslateUi(FeedPostWidget)

        QMetaObject.connectSlotsByName(FeedPostWidget)
    # setupUi

    def retranslateUi(self, FeedPostWidget):
        self.communityName.setText(QCoreApplication.translate("FeedPostWidget", u"RoadAccidents", None))
        self.postTime.setText(QCoreApplication.translate("FeedPostWidget", u"1h ago", None))
        self.username.setText(QCoreApplication.translate("FeedPostWidget", u"Gaudy3!p", None))
        self.usernamePoints.setText(QCoreApplication.translate("FeedPostWidget", u"190 points", None))
        self.authorLabel.setText(QCoreApplication.translate("FeedPostWidget", u"author", None))
        self.postTitle.setText(QCoreApplication.translate("FeedPostWidget", u"Had a car accident, could use some advice", None))
        self.textBrowserContent.setHtml(QCoreApplication.translate("FeedPostWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Raleway'; font-size:14px; font-weight:500; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#1a1a1b;\">Hey everyone, I'm reaching out because I'm feeling a bit overwhelmed after being in a car accident, and I could really use some advice or just to hear from others who might have gone through something similar.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#1a"
                        "1a1b;\">So, here's what happened: I was driving home from work the other day, just like any other day, when out of nowhere, a car ran a red light and slammed into the front of my vehicle. Honestly, I'm still kind of in shock.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#1a1a1b;\">The damage to my car is significant, especially to the bumper and fender, but thankfully, I wasn't seriously hurt\u2014just some soreness and a few bruises. It's a relief, but it's still been a lot to process.</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" color:#1a1a1b;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Insurance confusion: I've filed the claim, but I'm not really sure what to expect next. The insurance company mentioned something about a &quo"
                        "t;coverage assessment,&quot; and I'm feeling kind of lost in the whole process. Anyone been through this?</li>\n"
"<li style=\" color:#1a1a1b;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Car repair worries: My car definitely needs some work, and I'm trying to figure out where to go for repairs. I want to make sure I find a good place that won't rip me off, but I'm just not sure how to go about it.</li>\n"
"<li style=\" color:#1a1a1b;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Emotional stuff: Honestly, I didn't expect this part to hit me so hard, but I've been feeling pretty anxious and shaken up. I'm nervous about getting back behind the wheel. Has anyone experienced this after an accident? How did you get through it?</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span"
                        " style=\" color:#1a1a1b;\">I know I'm lucky that things weren't worse, but it's still a lot to handle. </span></p></body></html>", None))
        self.likeButton.setText("")
        self.likeCount.setText(QCoreApplication.translate("FeedPostWidget", u"103", None))
        self.commentButton.setText("")
        self.commentCount.setText(QCoreApplication.translate("FeedPostWidget", u"25", None))
        self.tagsBrowser.setHtml(QCoreApplication.translate("FeedPostWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Raleway'; font-size:10px; font-weight:500; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">adadadad</p></body></html>", None))
        self.commentSectionLabel.setText(QCoreApplication.translate("FeedPostWidget", u"Comment Section", None))
        self.commentContent.setHtml(QCoreApplication.translate("FeedPostWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Raleway'; font-size:14px; font-weight:500; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400;\">I totally get what you\u2019re going through. I had a similar experience last year, and the aftermath can be just as tough as the accident itself. The insurance process was confusing...</span></p></body></html>", None))
        self.icon.setText("")
        self.username_2.setText(QCoreApplication.translate("FeedPostWidget", u"PrestonAvy", None))
        self.pointsLabel.setText(QCoreApplication.translate("FeedPostWidget", u"102 points", None))
        self.postTime_2.setText(QCoreApplication.translate("FeedPostWidget", u"1h ago", None))
        self.commentCount_2.setText(QCoreApplication.translate("FeedPostWidget", u"25", None))
        self.commentButton_2.setText("")
        self.likeButton_2.setText("")
        self.likeCount_2.setText(QCoreApplication.translate("FeedPostWidget", u"103", None))
        pass
    # retranslateUi

