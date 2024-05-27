import tkinter as tk
from tkinter import messagebox
import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
tamil_font = ("Latha (1).ttf", 12)
primary_color = "#007f4f"
secondary_color = '#2b9348'
accent = '#55a630'
bgcolor = '#f0f3bd'


def aae():
    aa_win = tk.Tk()
    aa_win.configure(bg=bgcolor)
    aa_win.title("Basil Plant - Powdery Mildew")
    aa_win.iconbitmap('Tavaram.ico')
    aa_path = os.path.join(current_dir, 'aae.txt')
    aaf = open(aa_path, 'r')
    aad = aaf.read()
    aat = tk.Text(aa_win, bg=bgcolor, fg=primary_color)
    aat.pack(pady=20)
    aat.insert("insert", "Powdery Mildew on Basil Plants"
                         "Cause:"
                         "	Basil downy mildew is caused by a fungal pathogen."
                         "	It initially appears as tiny greyish specks on the underside of leaves and progresses to cover larger areas of the lower leaf surface. "
                         "The fungus may appear raised from the leaf surface or 'fluffy' in appearance."
                         "Treatment:"
                         "	Baking soda is one of the best home remedies for treating powdery mildew. "
                         "For this method, 1ix 1 tablespoon baking soda and ½ teaspoon liquid soap in 1 gallon of water."
                         "	Transfer it into a spray bottle and spray the tops and underside of leaves and any other affected areas.")


def aat():
    aa_win = tk.Tk()
    aa_win.configure(bg=bgcolor)
    aa_win.title("துளசி செடிகளில் நுண்துகள் பூஞ்சை காளான்")
    aa_win.iconbitmap('Tavaram.ico')
    aat = tk.Text(aa_win, bg=bgcolor, fg=secondary_color, font=tamil_font)
    aat.pack(pady=20)
    aat.insert("insert","துளசி செடிகளில் நுண்துகள் பூஞ்சை காளான்.  காரணம்: துளசி பூஞ்சை காளான் ஒரு பூஞ்சை நோய்க்கிருமியால் ஏற்படுகிறது.  இது ஆரம்பத்தில் இலைகளின் அடிப்பகுதியில் சிறிய சாம்பல் நிற புள்ளிகளாகத் தோன்றி, கீழ் இலை மேற்பரப்பின் பெரிய பகுதிகளை மறைப்பதற்கு முன்னேறும்.  பூஞ்சை இலையின் மேற்பரப்பிலிருந்து எழும்பி அல்லது பஞ்சுபோன்ற தோற்றத்தில் தோன்றலாம்.  சிகிச்சை: பேக்கிங் சோடா நுண்துகள் பூஞ்சை காளான் சிகிச்சைக்கான சிறந்த வீட்டு வைத்தியம் ஆகும்.ந்த முறைக்கு, 1 கேலன் தண்ணீரில் 1x 1 தேக்கரண்டி பேக்கிங் சோடா மற்றும் ½ தேக்கரண்டி திரவ சோப்பு.  அதை ஒரு ஸ்ப்ரே பாட்டிலில் மாற்றி, இலைகளின் மேல் மற்றும் அடிப்பகுதி மற்றும் பாதிக்கப்பட்ட பகுதிகளில் தெளிக்கவும்.")


def abe():
    ab_win = tk.Tk()
    ab_win.configure(bg=bgcolor)
    ab_win.iconbitmap('Tavaram.ico')
    ab_win.title("Basil Plant - Red Bug Disease")
    ab_path = os.path.join(current_dir, 'abe.txt')
    abf = open(ab_path, 'r')
    abd = abf.read()
    abt = tk.Text(ab_win, fg=bgcolor, bg=primary_color)
    abt.pack(pady=20)
    abt.insert("insert", abd)


