<pre>
def generated_port(self):
        """
        List all comm port available in devices manager
        """
        self.comPort = [
            comport.device for comport in serial.tools.list_ports.comports()
        ]
        count = len(self.comPort)
        if count == 0:
            pass
        elif count == 1:
            self.ui.port.addItem(str(self.comPort[0]))
        elif count == 2:
            self.ui.port.addItem(str(self.comPort[0]))
            self.ui.port.addItem(str(self.comPort[1]))
        elif count == 3:
            self.ui.port.addItem(str(self.comPort[0]))
            self.ui.port.addItem(str(self.comPort[1]))
            self.ui.port.addItem(str(self.comPort[2]))
        else:
            self.ui.port.addItem(str(self.comPort[0]))
            self.ui.port.addItem(str(self.comPort[1]))
            self.ui.port.addItem(str(self.comPort[2]))
            self.ui.port.addItem(str(self.comPort[3]))
</pre>
<pre>
def connectInitial(self, port, baudrate):
        self.ui.ser.port = port
        self.ui.ser.baudrate = baudrate
        self.ui.ser.bytesize = serial.EIGHTBITS  # number of bits per bytes
        self.ui.ser.parity = serial.PARITY_NONE  # set parity check: no parity
        self.ui.ser.stopbits = serial.STOPBITS_ONE  # number of stop bits
        self.ui.ser.xonxoff = False  # disable software flow control
        self.ui.ser.rtscts = False  # disable hardware (RTS/CTS) flow control
        self.ui.ser.dsrdtr = False  # disable hardware (DSR/DTR) flow control
        self.ui.ser.writeTimeout = 0  # timeout for write
        self.ui.ser.timeout = 10
        self.ui.ser.open()

    def connectFunction(self):
        if (
            self.ui.port.currentText() != "Arduino Port"
            and self.ui.port.currentText() != ""
        ):
            port = self.ui.port.currentText()
            baudrate = self.ui.baud.currentText()
            guiEvent.connectInitial(self, port, baudrate)

            if self.ui.ser.isOpen():
                self.ui.status.setText("Connected to " + 
                self.ui.port.currentText())
                self.ui.status.adjustSize()
#hien thi nut nhan tren trang thai status ( disconect)
    def disconnectFunction(self):
        if self.ui.ser.isOpen():
            self.ui.ser.close()
            self.ui.status.setText("Disconnected")
            self.ui.status.adjustSize()
            self.ui.btn_diconnect.setEnabled(False)
        else:
            self.ui.status.setText("Disconnected")
            self.ui.status.adjustSize()
</pre>