import sys
import time
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap,QIcon
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QStackedWidget,QLineEdit,QTableWidget
from PyQt5.QtWidgets import *
from day4 import *
import serial
from threading import Event
import serial.tools.list_ports
import numpy as np
from firebase_admin import credentials, auth, initialize_app
from pyrebase import pyrebase
# cred = credentials.Certificate('firebase-sdk.json')
# firebase_app = initialize_app(cred)
# firebase_config = {
#   "type": "service_account",
#   "project_id": "guipython2",
#   "private_key_id": "5a8ab6f5cd621203d576d509671e5c9fadade9e9",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDk6JdLymA/aqsP\n75LYZc4MncQgGyYOVyd2zaeLu3sSIfqOwafjpJTayxZyi7yTyAzHgnLfVnJUvE2+\nwGdV4xIYN+I74FgV5vDUzZ7tn2N7Mbo+drZZpoRiCMTpbiEYRepfN+jYTZL8l6tj\nbxb3t1gSa2dx6NT0W/b/rI1blZLywEe/MoGs3ly6PGFdNI2Uv1JS8aOT5pAuQNgr\natkM3t+89IhFah/j34Q1JTj5Ty/rYqpzLTTmmuohg29/mJ6C0XIMmCjibW5Weo7+\nBSfHj1x8bqrS2fuI3zi7444WMrr5P3QvBs0D47y30915spQh+nGBREsqFZh+8goh\nYAO4Xn47AgMBAAECggEAYL50gxGrD+JTHc8Q7uhH50keRLt0oAbxpOJR91prL0Sx\nEniCLlG2n6nJeOvZ7VNVI1Tcm8t7Upiq+v1yLvhjA11K/idY0xjhm+6zRpZggwaH\nQjMF6mnX9V7jagyjbBDQdyG4BQL0JlErnECtIlCYpmBCPgA7UHM1tuUEcTqL+o/A\npAWbSzUtq7UvT7dn+v1Czc9PmNKI83+MO8emevDaHsMicL6Bn1HxxRApV6NBrAmD\nIom36EQuzjqo1x+k2HSguCopa7wiHjDtn3iWJOsf7ry43zBQwy//XfCGk0FHj9Yb\nnCz5IBg0A9LwvsxtaqBJ4NZfeApeKgue8L+78g3HQQKBgQDyPSslfPcazxV0poDp\n9eiOHusKd4k5QBaleOiquVSPKjdVNErS/VI0a77PxA1zMKhhD1DuEOeN9C23RGQU\nSzpfMOyYr7ruDPQXHv3yFxL2+GiFr48HnmCIMVUuiZXdyCmVH3b2kMRzRHVXFaJA\nbymNyD3o9Q0HrWiJw26/l5YmEQKBgQDx6Y+7HnexHd4Ckr3YgK2jlev3cGDMYmBA\nPA6g1gOkHGLL2OZ+CRrJVdmy33r97s7Gm4xTFyyJ1NoGql693RLSCsMUg+gJCXI/\nTZqhwf+A3/s0nFc1d/3AQQ935WqdL6DPdO2/l540W+Jkb6lc7molDqCHJ7BQ5KvR\nsqv+/uujiwKBgCtCsUnon1iyUuqaMbuWpwl6jA86ec83mtPCXArhPjCzIV6eEB7O\nDrg95b3FDYHc1rU+vv1FF5VKXj+0fwsAxFPrsNUzzPZmadEXP9LUPBbPFhuJ1slN\nh3/LD6NX/uO0s3hmPiCaifrr5ui+fFN1hr5DXIsV+FW+qkSwGj8tGyuBAoGACnMr\naUrcosMGhxftqX+NgKaGRe8Nz2ZkgAHYI+x6xckQH3wkIMel55KUz9xFhNifCAdK\nHYC/xMh0Dpuncg4ttPMQED/Ocy18SO3CQ0CNF/UU9eXXApFHXdmxoF1BqL6Y9L05\nU/BpvhtGAU6tgz0tSqKCHrSBMk1eerV8Joy+gxcCgYBSShUgl2wRg3TkpD7YMOwn\nhrZCFfSu10kXcf3CxJlbLdnUQkOAgZj6iVpbt/jIFch5xbSuzv1unSAgCCdArORH\nPWEeYqj1FWlcHKxrOPO5oILFv703Vf9p6DdIwnn6BE7L1ISi9h4paC8CJGUnkqBN\nQHxTR8qmaeOeZQcWBZNpQw==\n-----END PRIVATE KEY-----\n",
#   "client_email": "firebase-adminsdk-xeobr@guipython2.iam.gserviceaccount.com",
#   "client_id": "114708398236668648383",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-xeobr%40guipython2.iam.gserviceaccount.com",
#   "universe_domain": "googleapis.com"
# }
# firebase = pyrebase.initialize_app(firebase_config)
# db = firebase.database()
class MainWindow(QMainWindow):
    def __init__(self): # cho phép bạn thiết lập các thuộc tính ban đầu của đối tượng class MainWindow
        # self là tham số đầu tiên của __init__ và đại diện cho chính đối tượng đang được khởi tạo. 
        # Bạn có thể sử dụng self để truy cập và thiết lập các thuộc tính của đối tượng.
        ## IMPORT MAIN WINDOWN USER INTERFACE ##
        QMainWindow.__init__(self)
        self.temp = 0
        self.toogle = False
        self.check = False
        self.cnt = 0
        self.ui = Ui_MainWindow() # Create an instance of the UI
        self.ui.setupUi(self) # Set up the UI for the current object
        self.timer = QtCore.QTimer() # khoi tao bien Timer
        self.threadpool = QtCore.QThreadPool()
        self.ui.ser = serial.Serial()
        self.generated_port()
        self.Read_information()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.Read_information)
        self.timer.timeout.connect(self.updateRealTime)
        self.timer.timeout.connect(self.persent)
        self.timer.start()
        self.ui.widget_main.setCurrentWidget(self.ui.page_Home)
        self.ui.lb_background.setPixmap(QPixmap("background_manual.jpg"))
        self.ui.btn_led.clicked.connect(self.button)
        self.ui.btn_led.setToolTip("TURN ON/OFF LED")
        self.ui.slider_brightness.valueChanged.connect(self.slider)
        self.ui.slider_brightness.setSliderPosition(10)
        self.ui.spin_numLED.valueChanged.connect(self.spin)
        self.ui.label_8.setText("LED: 0")
        self.ui.btn_home.clicked.connect(self.page)
        self.ui.btn_setting.clicked.connect(self.page)
        self.ui.btn_manual.clicked.connect(self.page)
        self.ui.btn_data.clicked.connect(self.page)
        self.ui.checkBox.stateChanged.connect(self.checkbox_function)
        self.ui.spin_numLED.setSuffix("km")
        self.ui.spin_numLED.setPrefix("$")