def abt():
    ab_win = tk.Tk()
    ab_win.configure(bg=bgcolor)
    ab_win.iconbitmap('Tavaram.ico')
    ab_win.title("துளசி செடியில் சிவப்பு பூச்சி நோய்")
    abt = tk.Text(ab_win, fg=secondary_color, bg=bgcolor, font=tamil_font)
    abt.pack(pady=20)
    abt.insert("insert", "துளசி செடியில் சிவப்பு பூச்சி நோய்.  காரணம்: சிவப்பு பூச்சிகளின் வளர்ச்சி.  சிகிச்சை: பூச்சிக்கொல்லி சோப்பு அல்லது 1 முதல் 2 சதவிகிதம் வேப்பெண்ணெய் கரைசலை வாரத்திற்கு ஒருமுறை செடிகளை நன்கு தெளித்து, இருக்கும் அசுவினி அல்லது சிலந்திப் பூச்சிகளை அழிக்கவும்.   இலைகளின் அடிப்பகுதி உட்பட தாவரத்தின் அனைத்து பகுதிகளையும் மூடி வைக்கவும். பூச்சிகள் மறைந்தவுடன் தெளிப்பதை நிறுத்துங்கள்")


def ace():
    ac_win = tk.Tk()
    ac_win.configure(bg=bgcolor)
    ac_win.iconbitmap('Tavaram.ico')
    ac_win.title("Basil Plant - Root rot")
    ac_path = os.path.join(current_dir, 'ace.txt')
    acf = open(ac_path, 'r')
    acd = acf.read()
    act = tk.Text(ac_win, fg=primary_color, bg=bgcolor)
    act.pack(pady=20)
    act.insert("insert", acd)


def act():
    ac_win = tk.Tk()
    ac_win.configure(bg=bgcolor)
    ac_win.iconbitmap('Tavaram.ico')
    ac_win.title("துளசி செடியில் வேர் அழுகல் நோய்")
    act = tk.Text(ac_win, fg=secondary_color, bg=bgcolor, font=tamil_font)
    act.pack(pady=20)
    act.insert("insert", "துளசி செடியில் வேர் அழுகல் நோய்.  காரணங்கள்: துளசிக்கு அதிகமாக நீர் பாய்ச்சுவது அல்லது போதிய வடிகால் இல்லாத பானை கலவையைப் பயன்படுத்துவது வேர் அழுகலை ஏற்படுத்துகிறது.  Fusarium wilt என்பது மண்ணில் பரவும் ஒரு பூஞ்சை ஆகும், இது தண்டுக்குள் நுழைந்தவுடன், தாவரத்தின் வழியாக செல்லும் தண்ணீரை நிறுத்துகிறது.  இலையின் நிறமாற்றம், வாடிப்போதல், இலைகள் சுருண்டு விழுதல், தொங்குதல், இலை உதிர்தல் மற்றும் தண்டு முறுக்குதல் ஆகியவை ஆரம்ப அறிகுறிகளாகும்.  சிகிச்சை: இறக்கும் துளசியை உயிர்ப்பிக்க, அதை நிழலில் வைக்கவும், அதிகப்படியான காற்றிலிருந்து அதைத் தடுக்கவும், மண் தொடர்ந்து ஈரமாக இருப்பதை உறுதி செய்கிறது, ஆனால் நிறைவுற்றது மற்றும் பழுப்பு நிற இலைகளை மீண்டும் கத்தரிக்கவும்.")


def bae():
    ba_win = tk.Tk()
    ba_win.configure(bg=bgcolor)
    ba_win.iconbitmap('Tavaram.ico')
    ba_win.title("Rose Plant - Powdery Mildew")
    ba_path = os.path.join(current_dir, 'bae.txt')
    baf = open(ba_path, 'r')
    bad = baf.read()
    bat = tk.Text(ba_win, fg=primary_color, bg=bgcolor)
    bat.pack(pady=20)
    bat.insert("insert", bad)


