# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFormLayout, QFrame,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1440, 1024)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -10, 1440, 1050))
        self.frame.setStyleSheet(u"background: #D9D9D9;\n"
"")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.loginButton = QPushButton(self.frame)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(490, 690, 465, 72))
        self.loginButton.setMinimumSize(QSize(465, 72))
        self.loginButton.setMaximumSize(QSize(458, 72))
        self.loginButton.setStyleSheet(u"background: #1E1E1E;\n"
"font: 600 24pt \"Segoe UI\";\n"
"border-radius: 36px;\n"
"color:white;\n"
"")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(500, 280, 458, 295))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.userNameFrame = QFrame(self.widget)
        self.userNameFrame.setObjectName(u"userNameFrame")
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

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.userNameFrame)

        self.userNameFrame_2 = QFrame(self.widget)
        self.userNameFrame_2.setObjectName(u"userNameFrame_2")
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordInput.sizePolicy().hasHeightForWidth())
        self.passwordInput.setSizePolicy(sizePolicy)
        self.passwordInput.setMinimumSize(QSize(400, 60))
        self.passwordInput.setMaximumSize(QSize(400, 16777215))
        self.passwordInput.setStyleSheet(u"")
        self.passwordInput.setFrame(False)
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.userNameFrame_2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.linkResetPassword = QCommandLinkButton(self.widget)
        self.linkResetPassword.setObjectName(u"linkResetPassword")
        self.linkResetPassword.setMaximumSize(QSize(16777215, 42))
        self.linkResetPassword.setAutoFillBackground(False)
        self.linkResetPassword.setStyleSheet(u"font: 600 18pt \"Segoe UI\";\n"
"transition: none;  \n"
"background-color: rgba(255, 255, 255, 0);")
        self.linkResetPassword.setText(u"   Reset Password")
        self.linkResetPassword.setIconSize(QSize(0, 0))
        self.linkResetPassword.setAutoRepeatDelay(0)
        self.linkResetPassword.setAutoRepeatInterval(0)
        self.linkResetPassword.setAutoDefault(False)
        self.linkResetPassword.setDefault(False)
        self.linkResetPassword.setDescription(u"")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.linkResetPassword)

        self.linkRegister = QCommandLinkButton(self.widget)
        self.linkRegister.setObjectName(u"linkRegister")
        self.linkRegister.setMaximumSize(QSize(16777215, 42))
        self.linkRegister.setAutoFillBackground(False)
        self.linkRegister.setStyleSheet(u"font: 600 18pt \"Segoe UI\";\n"
"transition: none;  \n"
"background-color: rgba(255, 255, 255, 0);")
        self.linkRegister.setText(u"   Not registered yet? Register now")
        self.linkRegister.setIconSize(QSize(0, 0))
        self.linkRegister.setAutoRepeatDelay(0)
        self.linkRegister.setAutoRepeatInterval(0)
        self.linkRegister.setAutoDefault(False)
        self.linkRegister.setDefault(False)
        self.linkRegister.setDescription(u"")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.linkRegister)


        self.formLayout.setLayout(2, QFormLayout.LabelRole, self.formLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.loginButton.setText(QCoreApplication.translate("Form", u"Login", None))
        self.userNameInput.setText("")
        self.userNameInput.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.passwordInput.setText("")
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
    # retranslateUi

