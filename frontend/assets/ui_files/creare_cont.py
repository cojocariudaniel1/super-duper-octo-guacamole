# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'creare_cont.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_CreateAccountPage(object):
    def setupUi(self, CreateAccountPage):
        if not CreateAccountPage.objectName():
            CreateAccountPage.setObjectName(u"CreateAccountPage")
        CreateAccountPage.resize(1440, 900)
        self.mainLayout = QVBoxLayout(CreateAccountPage)
        self.mainLayout.setObjectName(u"mainLayout")
        self.titleLabel = QLabel(CreateAccountPage)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.mainLayout.addWidget(self.titleLabel)

        self.usernameInput = QLineEdit(CreateAccountPage)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setMinimumSize(QSize(400, 50))

        self.mainLayout.addWidget(self.usernameInput)

        self.emailInput = QLineEdit(CreateAccountPage)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setMinimumSize(QSize(400, 50))

        self.mainLayout.addWidget(self.emailInput)

        self.passwordInput = QLineEdit(CreateAccountPage)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setMinimumSize(QSize(400, 50))

        self.mainLayout.addWidget(self.passwordInput)

        self.confirmPasswordInput = QLineEdit(CreateAccountPage)
        self.confirmPasswordInput.setObjectName(u"confirmPasswordInput")
        self.confirmPasswordInput.setEchoMode(QLineEdit.Password)
        self.confirmPasswordInput.setMinimumSize(QSize(400, 50))

        self.mainLayout.addWidget(self.confirmPasswordInput)

        self.createAccountButton = QPushButton(CreateAccountPage)
        self.createAccountButton.setObjectName(u"createAccountButton")
        self.createAccountButton.setMinimumSize(QSize(200, 50))

        self.mainLayout.addWidget(self.createAccountButton)

        self.backToLoginButton = QPushButton(CreateAccountPage)
        self.backToLoginButton.setObjectName(u"backToLoginButton")
        self.backToLoginButton.setMinimumSize(QSize(200, 50))

        self.mainLayout.addWidget(self.backToLoginButton)


        self.retranslateUi(CreateAccountPage)

        QMetaObject.connectSlotsByName(CreateAccountPage)
    # setupUi

    def retranslateUi(self, CreateAccountPage):
        CreateAccountPage.setStyleSheet(QCoreApplication.translate("CreateAccountPage", u"background-color: rgb(40, 40, 40); color: white;", None))
        self.titleLabel.setStyleSheet(QCoreApplication.translate("CreateAccountPage", u"font-size: 36px; font-weight: bold; color: white;", None))
        self.titleLabel.setText(QCoreApplication.translate("CreateAccountPage", u"Create Account", None))
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("CreateAccountPage", u"Username", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("CreateAccountPage", u"Email", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("CreateAccountPage", u"Password", None))
        self.confirmPasswordInput.setPlaceholderText(QCoreApplication.translate("CreateAccountPage", u"Confirm Password", None))
        self.createAccountButton.setText(QCoreApplication.translate("CreateAccountPage", u"Create Account", None))
        self.createAccountButton.setStyleSheet(QCoreApplication.translate("CreateAccountPage", u"background-color: rgb(0, 122, 204); color: white; font-weight: bold; padding: 10px;", None))
        self.backToLoginButton.setText(QCoreApplication.translate("CreateAccountPage", u"Back to Login", None))
        self.backToLoginButton.setStyleSheet(QCoreApplication.translate("CreateAccountPage", u"color: white; font-weight: bold;", None))
    # retranslateUi