def bat():
    ba_win = tk.Tk()
    ba_win.configure(bg=bgcolor)
    ba_win.iconbitmap('Tavaram.ico')
    ba_win.title("ரோஜா செடியில் பூஞ்சை காளான்")
    bat = tk.Text(ba_win, fg=secondary_color, bg=bgcolor, font=tamil_font)
    bat.pack(pady=20)
    bat.insert("insert", "ரோஜா செடியில் பூஞ்சை காளான்.  காரணங்கள்: ரோஜா நுண்துகள் பூஞ்சை காளான் என்பது போடோஸ்பேரா பன்னோசா என்ற பூஞ்சையால் ஏற்படும் ரோஜாக்களின் நோயாகும்.  வெளிப்படையான வெள்ளை வளர்ச்சி தாவரத்தின் அனைத்து வான்வழி பகுதிகளையும் பாதிக்கலாம், இது நோயை பரப்பும் நுண்ணிய வித்திகளை உருவாக்குகிறது.  சிகிச்சை: 1 கேலன் தண்ணீரில் 1 டேபிள் ஸ்பூன் பேக்கிங் சோடா மற்றும் ½ டீஸ்பூன் திரவ சோப்பைக் கலக்கவும்.  தாராளமாக தெளிக்கவும், மேல் மற்றும் கீழ் இலை மேற்பரப்புகள் மற்றும் ஏதேனும் பாதிக்கப்பட்ட பகுதிகளை பெறவும்.")


def bbe():
    bb_win = tk.Tk()
    bb_win.configure(bg=bgcolor)
    bb_win.iconbitmap('Tavaram.ico')
    bb_win.title("Rose Plant - Aphids")
    bb_path = os.path.join(current_dir, 'bbe.txt')
    bbf = open(bb_path, 'r')
    bbd = bbf.read()
    bbt = tk.Text(bb_win, fg=primary_color, bg=bgcolor)
    bbt.pack(pady=20)
    bbt.insert("insert", bbd)


def bbt():
    bb_win = tk.Tk()
    bb_win.configure(bg=bgcolor)
    bb_win.iconbitmap('Tavaram.ico')
    bb_win.title("ரோஜா செடியில் அஃபிட்ஸ்")
    bbt = tk.Text(bb_win, fg=secondary_color, bg=bgcolor, font=tamil_font)
    bbt.pack(pady=20)
    bbt.insert("insert", "ரோஜா செடியில் அஃபிட்ஸ்.  காரணங்கள்: முந்தைய இலையுதிர்காலத்தில் தண்டுகளில் முட்டையிட்டதால், அசுவினிகள் பொதுவாக ரோஜாக்களில் குளிர்காலம் அதிகமாக இருக்கும்.  இருப்பினும், பாதுகாப்பான இடங்களில் ஆண்டு முழுவதும் சுறுசுறுப்பான நிம்ஃப்கள் மற்றும் பெரியவர்கள் இருக்கலாம்.  ரோஜாக்கள் புதிய வளர்ச்சியை உருவாக்கும் மற்றும் கோடையின் தொடக்கத்தில் உச்சத்தை அடையும் போது அஃபிட் எண்ணிக்கை வசந்த காலத்தில் அதிகரிக்கத் தொடங்குகிறது.  சிகிச்சை:  ஒரு ஸ்ப்ரே பாட்டிலில் 1 பங்கு வினிகரை மூன்று பங்கு தண்ணீருடன் கலக்கவும்.  கலவையில் 2-5 மில்லி சில துளிகள் டிஷ் சோப்பை சேர்க்கவும், இது தாவரங்களின் இலைகளில் ஒட்டிக்கொள்ள உதவும்.  கலவையை நன்றாக கலக்கவும்.  கலவையை அசுவினிகள் மற்றும் அவை இருக்கும் தாவரங்களின் இலைகள் மீது நேரடியாக தெளிக்கவும்.")


def bce():
    bc_win = tk.Tk()
    bc_win.configure(bg=bgcolor)
    bc_win.iconbitmap('Tavaram.ico')
    bc_win.title("Rose Plant - Downey Mildew")
    bc_path = os.path.join(current_dir, 'bce.txt')
    bcf = open(bc_path, 'r')
    bcd = bcf.read()
    bct = tk.Text(bc_win, bg=bgcolor, fg=primary_color)
    bct.pack(pady=20)
    bct.insert("insert", bcd)


