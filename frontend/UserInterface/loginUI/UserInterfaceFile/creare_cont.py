# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'creare_cont.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

class Ui_CreateAccountPage(object):
    def setupUi(self, CreateAccountPage):
        if not CreateAccountPage.objectName():
            CreateAccountPage.setObjectName(u"CreateAccountPage")
        CreateAccountPage.resize(1440, 900)
        self.mainLayout = QVBoxLayout(CreateAccountPage)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(450, 150, 450, 200)
        self.titleLabel = QLabel(CreateAccountPage)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMaximumSize(QSize(16777215, 40))
        self.titleLabel.setStyleSheet(u"font: 800 24pt \"Raleway\";\n"
"color:#D9D9D9;")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainLayout.addWidget(self.titleLabel)

        self.textBrowser_2 = QTextBrowser(CreateAccountPage)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setMaximumSize(QSize(16777215, 60))
        self.textBrowser_2.setStyleSheet(u"font: 500 9pt \"Raleway\";\n"
"border:none;\n"
"padding-left: -10px;")

        self.mainLayout.addWidget(self.textBrowser_2)

        self.usernameInput = QLineEdit(CreateAccountPage)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setMinimumSize(QSize(400, 52))
        self.usernameInput.setStyleSheet(u"background: #D9D9D9;\n"
"font: 500 16pt \"Raleway\";\n"
"border-radius: 18px;\n"
"color:#555555;\n"
"padding-left: 10px;")

        self.mainLayout.addWidget(self.usernameInput)

        self.emailInput = QLineEdit(CreateAccountPage)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setMinimumSize(QSize(400, 50))
        self.emailInput.setStyleSheet(u"background: #D9D9D9;\n"
"font: 500 16pt \"Raleway\";\n"
"border-radius: 18px;\n"
"color:#555555;\n"
"padding-left: 10px;\n"
"")

        self.mainLayout.addWidget(self.emailInput)

        self.passwordInput = QLineEdit(CreateAccountPage)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setMinimumSize(QSize(400, 50))
        self.passwordInput.setStyleSheet(u"background: #D9D9D9;\n"
"font: 500 16pt \"Raleway\";\n"
"border-radius: 18px;\n"
"color:#555555;\n"
"padding-left: 10px;\n"
"")
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.mainLayout.addWidget(self.passwordInput)

        self.confirmPasswordInput = QLineEdit(CreateAccountPage)
        self.confirmPasswordInput.setObjectName(u"confirmPasswordInput")
        self.confirmPasswordInput.setMinimumSize(QSize(400, 50))
        self.confirmPasswordInput.setStyleSheet(u"background: #D9D9D9;\n"
"font: 500 16pt \"Raleway\";\n"
"border-radius: 18px;\n"
"color:#555555;\n"
"padding-left: 10px;\n"
"")
        self.confirmPasswordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.mainLayout.addWidget(self.confirmPasswordInput)

        self.textBrowser = QTextBrowser(CreateAccountPage)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(0, 60))
        self.textBrowser.setMaximumSize(QSize(16777215, 60))
        self.textBrowser.setStyleSheet(u"border:none;\n"
"padding-left: -10px;")

        self.mainLayout.addWidget(self.textBrowser)

        self.createAccountButton = QPushButton(CreateAccountPage)
        self.createAccountButton.setObjectName(u"createAccountButton")
        self.createAccountButton.setMinimumSize(QSize(200, 50))
        self.createAccountButton.setStyleSheet(u"background: #B3D334;\n"
"font: 700 16pt \"Raleway\";\n"
"border-radius: 18px;\n"
"color:#3A3A3A;\n"
"")

        self.mainLayout.addWidget(self.createAccountButton)


        self.retranslateUi(CreateAccountPage)

        QMetaObject.connectSlotsByName(CreateAccountPage)
    # setupUi

    def retranslateUi(self, CreateAccountPage):
        CreateAccountPage.setStyleSheet(QCoreApplication.translate("CreateAccountPage", u"background-color: rgb(40, 40, 40); color: white;", None))
        self.titleLabel.setText(QCoreApplication.translate("CreateAccountPage", u"SignUp", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("CreateAccountPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Raleway'; font-size:9pt; font-weight:500; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:400; color:#d9d9d9;\">  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:400; color:#d9d9d9;\">    By proceeding, you consent to our     </span><span style=\" font-family:'Segoe UI'; font-weight:400; color:#b3d334;\""
                        ">User Agreement</span><span style=\" font-family:'Segoe UI'; font-weight:400; color:#d9d9d9;\"><br />    and confirm that you have read and understood the     </span><span style=\" font-family:'Segoe UI'; font-weight:400; color:#b3d334;\">Privacy Policy</span><span style=\" font-family:'Segoe UI'; font-weight:400; color:#d9d9d9;\">.  </span></p></body></html>", None))
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("CreateAccountPage", u"Username", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("CreateAccountPage", u"Email", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("CreateAccountPage", u"Password", None))
        self.confirmPasswordInput.setPlaceholderText(QCoreApplication.translate("CreateAccountPage", u"Confirm Password", None))
        self.textBrowser.setHtml(QCoreApplication.translate("CreateAccountPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d9d9d9;\">  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d9d9d9;\">    Don\u2019t have an account yet?     </span><span style=\" color:#b3d334;\">Sign up</span><span style=\" color:#d9d9d9;\">  </span></p></body></html>", None))
        self.createAccountButton.setText(QCoreApplication.translate("CreateAccountPage", u"Sign Up", None))
    # retranslateUi

