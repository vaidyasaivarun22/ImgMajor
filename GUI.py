import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
import os
import AES_EncryptDecrypt
import tkinter.colorchooser as cc
from PIL import Image, ImageDraw, ImageTk

class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.config(
            bg="#2c3e50",  # background color
            fg="#ecf0f1",  # foreground color
            relief="flat",  # border style
            bd=5,  # border width
            highlightbackground="white",
            padx=10,  # horizontal padding
            pady=5,  # vertical padding
            font=("Helvetica", 12, "bold")  # font style
        )
        self.config(bg=self["bg"], fg=self["fg"])
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
    
    def on_enter(self, event):
        self.config(bg=self["fg"], fg=self["bg"])
        
    def on_leave(self, event):
        self.config(bg=self["activebackground"], fg=self["activeforeground"])

parent_dir=os.getcwd()+"/Database/"
global enc_file
global enc_key
global enc_v
global dec_v
global dec_key
global dec_file

def mk():
    if(not(os.path.isdir("Database"))):
        os.mkdir("Database")
        os.mkdir(os.path.join(parent_dir,"input"))
        os.mkdir(os.path.join(parent_dir,"encrypt"))
        os.mkdir(os.path.join(parent_dir,"decrypt"))
mk()

def e():
    exit()

def openfileEnc():
    global enc_file
    path=os.path.join(parent_dir,"input")
    filename=filedialog.askopenfile(initialdir=path,title="Select file",filetype=(("image files",".jpg"),("image files",".png"),("all files","*.*")))
    if filename is None:
        enc_file=""
        i.set("No File Selected")
    else:
        enc_file=filename.name
        i.set(enc_file)

def openfileDec():
    global dec_file
    path=os.path.join(parent_dir,"encrypt")
    filename=filedialog.askopenfile(initialdir=path,title="Select file",filetype=(("image files",".jpg"),("image files",".png"),("all files","*.*")))
    if filename is None:
        dec_file=""
        j.set("No File Selected")
    else:
        dec_file=filename.name
        j.set(dec_file)

def key():
    global enc_v
    global enc_key
    if(enc_v.get()=="AES-512"):
        enc_key=simpledialog.askstring("password","Enter the password")
   
    else:
        messagebox.showwarning("warning","No method selected")

def Deckey():
    global dec_v
    global dec_key
    if(dec_v.get()=="AES-512"):
        dec_key=simpledialog.askstring("password","Enter the password")
    else:
        messagebox.showwarning("warning","No method selected")

def encrypt():
    global enc_v
    global enc_file
    global enc_key
    if(enc_v.get()=="AES-512"):
        AES_EncryptDecrypt.aes_encrypt(parent_dir,enc_key,enc_file)
        tk.messagebox.showinfo("Success","Encryption Successful")
    else:
        messagebox.showwarning("warning","Encryption input not Found")
        print(enc_v.get())

def decrypt():
    global dec_v
    global dec_file
    global dec_key
    if(dec_v.get()=="AES-512"):
        AES_EncryptDecrypt.aes_decrypt(parent_dir,dec_key,dec_file)
        tk.messagebox.showinfo("success","Decryption Successful")
    else:
        messagebox.showwarning("warning","Decryption input not Found")
        print(dec_v.get())

def pick_color(labelframe1,labelframe2):
    color = cc.askcolor()[1] # askcolor() returns a tuple of (color in RGB, color in hexadecimal), we only need the hexadecimal color
    if color:
        labelframe1.config(bg=color)
        labelframe2.config(bg=color)

# def about_frame():
#     top = tk.Tk()

