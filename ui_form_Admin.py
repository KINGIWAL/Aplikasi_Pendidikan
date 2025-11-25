# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_Admin.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"Background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255),stop: 0.5 rgb(19, 46, 53), stop:1 rgba(0, 0, 0, 255))\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stackedWidget_Utama = QStackedWidget(self.centralwidget)
        self.stackedWidget_Utama.setObjectName(u"stackedWidget_Utama")
        self.page_Login = QWidget()
        self.page_Login.setObjectName(u"page_Login")
        self.horizontalLayout_8 = QHBoxLayout(self.page_Login)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_Login = QWidget(self.page_Login)
        self.widget_Login.setObjectName(u"widget_Login")
        self.widget_Login.setMaximumSize(QSize(450, 600))
        self.widget_Login.setStyleSheet(u"QWidget{\n"
"background-color: rgba(0,0,0, 90);\n"
"border-radius:15px;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.widget_Login)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_9 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 0, 1, 1, 1)

        self.label_3 = QLabel(self.widget_Login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(200, 30))
        self.label_3.setStyleSheet(u"QLabel{\n"
"    qproperty-alignment: 'AlignLeft';\n"
"    color: white;\n"
"    background-color: none;\n"
"    font-size: 20px;\n"
"	font-weight:bold;\n"
"    border-radius: 10px;\n"
"}")

        self.gridLayout_2.addWidget(self.label_3, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(32, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 4, 0, 1, 1)

        self.btnDaftar = QPushButton(self.widget_Login)
        self.btnDaftar.setObjectName(u"btnDaftar")
        self.btnDaftar.setStyleSheet(u"QPushButton{\n"
"    qproperty-alignment: AlignCenter;\n"
"    background-color:#11212D;\n"
"    font-size: 20px;\n"
"	font-weight:bold;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	padding:10px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color:#4A5C6A;\n"
"}")
        self.btnDaftar.setCheckable(False)

        self.gridLayout_2.addWidget(self.btnDaftar, 8, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.lineEdit_LoginUsername = QLineEdit(self.widget_Login)
        self.lineEdit_LoginUsername.setObjectName(u"lineEdit_LoginUsername")
        self.lineEdit_LoginUsername.setStyleSheet(u"QLineEdit{\n"
"	background-color:#06141D;\n"
"    font-size: 25px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")

        self.gridLayout_2.addWidget(self.lineEdit_LoginUsername, 4, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 7, 1, 1, 1)

        self.label = QLabel(self.widget_Login)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setStyleSheet(u"QLabel{\n"
"    qproperty-alignment: AlignCenter;\n"
"    color: white;\n"
"    background-color: none;\n"
"    font-size: 50px;\n"
"	font-weight:bold;\n"
"    border-radius: 10px;\n"
"}")

        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(32, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 4, 2, 1, 1)

        self.lineEdit_LoginPassword = QLineEdit(self.widget_Login)
        self.lineEdit_LoginPassword.setObjectName(u"lineEdit_LoginPassword")
        self.lineEdit_LoginPassword.setStyleSheet(u"QLineEdit{\n"
"	background-color:#06141D;\n"
"    font-size: 25px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")
        self.lineEdit_LoginPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_2.addWidget(self.lineEdit_LoginPassword, 6, 1, 1, 1)

        self.label_2 = QLabel(self.widget_Login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 30))
        self.label_2.setStyleSheet(u"QLabel{\n"
"    qproperty-alignment: 'AlignLeft';\n"
"    color: white;\n"
"    background-color: none;\n"
"    font-size: 20px;\n"
"	font-weight:bold;\n"
"    border-radius: 10px;\n"
"}")

        self.gridLayout_2.addWidget(self.label_2, 5, 1, 1, 1)

        self.btnLogin = QPushButton(self.widget_Login)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setStyleSheet(u"QPushButton{\n"
"    qproperty-alignment: AlignCenter;\n"
"    background-color:#11212D;\n"
"    font-size: 20px;\n"
"	font-weight:bold;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	padding:10px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color:#4A5C6A;\n"
"}")

        self.gridLayout_2.addWidget(self.btnLogin, 9, 1, 1, 1)


        self.horizontalLayout_8.addWidget(self.widget_Login)

        self.stackedWidget_Utama.addWidget(self.page_Login)
        self.page_Daftar = QWidget()
        self.page_Daftar.setObjectName(u"page_Daftar")
        self.horizontalLayout_11 = QHBoxLayout(self.page_Daftar)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.widget_Daftar = QWidget(self.page_Daftar)
        self.widget_Daftar.setObjectName(u"widget_Daftar")
        self.widget_Daftar.setMaximumSize(QSize(450, 831))
        self.widget_Daftar.setStyleSheet(u"QWidget{\n"
"background-color: rgba(0,0,0, 90);\n"
"border-radius:15px;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.widget_Daftar)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btnKembali = QPushButton(self.widget_Daftar)
        self.btnKembali.setObjectName(u"btnKembali")
        self.btnKembali.setStyleSheet(u"QPushButton{\n"
"    qproperty-alignment: AlignCenter;\n"
"    background-color:#11212D;\n"
"    font-size: 20px;\n"
"	font-weight:bold;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	padding:10px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color:#4A5C6A;\n"
"}")

        self.gridLayout_3.addWidget(self.btnKembali, 16, 1, 1, 1)

        self.lineEdit_Password = QLineEdit(self.widget_Daftar)
        self.lineEdit_Password.setObjectName(u"lineEdit_Password")
        self.lineEdit_Password.setStyleSheet(u"QLineEdit{\n"
"	background-color:#06141D;\n"
"    font-size: 25px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")
        self.lineEdit_Password.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_3.addWidget(self.lineEdit_Password, 10, 1, 1, 1)

        self.btnRegister = QPushButton(self.widget_Daftar)
        self.btnRegister.setObjectName(u"btnRegister")
        self.btnRegister.setStyleSheet(u"QPushButton{\n"
"    qproperty-alignment: AlignCenter;\n"
"    background-color:#11212D;\n"
"    font-size: 20px;\n"
"	font-weight:bold;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	padding:10px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color:#4A5C6A;\n"
"}")

        self.gridLayout_3.addWidget(self.btnRegister, 14, 1, 1, 1)

        self.label_8 = QLabel(self.widget_Daftar)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel{\n"
"    qproperty-alignment: 'AlignLeft';\n"
"    color: white;\n"
"    background-color: none;\n"
"    font-size: 20px;\n"
"	font-weight:bold;\n"
"    border-radius: 10px;\n"
"}")

        self.gridLayout_3.addWidget(self.label_8, 5, 1, 1, 1)

        self.label_7 = QLabel(self.widget_Daftar)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel{\n"
"    qproperty-alignment: 'AlignLeft';\n"
"    color: white;\n"
"    background-color: none;\n"
"    font-size: 20px;\n"
"	font-weight:bold;\n"
"    border-radius: 10px;\n"
"}")

        self.gridLayout_3.addWidget(self.label_7, 3, 1, 1, 1)

        self.label_5 = QLabel(self.widget_Daftar)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(200, 30))
        self.label_5.setStyleSheet(u"QLabel{\n"
"    qproperty-alignment: 'AlignLeft';\n"
"    color: white;\n"
"    background-color: none;\n"
"    font-size: 20px;\n"
"	font-weight:bold;\n"
"    border-radius: 10px;\n"
"}")

        self.gridLayout_3.addWidget(self.label_5, 7, 1, 1, 1)

        self.lineEdit_Username = QLineEdit(self.widget_Daftar)
        self.lineEdit_Username.setObjectName(u"lineEdit_Username")
        self.lineEdit_Username.setStyleSheet(u"QLineEdit{\n"
"	background-color:#06141D;\n"
"    font-size: 25px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")

        self.gridLayout_3.addWidget(self.lineEdit_Username, 8, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(32, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 8, 0, 1, 1)

        self.label_6 = QLabel(self.widget_Daftar)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(200, 30))
        self.label_6.setStyleSheet(u"QLabel{\n"
"    qproperty-alignment: 'AlignLeft';\n"
"    color: white;\n"
"    background-color: none;\n"
"    font-size: 20px;\n"
"	font-weight:bold;\n"
"    border-radius: 10px;\n"
"}")

        self.gridLayout_3.addWidget(self.label_6, 9, 1, 1, 1)

        self.label_4 = QLabel(self.widget_Daftar)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 50))
        self.label_4.setStyleSheet(u"QLabel{\n"
"    qproperty-alignment: AlignCenter;\n"
"    color: white;\n"
"    background-color: none;\n"
"    font-size: 50px;\n"
"font-weight:bold;\n"
"\n"
"    border-radius: 10px;\n"
"}")

        self.gridLayout_3.addWidget(self.label_4, 1, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 2, 1, 1, 1)

        self.lineEdit_Verification = QLineEdit(self.widget_Daftar)
        self.lineEdit_Verification.setObjectName(u"lineEdit_Verification")
        self.lineEdit_Verification.setStyleSheet(u"QLineEdit{\n"
"	background-color:#06141D;\n"
"    font-size: 25px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")
        self.lineEdit_Verification.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_3.addWidget(self.lineEdit_Verification, 12, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_10, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(32, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 8, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_8, 17, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 13, 1, 1, 1)

        self.lineEdit_Email = QLineEdit(self.widget_Daftar)
        self.lineEdit_Email.setObjectName(u"lineEdit_Email")
        self.lineEdit_Email.setStyleSheet(u"QLineEdit{\n"
"	background-color:#06141D;\n"
"    font-size: 25px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")

        self.gridLayout_3.addWidget(self.lineEdit_Email, 6, 1, 1, 1)

        self.lineEdit_NamaLengkap = QLineEdit(self.widget_Daftar)
        self.lineEdit_NamaLengkap.setObjectName(u"lineEdit_NamaLengkap")
        self.lineEdit_NamaLengkap.setStyleSheet(u"QLineEdit{\n"
"	background-color:#06141D;\n"
"    font-size: 25px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")

        self.gridLayout_3.addWidget(self.lineEdit_NamaLengkap, 4, 1, 1, 1)

        self.label_9 = QLabel(self.widget_Daftar)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QLabel{\n"
"    qproperty-alignment: 'AlignLeft';\n"
"    color: white;\n"
"    background-color: none;\n"
"    font-size: 20px;\n"
"	font-weight:bold;\n"
"    border-radius: 10px;\n"
"}")

        self.gridLayout_3.addWidget(self.label_9, 11, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer, 15, 1, 1, 1)


        self.horizontalLayout_11.addWidget(self.widget_Daftar)

        self.stackedWidget_Utama.addWidget(self.page_Daftar)
        self.page_Main = QWidget()
        self.page_Main.setObjectName(u"page_Main")
        self.horizontalLayout = QHBoxLayout(self.page_Main)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.page_Main)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(450, 16777215))
        self.widget.setStyleSheet(u"QWidget{\n"
"background-color: rgba(0,0,0, 90);\n"
"border-radius:12px;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.SideBarSmall = QWidget(self.widget_2)
        self.SideBarSmall.setObjectName(u"SideBarSmall")
        self.SideBarSmall.setStyleSheet(u"QWidget{\n"
"background-color:rgb(19, 46, 53);\n"
"border-radius:12px;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.SideBarSmall)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(11, -1, -1, -1)
        self.btnBeranda = QPushButton(self.SideBarSmall)
        self.btnBeranda.setObjectName(u"btnBeranda")
        self.btnBeranda.setMinimumSize(QSize(0, 57))
        self.btnBeranda.setMaximumSize(QSize(16777215, 60))
        self.btnBeranda.setStyleSheet(u"QPushButton {\n"
"	qproperty-alignment: AlignLeft;\n"
"	background-color:#0D171A;\n"
"    border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"	font-family: \"Century Gothic\";\n"
"	padding :10px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(197, 197, 197);\n"
"	color:rgb(33, 57, 37);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_15.addWidget(self.btnBeranda)

        self.verticalSpacer_11 = QSpacerItem(20, 136, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_15.addItem(self.verticalSpacer_11)

        self.btnMateri = QPushButton(self.SideBarSmall)
        self.btnMateri.setObjectName(u"btnMateri")
        self.btnMateri.setMinimumSize(QSize(0, 57))
        self.btnMateri.setMaximumSize(QSize(16777215, 60))
        self.btnMateri.setStyleSheet(u"QPushButton {\n"
"	qproperty-alignment: AlignLeft;\n"
"	background-color:#0D171A;\n"
"    border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"	font-family: \"Century Gothic\";\n"
"	padding :10px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(197, 197, 197);\n"
"	color:rgb(33, 57, 37);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_15.addWidget(self.btnMateri)

        self.verticalSpacer_3 = QSpacerItem(20, 136, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_15.addItem(self.verticalSpacer_3)

        self.btnCatatan = QPushButton(self.SideBarSmall)
        self.btnCatatan.setObjectName(u"btnCatatan")
        self.btnCatatan.setMinimumSize(QSize(0, 57))
        self.btnCatatan.setMaximumSize(QSize(16777215, 60))
        self.btnCatatan.setStyleSheet(u"QPushButton {\n"
"	qproperty-alignment: AlignLeft;\n"
"	background-color:#0D171A;\n"
"    border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"	font-family: \"Century Gothic\";\n"
"	padding :10px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(197, 197, 197);\n"
"	color:rgb(33, 57, 37);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_15.addWidget(self.btnCatatan)

        self.verticalSpacer_2 = QSpacerItem(20, 136, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)

        self.btnStudent = QPushButton(self.SideBarSmall)
        self.btnStudent.setObjectName(u"btnStudent")
        self.btnStudent.setMinimumSize(QSize(0, 57))
        self.btnStudent.setStyleSheet(u"QPushButton {\n"
"	qproperty-alignment: AlignLeft;\n"
"	background-color:#0D171A;\n"
"    border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"	font-family: \"Century Gothic\";\n"
"	padding :10px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(197, 197, 197);\n"
"	color:rgb(33, 57, 37);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_15.addWidget(self.btnStudent)

        self.verticalSpacer_13 = QSpacerItem(20, 136, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_15.addItem(self.verticalSpacer_13)

        self.btnQuis = QPushButton(self.SideBarSmall)
        self.btnQuis.setObjectName(u"btnQuis")
        self.btnQuis.setMinimumSize(QSize(0, 57))
        self.btnQuis.setStyleSheet(u"QPushButton {\n"
"	qproperty-alignment: AlignLeft;\n"
"	background-color:#0D171A;\n"
"    border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"	font-family: \"Century Gothic\";\n"
"	padding :10px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(197, 197, 197);\n"
"	color:rgb(33, 57, 37);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_15.addWidget(self.btnQuis)

        self.verticalSpacer_12 = QSpacerItem(20, 500, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_15.addItem(self.verticalSpacer_12)

        self.btnLogout = QPushButton(self.SideBarSmall)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setMinimumSize(QSize(0, 57))
        self.btnLogout.setStyleSheet(u"QPushButton {\n"
"	qproperty-alignment: AlignLeft;\n"
"	background-color:#0D171A;\n"
"    border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"	font-family: \"Century Gothic\";\n"
"	padding :10px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(197, 197, 197);\n"
"	color:rgb(33, 57, 37);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_15.addWidget(self.btnLogout)


        self.horizontalLayout_5.addWidget(self.SideBarSmall)

        self.stackedWidget_Sidebar = QStackedWidget(self.widget_2)
        self.stackedWidget_Sidebar.setObjectName(u"stackedWidget_Sidebar")
        self.stackedWidget_Sidebar.setStyleSheet(u"QWidget{\n"
"background-color: rgba(0,0,0, 90);\n"
"border-radius:12px;\n"
"}")
        self.page_Sidebar_Beranda = QWidget()
        self.page_Sidebar_Beranda.setObjectName(u"page_Sidebar_Beranda")
        self.verticalLayout_19 = QVBoxLayout(self.page_Sidebar_Beranda)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.btnBeranda_2 = QPushButton(self.page_Sidebar_Beranda)
        self.btnBeranda_2.setObjectName(u"btnBeranda_2")
        self.btnBeranda_2.setMaximumSize(QSize(16777215, 60))
        self.btnBeranda_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:white;\n"
"    border-radius: 15px;\n"
"	font-weight:bold;\n"
"	font-size:30px;\n"
"	padding:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.btnBeranda_2.setIconSize(QSize(40, 40))

        self.verticalLayout_19.addWidget(self.btnBeranda_2)

        self.btnTambah = QPushButton(self.page_Sidebar_Beranda)
        self.btnTambah.setObjectName(u"btnTambah")
        self.btnTambah.setStyleSheet(u"QPushButton{\n"
"	background-color:#2D4A53;\n"
"	border-radius:15px;\n"
"	color :#AFB3B7;\n"
"	padding:15px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#0D1F23;\n"
"}")

        self.verticalLayout_19.addWidget(self.btnTambah)

        self.scrollArea_Sidebar_Materi_2 = QScrollArea(self.page_Sidebar_Beranda)
        self.scrollArea_Sidebar_Materi_2.setObjectName(u"scrollArea_Sidebar_Materi_2")
        self.scrollArea_Sidebar_Materi_2.setWidgetResizable(True)
        self.scrollArea_Sidebar_Materi_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents_12 = QWidget()
        self.scrollAreaWidgetContents_12.setObjectName(u"scrollAreaWidgetContents_12")
        self.scrollAreaWidgetContents_12.setGeometry(QRect(0, 0, 78, 24))
        self.verticalLayout_41 = QVBoxLayout(self.scrollAreaWidgetContents_12)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_Sidebar_Materi_2 = QVBoxLayout()
        self.verticalLayout_Sidebar_Materi_2.setObjectName(u"verticalLayout_Sidebar_Materi_2")

        self.verticalLayout_41.addLayout(self.verticalLayout_Sidebar_Materi_2)

        self.scrollArea_Sidebar_Materi_2.setWidget(self.scrollAreaWidgetContents_12)

        self.verticalLayout_19.addWidget(self.scrollArea_Sidebar_Materi_2)

        self.stackedWidget_Sidebar.addWidget(self.page_Sidebar_Beranda)
        self.page_Sidebar_Quis = QWidget()
        self.page_Sidebar_Quis.setObjectName(u"page_Sidebar_Quis")
        self.verticalLayout_17 = QVBoxLayout(self.page_Sidebar_Quis)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.btnLabelQuis = QPushButton(self.page_Sidebar_Quis)
        self.btnLabelQuis.setObjectName(u"btnLabelQuis")
        self.btnLabelQuis.setMaximumSize(QSize(16777215, 60))
        self.btnLabelQuis.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:white;\n"
"    border-radius: 15px;\n"
"	font-weight:bold;\n"
"	font-size:30px;\n"
"	padding:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.btnLabelQuis.setIconSize(QSize(40, 40))

        self.verticalLayout_17.addWidget(self.btnLabelQuis)

        self.btnTambah_Quis = QPushButton(self.page_Sidebar_Quis)
        self.btnTambah_Quis.setObjectName(u"btnTambah_Quis")
        self.btnTambah_Quis.setStyleSheet(u"QPushButton{\n"
"	background-color:#2D4A53;\n"
"	border-radius:15px;\n"
"	color :white;\n"
"	padding:15px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#0D1F23;\n"
"}")

        self.verticalLayout_17.addWidget(self.btnTambah_Quis)

        self.scrollArea_Sidebar_Quis = QScrollArea(self.page_Sidebar_Quis)
        self.scrollArea_Sidebar_Quis.setObjectName(u"scrollArea_Sidebar_Quis")
        self.scrollArea_Sidebar_Quis.setWidgetResizable(True)
        self.scrollArea_Sidebar_Quis.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents_13 = QWidget()
        self.scrollAreaWidgetContents_13.setObjectName(u"scrollAreaWidgetContents_13")
        self.scrollAreaWidgetContents_13.setGeometry(QRect(0, 0, 253, 835))
        self.verticalLayout_43 = QVBoxLayout(self.scrollAreaWidgetContents_13)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_Sidebar_Quis = QVBoxLayout()
        self.verticalLayout_Sidebar_Quis.setObjectName(u"verticalLayout_Sidebar_Quis")

        self.verticalLayout_43.addLayout(self.verticalLayout_Sidebar_Quis)

        self.scrollArea_Sidebar_Quis.setWidget(self.scrollAreaWidgetContents_13)

        self.verticalLayout_17.addWidget(self.scrollArea_Sidebar_Quis)

        self.stackedWidget_Sidebar.addWidget(self.page_Sidebar_Quis)
        self.page_Sidebar_Student = QWidget()
        self.page_Sidebar_Student.setObjectName(u"page_Sidebar_Student")
        self.verticalLayout_16 = QVBoxLayout(self.page_Sidebar_Student)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.pushButton_38 = QPushButton(self.page_Sidebar_Student)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:white;\n"
"    border-radius: 15px;\n"
"	font-weight:bold;\n"
"	font-size:30px;\n"
"	padding:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pushButton_38.setIconSize(QSize(40, 40))

        self.verticalLayout_16.addWidget(self.pushButton_38)

        self.scrollArea = QScrollArea(self.page_Sidebar_Student)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContents_Student = QWidget()
        self.scrollAreaWidgetContents_Student.setObjectName(u"scrollAreaWidgetContents_Student")
        self.scrollAreaWidgetContents_Student.setGeometry(QRect(0, 0, 78, 24))
        self.verticalLayout_28 = QVBoxLayout(self.scrollAreaWidgetContents_Student)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_Sidebar_Student = QVBoxLayout()
        self.verticalLayout_Sidebar_Student.setObjectName(u"verticalLayout_Sidebar_Student")

        self.verticalLayout_28.addLayout(self.verticalLayout_Sidebar_Student)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_Student)

        self.verticalLayout_16.addWidget(self.scrollArea)

        self.stackedWidget_Sidebar.addWidget(self.page_Sidebar_Student)
        self.page_Sidebar_Catatan = QWidget()
        self.page_Sidebar_Catatan.setObjectName(u"page_Sidebar_Catatan")
        self.verticalLayout_3 = QVBoxLayout(self.page_Sidebar_Catatan)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btnCatatan_2 = QPushButton(self.page_Sidebar_Catatan)
        self.btnCatatan_2.setObjectName(u"btnCatatan_2")
        self.btnCatatan_2.setMaximumSize(QSize(16777215, 60))
        self.btnCatatan_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:white;\n"
"    border-radius: 15px;\n"
"	font-weight:bold;\n"
"	font-size:30px;\n"
"	padding:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.btnCatatan_2.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.btnCatatan_2)

        self.btnTambah_Catatan = QPushButton(self.page_Sidebar_Catatan)
        self.btnTambah_Catatan.setObjectName(u"btnTambah_Catatan")
        self.btnTambah_Catatan.setStyleSheet(u"QPushButton{\n"
"	background-color:#2D4A53;\n"
"	border-radius:15px;\n"
"	color :#AFB3B7;\n"
"	padding:15px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#0D1F23;\n"
"}")

        self.verticalLayout_3.addWidget(self.btnTambah_Catatan)

        self.scrollArea_Sidebar_Materi_3 = QScrollArea(self.page_Sidebar_Catatan)
        self.scrollArea_Sidebar_Materi_3.setObjectName(u"scrollArea_Sidebar_Materi_3")
        self.scrollArea_Sidebar_Materi_3.setWidgetResizable(True)
        self.scrollArea_Sidebar_Materi_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents_Catatan = QWidget()
        self.scrollAreaWidgetContents_Catatan.setObjectName(u"scrollAreaWidgetContents_Catatan")
        self.scrollAreaWidgetContents_Catatan.setGeometry(QRect(0, 0, 78, 24))
        self.verticalLayout_42 = QVBoxLayout(self.scrollAreaWidgetContents_Catatan)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_Sidebar_Catatan = QVBoxLayout()
        self.verticalLayout_Sidebar_Catatan.setObjectName(u"verticalLayout_Sidebar_Catatan")

        self.verticalLayout_42.addLayout(self.verticalLayout_Sidebar_Catatan)

        self.scrollArea_Sidebar_Materi_3.setWidget(self.scrollAreaWidgetContents_Catatan)

        self.verticalLayout_3.addWidget(self.scrollArea_Sidebar_Materi_3)

        self.stackedWidget_Sidebar.addWidget(self.page_Sidebar_Catatan)
        self.page_Sidebar_Materi = QWidget()
        self.page_Sidebar_Materi.setObjectName(u"page_Sidebar_Materi")
        self.verticalLayout_7 = QVBoxLayout(self.page_Sidebar_Materi)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btnMateri_2 = QPushButton(self.page_Sidebar_Materi)
        self.btnMateri_2.setObjectName(u"btnMateri_2")
        self.btnMateri_2.setMaximumSize(QSize(16777215, 60))
        self.btnMateri_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:white;\n"
"    border-radius: 15px;\n"
"	font-weight:bold;\n"
"	font-size:30px;\n"
"	padding:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.btnMateri_2.setIconSize(QSize(40, 40))

        self.verticalLayout_7.addWidget(self.btnMateri_2)

        self.btnTambah_Materi = QPushButton(self.page_Sidebar_Materi)
        self.btnTambah_Materi.setObjectName(u"btnTambah_Materi")
        self.btnTambah_Materi.setMaximumSize(QSize(16777215, 16777215))
        self.btnTambah_Materi.setStyleSheet(u"QPushButton{\n"
"	background-color:#2D4A53;\n"
"	border-radius:15px;\n"
"	color :#AFB3B7;\n"
"	padding:15px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#0D1F23;\n"
"}")

        self.verticalLayout_7.addWidget(self.btnTambah_Materi)

        self.scrollArea_Sidebar_Materi = QScrollArea(self.page_Sidebar_Materi)
        self.scrollArea_Sidebar_Materi.setObjectName(u"scrollArea_Sidebar_Materi")
        self.scrollArea_Sidebar_Materi.setWidgetResizable(True)
        self.scrollArea_Sidebar_Materi.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 78, 24))
        self.verticalLayout_38 = QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_Sidebar_Materi = QVBoxLayout()
        self.verticalLayout_Sidebar_Materi.setObjectName(u"verticalLayout_Sidebar_Materi")

        self.verticalLayout_38.addLayout(self.verticalLayout_Sidebar_Materi)

        self.scrollArea_Sidebar_Materi.setWidget(self.scrollAreaWidgetContents_11)

        self.verticalLayout_7.addWidget(self.scrollArea_Sidebar_Materi)

        self.stackedWidget_Sidebar.addWidget(self.page_Sidebar_Materi)

        self.horizontalLayout_5.addWidget(self.stackedWidget_Sidebar)


        self.horizontalLayout_4.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.widget)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget_Main = QStackedWidget(self.page_Main)
        self.stackedWidget_Main.setObjectName(u"stackedWidget_Main")
        self.stackedWidget_Main.setEnabled(True)
        self.stackedWidget_Main.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.stackedWidget_Main.setAutoFillBackground(False)
        self.stackedWidget_Main.setStyleSheet(u"QWidget{\n"
"background-color: rgba(0,0,0, 90);\n"
"border-radius:12px;\n"
"}")
        self.page_Main_Input_Materi = QWidget()
        self.page_Main_Input_Materi.setObjectName(u"page_Main_Input_Materi")
        self.page_Main_Input_Materi.setStyleSheet(u"QWidget{\n"
"    background: qlineargradient(\n"
"        x2:0, y1:1,\n"
"        x2:1, y2:1,\n"
"        stop:0 #040e0f,\n"
"        stop:1 #054247\n"
"    );\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 15px;\n"
"    color: #E9FFFF;\n"
"\n"
"    border-radius: 10px;\n"
"\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.page_Main_Input_Materi)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea_5 = QScrollArea(self.page_Main_Input_Materi)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 206, 261))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_Input_Materi2 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_Input_Materi2.setObjectName(u"widget_Input_Materi2")
        self.widget_Input_Materi2.setMaximumSize(QSize(16777215, 123))
        self.widget_Input_Materi2.setStyleSheet(u"QWidget{\n"
"background-color: rgba(0,0,0, 90);\n"
"	border-radius:12px;\n"
"	font-size:18px;\n"
"	padding :5px;\n"
"	color:white;\n"
"}")
        self.verticalLayout_21 = QVBoxLayout(self.widget_Input_Materi2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_15 = QLabel(self.widget_Input_Materi2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:white;\n"
"    border-radius: 15px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_21.addWidget(self.label_15)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.comboBox_folder_Materi = QComboBox(self.widget_Input_Materi2)
        self.comboBox_folder_Materi.setObjectName(u"comboBox_folder_Materi")
        self.comboBox_folder_Materi.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_folder_Materi.setSizeIncrement(QSize(0, 0))
        self.comboBox_folder_Materi.setStyleSheet(u"QComboBox {\n"
"	qproperty-alignment: AlignCenter;\n"
"	background-color:#06141D;\n"
"    font-size: 25px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QComboBox:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}\n"
" QComboBox QAbstractItemView {\n"
"	qproperty-alignment: AlignCenter;\n"
"	background-color:Black;\n"
"    font-size: 25px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}")
        self.comboBox_folder_Materi.setEditable(True)

        self.horizontalLayout_10.addWidget(self.comboBox_folder_Materi)


        self.verticalLayout_21.addLayout(self.horizontalLayout_10)


        self.verticalLayout_12.addWidget(self.widget_Input_Materi2)

        self.widget_Input_Materi = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_Input_Materi.setObjectName(u"widget_Input_Materi")
        self.widget_Input_Materi.setMaximumSize(QSize(16777215, 16777215))
        self.widget_Input_Materi.setStyleSheet(u"QWidget{\n"
"background-color: rgba(0,0,0, 90);\n"
"	border-radius:12px;\n"
"	font-size:18px;\n"
"	padding :5px;\n"
"	color:white;\n"
"}")
        self.verticalLayout_22 = QVBoxLayout(self.widget_Input_Materi)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.scrollArea_Input_materi = QScrollArea(self.widget_Input_Materi)
        self.scrollArea_Input_materi.setObjectName(u"scrollArea_Input_materi")
        self.scrollArea_Input_materi.setStyleSheet(u"QScrollArea{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.scrollArea_Input_materi.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 147, 962))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_judul = QLabel(self.scrollAreaWidgetContents_4)
        self.label_judul.setObjectName(u"label_judul")
        self.label_judul.setMaximumSize(QSize(16777215, 36))
        self.label_judul.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:white;\n"
"    border-radius: 15px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_9.addWidget(self.label_judul)

        self.lineEdit_Judul = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_Judul.setObjectName(u"lineEdit_Judul")
        self.lineEdit_Judul.setStyleSheet(u"QLineEdit{\n"
"	background-color:#06141D;\n"
"    font-size: 25px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")

        self.verticalLayout_9.addWidget(self.lineEdit_Judul)

        self.label_materi = QLabel(self.scrollAreaWidgetContents_4)
        self.label_materi.setObjectName(u"label_materi")
        self.label_materi.setMaximumSize(QSize(16777215, 36))
        self.label_materi.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:white;\n"
"    border-radius: 15px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_9.addWidget(self.label_materi)

        self.textEdit_Materi = QTextEdit(self.scrollAreaWidgetContents_4)
        self.textEdit_Materi.setObjectName(u"textEdit_Materi")
        self.textEdit_Materi.setMinimumSize(QSize(0, 300))
        self.textEdit_Materi.setStyleSheet(u"QTextEdit{\n"
"	 qproperty-alignment: AlignLeft;\n"
"	background-color:#06141D;\n"
"    font-size: 12px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QTextEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")
        self.textEdit_Materi.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoNone)
        self.textEdit_Materi.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.textEdit_Materi.setLineWrapColumnOrWidth(-2)

        self.verticalLayout_9.addWidget(self.textEdit_Materi)

        self.label_contoh = QLabel(self.scrollAreaWidgetContents_4)
        self.label_contoh.setObjectName(u"label_contoh")
        self.label_contoh.setMaximumSize(QSize(16777215, 36))
        self.label_contoh.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:white;\n"
"    border-radius: 15px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_9.addWidget(self.label_contoh)

        self.textEdit_Contoh = QTextEdit(self.scrollAreaWidgetContents_4)
        self.textEdit_Contoh.setObjectName(u"textEdit_Contoh")
        self.textEdit_Contoh.setMinimumSize(QSize(0, 300))
        self.textEdit_Contoh.setStyleSheet(u"QTextEdit{\n"
"	 qproperty-alignment: AlignLeft;\n"
"	background-color:#06141D;\n"
"    font-size: 12px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QTextEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")
        self.textEdit_Contoh.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.textEdit_Contoh.setLineWrapColumnOrWidth(-2)

        self.verticalLayout_9.addWidget(self.textEdit_Contoh)

        self.label_peringatan = QLabel(self.scrollAreaWidgetContents_4)
        self.label_peringatan.setObjectName(u"label_peringatan")
        self.label_peringatan.setMaximumSize(QSize(16777215, 37))
        self.label_peringatan.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:white;\n"
"    border-radius: 15px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_9.addWidget(self.label_peringatan)

        self.textEdit_Peringatan = QTextEdit(self.scrollAreaWidgetContents_4)
        self.textEdit_Peringatan.setObjectName(u"textEdit_Peringatan")
        self.textEdit_Peringatan.setStyleSheet(u"QTextEdit{\n"
"	 qproperty-alignment: AlignLeft;\n"
"	background-color:#06141D;\n"
"    font-size: 12px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QTextEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")
        self.textEdit_Peringatan.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.textEdit_Peringatan.setLineWrapColumnOrWidth(-2)

        self.verticalLayout_9.addWidget(self.textEdit_Peringatan)

        self.scrollArea_Input_materi.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_22.addWidget(self.scrollArea_Input_materi)


        self.verticalLayout_12.addWidget(self.widget_Input_Materi)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_10.addWidget(self.scrollArea_5)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.widget_5 = QWidget(self.page_Main_Input_Materi)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btnSimpan_Materi = QPushButton(self.widget_5)
        self.btnSimpan_Materi.setObjectName(u"btnSimpan_Materi")
        self.btnSimpan_Materi.setMaximumSize(QSize(300, 16777215))
        self.btnSimpan_Materi.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(19, 46, 53);\n"
"	border-radius:15px;\n"
"	color :#AFB3B7;\n"
"	padding:15px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#0D1F23;\n"
"}")

        self.horizontalLayout_7.addWidget(self.btnSimpan_Materi)


        self.horizontalLayout_16.addWidget(self.widget_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.stackedWidget_Main.addWidget(self.page_Main_Input_Materi)
        self.page_Main_Materi = QWidget()
        self.page_Main_Materi.setObjectName(u"page_Main_Materi")
        self.page_Main_Materi.setStyleSheet(u"QWidget{\n"
"    background: qlineargradient(\n"
"        x2:0, y1:1,\n"
"        x2:1, y2:1,\n"
"        stop:0 #040e0f,\n"
"        stop:1 #054247\n"
"    );\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 15px;\n"
"    color: #E9FFFF;\n"
"\n"
"    border-radius: 10px;\n"
"\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.page_Main_Materi)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_Materi = QVBoxLayout()
        self.verticalLayout_Materi.setObjectName(u"verticalLayout_Materi")
        self.widget_4 = QWidget(self.page_Main_Materi)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(467, 0))

        self.verticalLayout_Materi.addWidget(self.widget_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_Materi)

        self.LayoutMateri = QVBoxLayout()
        self.LayoutMateri.setObjectName(u"LayoutMateri")
        self.widgetSubBabMateri = QWidget(self.page_Main_Materi)
        self.widgetSubBabMateri.setObjectName(u"widgetSubBabMateri")
        self.widgetSubBabMateri.setMaximumSize(QSize(300, 16777215))
        self.widgetSubBabMateri.setStyleSheet(u"QWidget{\n"
"background-color:#0D171A;\n"
"border-radius:12px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widgetSubBabMateri)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea_JudulMateri = QScrollArea(self.widgetSubBabMateri)
        self.scrollArea_JudulMateri.setObjectName(u"scrollArea_JudulMateri")
        self.scrollArea_JudulMateri.setWidgetResizable(True)
        self.scrollArea_JudulMateri.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 24, 24))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_JudulMateri = QVBoxLayout()
        self.verticalLayout_JudulMateri.setObjectName(u"verticalLayout_JudulMateri")

        self.verticalLayout_4.addLayout(self.verticalLayout_JudulMateri)

        self.scrollArea_JudulMateri.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_2.addWidget(self.scrollArea_JudulMateri)


        self.LayoutMateri.addWidget(self.widgetSubBabMateri)


        self.horizontalLayout_6.addLayout(self.LayoutMateri)

        self.stackedWidget_Main.addWidget(self.page_Main_Materi)
        self.page_Main_Quis = QWidget()
        self.page_Main_Quis.setObjectName(u"page_Main_Quis")
        self.page_Main_Quis.setStyleSheet(u"QWidget{\n"
"    background: qlineargradient(\n"
"        x2:0, y1:1,\n"
"        x2:1, y2:1,\n"
"        stop:0 #040e0f,\n"
"        stop:1 #054247\n"
"    );\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 15px;\n"
"    color: #E9FFFF;\n"
"\n"
"    border-radius: 10px;\n"
"\n"
"}")
        self.horizontalLayout_14 = QHBoxLayout(self.page_Main_Quis)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.widget_6 = QWidget(self.page_Main_Quis)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(590, 0))
        self.verticalLayout_32 = QVBoxLayout(self.widget_6)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.scrollArea_3 = QScrollArea(self.widget_6)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 568, 24))
        self.verticalLayout_34 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_Tanya_Jawab = QVBoxLayout()
        self.verticalLayout_Tanya_Jawab.setObjectName(u"verticalLayout_Tanya_Jawab")

        self.verticalLayout_34.addLayout(self.verticalLayout_Tanya_Jawab)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_32.addWidget(self.scrollArea_3)


        self.verticalLayout_25.addWidget(self.widget_6)


        self.horizontalLayout_14.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.widgetSubBabQuis = QWidget(self.page_Main_Quis)
        self.widgetSubBabQuis.setObjectName(u"widgetSubBabQuis")
        self.widgetSubBabQuis.setMaximumSize(QSize(300, 16777215))
        self.widgetSubBabQuis.setStyleSheet(u"QWidget{\n"
"background-color:#0D171A;\n"
"border-radius:12px;\n"
"}")
        self.verticalLayout_27 = QVBoxLayout(self.widgetSubBabQuis)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.scrollArea_Quis_2 = QScrollArea(self.widgetSubBabQuis)
        self.scrollArea_Quis_2.setObjectName(u"scrollArea_Quis_2")
        self.scrollArea_Quis_2.setWidgetResizable(True)
        self.scrollArea_Quis_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 24, 24))
        self.verticalLayout_30 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_Soal_Quis = QVBoxLayout()
        self.verticalLayout_Soal_Quis.setObjectName(u"verticalLayout_Soal_Quis")

        self.verticalLayout_30.addLayout(self.verticalLayout_Soal_Quis)

        self.scrollArea_Quis_2.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_27.addWidget(self.scrollArea_Quis_2)


        self.verticalLayout_26.addWidget(self.widgetSubBabQuis)


        self.horizontalLayout_14.addLayout(self.verticalLayout_26)

        self.stackedWidget_Main.addWidget(self.page_Main_Quis)
        self.page_Main_Student = QWidget()
        self.page_Main_Student.setObjectName(u"page_Main_Student")
        self.page_Main_Student.setStyleSheet(u"QWidget{\n"
"    background: qlineargradient(\n"
"        x2:0, y1:1,\n"
"        x2:1, y2:1,\n"
"        stop:0 #040e0f,\n"
"        stop:1 #054247\n"
"    );\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 15px;\n"
"    color: #E9FFFF;\n"
"\n"
"    border-radius: 10px;\n"
"\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.page_Main_Student)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget_Register_Student = QWidget(self.page_Main_Student)
        self.widget_Register_Student.setObjectName(u"widget_Register_Student")
        self.widget_Register_Student.setMaximumSize(QSize(450, 831))
        self.verticalLayout_6 = QVBoxLayout(self.widget_Register_Student)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(38, -1, 38, -1)
        self.label_10 = QLabel(self.widget_Register_Student)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 26))
        self.label_10.setStyleSheet(u"QLabel{\n"
"    qproperty-alignment: 'AlignLeft';\n"
"    color: white;\n"
"    background-color: none;\n"
"    font-size: 20px;\n"
"	font-weight:bold;\n"
"    border-radius: 10px;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_10)

        self.lineEdit_NamaLengkap_2 = QLineEdit(self.widget_Register_Student)
        self.lineEdit_NamaLengkap_2.setObjectName(u"lineEdit_NamaLengkap_2")
        self.lineEdit_NamaLengkap_2.setStyleSheet(u"QLineEdit{\n"
"	background-color:#06141D;\n"
"    font-size: 25px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")

        self.verticalLayout_6.addWidget(self.lineEdit_NamaLengkap_2)

        self.label_11 = QLabel(self.widget_Register_Student)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 26))
        self.label_11.setStyleSheet(u"QLabel{\n"
"    qproperty-alignment: 'AlignLeft';\n"
"    color: white;\n"
"    background-color: none;\n"
"    font-size: 20px;\n"
"	font-weight:bold;\n"
"    border-radius: 10px;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_11)

        self.lineEdit_Username_2 = QLineEdit(self.widget_Register_Student)
        self.lineEdit_Username_2.setObjectName(u"lineEdit_Username_2")
        self.lineEdit_Username_2.setStyleSheet(u"QLineEdit{\n"
"	background-color:#06141D;\n"
"    font-size: 25px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")

        self.verticalLayout_6.addWidget(self.lineEdit_Username_2)

        self.label_12 = QLabel(self.widget_Register_Student)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 26))
        self.label_12.setStyleSheet(u"QLabel{\n"
"    qproperty-alignment: 'AlignLeft';\n"
"    color: white;\n"
"    background-color: none;\n"
"    font-size: 20px;\n"
"	font-weight:bold;\n"
"    border-radius: 10px;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_12)

        self.lineEdit_Email_2 = QLineEdit(self.widget_Register_Student)
        self.lineEdit_Email_2.setObjectName(u"lineEdit_Email_2")
        self.lineEdit_Email_2.setStyleSheet(u"QLineEdit{\n"
"	background-color:#06141D;\n"
"    font-size: 25px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")

        self.verticalLayout_6.addWidget(self.lineEdit_Email_2)

        self.label_13 = QLabel(self.widget_Register_Student)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 26))
        self.label_13.setStyleSheet(u"QLabel{\n"
"    qproperty-alignment: 'AlignLeft';\n"
"    color: white;\n"
"    background-color: none;\n"
"    font-size: 20px;\n"
"	font-weight:bold;\n"
"    border-radius: 10px;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_13)

        self.lineEdit_Password_2 = QLineEdit(self.widget_Register_Student)
        self.lineEdit_Password_2.setObjectName(u"lineEdit_Password_2")
        self.lineEdit_Password_2.setStyleSheet(u"QLineEdit{\n"
"	background-color:#06141D;\n"
"    font-size: 25px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")

        self.verticalLayout_6.addWidget(self.lineEdit_Password_2)

        self.btnSimpan_Student = QPushButton(self.widget_Register_Student)
        self.btnSimpan_Student.setObjectName(u"btnSimpan_Student")
        self.btnSimpan_Student.setStyleSheet(u"QPushButton{\n"
"    qproperty-alignment: AlignCenter;\n"
"    background-color:#11212D;\n"
"    font-size: 20px;\n"
"	font-weight:bold;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	padding:10px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color:#4A5C6A;\n"
"}")

        self.verticalLayout_6.addWidget(self.btnSimpan_Student)


        self.horizontalLayout_12.addWidget(self.widget_Register_Student)

        self.stackedWidget_Main.addWidget(self.page_Main_Student)
        self.page_Main_Input_Quis = QWidget()
        self.page_Main_Input_Quis.setObjectName(u"page_Main_Input_Quis")
        self.page_Main_Input_Quis.setStyleSheet(u"QWidget{\n"
"    background: qlineargradient(\n"
"        x2:0, y1:1,\n"
"        x2:1, y2:1,\n"
"        stop:0 #040e0f,\n"
"        stop:1 #054247\n"
"    );\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 15px;\n"
"    color: #E9FFFF;\n"
"\n"
"    border-radius: 10px;\n"
"\n"
"}")
        self.verticalLayout_18 = QVBoxLayout(self.page_Main_Input_Quis)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_Input_Nama_Latihan = QWidget(self.page_Main_Input_Quis)
        self.widget_Input_Nama_Latihan.setObjectName(u"widget_Input_Nama_Latihan")
        self.widget_Input_Nama_Latihan.setMaximumSize(QSize(16777215, 16777215))
        self.widget_Input_Nama_Latihan.setStyleSheet(u"QWidget{\n"
"background-color: rgba(0,0,0,0);\n"
"	border-radius:12px;\n"
"	font-size:18px;\n"
"	padding :5px;\n"
"	color:white;\n"
"}")
        self.verticalLayout_23 = QVBoxLayout(self.widget_Input_Nama_Latihan)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_17 = QLabel(self.widget_Input_Nama_Latihan)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:white;\n"
"    border-radius: 15px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_23.addWidget(self.label_17)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.comboBox_Nama_KategoriSoal = QComboBox(self.widget_Input_Nama_Latihan)
        self.comboBox_Nama_KategoriSoal.setObjectName(u"comboBox_Nama_KategoriSoal")
        self.comboBox_Nama_KategoriSoal.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_Nama_KategoriSoal.setSizeIncrement(QSize(0, 0))
        self.comboBox_Nama_KategoriSoal.setStyleSheet(u"QComboBox {\n"
"	qproperty-alignment: AlignCenter;\n"
"	background-color:#06141D;\n"
"    font-size: 25px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QComboBox:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}\n"
" QComboBox QAbstractItemView {\n"
"	qproperty-alignment: AlignCenter;\n"
"	background-color:Black;\n"
"    font-size: 25px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}")
        self.comboBox_Nama_KategoriSoal.setEditable(True)

        self.horizontalLayout_13.addWidget(self.comboBox_Nama_KategoriSoal)


        self.verticalLayout_23.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_18 = QLabel(self.widget_Input_Nama_Latihan)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(652, 0))
        self.label_18.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:white;\n"
"    border-radius: 15px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_29.addWidget(self.label_18)

        self.lineEdit_Nama_Soal = QLineEdit(self.widget_Input_Nama_Latihan)
        self.lineEdit_Nama_Soal.setObjectName(u"lineEdit_Nama_Soal")
        self.lineEdit_Nama_Soal.setMinimumSize(QSize(652, 0))
        self.lineEdit_Nama_Soal.setStyleSheet(u"QLineEdit{\n"
"	background-color:#06141D;\n"
"    font-size: 15px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")

        self.verticalLayout_29.addWidget(self.lineEdit_Nama_Soal)


        self.horizontalLayout_18.addLayout(self.verticalLayout_29)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_19 = QLabel(self.widget_Input_Nama_Latihan)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:white;\n"
"    border-radius: 15px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_24.addWidget(self.label_19)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lineEdit_JumlahSoal = QLineEdit(self.widget_Input_Nama_Latihan)
        self.lineEdit_JumlahSoal.setObjectName(u"lineEdit_JumlahSoal")
        self.lineEdit_JumlahSoal.setStyleSheet(u"QLineEdit{\n"
"	background-color:#06141D;\n"
"    font-size: 15px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"	Padding:10px;\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(25, 201, 255); \n"
"    background-color: #253745;\n"
"}")

        self.horizontalLayout_17.addWidget(self.lineEdit_JumlahSoal)

        self.btn_JumlahSoal = QPushButton(self.widget_Input_Nama_Latihan)
        self.btn_JumlahSoal.setObjectName(u"btn_JumlahSoal")
        self.btn_JumlahSoal.setStyleSheet(u"QPushButton {\n"
"	qproperty-alignment: AlignLeft;\n"
"	background-color:#0D171A;\n"
"    border-radius: 6px;\n"
"	font-weight:bold;\n"
"	font-size:15px;\n"
"	padding :10px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(0, 0, 0, 120);\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_17.addWidget(self.btn_JumlahSoal)


        self.verticalLayout_24.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_18.addLayout(self.verticalLayout_24)


        self.verticalLayout_23.addLayout(self.horizontalLayout_18)


        self.verticalLayout_18.addWidget(self.widget_Input_Nama_Latihan)

        self.scrollArea_Quis = QScrollArea(self.page_Main_Input_Quis)
        self.scrollArea_Quis.setObjectName(u"scrollArea_Quis")
        self.scrollArea_Quis.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 78, 24))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_Quis = QVBoxLayout()
        self.verticalLayout_Quis.setObjectName(u"verticalLayout_Quis")

        self.verticalLayout_20.addLayout(self.verticalLayout_Quis)

        self.scrollArea_Quis.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_18.addWidget(self.scrollArea_Quis)

        self.btn_SimpanSoal = QPushButton(self.page_Main_Input_Quis)
        self.btn_SimpanSoal.setObjectName(u"btn_SimpanSoal")
        self.btn_SimpanSoal.setStyleSheet(u"QPushButton {\n"
"	qproperty-alignment: AlignLeft;\n"
"	background-color:#2D4A53;\n"
"    border-radius: 6px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"	padding :10px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(0, 0, 0, 120);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_18.addWidget(self.btn_SimpanSoal)

        self.stackedWidget_Main.addWidget(self.page_Main_Input_Quis)
        self.page_Main_Catatan = QWidget()
        self.page_Main_Catatan.setObjectName(u"page_Main_Catatan")
        self.verticalLayout_40 = QVBoxLayout(self.page_Main_Catatan)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.widget_Main_Catatan = QWidget(self.page_Main_Catatan)
        self.widget_Main_Catatan.setObjectName(u"widget_Main_Catatan")
        self.widget_Main_Catatan.setMinimumSize(QSize(467, 0))
        self.widget_Main_Catatan.setStyleSheet(u"QWidget{\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.widget_Main_Catatan)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.judul_input = QLineEdit(self.widget_Main_Catatan)
        self.judul_input.setObjectName(u"judul_input")
        self.judul_input.setStyleSheet(u"QLineEdit{\n"
"   background-color:#202f2f;\n"
"   padding:10px;\n"
"   font-size:20px;\n"
"	font-family: \"Century Gothic\";\n"
"   font-weight:bold;\n"
"   border-radius:3px;\n"
"   color:white;\n"
"}")

        self.verticalLayout_13.addWidget(self.judul_input)

        self.editor = QTextEdit(self.widget_Main_Catatan)
        self.editor.setObjectName(u"editor")
        self.editor.setStyleSheet(u"QTextEdit {\n"
"    background: qlineargradient(\n"
"        x2:0, y1:1,\n"
"        x2:1, y2:1,\n"
"        stop:0 #040e0f,\n"
"        stop:1 #054247\n"
"    );\n"
"    padding: 22px;\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 15px;\n"
"    color: #E9FFFF;\n"
"\n"
"    border-radius: 10px;\n"
"    border: 1px solid rgba(0,200,200,0.25);\n"
"\n"
"    selection-background-color: rgba(0,255,200,0.3);\n"
"    selection-color: black;\n"
"}\n"
"")

        self.verticalLayout_13.addWidget(self.editor)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.btn_Simpan_Catatan_dan_edit = QPushButton(self.widget_Main_Catatan)
        self.btn_Simpan_Catatan_dan_edit.setObjectName(u"btn_Simpan_Catatan_dan_edit")
        self.btn_Simpan_Catatan_dan_edit.setStyleSheet(u"            QPushButton{\n"
"                    background-color:rgb(19, 46, 53);\n"
"                    border-radius:3px;\n"
"                    color :White;\n"
"                    font-weight:bold;\n"
"                    font-size:13px;\n"
"                    padding: 10px;\n"
"                    border: 2px solid Gray;\n"
"\n"
"            }\n"
"            QPushButton:hover{\n"
"                    background-color:#0D1F23;\n"
"                    border-color: rgb(76, 255, 228);\n"
"                    font-size:18px;\n"
"            }")

        self.horizontalLayout_19.addWidget(self.btn_Simpan_Catatan_dan_edit)


        self.verticalLayout_13.addLayout(self.horizontalLayout_19)


        self.verticalLayout_40.addWidget(self.widget_Main_Catatan)

        self.stackedWidget_Main.addWidget(self.page_Main_Catatan)
        self.page_Main_Student_2 = QWidget()
        self.page_Main_Student_2.setObjectName(u"page_Main_Student_2")
        self.page_Main_Student_2.setStyleSheet(u"QWidget{\n"
"    background: qlineargradient(\n"
"        x2:0, y1:1,\n"
"        x2:1, y2:1,\n"
"        stop:0 #040e0f,\n"
"        stop:1 #054247\n"
"    );\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 15px;\n"
"    color: #E9FFFF;\n"
"\n"
"    border-radius: 10px;\n"
"\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.page_Main_Student_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_6 = QSpacerItem(2, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_6)

        self.btnTambah_Student = QPushButton(self.page_Main_Student_2)
        self.btnTambah_Student.setObjectName(u"btnTambah_Student")
        self.btnTambah_Student.setMaximumSize(QSize(40, 40))
        self.btnTambah_Student.setStyleSheet(u"QPushButton{\n"
"	background-color:#2D4A53;\n"
"	border-radius:15px;\n"
"	color :white;\n"
"	padding:15px;\n"
"	font-weight:bold;\n"
"	font-size:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#0D1F23;\n"
"}")

        self.horizontalLayout_15.addWidget(self.btnTambah_Student)

        self.btnEkspor_Student = QPushButton(self.page_Main_Student_2)
        self.btnEkspor_Student.setObjectName(u"btnEkspor_Student")
        self.btnEkspor_Student.setMaximumSize(QSize(129, 40))
        self.btnEkspor_Student.setMouseTracking(True)
        self.btnEkspor_Student.setStyleSheet(u"QPushButton{\n"
"	background-color:#2D4A53;\n"
"	border-radius:15px;\n"
"	color :white;\n"
"	padding:10px;\n"
"	font-weight:bold;\n"
"	font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#0D1F23;\n"
"}")

        self.horizontalLayout_15.addWidget(self.btnEkspor_Student)

        self.horizontalSpacer = QSpacerItem(841, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)


        self.verticalLayout_14.addLayout(self.horizontalLayout_15)

        self.scrollArea_2 = QScrollArea(self.page_Main_Student_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 976, 961))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_Main_Student = QVBoxLayout()
        self.verticalLayout_Main_Student.setObjectName(u"verticalLayout_Main_Student")

        self.verticalLayout_11.addLayout(self.verticalLayout_Main_Student)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_14.addWidget(self.scrollArea_2)

        self.stackedWidget_Main.addWidget(self.page_Main_Student_2)
        self.page_Main_Beranda = QWidget()
        self.page_Main_Beranda.setObjectName(u"page_Main_Beranda")
        self.horizontalLayout_9 = QHBoxLayout(self.page_Main_Beranda)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_3 = QWidget(self.page_Main_Beranda)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(1022, 500))
        self.widget_3.setStyleSheet(u"QWidget{\n"
"background-color: rgba(0,0,0, 90);\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(1400, 600))
        self.label_16.setStyleSheet(u"QLabel {\n"
"    qproperty-alignment: AlignCenter;\n"
"\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0,\n"
"        x2:1, y2:1,\n"
"        stop:0 #040e0f,\n"
"        stop:1 #054247\n"
"    );\n"
"\n"
"    border-radius: 18px;\n"
"    border: 2px solid rgba(0,255,230,150);  /* neon border */\n"
"\n"
"    font-family: \"Century Gothic\";\n"
"    font-size: 52px;\n"
"    font-weight: 700;\n"
"    letter-spacing: 3px;\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgb(179, 247, 255));\n"
"\n"
"    padding: 25px;\n"
"\n"
"    /* Cyber Glow */\n"
"    text-shadow: 0 0 10px rgba(0,255,255,0.8),\n"
"                 0 0 25px rgba(0,180,255,0.6),\n"
"                 0 0 40px rgba(0,150,255,0.4);\n"
"}\n"
"")
        self.label_16.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_16)


        self.horizontalLayout_9.addWidget(self.widget_3)

        self.stackedWidget_Main.addWidget(self.page_Main_Beranda)

        self.verticalLayout_5.addWidget(self.stackedWidget_Main)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.stackedWidget_Utama.addWidget(self.page_Main)

        self.horizontalLayout_3.addWidget(self.stackedWidget_Utama)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_Utama.setCurrentIndex(2)
        self.stackedWidget_Sidebar.setCurrentIndex(1)
        self.stackedWidget_Main.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.btnDaftar.setText(QCoreApplication.translate("MainWindow", u"Daftar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.btnKembali.setText(QCoreApplication.translate("MainWindow", u"Kembali", None))
        self.btnRegister.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nama Lengkap", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"verification", None))
        self.btnBeranda.setText(QCoreApplication.translate("MainWindow", u"Beranda", None))
        self.btnMateri.setText(QCoreApplication.translate("MainWindow", u"Materi", None))
        self.btnCatatan.setText(QCoreApplication.translate("MainWindow", u"Catatan", None))
        self.btnStudent.setText(QCoreApplication.translate("MainWindow", u"Student", None))
        self.btnQuis.setText(QCoreApplication.translate("MainWindow", u"Quis", None))
        self.btnLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.btnBeranda_2.setText(QCoreApplication.translate("MainWindow", u"Beranda", None))
        self.btnTambah.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btnLabelQuis.setText(QCoreApplication.translate("MainWindow", u"Quis", None))
        self.btnTambah_Quis.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"Student", None))
        self.btnCatatan_2.setText(QCoreApplication.translate("MainWindow", u"Catatan", None))
        self.btnTambah_Catatan.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btnMateri_2.setText(QCoreApplication.translate("MainWindow", u" Materi", None))
        self.btnTambah_Materi.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Nama Folder", None))
        self.comboBox_folder_Materi.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Isi folder ...", None))
        self.label_judul.setText(QCoreApplication.translate("MainWindow", u"Judul", None))
        self.lineEdit_Judul.setPlaceholderText(QCoreApplication.translate("MainWindow", u"... Judul ...", None))
        self.label_materi.setText(QCoreApplication.translate("MainWindow", u"Materi", None))
        self.textEdit_Materi.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Isi Materi ...", None))
        self.label_contoh.setText(QCoreApplication.translate("MainWindow", u"Contoh", None))
        self.textEdit_Contoh.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Isi Contoh ...", None))
        self.label_peringatan.setText(QCoreApplication.translate("MainWindow", u"Peringatan", None))
        self.textEdit_Peringatan.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Isi Peringatan ...", None))
        self.btnSimpan_Materi.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Nama Lengkap", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btnSimpan_Student.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Kategori", None))
        self.comboBox_Nama_KategoriSoal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Isi folder ...", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Nama Soal", None))
        self.lineEdit_Nama_Soal.setPlaceholderText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Jumlah Soal", None))
        self.lineEdit_JumlahSoal.setPlaceholderText("")
        self.btn_JumlahSoal.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.btn_SimpanSoal.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.judul_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Isi judul  ...", None))
        self.editor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tulis isi catatan ...", None))
        self.btn_Simpan_Catatan_dan_edit.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.btnTambah_Student.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btnEkspor_Student.setText(QCoreApplication.translate("MainWindow", u"Ekspor", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Informatics Learning Platform", None))
    # retranslateUi

