import tkinter as tk
from pyrebase import pyrebase

# Firebase configuration
firebase_config = {
    "apiKey": "your_api_key",
    "authDomain": "your_project_id.firebaseapp.com",
    "databaseURL": "https://your_project_id.firebaseio.com",
    "projectId": "your_project_id",
    "storageBucket": "your_project_id.appspot.com",
    "messagingSenderId": "your_messaging_sender_id",
    "appId": "your_app_id"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

# Function to read data from Firebase and update GUI
def read_data():
    data = db.child("messages").get().val()
    message_label.config(text=data)

# Function to write data to Firebase
def write_data():
    message = message_entry.get()
    db.child("messages").set(message)
    read_data()  # Update GUI after writing data

# GUI setup
root = tk.Tk()
root.title("Firebase Realtime Database GUI")

# Create and place GUI elements
message_label = tk.Label(root, text="Message:")
message_label.pack()

message_entry = tk.Entry(root)
message_entry.pack()

write_button = tk.Button(root, text="Write to Firebase", command=write_data)
write_button.pack()

read_button = tk.Button(root, text="Read from Firebase", command=read_data)
read_button.pack()

# Run the GUI loop
root.mainloop()