def para_frame():
    
    # create new window
    para_frame_1 = tk.Tk()
    para_frame_1.title("About AES Encryption")

    # set window size and position
    para_frame_1.geometry("800x250+340+75")

    text1 = tk.Text(para_frame_1, font=('Helvetica', 12))
    text1.pack()
    # create text widgets
    text1.tag_configure( "bullet", font=('Helvetica', 12), foreground='black', background= '#ecf0f1', lmargin1=0, lmargin2=10, justify='left', tabs=('5'))
    text1.insert(tk.END, '• The AES Encryption algorithm (also known as the Rijndael algorithm) is a symmetric block cipher algorithm with a block/chunk size of 128 bits. It converts these individual blocks using keys of 128, 192, and 256 bits. Once it encrypts these blocks, it joins them together to form the ciphertext\n', 'bullet')
    text1.insert(tk.END, '• It is based on a substitution-permutation network, also known as an SP network. It consists of a series of linked operations, including replacing inputs with specific outputs (substitutions) and others involving bit shuffling (permutations)\n', 'bullet')
    text1.insert(tk.END, '• For encryption, each round consists of the following four steps:\n1) Substitute bytes\n2) Shift rows\n3) Mix columns\n4) Add round key\n• The last step consists of XORing the output of the previous three steps with four words from the key schedule.\n\n\n', 'bullet')
    text1.pack(fill="both", expand=True)



    para_frame_2 = tk.Tk()
    para_frame_2.title("About AES Decryption")

    # set window size and position
    para_frame_2.geometry("800x230+340+450")

    text2 = tk.Text(para_frame_2, font=('Helvetica', 12))
    text2.pack(fill="both", expand=True)
    # create text widgets
    text2.tag_configure( "bullet", font=('Helvetica', 12), foreground='black', background= '#ecf0f1', lmargin1=0, lmargin2=10, justify='left', tabs=('5'))
    text2.insert(tk.END, '• AES is a symmetric algorithm which uses the same 128, 192, or 256 bit key for both encryption and decryption (the security of an AES system increases exponentially with key length)\n', 'bullet')
    text2.insert(tk.END, '• For decryption, each round consists of the following four steps: \n1) Inverse shift rows\n2) Inverse substitute bytes\n3) Add round key\n4) Inverse mix columns\n• The third step consists of XORing the output of the previous two steps with four words from the key schedule\n', 'bullet')
    text2.insert(tk.END, '• The last round for encryption does not involve the “Mix columns” step. The last round for decryption does not involve the “Inverse mix columns” step.\n\n\n\n\n', 'bullet')

    text2.pack()

def db_connect():
    messagebox.showinfo("Info", "This feature is launching soon!")

def capture_image():
    messagebox.showinfo("Alert", "Capturing Image!")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    cv2.imwrite("captured_image.jpg", frame)
    image = Image.open("captured_image.jpg")
    photo = ImageTk.PhotoImage(image)

    messagebox.showinfo("Info", "Image captured and saved successfully!")

