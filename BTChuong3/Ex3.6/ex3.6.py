# import required modules
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

# contrast border thumbnail 
r = Tk()
r.title("Phan mem edit anh")
r.geometry("640x640")
# create functions
def selected():
    global path, image
    path = filedialog.askopenfilename(initialdir=os.getcwd()) 
    image = Image.open(path)
    image.thumbnail((350, 350))
    #imageg = image.filter(ImageFilter.BoxBlur(0))
    image1 = ImageTk.PhotoImage(image)
    nen_trang2.create_image(300, 210, image=image1)
    nen_trang2.image=image1                                                                                                                                                                                                                
def blur(event):
    global path, image1, imageg
    for m in range(0, v1.get()+1):
            image = Image.open(path)
            image.thumbnail((350, 350))
            imageg = image.filter(ImageFilter.BoxBlur(m))
            image1 = ImageTk.PhotoImage(imageg) 
            nen_trang2.create_image(300, 210, image=image1)
            nen_trang2.image=image1
            
def brightness(event):
    global path, image2, image3
    for m in range(0, v2.get()+1):
            image = Image.open(path)
            image.thumbnail((350, 350))
            imageg = ImageEnhance.Brightness(image)
            image2 = imageg.enhance(m)
            image3 = ImageTk.PhotoImage(image2)
            nen_trang2.create_image(300, 210, image=image3)
            nen_trang2.image=image3
def contrast(event):
    global path, image4, image5
    for m in range(0, v3.get()+1):
            image = Image.open(path)
            image.thumbnail((350, 350))
            imageg = ImageEnhance.Contrast(image)
            image4 = imageg.enhance(m)
            image5 = ImageTk.PhotoImage(image4)
            nen_trang2.create_image(300, 210, image=image5)
            nen_trang2.image=image5
def rotate_image(event):
        global path, image6, image7
        image = Image.open(path)
        image.thumbnail((350, 350))
        image6 = image.rotate(int(rotate_combo.get()))
        image7 = ImageTk.PhotoImage(image6)
        nen_trang2.create_image(300, 210, image=image7)
        nen_trang2.image=image7
        
def flip_image(event):
        global path, image8, image9
        image = Image.open(path)
        image.thumbnail((350, 350))
        if flip_combo.get() == "FLIP LEFT TO RIGHT":
            image8 = image.transpose(Image.FLIP_LEFT_RIGHT)
        elif flip_combo.get() == "FLIP TOP TO BOTTOM":
            image8 = image.transpose(Image.FLIP_TOP_BOTTOM)
        image9 = ImageTk.PhotoImage(image8)
        nen_trang2.create_image(300, 210, image=image9)
        nen_trang2.image=image9   
def image_border(event):
    global path, image10, image11
    image = Image.open(path)
    image.thumbnail((350, 350))
    image10 = ImageOps.expand(image, border=int(border_combo.get()), fill=95)
    image11 = ImageTk.PhotoImage(image10)
    nen_trang2.create_image(300, 210, image=image11)
    nen_trang2.image=image11    
image1 = None
image3 = None
image5 = None
image7 = None
image9 = None
image11 = None
def save():
    global path, imageg, image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11
    #file=None
    ext = path.split(".")[-1]
    file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
    if file: 
            if nen_trang2.image==image1:
                imageg.save(file)
            elif nen_trang2.image==image3:
                image2.save(file)
            elif nen_trang2.image==image5:
                image4.save(file)
            elif nen_trang2.image==image7:
                image6.save(file)
            elif nen_trang2.image==image9:
                image8.save(file)
            elif nen_trang2.image==image11:
                image10.save(file)        
# create labels, scales and comboboxes
blurr = Label(r, text="Blur:", font=("ariel 17 bold"), width=9, anchor='e')
blurr.place(x=15, y=8)
v1 = IntVar()
scale1 = ttk.Scale(r, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=blur) 
scale1.place(x=150, y=10)
bright = Label(r, text="Brightness:", font=("ariel 17 bold"))
bright.place(x=8, y=50)
v2 = IntVar()   
scale2 = ttk.Scale(r, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=brightness) 
scale2.place(x=150, y=55)
contrastt = Label(r, text="Contrast:", font=("ariel 17 bold"))
contrastt.place(x=35, y=92)
v3 = IntVar()   
scale3 = ttk.Scale(r, from_=0, to=10, variable=v3, orient=HORIZONTAL, command=contrast) 
scale3.place(x=150, y=100)
rotate = Label(r, text="Rotate:", font=("ariel 17 bold"))
rotate.place(x=370, y=8)
values = [0, 90, 180, 270, 360]
rotate_combo = ttk.Combobox(r, values=values, font=('ariel 10 bold'))
rotate_combo.place(x=460, y=15)
rotate_combo.bind("<<ComboboxSelected>>", rotate_image)
flip = Label(r, text="Flip:", font=("ariel 17 bold"))
flip.place(x=400, y=50)
values1 = ["FLIP LEFT TO RIGHT", "FLIP TOP TO BOTTOM"]
flip_combo = ttk.Combobox(r, values=values1, font=('ariel 10 bold'))
flip_combo.place(x=460, y=57)
flip_combo.bind("<<ComboboxSelected>>", flip_image)
border = Label(r, text="Add border:", font=("ariel 17 bold"))
border.place(x=320, y=92)
values2 = [i for i in range(10, 45, 5)]
border_combo = ttk.Combobox(r, values=values2, font=("ariel 10 bold"))
border_combo.place(x=460, y=99)
border_combo.bind("<<ComboboxSelected>>", image_border)
# create nen_trang to display image
nen_trang2 = Canvas(r, width="600", height="420", relief=RIDGE, bd=2)
nen_trang2.place(x=15, y=150)
# create buttons
btn1 = Button(r, text="Select Image", bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=selected)
btn1.place(x=100, y=595)
btn2 = Button(r, text="Save", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=save)
btn2.place(x=280, y=595)
btn3 = Button(r, text="Exit", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=r.destroy)
btn3.place(x=460, y=595)
r.mainloop()