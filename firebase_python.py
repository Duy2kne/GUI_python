import tkinter as tk
from firebase_admin import credentials, auth, initialize_app

# Initialize Firebase with your credentials
cred = credentials.Certificate('firebase-sdk.json')
firebase_app = initialize_app(cred)

# Function to handle authentication
def authenticate(email, password):
    try:
        user = auth.get_user_by_email(email)
        # User exists, perform login logic here
        print(f"Login successful for user: {user.uid}")
    except auth.UserNotFoundError:
        # User does not exist, perform signup logic here
        new_user = auth.create_user(email=email, password=password)
        print(f"User created: {new_user.uid}")

# GUI setup
def on_submit():
    email = email_entry.get()
    password = password_entry.get()
    authenticate(email, password)

# Create the main window
root = tk.Tk()
root.title("Firebase Authentication")

# Create and place GUI elements
email_label = tk.Label(root, text="Email:")
email_label.pack()

email_entry = tk.Entry(root)
email_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Run the GUI loop
root.mainloop()
