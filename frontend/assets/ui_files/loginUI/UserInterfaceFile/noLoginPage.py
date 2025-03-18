# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noLoginPage.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLayout,
    QPushButton, QSizePolicy, QWidget)

class Ui_noLoginWindow(object):
    def setupUi(self, noLoginWindow):
        if not noLoginWindow.objectName():
            noLoginWindow.setObjectName(u"noLoginWindow")
        noLoginWindow.resize(1440, 1024)
        self.frame = QFrame(noLoginWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -10, 1440, 1050))
        self.frame.setStyleSheet(u"background-color: rgb(98, 98, 98);\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(500, 390, 473, 171))
        self.formLayout_2 = QFormLayout(self.layoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setVerticalSpacing(0)
        self.loginButton = QPushButton(self.layoutWidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(0, 72))
        self.loginButton.setMaximumSize(QSize(230, 100))
        self.loginButton.setStyleSheet(u"background: #1E1E1E;\n"
"font: 600 24pt \"Segoe UI\";\n"
"width: 458;\n"
"height: 62;\n"
"top: -656px;\n"
"left: -610px;\n"
"border-radius: 36px;\n"
"color:white;\n"
"")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.loginButton)

        self.registerButton = QPushButton(self.layoutWidget)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setMinimumSize(QSize(0, 72))
        self.registerButton.setMaximumSize(QSize(226, 72))
        self.registerButton.setStyleSheet(u"background: #1E1E1E;\n"
"font: 600 24pt \"Segoe UI\";\n"
"width: 458;\n"
"height: 62;\n"
"top: -656px;\n"
"left: -610px;\n"
"border-radius: 36px;\n"
"color:white;\n"
"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.registerButton)


        self.formLayout_2.setLayout(0, QFormLayout.LabelRole, self.formLayout)

        self.loginAsGuestButton = QPushButton(self.layoutWidget)
        self.loginAsGuestButton.setObjectName(u"loginAsGuestButton")
        self.loginAsGuestButton.setMinimumSize(QSize(465, 72))
        self.loginAsGuestButton.setMaximumSize(QSize(458, 72))
        self.loginAsGuestButton.setStyleSheet(u"background: #1E1E1E;\n"
"font: 600 24pt \"Segoe UI\";\n"
"width: 458;\n"
"height: 62;\n"
"top: -656px;\n"
"left: -610px;\n"
"border-radius: 36px;\n"
"color:white;\n"
"")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.loginAsGuestButton)


        self.retranslateUi(noLoginWindow)

        QMetaObject.connectSlotsByName(noLoginWindow)
    # setupUi

    def retranslateUi(self, noLoginWindow):
        noLoginWindow.setWindowTitle(QCoreApplication.translate("noLoginWindow", u"Form", None))
        self.loginButton.setText(QCoreApplication.translate("noLoginWindow", u"Login", None))
        self.registerButton.setText(QCoreApplication.translate("noLoginWindow", u"Register", None))
        self.loginAsGuestButton.setText(QCoreApplication.translate("noLoginWindow", u"Login as Guest", None))
    # retranslateUi