def bct():
    bc_win = tk.Tk()
    bc_win.configure(bg=bgcolor)
    bc_win.iconbitmap('Tavaram.ico')
    bc_win.title("ரோஜா செடிகளில் டவுனி பூஞ்சை காளான்")
    bct = tk.Text(bc_win, bg=bgcolor, fg=secondary_color, font=tamil_font)
    bct.pack(pady=20)
    bct.insert("insert", "ரோஜா செடிகளில் டவுனி பூஞ்சை காளான்.  காரணங்கள்: ரோஸ் டவுனி பூஞ்சை காளான் நோய் பெரோனோஸ்போரா ஸ்பார்சா, ஒரு கட்டாய பயோட்ரோபிக் ஓமைசீட் மூலம் ஏற்படுகிறது.  இந்த நோய் ரோஜா செடிகளின் மிகவும் அழிவுகரமான நோய்களில் ஒன்றாகும் மற்றும் கிரீன்ஹவுஸ், நர்சரி மற்றும் இயற்கை அமைப்புகளில் உள்ள அனைத்து வகையான ரோஜாக்களையும் தாக்குகிறது.  சிகிச்சை: காற்று சுழற்சியை அதிகரிக்கவும் மற்றும் அதிகப்படியான ஈரப்பதத்தை குறைக்கவும், கரும்புகளை மெல்லியதாகவும், முடிந்தவரை இலைகளை குறைக்கவும்.  சரியான இடைவெளி காற்று சுழற்சியை மேம்படுத்துவதோடு நோய் பரவாமல் தடுக்கவும் உதவும்.")


def bde():
    bd_win = tk.Tk()
    bd_win.configure(bg=bgcolor)
    bd_win.iconbitmap('Tavaram.ico')
    bd_win.title("Plant Looks Healthy")
    bd_path = os.path.join(current_dir, 'bde.txt')
    bdf = open(bd_path, 'r')
    bdd = bdf.read()
    bdt = tk.Text(bd_win, bg=bgcolor, fg=primary_color)
    bdt.pack(pady=20)
    bdt.insert("insert", bdd)


def bdt():
    bd_win = tk.Tk()
    bd_win.configure(bg=bgcolor)
    bd_win.iconbitmap('Tavaram.ico')
    bd_win.title("தாவரம் ஆரோக்கியமாக தெரிகிறது")
    bdt = tk.Text(bd_win, bg=bgcolor, fg=secondary_color, font=tamil_font)
    bdt.pack(pady=20)
    bdt.insert("insert", "உங்கள் ரோஜா செடி ஆரோக்கியமாக இருக்கிறது. ஏதேனும் அறிகுறிகள் இருந்தால், வேறு கோணத்தில் மீண்டும் முயற்சிக்கவும்.")


def ade():
    ad_win = tk.Tk()
    ad_win.configure(bg=bgcolor)
    ad_win.iconbitmap('Tavaram.ico')
    ad_win.title("Plant Looks Healthy")
    ad_path = os.path.join(current_dir, 'ade.txt')
    adf = open(ad_path, 'r')
    add = adf.read()
    adt = tk.Text(ad_win, bg=bgcolor, fg=primary_color)
    adt.pack(pady=20)
    adt.insert("insert", add)


def adt():
    ad_win = tk.Tk()
    ad_win.configure(bg=bgcolor)
    ad_win.iconbitmap('Tavaram.ico')
    ad_win.title("தாவரம் ஆரோக்கியமாக தெரிகிறது")
    adt = tk.Text(ad_win, bg=bgcolor, fg=secondary_color, font=tamil_font)
    adt.pack(pady=20)
    adt.insert("insert", "உங்கள் துளசி செடி ஆரோக்கியமாக இருக்கிறது. ஏதேனும் அறிகுறிகள் இருந்தால், வேறு கோணத்தில் மீண்டும் முயற்சிக்கவும்.")


def aa():

    aa_win = tk.Tk()
    aa_win.configure(bg=bgcolor)
    aa_win.iconbitmap('Tavaram.ico')
    aaeb = tk.Button(aa_win, text="English", command=aae, bg=bgcolor, fg=secondary_color)
    aatb = tk.Button(aa_win, text="Tamil", command=aat, bg=bgcolor, fg=primary_color)
    aaeb.pack()
    aatb.pack()


def ab():
    aa_win = tk.Tk()
    aa_win.configure(bg=bgcolor)
    aa_win.iconbitmap('Tavaram.ico')
    abeb = tk.Button(aa_win, text="English", command=abe, bg=bgcolor, fg=secondary_color)
    abtb = tk.Button(aa_win, text="Tamil", command=abt, bg=bgcolor, fg=primary_color)
    abeb.pack()
    abtb.pack()