<<<<<<< HEAD
        self.ui.slider_brightness.setDisabled(False)
        self.ui.btn_connect.clicked.connect(self.connect_Function)
        self.ui.btn_diconnect.clicked.connect(self.disconnectFunction)
        self.ui.btn_send.clicked.connect(self.sendInformation)
        self.ui.groupBox_information.hide()
        self.ui.btn_signup_2.clicked.connect(self.Okefunction)
        self.ui.btn_signup.clicked.connect(self.on_submit)
        self.ui.btn_signin.clicked.connect(self.checkaccoun)
        self.ui.lb_Password.setEchoMode(QLineEdit.Password) 
        self.ui.lb_Password_login.setEchoMode(QLineEdit.Password) 
        self.ui.btn_hide.clicked.connect(self.toggle_password_visibility)
        self.ui.btn_hide_2.clicked.connect(self.toggle_password_visibility)
        self.ui.get_inf.clicked.connect(self.addRow)
        # self.ui.progressBar.setFormat("%p%")
        # self.ui.progressBar.setTextVisible(True)
=======
        self.ui.comboBox.addItem("Option 1", 1)
        # self.ui.slider_brightness.setDisabled(True)
        self.ui.progressBar.setFormat("%p%")
        # self.ui.progressBar.setTextVisible(False)
