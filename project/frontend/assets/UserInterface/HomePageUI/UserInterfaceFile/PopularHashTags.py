# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PopularHashTags.ui'
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
    QSizePolicy, QWidget)

class Ui_PopularHashTagsWidget(object):
    def setupUi(self, PopularHashTagsWidget):
        if not PopularHashTagsWidget.objectName():
            PopularHashTagsWidget.setObjectName(u"PopularHashTagsWidget")
        PopularHashTagsWidget.resize(204, 67)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PopularHashTagsWidget.sizePolicy().hasHeightForWidth())
        PopularHashTagsWidget.setSizePolicy(sizePolicy)
        PopularHashTagsWidget.setMinimumSize(QSize(204, 50))
        PopularHashTagsWidget.setMaximumSize(QSize(16777215, 16777215))
        PopularHashTagsWidget.setStyleSheet(u"background-color: rgb(30, 30, 30,0);")
        self.horizontalLayout_2 = QHBoxLayout(PopularHashTagsWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(PopularHashTagsWidget)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.widget.setStyleSheet(u"background-color: rgb(58, 58, 58);\n"
"border-radius:24px;")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.tagName = QLabel(self.frame)
        self.tagName.setObjectName(u"tagName")
        self.tagName.setGeometry(QRect(10, 0, 161, 32))
        self.tagName.setStyleSheet(u"font: 500 12pt \"Raleway\";\n"
"color: rgb(217, 217, 217);")

        self.horizontalLayout.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.widget)


        self.retranslateUi(PopularHashTagsWidget)

        QMetaObject.connectSlotsByName(PopularHashTagsWidget)
    # setupUi

    def retranslateUi(self, PopularHashTagsWidget):
        PopularHashTagsWidget.setWindowTitle(QCoreApplication.translate("PopularHashTagsWidget", u"Form", None))
        self.tagName.setText(QCoreApplication.translate("PopularHashTagsWidget", u"#Gaudy3!p", None))
    # retranslateUi

