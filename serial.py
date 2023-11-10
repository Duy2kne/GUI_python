import tkinter as tk
from tkinter import scrolledtext
import serial
import threading

class SerialGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Serial Communication GUI")

        # Create and place GUI elements
        self.port_label = tk.Label(master, text="COM Port:")
        self.port_label.grid(row=0, column=0)

        self.port_entry = tk.Entry(master)
        self.port_entry.grid(row=0, column=1)

        self.connect_button = tk.Button(master, text="Connect", command=self.connect_serial)
        self.connect_button.grid(row=0, column=2)

        self.message_label = tk.Label(master, text="Message:")
        self.message_label.grid(row=1, column=0)

        self.message_entry = tk.Entry(master)
        self.message_entry.grid(row=1, column=1)

        self.send_button = tk.Button(master, text="Send", command=self.send_data)
        self.send_button.grid(row=1, column=2)

        self.log_text = scrolledtext.ScrolledText(master, height=10, width=40)
        self.log_text.grid(row=2, columnspan=3)

        # Serial communication variables
        self.serial_port = None
        self.serial_thread = None
        self.serial_running = False

    def connect_serial(self):
        port = self.port_entry.get()
        try:
            self.serial_port = serial.Serial(port, baudrate=9600, timeout=1)
            self.log_message(f"Connected to {port}")
            self.start_serial_thread()
        except serial.SerialException as e:
            self.log_message(f"Error connecting to {port}: {e}")

    def start_serial_thread(self):
        self.serial_running = True
        self.serial_thread = threading.Thread(target=self.serial_receive)
        self.serial_thread.start()

    def serial_receive(self):
        while self.serial_running:
            try:
                data = self.serial_port.readline().decode("utf-8").strip()
                if data:
                    self.log_message(f"Received: {data}")
            except Exception as e:
                self.log_message(f"Error receiving data: {e}")

    def send_data(self):
        if self.serial_port:
            message = self.message_entry.get()
            self.serial_port.write(message.encode("utf-8"))
            self.log_message(f"Sent: {message}")

    def log_message(self, message):
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SerialGUI(root)
    root.mainloop()
