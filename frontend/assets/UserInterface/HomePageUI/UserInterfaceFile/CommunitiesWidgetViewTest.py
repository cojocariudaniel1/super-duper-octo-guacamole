# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CommunitiesWidgetViewTest.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(205, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(143, 50))
        Form.setMaximumSize(QSize(16777215, 50))
        Form.setStyleSheet(u"background-color: rgb(58, 58, 58);\n"
"border-radius:24px;")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon = QLabel(Form)
        self.icon.setObjectName(u"icon")
        self.icon.setMaximumSize(QSize(32, 31))
        self.icon.setPixmap(QPixmap(u"../../../images/userIcon1.png"))
        self.icon.setScaledContents(False)
        self.icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icon.setWordWrap(False)

        self.horizontalLayout.addWidget(self.icon)

        self.username = QLabel(Form)
        self.username.setObjectName(u"username")
        self.username.setStyleSheet(u"font: 500 12pt \"Raleway\";\n"
"color: rgb(217, 217, 217);")

        self.horizontalLayout.addWidget(self.username)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.icon.setText("")
        self.username.setText(QCoreApplication.translate("Form", u"Gaudy3!p", None))
    # retranslateUi

