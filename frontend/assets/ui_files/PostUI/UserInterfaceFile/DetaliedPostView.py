# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DetaliedPostView.ui'
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
    QLayout, QSizePolicy, QVBoxLayout, QWidget)

class Ui_DetailedPostView(object):
    def setupUi(self, DetailedPostView):
        if not DetailedPostView.objectName():
            DetailedPostView.setObjectName(u"DetailedPostView")
        DetailedPostView.resize(1206, 264)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DetailedPostView.sizePolicy().hasHeightForWidth())
        DetailedPostView.setSizePolicy(sizePolicy)
        DetailedPostView.setMinimumSize(QSize(0, 200))
        DetailedPostView.setStyleSheet(u"background: #252526; border-radius: 8px; padding: 10px; margin: 5px; color: white;")
        self.postLayout = QVBoxLayout(DetailedPostView)
        self.postLayout.setObjectName(u"postLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.frame_2 = QFrame(DetailedPostView)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(400, 75))
        self.frame_2.setStyleSheet(u"background: #1A1A1B;")
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
        self.author_label = QLabel(self.horizontalLayoutWidget)
        self.author_label.setObjectName(u"author_label")
        self.author_label.setStyleSheet(u"font: 12pt \"Raleway\";")

        self.horizontalLayout.addWidget(self.author_label)

        self.timestamp_label = QLabel(self.horizontalLayoutWidget)
        self.timestamp_label.setObjectName(u"timestamp_label")
        self.timestamp_label.setStyleSheet(u"font: 12pt \"Raleway\";")

        self.horizontalLayout.addWidget(self.timestamp_label)


        self.verticalLayout.addWidget(self.frame_2)

        self.post_title_label = QLabel(DetailedPostView)
        self.post_title_label.setObjectName(u"post_title_label")
        self.post_title_label.setStyleSheet(u"color: white;\n"
"font: 800 18pt \"Raleway\";")

        self.verticalLayout.addWidget(self.post_title_label)

        self.content_label = QLabel(DetailedPostView)
        self.content_label.setObjectName(u"content_label")
        self.content_label.setStyleSheet(u"font:14pt \"Raleway\";\n"
"border-radius: 10px; ")
        self.content_label.setTextFormat(Qt.TextFormat.AutoText)
        self.content_label.setScaledContents(True)
        self.content_label.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)
        self.content_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.content_label)


        self.postLayout.addLayout(self.verticalLayout)


        self.retranslateUi(DetailedPostView)

        QMetaObject.connectSlotsByName(DetailedPostView)
    # setupUi

    def retranslateUi(self, DetailedPostView):
        self.profileIcon.setText("")
        self.author_label.setText(QCoreApplication.translate("DetailedPostView", u"Author Name", None))
        self.timestamp_label.setText(QCoreApplication.translate("DetailedPostView", u"Timestamp", None))
        self.post_title_label.setText(QCoreApplication.translate("DetailedPostView", u"Post Title", None))
        self.content_label.setText(QCoreApplication.translate("DetailedPostView", u"Post content goes here...", None))
        pass
    # retranslateUi

