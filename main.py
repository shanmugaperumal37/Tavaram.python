import tkinter as tk
from tkinter import messagebox
import json
import os
current_dir = os.path.dirname(os.path.abspath(__file__))


def aa():
    aa_win = tk.Tk()
    aa_win.configure(bg='green')
    aa_win.title("Basil Plant - Powdery Mildew")
    aa_path = os.path.join(current_dir, 'aa.txt')
    aaf = open(aa_path, 'r')
    aad = aaf.read()
    aat = tk.Text(aa_win, bg='red', fg='cyan')
    aat.pack(pady=20)
    aat.insert("insert", aad)


def ab():
    ab_win = tk.Tk()
    ab_win.configure(bg='green')
    ab_win.title("Basil Plant - Red Bug Disease")
    ab_path = os.path.join(current_dir, 'ab.txt')
    abf = open(ab_path, 'r')
    abd = abf.read()
    abt = tk.Text(ab_win, fg='cyan', bg='red')
    abt.pack(pady=20)
    abt.insert("insert", abd)


def ac():
    ac_win = tk.Tk()
    ac_win.configure(bg='green')
    ac_win.title("Basil Plant - Root rot")
    ac_path = os.path.join(current_dir, 'ac.txt')
    acf = open(ac_path, 'r')
    acd = acf.read()
    act = tk.Text(ac_win, fg='cyan', bg='red')
    act.pack(pady=20)
    act.insert("insert", acd)


def ba():
    ba_win = tk.Tk()
    ba_ein.configure(bg='green')
    ba_win.title("Rose Plant - Powdery Mildew")
    ba_path = os.path.join(current_dir, 'ba.txt')
    baf = open(ba_path, 'r')
    bad = baf.read()
    bat = tk.Text(ba_win, fg='cyan', bg='red')
    bat.pack(pady=20)
    bat.insert("insert", bad)


def bb():
    bb_win = tk.Tk()
    bb_win.configure(bg='green')
    bb_win.title("Rose Plant - Aphids")
    bb_path = os.path.join(current_dir, 'bb.txt')
    bbf = open(bb_path, 'r')
    bbd = bbf.read()
    bbt = tk.Text(bb_win, fg='cyan', bg='red')
    bbt.pack(pady=20)
    bbt.insert("insert", bbd)


def bc():
    bc_win = tk.Tk()
    bc_win.configure(bg='green')
    bc_win.title("Rose Plant - Downey Mildew")
    bc_path = os.path.join(current_dir, 'bc.txt')
    bcf = open(bc_path, 'r')
    bcd = bcf.read()
    bct = tk.Text(bc_win, bg='cyan', fg='green')
    bct.pack(pady=20)
    bct.insert("insert", bcd)


def login():
    username = username_entry.get()
    password = password_entry.get()

    with open('users.json', 'r') as fl:
        users = json.load(fl)

    if username in users and users[username] == password:
        messagebox.showinfo("Login", "Login successful!")
        main()
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
        main()


def quit_program():
    window.destroy()


def main():

    main_win = tk.Tk()
    main_win.title("Analysis and Diagnosis")
    main_win.configure(bg='green')
    path_label = tk.Label(main_win, text="Enter Image path:", bg='red', fg='black')
    path_label.pack()
    path_entry = tk.Entry(main_win, bg='black', fg='white')
    path_entry.pack()
    from keras.models import load_model  # TensorFlow is required for Keras to work
    from PIL import Image, ImageOps  # Install pillow instead of PIL
    import numpy as np

    def image_path():
        # Replace this with the path to your image
        image = Image.open(path_entry.get()).convert("RGB")
        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)

        # Load the model
        model = load_model("keras_Model.h5", compile=False)

        # Load the labels
        class_names = open("labels.txt", "r").readlines()

        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        # turn the image into a numpy array
        image_array = np.asarray(image)

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        # Load the image into the array
        data[0] = normalized_image_array

        # Predicts the model
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        if index == 0:
            aa()
        elif index == 1:
            ab()
        elif index == 2:
            ac()
        elif index == 3:
            ba()
        elif index == 4:
            bb()
        else:
            bc()

    path_button = tk.Button(main_win, text="Go", command=image_path, bg='purple', fg='orange')
    path_button.pack()
    main_win.mainloop()


# Create the JSON file if it doesn't exist
try:
    with open('users.json', 'r') as file:
        pass
except FileNotFoundError:
    with open('users.json', 'w') as file:
        json.dump({}, file)


window = tk.Tk()
window.configure(bg='green')
window.title("Login/Signup System")

# Create username label and entry
username_label = tk.Label(window, text="Username:", bg='green', fg='red')
username_label.pack()
username_entry = tk.Entry(window, bg='black', fg='white')
username_entry.pack()

# Create password label and entry
password_label = tk.Label(window, text="Password:", bg='green', fg='red')
password_label.pack()
password_entry = tk.Entry(window, show="*", bg='black', fg='white')
password_entry.pack()

# Create login button
login_button = tk.Button(window, text="Login", command=login, bg='black', fg='yellow')
login_button.pack()

# Create signup button
signup_button = tk.Button(window, text="Signup", command=signup, bg='black', fg='yellow')
signup_button.pack()

# Create quit button
quit_button = tk.Button(window, text="Quit", command=quit_program, bg='red', fg='black')
quit_button.pack()

window.mainloop()