def frame():
    # Adjusting the Window size of the GUI form the top left corner
    top = tk.Tk()
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    top.geometry("%dx%d+0+0" % (screen_width, screen_height))
    top.configure(bg="black")
    top.title("Image Cryptography")
    labelframe2=tk.LabelFrame(top,text="IMAGE ENCRYPTION ",height=355,bg="#ECF9FF",width=1500,font=("Helvetica", 24))
    labelframe2.place(x=150,y=0)
    labelframe3=tk.LabelFrame(top,text="IMAGE DECRYPTION ",height=400,bg="#ECF9FF",width=1500,font=("Helvetica", 24))
    labelframe3.place(x=150,y=356)

    menu_frame = tk.Frame(top, bg="#FFE7CC", width=200)

    # create the menu items as buttons
    home_btn = tk.Button(menu_frame, text="Home", bg="#FFFBEB", fg="black", activebackground="white", width=20)
    about_btn = tk.Button(menu_frame, text="About", bg="#FFFBEB", fg="black", width=20, command=para_frame)
    contact_btn = tk.Button(menu_frame, text="Connect DB", bg="#FFFBEB", fg="black", width=20, command=db_connect)
    featuresButton = tk.Label(menu_frame, text="Features", bg="#FFFBEB", fg="black",width=22).place(y=500)
    capture_button = tk.Button(menu_frame, text="Capture Image", bg="#FFFBEB", fg="black", width=20, command=capture_image)
    # pack the menu items into the menu frame
    home_btn.pack(pady=10)
    about_btn.pack(pady=10)
    contact_btn.pack(pady=10)

    # pack the menu frame into the main window
    menu_frame.pack(side="left", fill="y")

    # create a new image with size 16x16 and color mode "RGB"
    image = Image.new("RGB", (16, 16), (255, 255, 255))

    # create a draw object
    draw = ImageDraw.Draw(image)

    # draw a circle in the center of the image with radius 7 and outline color (0, 0, 0)
    draw.ellipse((4, 4, 11, 11), outline=(0, 0, 0))

    # draw a smaller circle inside the first circle with radius 4 and fill color (255, 0, 0)
    draw.ellipse((6, 6, 9, 9), fill=(255, 0, 0))

    # save the image to a file
    image.save("colorpicker.png")

    icon = Image.open("colorpicker.png")

    # create a PhotoImage object from the icon
    photo = ImageTk.PhotoImage(icon)

    # create the buttons to pick the colors
    button2 = tk.Button(top, image=photo, command=lambda: pick_color(labelframe2,labelframe3),fg="black").place(x=10, y=540)
    # Create a label for the text
    text_label = tk.Label(top,text= "change Bg color",bg="#FFE7CC")
    text_label.pack(side="left")
    text_label.place(x=40, y=540)

    capture_button.place(x=0, y=590)

    global i
    global enc_v
    global enc_key
    global enc_file
    listus=["AES-512"]
    enc_v=tk.StringVar()
    enc_v.set("Select")
    i=tk.StringVar()
    
    inputEncFile = tk.Label(labelframe2, text="Select Image",font=("Arial", 14)).place(x=200,y=50)
    inputEncFileEntry = tk.Entry(labelframe2,width=42,textvariable=i,font=("Arial", 14)).place(x=350,y=50)
    inputEncBtn = tk.Button(labelframe2, text="Browse",width=10, height=1,bg="blue",command=openfileEnc,font=("Arial", 14)).place(x=850,y=46)
    recEncFile = tk.Label(labelframe2, text="Select Method",font=("Arial", 14)).place(x=200,y=100)
    reclistBtn=tk.OptionMenu(labelframe2,enc_v,*listus).place(x=350,y=97,width=100)
    keyEncFile = tk.Label(labelframe2, text="Generate Key",font=("Arial", 14)).place(x=200,y=150)
    keyBtn=tk.Button(labelframe2,text="Input Key", height=1,activebackground="white",command=key,font=("Arial", 14)).place(x=350,y=150,width=100)
    EncryptBTN= CustomButton(labelframe2,text="Encrypt",width=20, height=2,activebackground="#FFE7CC",command=encrypt,font=("Arial", 14),borderwidth=5).place(anchor="e",relx=.55,rely=.65)

    global j
    global dec_key
    global dec_file
    global dec_v
    j=tk.StringVar()
    dec_v=tk.StringVar()
    dec_v.set("Select")


    inputDecFile = tk.Label(labelframe3, text="Select Image",font=("Arial", 14)).place(x=200,y=50)
    inputDecFileEntry = tk.Entry(labelframe3,width=42,textvariable=j,font=("Arial", 14)).place(x=350,y=50)
    inputDecBtn = tk.Button(labelframe3, text="Browse",width=10, height=1,bg="blue",command=openfileDec,font=("Arial", 14)).place(x=850,y=46)
    recDecFile = tk.Label(labelframe3, text="Select Method",font=("Arial", 14)).place(x=200,y=100)
    reclistBtn=tk.OptionMenu(labelframe3,dec_v,*listus).place(x=350,y=97,width=100)
    keyEncFile = tk.Label(labelframe3, text="Select secret",font=("Arial", 14)).place(x=200,y=150)
    keyBtn=tk.Button(labelframe3,text="Input Key", height=1,activebackground="white",command=Deckey,font=("Arial", 14)).place(x=350,y=150,width=100)
    EncryptBTN=CustomButton(labelframe3,text="Decrypt",width=20, height=2,activebackground="#FFE7CC",command=decrypt,font=("Arial", 14)).place(anchor="e",relx=.55,rely=.65)

    top.mainloop()

frame()