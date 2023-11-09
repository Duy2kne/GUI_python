import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, Qt
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QStackedWidget
from testing import *
import serial
from threading import Event
import serial.tools.list_ports

class MainWindow(QMainWindow):
    def __init__(self): # cho phép bạn thiết lập các thuộc tính ban đầu của đối tượng class MainWindow
        # self là tham số đầu tiên của __init__ và đại diện cho chính đối tượng đang được khởi tạo. 
        # Bạn có thể sử dụng self để truy cập và thiết lập các thuộc tính của đối tượng.
        ## IMPORT MAIN WINDOWN USER INTERFACE ##
        QMainWindow.__init__(self)
        self.temp=0
        self.toogle= False
        self.check= False
        self.ui = Ui_MainWindow() # Create an instance of the UI
        self.ui.setupUi(self) # Set up the UI for the current object
        self.timer = QtCore.QTimer() # khoi tao bien Timer
        self.threadpool = QtCore.QThreadPool()
        self.ui.ser = serial.Serial()
        self.Read_information()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.Read_information)
        self.timer.timeout.connect(self.persent)
        self.timer.start()
        self.ui.widget_main.setCurrentWidget(self.ui.page_Home)
        self.ui.lb_background.setPixmap(QPixmap("background_manual.jpg"))
        self.ui.btn_led.clicked.connect(self.button)
        self.ui.btn_led.setToolTip("TURN ON/OFF LED")
        self.ui.slider_brightness.valueChanged.connect(self.slider)
        self.ui.spin_numLED.valueChanged.connect(self.spin)
        self.ui.label_8.setText("LED: 0")
        self.ui.btn_home.clicked.connect(self.page)
        self.ui.btn_setting.clicked.connect(self.page)
        self.ui.btn_manual.clicked.connect(self.page)
        self.ui.checkBox.stateChanged.connect(self.checkbox_function)
        self.ui.spin_numLED.setSuffix("km")
        self.ui.spin_numLED.setPrefix("$")
        # self.ui.progressBar.setFormat("%p%")
        # self.ui.progressBar.setTextVisible(True)
        # self.ui.progressBar.setInvertedAppearance(True)
        
    def page(self):
        btnWidget= self.sender()
        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.widget_main.setCurrentWidget(self.ui.page_Home)
        # PAGE MANUAL
        if btnWidget.objectName() == "btn_manual":
            self.ui.widget_main.setCurrentWidget(self.ui.page_Manual)
        # PAGE SETTINg
        if btnWidget.objectName() == "btn_setting":
            self.ui.widget_main.setCurrentWidget(self.ui.page_Setting)
    def checkbox_function(self):
        if self.ui.checkBox.isChecked():  
            print("Checkbox is checked")
        else:
            print("Checkbox is unchecked")
    def button(self):
        if self.toogle:
            self.ui.lb_LED.setPixmap(QPixmap("led_on.png"))
            self.ui.btn_led.setIcon(QIcon("icons8-on.png"))
            self.ui.btn_led.setText("LED ON")
            self.ui.label_5.setText("Status LED: ON")
        else:
            self.ui.lb_LED.setPixmap(QPixmap("led_off.png"))
            self.ui.btn_led.setIcon(QIcon("icons8-off.png"))
            self.ui.btn_led.setText("LED OFF")
            self.ui.label_5.setText("Status LED: OFF")
        self.toogle = not self.toogle
    def checkbox(self):
        print(self.ui.checkBox.checkState())
    def slider(self):
        self.ui.lb_brightness.setText(str(self.ui.slider_brightness.value()))
    def spin(self):
        self.ui.label_8.setText("LED: "+str(self.ui.spin_numLED.value()))
    def Read_information(self):
        if self.ui.ser.isOpen():
            data =self.ui.ser.readline().decode()
            self.ui.ser.flushInput()
            self.ui.ser.flushOutput()
            print(data)
            time.sleep(0.1)
            self.theta_receive=data.split()
            if len(self.theta_receive)==3 :
                print("have data")
    def persent(self):
        current_time = QTime.currentTime()
        self.ui.timeEdit.setTime(current_time)
        self.temp=self.temp+1
        if self.temp ==100:
            self.temp=0
        self.ui.progressBar.setValue(self.temp)
    

## CODE RUNNING ##
if __name__ == "__main__":
    display = QtWidgets.QApplication(sys.argv) 
    # Dòng này tạo một ứng dụng Qt sử dụng QApplication. 
    #Đối số sys.argv chứa danh sách các đối số dòng lệnh
    # và nó được sử dụng để truyền các đối số dòng lệnh cho ứng dụng Qt.
    window = MainWindow() # khai bào windown bằng object MainWindow
    window.show() # hiển thị object MainWindow trên màn hình
    sys.exit(display.exec_())
    #lệnh đảm bảo rằng ứng dụng tiếp tục chạy cho đến khi người dùng đóng cửa sổ chính (hoặc chương trình thoát)

