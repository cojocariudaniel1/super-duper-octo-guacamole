# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLayout,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(765, 351)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.MainWindowScrollArea = QScrollArea(self.frame)
        self.MainWindowScrollArea.setObjectName(u"MainWindowScrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainWindowScrollArea.sizePolicy().hasHeightForWidth())
        self.MainWindowScrollArea.setSizePolicy(sizePolicy)
        self.MainWindowScrollArea.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"")
        self.MainWindowScrollArea.setWidgetResizable(True)
        self.MainWindowScrollArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainWindowScrollAreaWidget = QWidget()
        self.mainWindowScrollAreaWidget.setObjectName(u"mainWindowScrollAreaWidget")
        self.mainWindowScrollAreaWidget.setGeometry(QRect(0, 0, 727, 313))
        self.postsLayout = QHBoxLayout(self.mainWindowScrollAreaWidget)
        self.postsLayout.setSpacing(0)
        self.postsLayout.setObjectName(u"postsLayout")
        self.postsLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.postsLayout.setContentsMargins(0, 0, 0, 0)
        self.MainWindowScrollArea.setWidget(self.mainWindowScrollAreaWidget)

        self.horizontalLayout.addWidget(self.MainWindowScrollArea)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