>>>>>>> d56ab5fd5d2653ed50693bbdb80b9e49ecc31940
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
        # PAGE DATA
        if btnWidget.objectName() == "btn_data":
            self.ui.widget_main.setCurrentWidget(self.ui.page_Data)
        
    def checkbox_function(self):
        if self.ui.checkBox.isChecked():  
            print("Checkbox is checked")
            # self.ui.slider_brightness.setEnabled(True)
        else:
            print("Checkbox is unchecked")
            # self.ui.slider_brightness.setDisabled(True)
    def button(self):
        if self.toogle:
            self.ui.lb_LED.setPixmap(QPixmap("led_on.png"))
            self.ui.btn_led.setIcon(QIcon("icons8-on.png"))
            self.ui.btn_led.setText("LED ON")
            self.ui.label_5.setText("Status LED: ON")
            print("Value Idx for ComboBox: "+str(self.ui.comboBox.currentIndex()))
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
            print(self.theta_receive)
            if len(self.theta_receive)==3 :
                print("have data")
                self.ui.real_temp.setText(str(self.theta_receive[0]))
                self.ui.real_hum.setText(str(self.theta_receive[1]))
                self.ui.real_brig.setText(str(self.theta_receive[2]))
    def persent(self):
        self.temp=self.temp+1
        if self.temp ==100:
            self.temp=0
        self.ui.progressBar.setValue(self.temp)
    def connectInitial(self, port_connect, baud_connect):
        self.ui.ser.port = port_connect
        self.ui.ser.baudrate  = baud_connect       
        self.ui.ser.bytesize = serial.EIGHTBITS
        # number of bits per bytes
        self.ui.ser.parity = serial.PARITY_NONE
        # set parity check: no parity
        self.ui.ser.stopbits = serial.STOPBITS_ONE
        # number of stop bits
        self.ui.ser.xonxoff = False 
        # disable software flow control
        self.ui.ser.rtscts = False
        # disable hardware (RTS/CTS) flow control
        self.ui.ser.dsrdtr = False
        # disable hardware (DSR/DTR) flow control
        self.ui.ser.writeTimeout = 0 
        # timeout for write
        self.ui.ser.timeout = 10
        self.ui.ser.open()
        self.Enable_video=False
    def generated_port(self):
        # list all com port available in devices manager
        ports = serial.tools.list_ports.comports()
        print(str(ports))
        self.comPort = [
            comport.device for comport in
            serial.tools.list_ports.comports()
        ]
        count = len(self.comPort)
        if count == 0:
            pass
        elif count == 1:
            self.ui.port.addItem(str(self.comPort[0]))
        else:
            self.ui.port.addItem(str(self.comPort[0]))
            self.ui.port.addItem(str(self.comPort[1]))
    def connect_Function(self):
        if (self.ui.port.currentText() != "Arduino" and self.ui.port.currentText() != ""):
            port_ar = self.ui.port.currentText()
            baud_ar = self.ui.baud.currentText()
            self.connectInitial(port_ar, baud_ar)
            if self.ui.ser.isOpen():
                self.ui.status.setText("Arduino:" + self.ui.port.currentText())
                self.ui.status.adjustSize() 
    def Okefunction(self):
        self.ui.groupBox_information.hide()
    def disconnectFunction(self):
        if self.ui.ser.isOpen():
            self.ui.ser.close()
            self.ui.status.setText("Disconnect")
            self.ui.status.adjustSize()
            self.ui.status.setEnabled(False)
        else:
            self.ui.status.setText("Disconnect")
            self.ui.status.adjustSize()
    def is_valid_email(self,email):
    # Biểu thức chính quy kiểm tra xem chuỗi có đúng định dạng email hay không
        email_pattern = re.compile(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$')
        return bool(email_pattern.match(email))

    def is_valid_password(self,password):
        # Kiểm tra xem mật khẩu có ít nhất 8 ký tự không
        return len(password) >= 8
    def sendInformation(self):
        # Encoding messages to send to serial connected deviecs
        if self.ui.ser.isOpen():
            # Format string to encode
            temperatureVal =float(self.ui.set_temp.text())
            humidityVal = float(self.ui.set_hum.text())
            brightnessVal = float(self.ui.set_brigh.text())

            self.data = np.array([temperatureVal,humidityVal,brightnessVal])
            self.ui.ser.write('{},{},{}'.format(*self.data).encode())
            Data_send =str('{},{},{}'.format(*self.data))
            self.ui.ser.flushInput()  #flush input buffer, discarding all its contents
            self.ui.ser.flushOutput()
            print(Data_send)
    def authenticate(self,email, password):
        try:
            user = auth.get_user_by_email(email)
            # User exists, perform login logic here
            print(f"Login successful for user: {user.uid}")
            self.ui.lb_title_9.setText("Note: Email already  "+ email)
            self.ui.lb_title_9.adjustSize()
            self.ui.groupBox_information.show()
        except auth.UserNotFoundError:
            # User does not exist, perform signup logic here
            new_user = auth.create_user(email=email, password=password)
            print(f"User created: {new_user.uid}")
            self.ui.lb_title_9.setText("Note: Signup successful for email "+ email )
            self.ui.lb_title_9.adjustSize()
            self.ui.groupBox_information.show()
    def on_submit(self):
        email = self.ui.lb_Email.text()
        password = self.ui.lb_Password.text()
        if self.is_valid_email(email) == False :
            self.ui.lb_title_9.setText("Note: Email Invalid! Please check email again")
            self.ui.lb_title_9.adjustSize()
            self.ui.groupBox_information.show()
        elif self.is_valid_password(password) == False :
            self.ui.lb_title_9.setText("Note: password has a size of at least 8 \n ! Please check password again")
            self.ui.lb_title_9.adjustSize()
            self.ui.groupBox_information.show()
        else:
            self.authenticate(email, password)
            self.ui.lb_Email.clear()
            self.ui.lb_Password.clear()
    def check_authentication(self,email, password):
        try:
            user = auth.get_user_by_email(email)
            self.ui.lb_title_9.setText("Note: Login successful for email "+ email)
            self.ui.lb_title_9.adjustSize()
            self.ui.groupBox_information.show()
        except auth.UserNotFoundError:
            self.ui.lb_title_9.setText("Note: Login fail for email "+ email + "\n Please check email and password")
            self.ui.lb_title_9.adjustSize()
            self.ui.groupBox_information.show()
    def toggle_password_visibility(self):
        # Chuyển đổi giữa chế độ hiển thị và ẩn của QLineEdit
        btnCheck= self.sender()
        # PAGE HOME
        if btnCheck.objectName() == "btn_hide":
            current_echo_mode = self.ui.lb_Password.echoMode()
            new_echo_mode = QLineEdit.Normal if current_echo_mode == QLineEdit.Password else QLineEdit.Password
            self.ui.lb_Password.setEchoMode(new_echo_mode)
        elif btnCheck.objectName() == "btn_hide_2":
            current_echo_mode = self.ui.lb_Password_login.echoMode()
            new_echo_mode = QLineEdit.Normal if current_echo_mode == QLineEdit.Password else QLineEdit.Password
            self.ui.lb_Password_login.setEchoMode(new_echo_mode)
    # GUI setup
    def checkaccoun(self):
        email = self.ui.lb_Email_login.text()
        password = self.ui.lb_Password_login.text()
        if self.is_valid_email(email) == False:
            self.ui.lb_title_9.setText("Note: Email Invalid! Please check email again")
            self.ui.lb_title_9.adjustSize()
            self.ui.groupBox_information.show()
        elif self.is_valid_password(password) == False:
            self.ui.lb_title_9.setText("Note: password has a size of at least 8 \n ! Please check password again")
            self.ui.lb_title_9.adjustSize()
            self.ui.groupBox_information.show()
        else:
            self.check_authentication(email, password)
            self.ui.lb_Email_login.clear()
            self.ui.lb_Password_login.clear()
    def updateRealTime(self):
        current_datetime = QDateTime.currentDateTime()
        current_datetime_str = current_datetime.toString("yyyy-MM-dd hh:mm:ss")
        self.ui.timeEdit.setDateTime(current_datetime)
        # self.datetime_edit.setText("Current Date and Time: " + current_datetime_str)
    def addRow(self):
        # Lấy thời gian và thông báo từ các trình chỉnh sửa
        datetime_str = self.ui.timeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        message = self.ui.lineEdit.text()
        self.cnt = self.cnt + 1
        # Tạo các ô dữ liệu mới
        datetime_item = QTableWidgetItem(datetime_str)
        message_item = QTableWidgetItem(message)
        # Thêm hàng mới vào QTableWidget
        row_position = 1
        self.ui.tableWidget.insertRow(row_position)
        # self.ui.tableWidget.setItem(row_position, 0, count_item)
        for i in range(self.cnt):
            self.ui.tableWidget.setItem(self.cnt-i, 0, QTableWidgetItem(str(self.cnt-i)))
        self.ui.tableWidget.setItem(row_position, 1, datetime_item)
        self.ui.tableWidget.setItem(row_position, 2, message_item)
        # Xóa nội dung của các trình chỉnh sửa
        self.ui.lineEdit.clear()

    # def read_data(self):
    #     user_id = self.user_id_entry.get()
    #     if user_id:
    #         data = db.child("stt").child(user_id).get().val()
    #         if data:
    #            print(data)
    #            print("have data") 
    #         else:
    #            print("don't have data")  
    #     else:
    #         print("have data") 

    # # Function to write data to Firebase
    # def write_data(self):
    #     db.child("messages").set("hello")
    #     self.read_data()  # Update GUI after writing data
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

