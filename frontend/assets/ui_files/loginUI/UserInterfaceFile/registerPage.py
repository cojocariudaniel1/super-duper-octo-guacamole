# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerPage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_registerForm(object):
    def setupUi(self, registerForm):
        if not registerForm.objectName():
            registerForm.setObjectName(u"registerForm")
        registerForm.resize(1440, 1024)
        self.userNameFrame = QFrame(registerForm)
        self.userNameFrame.setObjectName(u"userNameFrame")
        self.userNameFrame.setGeometry(QRect(450, 220, 450, 72))
        self.userNameFrame.setMinimumSize(QSize(450, 72))
        self.userNameFrame.setStyleSheet(u"background: #1E1E1E;\n"
"font: 600 24pt \"Segoe UI\";\n"
"border-radius: 36px;\n"
"color:white;\n"
"")
        self.userNameFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.userNameFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.userNameInput = QLineEdit(self.userNameFrame)
        self.userNameInput.setObjectName(u"userNameInput")
        self.userNameInput.setGeometry(QRect(28, 4, 400, 60))
        self.userNameInput.setMinimumSize(QSize(400, 60))
        self.userNameInput.setMaximumSize(QSize(400, 16777215))
        self.userNameInput.setStyleSheet(u"")
        self.userNameInput.setFrame(False)
        self.userNameFrame_2 = QFrame(registerForm)
        self.userNameFrame_2.setObjectName(u"userNameFrame_2")
        self.userNameFrame_2.setGeometry(QRect(450, 320, 450, 72))
        self.userNameFrame_2.setMinimumSize(QSize(450, 72))
        self.userNameFrame_2.setStyleSheet(u"background: #1E1E1E;\n"
"font: 600 24pt \"Segoe UI\";\n"
"border-radius: 36px;\n"
"color:white;\n"
"")
        self.userNameFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.userNameFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.passwordInput = QLineEdit(self.userNameFrame_2)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setGeometry(QRect(28, 4, 400, 60))
        self.passwordInput.setMinimumSize(QSize(400, 60))
        self.passwordInput.setMaximumSize(QSize(400, 16777215))
        self.passwordInput.setStyleSheet(u"")
        self.passwordInput.setFrame(False)
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.userNameFrame_3 = QFrame(registerForm)
        self.userNameFrame_3.setObjectName(u"userNameFrame_3")
        self.userNameFrame_3.setGeometry(QRect(450, 420, 450, 72))
        self.userNameFrame_3.setMinimumSize(QSize(450, 72))
        self.userNameFrame_3.setStyleSheet(u"background: #1E1E1E;\n"
"font: 600 24pt \"Segoe UI\";\n"
"border-radius: 36px;\n"
"color:white;\n"
"")
        self.userNameFrame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.userNameFrame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.repeatPasswordInput = QLineEdit(self.userNameFrame_3)
        self.repeatPasswordInput.setObjectName(u"repeatPasswordInput")
        self.repeatPasswordInput.setGeometry(QRect(28, 4, 400, 60))
        self.repeatPasswordInput.setMinimumSize(QSize(400, 60))
        self.repeatPasswordInput.setMaximumSize(QSize(400, 16777215))
        self.repeatPasswordInput.setStyleSheet(u"")
        self.repeatPasswordInput.setFrame(False)
        self.repeatPasswordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.userNameFrame_4 = QFrame(registerForm)
        self.userNameFrame_4.setObjectName(u"userNameFrame_4")
        self.userNameFrame_4.setGeometry(QRect(450, 520, 450, 72))
        self.userNameFrame_4.setMinimumSize(QSize(450, 72))
        self.userNameFrame_4.setStyleSheet(u"background: #1E1E1E;\n"
"font: 600 24pt \"Segoe UI\";\n"
"border-radius: 36px;\n"
"color:white;\n"
"")
        self.userNameFrame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.userNameFrame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.emailInput = QLineEdit(self.userNameFrame_4)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setGeometry(QRect(28, 4, 400, 60))
        self.emailInput.setMinimumSize(QSize(400, 60))
        self.emailInput.setMaximumSize(QSize(400, 16777215))
        self.emailInput.setStyleSheet(u"")
        self.emailInput.setFrame(False)
        self.userNameFrame_5 = QFrame(registerForm)
        self.userNameFrame_5.setObjectName(u"userNameFrame_5")
        self.userNameFrame_5.setGeometry(QRect(450, 610, 450, 72))
        self.userNameFrame_5.setMinimumSize(QSize(450, 72))
        self.userNameFrame_5.setStyleSheet(u"background: #1E1E1E;\n"
"font: 600 24pt \"Segoe UI\";\n"
"border-radius: 36px;\n"
"color:white;\n"
"")
        self.userNameFrame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.userNameFrame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.ageInput = QLineEdit(self.userNameFrame_5)
        self.ageInput.setObjectName(u"ageInput")
        self.ageInput.setGeometry(QRect(28, 4, 400, 60))
        self.ageInput.setMinimumSize(QSize(400, 60))
        self.ageInput.setMaximumSize(QSize(400, 16777215))
        self.ageInput.setStyleSheet(u"")
        self.ageInput.setFrame(False)
        self.registerButton = QPushButton(registerForm)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setGeometry(QRect(450, 750, 450, 72))
        self.registerButton.setMinimumSize(QSize(450, 72))
        self.registerButton.setMaximumSize(QSize(450, 72))
        self.registerButton.setStyleSheet(u"background: #1E1E1E;\n"
"font: 600 24pt \"Segoe UI\";\n"
"width: 458;\n"
"height: 62;\n"
"top: -656px;\n"
"left: -610px;\n"
"border-radius: 36px;\n"
"color:white;\n"
"")

        self.retranslateUi(registerForm)

        QMetaObject.connectSlotsByName(registerForm)
    # setupUi

    def retranslateUi(self, registerForm):
        registerForm.setWindowTitle(QCoreApplication.translate("registerForm", u"Form", None))
        self.userNameInput.setText("")
        self.userNameInput.setPlaceholderText(QCoreApplication.translate("registerForm", u"Username", None))
        self.passwordInput.setText("")
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("registerForm", u"Password", None))
        self.repeatPasswordInput.setText("")
        self.repeatPasswordInput.setPlaceholderText(QCoreApplication.translate("registerForm", u"Repeat password", None))
        self.emailInput.setText("")
        self.emailInput.setPlaceholderText(QCoreApplication.translate("registerForm", u"email", None))
        self.ageInput.setText("")
        self.ageInput.setPlaceholderText(QCoreApplication.translate("registerForm", u"age", None))
        self.registerButton.setText(QCoreApplication.translate("registerForm", u"Register", None))
    # retranslateUi

