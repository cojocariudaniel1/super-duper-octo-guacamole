# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        if not LoginPage.objectName():
            LoginPage.setObjectName(u"LoginPage")
        LoginPage.resize(1920, 1080)
        self.mainLayout = QVBoxLayout(LoginPage)
        self.mainLayout.setObjectName(u"mainLayout")
        self.topSpacer = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.topSpacer)

        self.titleLabel = QLabel(LoginPage)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.mainLayout.addWidget(self.titleLabel)

        self.middleSpacer1 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.middleSpacer1)

        self.usernameInput = QLineEdit(LoginPage)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setMinimumSize(QSize(400, 50))

        self.mainLayout.addWidget(self.usernameInput)

        self.middleSpacer2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.middleSpacer2)

        self.passwordInput = QLineEdit(LoginPage)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setMinimumSize(QSize(400, 50))

        self.mainLayout.addWidget(self.passwordInput)

        self.middleSpacer3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.middleSpacer3)

        self.loginButton = QPushButton(LoginPage)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(200, 50))

        self.mainLayout.addWidget(self.loginButton)

        self.middleSpacer4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.middleSpacer4)

        self.createAccountButton = QPushButton(LoginPage)
        self.createAccountButton.setObjectName(u"createAccountButton")
        self.createAccountButton.setMinimumSize(QSize(200, 50))

        self.mainLayout.addWidget(self.createAccountButton)

        self.bottomSpacer = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.bottomSpacer)


        self.retranslateUi(LoginPage)

        QMetaObject.connectSlotsByName(LoginPage)
    # setupUi

    def retranslateUi(self, LoginPage):
        LoginPage.setStyleSheet(QCoreApplication.translate("LoginPage", u"background-color: rgb(40, 40, 40); color: white;", None))
        self.titleLabel.setStyleSheet(QCoreApplication.translate("LoginPage", u"font-size: 36px; font-weight: bold; color: white;", None))
        self.titleLabel.setText(QCoreApplication.translate("LoginPage", u"Login", None))
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("LoginPage", u"Username or Email", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("LoginPage", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("LoginPage", u"Login", None))
        self.loginButton.setStyleSheet(QCoreApplication.translate("LoginPage", u"background-color: rgb(0, 122, 204); color: white; font-weight: bold; padding: 10px;", None))
        self.createAccountButton.setText(QCoreApplication.translate("LoginPage", u"Create Account", None))
        self.createAccountButton.setStyleSheet(QCoreApplication.translate("LoginPage", u"color: white; font-weight: bold;", None))
    # retranslateUi

