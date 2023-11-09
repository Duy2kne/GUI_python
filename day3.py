# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'day3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_main = QtWidgets.QStackedWidget(self.centralwidget)
        self.widget_main.setGeometry(QtCore.QRect(40, 40, 760, 560))
        self.widget_main.setObjectName("widget_main")
        self.page_Home = QtWidgets.QWidget()
        self.page_Home.setObjectName("page_Home")
        self.btn_led = QtWidgets.QPushButton(self.page_Home)
        self.btn_led.setGeometry(QtCore.QRect(300, 322, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_led.setFont(font)
        self.btn_led.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid  rgb(11, 255, 227);\n"
"    border-radius: 20px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(161, 161, 161);\n"
"    border: 2px solid rgb(109, 182, 168);\n"
"    border-radius: 20px; \n"
"\n"
"}\n"
"QPushButton:pressed { \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 40, 49); \n"
"    border: 2px solid rgb(43, 50, 61);\n"
"\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/icons8-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_led.setIcon(icon)
        self.btn_led.setIconSize(QtCore.QSize(32, 32))
        self.btn_led.setObjectName("btn_led")
        self.label = QtWidgets.QLabel(self.page_Home)
        self.label.setGeometry(QtCore.QRect(210, 40, 400, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.spin_numLED = QtWidgets.QSpinBox(self.page_Home)
        self.spin_numLED.setGeometry(QtCore.QRect(241, 380, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spin_numLED.setFont(font)
        self.spin_numLED.setObjectName("spin_numLED")
        self.slider_brightness = QtWidgets.QSlider(self.page_Home)
        self.slider_brightness.setGeometry(QtCore.QRect(460, 390, 160, 22))
        self.slider_brightness.setProperty("value", 50)
        self.slider_brightness.setOrientation(QtCore.Qt.Horizontal)
        self.slider_brightness.setObjectName("slider_brightness")
        self.label_2 = QtWidgets.QLabel(self.page_Home)
        self.label_2.setGeometry(QtCore.QRect(120, 390, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_Home)
        self.label_3.setGeometry(QtCore.QRect(320, 390, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lb_LED = QtWidgets.QLabel(self.page_Home)
        self.lb_LED.setGeometry(QtCore.QRect(300, 110, 100, 180))
        self.lb_LED.setText("")
        self.lb_LED.setPixmap(QtGui.QPixmap(":/icon/icon/led_off.png"))
        self.lb_LED.setScaledContents(True)
        self.lb_LED.setObjectName("lb_LED")
        self.label_5 = QtWidgets.QLabel(self.page_Home)
        self.label_5.setGeometry(QtCore.QRect(260, 440, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lb_brightness = QtWidgets.QLabel(self.page_Home)
        self.lb_brightness.setGeometry(QtCore.QRect(640, 390, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_brightness.setFont(font)
        self.lb_brightness.setObjectName("lb_brightness")
        self.lb_background = QtWidgets.QLabel(self.page_Home)
        self.lb_background.setGeometry(QtCore.QRect(0, 0, 760, 560))
        self.lb_background.setText("")
        self.lb_background.setScaledContents(True)
        self.lb_background.setObjectName("lb_background")
        self.checkBox = QtWidgets.QCheckBox(self.page_Home)
        self.checkBox.setGeometry(QtCore.QRect(420, 440, 161, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.label_8 = QtWidgets.QLabel(self.page_Home)
        self.label_8.setGeometry(QtCore.QRect(160, 440, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.progressBar = QtWidgets.QProgressBar(self.page_Home)
        self.progressBar.setGeometry(QtCore.QRect(130, 210, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.comboBox = QtWidgets.QComboBox(self.page_Home)
        self.comboBox.setGeometry(QtCore.QRect(500, 210, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lb_background.raise_()
        self.btn_led.raise_()
        self.label.raise_()
        self.spin_numLED.raise_()
        self.slider_brightness.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lb_LED.raise_()
        self.label_5.raise_()
        self.lb_brightness.raise_()
        self.checkBox.raise_()
        self.label_8.raise_()
        self.progressBar.raise_()
        self.comboBox.raise_()
        self.widget_main.addWidget(self.page_Home)
        self.page_Setting = QtWidgets.QWidget()
        self.page_Setting.setObjectName("page_Setting")
        self.label_4 = QtWidgets.QLabel(self.page_Setting)
        self.label_4.setGeometry(QtCore.QRect(210, 40, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lb_background_setting = QtWidgets.QLabel(self.page_Setting)
        self.lb_background_setting.setGeometry(QtCore.QRect(0, 0, 760, 560))
        self.lb_background_setting.setText("")
        self.lb_background_setting.setScaledContents(True)
        self.lb_background_setting.setObjectName("lb_background_setting")
        self.lb_background_setting.raise_()
        self.label_4.raise_()
        self.widget_main.addWidget(self.page_Setting)
        self.page_Manual = QtWidgets.QWidget()
        self.page_Manual.setObjectName("page_Manual")
        self.label_6 = QtWidgets.QLabel(self.page_Manual)
        self.label_6.setGeometry(QtCore.QRect(210, 40, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lb_background_manual = QtWidgets.QLabel(self.page_Manual)
        self.lb_background_manual.setGeometry(QtCore.QRect(0, 0, 760, 560))
        self.lb_background_manual.setText("")
        self.lb_background_manual.setScaledContents(True)
        self.lb_background_manual.setObjectName("lb_background_manual")
        self.lb_background_manual.raise_()
        self.label_6.raise_()
        self.widget_main.addWidget(self.page_Manual)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 40, 600))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_home = QtWidgets.QPushButton(self.frame_2)
        self.btn_home.setGeometry(QtCore.QRect(0, 40, 40, 80))
        self.btn_home.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(212, 212, 212);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(161, 161, 161);\n"
"\n"
"}\n"
"QPushButton:pressed { \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 40, 49); \n"
"\n"
"}")
        self.btn_home.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/icons8-home-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home.setIcon(icon1)
        self.btn_home.setIconSize(QtCore.QSize(36, 36))
        self.btn_home.setObjectName("btn_home")
        self.btn_setting = QtWidgets.QPushButton(self.frame_2)
        self.btn_setting.setGeometry(QtCore.QRect(0, 120, 40, 80))
        self.btn_setting.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(212, 212, 212);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(161, 161, 161);\n"
"\n"
"}\n"
"QPushButton:pressed { \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 40, 49); \n"
"\n"
"}")
        self.btn_setting.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/icons8-setting-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_setting.setIcon(icon2)
        self.btn_setting.setIconSize(QtCore.QSize(30, 36))
        self.btn_setting.setObjectName("btn_setting")
        self.btn_manual = QtWidgets.QPushButton(self.frame_2)
        self.btn_manual.setGeometry(QtCore.QRect(0, 200, 40, 80))
        self.btn_manual.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(212, 212, 212);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(161, 161, 161);\n"
"\n"
"}\n"
"QPushButton:pressed { \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 40, 49); \n"
"\n"
"}")
        self.btn_manual.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/icons8-manual-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_manual.setIcon(icon3)
        self.btn_manual.setIconSize(QtCore.QSize(30, 30))
        self.btn_manual.setObjectName("btn_manual")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(40, 0, 760, 40))
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lb_title = QtWidgets.QLabel(self.frame_4)
        self.lb_title.setGeometry(QtCore.QRect(10, 10, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_title.setFont(font)
        self.lb_title.setObjectName("lb_title")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.widget_main.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_led.setText(_translate("MainWindow", "LED OFF"))
        self.label.setText(_translate("MainWindow", "HOME PAGE"))
        self.label_2.setText(_translate("MainWindow", "Number LED:"))
        self.label_3.setText(_translate("MainWindow", "Brightness LED:"))
        self.label_5.setText(_translate("MainWindow", "Status LED:"))
        self.lb_brightness.setText(_translate("MainWindow", "50"))
        self.checkBox.setText(_translate("MainWindow", "Manual Control"))
        self.label_8.setText(_translate("MainWindow", "LED:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Option A"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Option B"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Option C"))
        self.label_4.setText(_translate("MainWindow", "SETTING PAGE"))
        self.label_6.setText(_translate("MainWindow", "MANUAL PAGE"))
        self.lb_title.setText(_translate("MainWindow", "APP TRANNING"))
import icon


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
