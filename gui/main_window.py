# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(849, 535)
        MainWindow.setStyleSheet(u"background-color: rgb(213, 198, 180);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(75, 75, 75)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_download_in_db = QPushButton(self.frame)
        self.pushButton_download_in_db.setObjectName(u"pushButton_download_in_db")
        self.pushButton_download_in_db.setStyleSheet(
                    u"QPushButton {\n"
                    "color: black;\n"
                    "background-color: rgba(255, 132, 83,  200);\n"
                    "font: 9pt \"Verdana\";\n"
                    "width: 200 px;\n"
                    "height: 50 px;\n"
                    "}\n"
                    "\n"
                    "QPushButton:hover:!pressed {\n"
                    "background-color: rgba(255, 132, 83,  250);\n"
                    "}\n"
                    "\n"
                    "QPushButton:hover:pressed {\n"
                    "background-color: rgba(255, 132, 83,  180);\n"
                    "}")

        self.gridLayout.addWidget(self.pushButton_download_in_db, 0, 0, 1, 1)

        self.pushButton_count_results = QPushButton(self.frame)
        self.pushButton_count_results.setObjectName(u"pushButton_count_results")
        self.pushButton_count_results.setStyleSheet(
                u"QPushButton {\n"
                "color: black;\n"
                "background-color: rgba(255, 132, 83,  200);\n"
                "font: 9pt \"Verdana\";\n"
                "width: 200 px;\n"
                "height: 50 px;\n"
                "}\n"
                "\n"
                "QPushButton:hover:!pressed {\n"
                "background-color: rgba(255, 132, 83,  250);\n"
                "}\n"
                "\n"
                "QPushButton: pressed {\n"
                "background-color: rgba(255, 132, 83,  150);\n"
                "}")

        self.gridLayout.addWidget(self.pushButton_count_results, 0, 1, 1, 1)

        self.pushButton_save_results_json = QPushButton(self.frame)
        self.pushButton_save_results_json.setObjectName(u"pushButton_save_results_json")
        self.pushButton_save_results_json.setStyleSheet(
                u"QPushButton {\n"
                "color: black;\n"
                "background-color: rgba(255, 132, 83,  200);\n"
                "font: 9pt \"Verdana\";\n"
                "width: 200 px;\n"
                "height: 50 px;\n"
                "}\n"
                "\n"
                "QPushButton:hover:!pressed {\n"
                "background-color: rgba(255, 132, 83,  250);\n"
                "}\n"
                "\n"
                "QPushButton: pressed {\n"
                "background-color: rgba(255, 132, 83,  150);\n"
                "}")

        self.gridLayout.addWidget(self.pushButton_save_results_json, 0, 2, 1, 1)

        self.table_results = QTableView(self.frame)
        self.table_results.setObjectName(u"table_results")
        self.table_results.setStyleSheet(
                u"QTableView {\n"
                "background-color: rgba(213, 198, 180, 200);\n"
                "selection-background-color: rgb(194, 112, 75);\n"
                "font-size: 14 pt;\n"
                "}\n"
                "\n"
                "")
        self.table_results.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout.addWidget(self.table_results, 1, 0, 1, 3)
        self.table_results.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Runners", None))
        self.pushButton_download_in_db.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0410\u0413\u0420\u0423\u0417\u0418\u0422\u042c \u0424\u0410\u0419\u041b\u042b", None))
        self.pushButton_count_results.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u0414\u0421\u0427\u0415\u0422 \u0420\u0415\u0417\u0423\u041b\u042c\u0422\u0410\u0422\u041e\u0412", None))
        self.pushButton_save_results_json.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041e\u0425\u0420\u0410\u041d\u0418\u0422\u042c \u0420\u0415\u0417\u0423\u041b\u042c\u0422\u0410\u0422\u042b (JSON)", None))
    # retranslateUi

