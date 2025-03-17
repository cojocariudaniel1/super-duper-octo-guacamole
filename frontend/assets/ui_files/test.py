# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ForumAppUI(object):
    def setupUi(self, ForumAppUI):
        if not ForumAppUI.objectName():
            ForumAppUI.setObjectName(u"ForumAppUI")
        ForumAppUI.resize(1440, 600)
        ForumAppUI.setStyleSheet(u"background: #1A1A1B;\n"
"")
        self.mainLayout = QHBoxLayout(ForumAppUI)
        self.mainLayout.setObjectName(u"mainLayout")
        self.sidebar = QWidget(ForumAppUI)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebarLayout = QVBoxLayout(self.sidebar)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.communityList = QListWidget(self.sidebar)
        self.communityList.setObjectName(u"communityList")

        self.sidebarLayout.addWidget(self.communityList)

        self.recentPostsList = QListWidget(self.sidebar)
        self.recentPostsList.setObjectName(u"recentPostsList")

        self.sidebarLayout.addWidget(self.recentPostsList)


        self.mainLayout.addWidget(self.sidebar)

        self.ContentPosts_ScrollArea = QScrollArea(ForumAppUI)
        self.ContentPosts_ScrollArea.setObjectName(u"ContentPosts_ScrollArea")
        self.ContentPosts_ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1140, 580))
        self.postsLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.postsLayout.setObjectName(u"postsLayout")
        self.ContentPosts_ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.mainLayout.addWidget(self.ContentPosts_ScrollArea)


        self.retranslateUi(ForumAppUI)

        QMetaObject.connectSlotsByName(ForumAppUI)
    # setupUi

    def retranslateUi(self, ForumAppUI):
        pass
    # retranslateUi