def ac():
    aa_win = tk.Tk()
    aa_win.configure(bg=bgcolor)
    aa_win.iconbitmap('Tavaram.ico')
    abeb = tk.Button(aa_win, text="English", command=ace, bg=bgcolor, fg=secondary_color)
    abtb = tk.Button(aa_win, text="Tamil", command=act, bg=bgcolor, fg=primary_color)
    abeb.pack()
    abtb.pack()


def ba():
    aa_win = tk.Tk()
    aa_win.configure(bg=bgcolor)
    aa_win.iconbitmap('Tavaram.ico')
    abeb = tk.Button(aa_win, text="English", command=bae, bg=bgcolor, fg=secondary_color)
    abtb = tk.Button(aa_win, text="Tamil", command=bat, bg=bgcolor, fg=primary_color)
    abeb.pack()
    abtb.pack()


def bb():
    aa_win = tk.Tk()
    aa_win.configure(bg=bgcolor)
    aa_win.iconbitmap('Tavaram.ico')
    abeb = tk.Button(aa_win, text="English", command=bbe, bg=bgcolor, fg=secondary_color)
    abtb = tk.Button(aa_win, text="Tamil", command=bbt, bg=bgcolor, fg=primary_color)
    abeb.pack()
    abtb.pack()


def bc():
    aa_win = tk.Tk()
    aa_win.configure(bg=bgcolor)
    aa_win.iconbitmap('Tavaram.ico')
    abeb = tk.Button(aa_win, text="English", command=bce, bg=bgcolor, fg=secondary_color)
    abtb = tk.Button(aa_win, text="Tamil", command=bct, bg=bgcolor, fg=primary_color)
    abeb.pack()
    abtb.pack()


def bd():
    aa_win = tk.Tk()
    aa_win.configure(bg=bgcolor)
    aa_win.iconbitmap('Tavaram.ico')
    abeb = tk.Button(aa_win, text="English", command=bde, bg=bgcolor, fg=secondary_color)
    abtb = tk.Button(aa_win, text="Tamil", command=bdt, bg=bgcolor, fg=primary_color)
    abeb.pack()
    abtb.pack()


def ad():
    aa_win = tk.Tk()
    aa_win.configure(bg=bgcolor)
    aa_win.iconbitmap('Tavaram.ico')
    abeb = tk.Button(aa_win, text="English", command=ade, bg=bgcolor, fg=secondary_color)
    abtb = tk.Button(aa_win, text="Tamil", command=adt, bg=bgcolor, fg=primary_color)
    abeb.pack()
    abtb.pack()


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
    main_win.configure(bg=bgcolor)
    main_win.iconbitmap('Tavaram.ico')
    path_label = tk.Label(main_win, text="Enter Image path:", bg=bgcolor, fg=secondary_color)
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
        elif index == 5:
            bc()
        elif index == 6:
            bd()
        elif index == 7:
            ad()



    path_button = tk.Button(main_win, text="Go", command=image_path, bg=primary_color, fg=accent)
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
window.configure(bg=bgcolor)
window.iconbitmap('Tavaram.ico')
window.title("Login/Signup System")

username_label = tk.Label(window, text="Username:", bg=bgcolor, fg=primary_color)
username_label.pack()
username_entry = tk.Entry(window, bg='black', fg='white')
username_entry.pack()

# Create password label and entry
password_label = tk.Label(window, text="Password:", bg=bgcolor, fg=primary_color)
password_label.pack()
password_entry = tk.Entry(window, show="*", bg='black', fg='white')
password_entry.pack()


# Create login button
login_button = tk.Button(window, text="Login", command=login, bg=secondary_color, fg=accent)
login_button.pack()

# Create signup button
signup_button = tk.Button(window, text="Signup", command=signup, bg=secondary_color, fg=accent)
signup_button.pack()

# Create quit button
quit_button = tk.Button(window, text="Quit", command=quit_program, bg=accent, fg=secondary_color)
quit_button.pack()

window.mainloop()
