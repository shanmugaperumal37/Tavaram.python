import json
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageOps
import numpy as np
from keras.models import load_model

# Create the JSON file if it doesn't exist
try:
    with open('users.json', 'r') as file:
        pass
except FileNotFoundError:
    with open('users.json', 'w') as file:
        json.dump({}, file)
try:
    with open('path.json', 'r') as file:
        pass
except FileNotFoundError:
    with open('path.json', 'w') as file:
        json.dump({}, file)

path_entry = None  # Declare path_entry as a global variable

def login():
    username = username_entry.get()
    password = password_entry.get()

    with open('users.json', 'r') as fl:
        users = json.load(fl)

    if username in users and users[username] == password:
        messagebox.showinfo("Login", "Login successful!")
        main_win = tk.Toplevel(window)
        main_win.title("Analysis and Diagnosis")

        path_label = tk.Label(main_win, text="Enter Image path:")
        path_label.pack()

        global path_entry
        path_entry = tk.Entry(main_win)
        path_entry.pack()

        path_button = tk.Button(main_win, text="Go", command=image_path)
        path_button.pack()
    else:
        messagebox.showerror("Login", "Invalid username or password.")

def signup():
    username = username_entry.get()

    with open('users.json', 'r') as f:
        users = json.load(f)

    if username in users:
        messagebox.showerror("Signup", "Username already exists. Please choose a different one.")
    else:
        password = password_entry.get()
        users[username] = password

        with open('users.json', 'w') as f:
            json.dump(users, f)

        messagebox.showinfo("Signup", "Signup successful!")

def quit_program():
    window.destroy()

def image_path():
    path = path_entry.get()
    image = Image.open(path).convert("RGB")
    np.set_printoptions(suppress=True)

    model = load_model("keras_Model.h5", compile=False)

    class_names = open("labels.txt", "r").readlines()

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    messagebox.showinfo("Prediction", f"Class: {class_name[2:]}\nConfidence Score: {confidence_score}")

window = tk.Tk()
window.title("Login/Signup System")

username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

login_button = tk.Button(window, text="Login", command=login)
login_button.pack()

signup_button = tk.Button(window, text="Signup", command=signup)
signup_button.pack()

quit_button = tk.Button(window, text="Quit", command=quit_program)
quit_button.pack()

window.mainloop()
