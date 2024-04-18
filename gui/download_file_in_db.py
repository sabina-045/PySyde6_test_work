# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'download_file_in_db.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(298, 386)
        Dialog.setMaximumSize(QSize(298, 386))
        Dialog.setBaseSize(QSize(0, 0))
        Dialog.setStyleSheet(u"background-color: rgba(213, 198, 180, 150);")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(280, 368))
        self.frame.setStyleSheet(u"background-color: rgb(75, 75, 75)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_open_file = QPushButton(self.frame)
        self.pushButton_open_file.setObjectName(u"pushButton_open_file")
        self.pushButton_open_file.setStyleSheet(
                u"QPushButton {\n"
                "background-color: rgba(255, 132, 83,  200);\n"
                "width: 200 px;\n"
                "height: 50 px;\n"
                "font: 10pt \"Verdana\";\n"
                "}\n"
                "\n"
                "QPushButton:hover:!pressed {\n"
                "background-color: rgba(255, 132, 83,  250);\n"
                "}\n"
                "\n"
                "QPushButton:hover:pressed {\n"
                "background-color: rgba(255, 132, 83,  180);\n"
                "}")

        self.verticalLayout.addWidget(self.pushButton_open_file)

        self.lineEdit_path = QLineEdit(self.frame)
        self.lineEdit_path.setObjectName(u"lineEdit_path")
        self.lineEdit_path.setStyleSheet(
                u"background-color: rgba(213, 198, 180, 150);\n"
                "width: 200 px;\n"
                "height: 25 px;\n"
                "font: 8pt \"Verdana\";")

        self.verticalLayout.addWidget(self.lineEdit_path)

        self.pushButton_download = QPushButton(self.frame)
        self.pushButton_download.setObjectName(u"pushButton_download")
        self.pushButton_download.setStyleSheet(
                u"QPushButton {\n"
                "background-color: rgba(255, 132, 83,  200);\n"
                "width: 200 px;\n"
                "height: 50 px;\n"
                "font: 10pt \"Verdana\";\n"
                "}\n"
                "\n"
                "QPushButton:hover:!pressed {\n"
                "background-color: rgba(255, 132, 83,  250);\n"
                "}\n"
                "\n"
                "QPushButton:hover:pressed {\n"
                "background-color: rgba(255, 132, 83,  180);\n"
                "}")

        self.verticalLayout.addWidget(self.pushButton_download)

        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_open_file.setText(QCoreApplication.translate("Dialog", u"\u041e\u0422\u041a\u0420\u042b\u0422\u042c \u0424\u0410\u0419\u041b", None))
        self.pushButton_download.setText(QCoreApplication.translate("Dialog", u"\u0417\u0410\u0413\u0420\u0423\u0417\u0418\u0422\u042c", None))
    # retranslateUi

