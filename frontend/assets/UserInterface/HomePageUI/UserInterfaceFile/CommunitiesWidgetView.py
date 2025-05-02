# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CommunitiesWidgetView.ui'
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

class Ui_CommunitiesWidget(object):
    def setupUi(self, CommunitiesWidget):
        if not CommunitiesWidget.objectName():
            CommunitiesWidget.setObjectName(u"CommunitiesWidget")
        CommunitiesWidget.resize(204, 67)
        CommunitiesWidget.setMinimumSize(QSize(204, 50))
        CommunitiesWidget.setMaximumSize(QSize(204, 16777215))
        CommunitiesWidget.setStyleSheet(u"background-color: rgb(30, 30, 30,0);")
        self.horizontalLayout_2 = QHBoxLayout(CommunitiesWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(CommunitiesWidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.widget.setStyleSheet(u"background-color: rgb(58, 58, 58);\n"
"border-radius:24px;")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon = QLabel(self.widget)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(32, 32))
        self.icon.setMaximumSize(QSize(32, 32))
        self.icon.setStyleSheet(u"border-radius: 16px;\n"
"")
        self.icon.setFrameShadow(QFrame.Shadow.Plain)
        self.icon.setPixmap(QPixmap(u"C:/Users/cojoc/Downloads/image 1.png"))
        self.icon.setScaledContents(False)
        self.icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icon.setWordWrap(False)

        self.horizontalLayout.addWidget(self.icon)

        self.communityName = QLabel(self.widget)
        self.communityName.setObjectName(u"communityName")
        self.communityName.setStyleSheet(u"font: 500 12pt \"Raleway\";\n"
"color: rgb(217, 217, 217);")

        self.horizontalLayout.addWidget(self.communityName)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frame)

        self.horizontalLayout.setStretch(0, 1)

        self.horizontalLayout_2.addWidget(self.widget)


        self.retranslateUi(CommunitiesWidget)

        QMetaObject.connectSlotsByName(CommunitiesWidget)
    # setupUi

    def retranslateUi(self, CommunitiesWidget):
        CommunitiesWidget.setWindowTitle(QCoreApplication.translate("CommunitiesWidget", u"Form", None))
        self.icon.setText("")
        self.communityName.setText(QCoreApplication.translate("CommunitiesWidget", u"Gaudy3!p", None))
    # retranslateUi

