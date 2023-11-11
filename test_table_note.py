import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Tạo QTableView
        self.table_view = QTableView(self)
        self.model = QStandardItemModel(self)
        self.model.setHorizontalHeaderLabels(['Thời Gian', 'Thông Báo'])
        # Tạo các trình chỉnh sửa cho thời gian và thông báo
        self.datetime_edit = QDateTimeEdit(self)
        self.message_edit = QLineEdit(self)

        # Tạo nút để thêm dòng mới
        self.add_button = QPushButton("Thêm", self)
        self.add_button.clicked.connect(self.addRow)

        # Tạo layout và thêm các phần tử vào layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.datetime_edit)
        layout.addWidget(self.message_edit)
        layout.addWidget(self.add_button)
        layout.addWidget(self.table_view)

        # Tạo widget chính và thiết lập layout chính
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateRealTime)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)

        # Update the real-time initially
        self.updateRealTime()
        # Thiết lập cột thời gian để hiển thị định dạng ngày giờ
        self.table_view.setColumnWidth(0, 150)
        self.table_view.setModel(self.model)
    def updateRealTime(self):
        current_datetime = QDateTime.currentDateTime()
        current_datetime_str = current_datetime.toString("yyyy-MM-dd hh:mm:ss")
        self.datetime_edit.setDateTime(current_datetime)
        # self.datetime_edit.setText("Current Date and Time: " + current_datetime_str)
    def addRow(self):
        # Lấy thời gian và thông báo từ các trình chỉnh sửa
        datetime_str = self.datetime_edit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        message = self.message_edit.text()

        # Lấy số hàng hiện tại từ mô hình
        row_position = self.model.rowCount()

        # Thêm dòng mới vào QStandardItemModel
        item_datetime = QStandardItem(datetime_str)
        item_message = QStandardItem(message)

        self.model.setItem(row_position, 0, item_datetime)
        self.model.setItem(row_position, 1, item_message)

        # Xóa nội dung của các trình chỉnh sửa
        self.datetime_edit.setDateTime(self.datetime_edit.minimumDateTime())
        self.message_edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
