import tkinter as tk
from tkinter import *
import customtkinter 
import customtkinter as CTK
from customtkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

root = customtkinter.CTk() #window
root.iconbitmap("logo.ico")     
root.title("घुम्न जाऔँ") #page title

# screen
frame=customtkinter.CTkFrame(master=root, fg_color="#FFFFFF", corner_radius=0)
frame.place(x =0,y =0, w=1920, h=1080)


# window resolution
screenwidth= root.winfo_screenwidth()
screenheight= root.winfo_screenheight()
root.geometry(f'{screenwidth}x{screenheight}+0+0')

def logout():
    root.destroy()
    import login

def nagarkot():
    root.destroy()
    import nagarkot

def chandragiri():
    root.destroy()
    import chandragiri

def shivapuri():
    root.destroy()
    import shivapuri

def chitlang():
    root.destroy()
    import chitlang     

# upperframe
frame=customtkinter.CTkFrame(master=root, fg_color="#153519", corner_radius=0)
frame.place(x =0,y =0, w=1920, h=160)


#insert image
pil_image = Image.open("dashicon.png")

# imageresize
pil_image = pil_image.resize((150,150))

# Convert the PIL image to a PhotoImage object
photo_image = ImageTk.PhotoImage(pil_image)

# Create a Label widget to display the image
label = tk.Label(root, image=photo_image)
label.place(x=20, y=14, w=133, h=133)

#to prevent images from being garbage collected
label=pil_image

#possible destination frame
frame=customtkinter.CTkFrame(master=root, fg_color="#000000", corner_radius=0)
frame.place(x =0,y =128, w=380, h=130)

#destinations frame
frame=customtkinter.CTkFrame(master=root, fg_color="#99B104",corner_radius=0)
frame.place(x =0,y =232, w=380, h=818)

# “That's what was great about him. He tried. Not many do.”
label1 = CTkLabel(master=root, text="“That's what was great about him. He tried. Not many do.”", font=("Bold Italic", 20, "bold"), text_color="#000000",fg_color="#FFFFFF")
label1.place(x=310, y=130, w=700, h=68)

#Hi, User*
label1 = CTkLabel(master=root, text="Hi, User*", font=("Calibri", 35, "bold"), text_color="#FFFFFF", fg_color="#153519")
label1.place(x=1300, y=50, w=182, h=38)

#  ― Jon Krakauer,
label1 = CTkLabel(master=root, text=" ― Jon Krakauer,", font=("Bold Italic", 20, ), text_color="#000000",fg_color="#FFFFFF")
label1.place(x=790, y=172, w=200, h=25)

#  Into the Wild
label1 = CTkLabel(master=root, text="Into the Wild", font=("Bold Italic", 20, "underline"), text_color="#000000",fg_color="#FFFFFF")
label1.place(x=947, y=172, w=168, h=28)

#Your Possible
label1 = CTkLabel(master=root, text="Your Possible", font=("Inter", 26, "bold"), text_color="#FFFFFF", fg_color="#000000")
label1.place(x=10, y=145, w=360, h=36)

#Destination
label1 = CTkLabel(master=root, text="Destination", font=("Inter", 26, "bold"), text_color="#FFFFFF", fg_color="#000000")
label1.place(x=10, y=185, w=360, h=36)

#Welcome to
label1 = CTkLabel(master=root, text="Welcome to", font=("Inter", 20), text_color="#FFFFFF", fg_color="#153519")
label1.place(x=100, y=40, w=150, h=36)

#Ghumna Jau
label1 = CTkLabel(master=root, text="Ghumna Jau", font=("Inter", 20,"bold"), text_color="#FFFFFF", fg_color="#153519")
label1.place(x=100, y=65, w=150, h=36)

#Destination: Dhulikhel
label1 = CTkLabel(master=root, text="Destination: Dhulikhel", font=("Jost", 30,"bold"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=310, y=220, w=420, h=64)

pil_image1=Image.open("dhulikhel.png")#insert image
pil_image1=pil_image1.resize((529,298))#resize
photo_image1=ImageTk.PhotoImage(pil_image1)#pil to photo image
label1 = tk.Label(root, image=photo_image1)#label
label1.place(x=390, y=330, w=529, h=298)
label1=pil_image1


frame=customtkinter.CTkFrame(master=root, fg_color="#3F452F", bg_color="#FFFFFF",corner_radius=23)
frame.place(x =1150,y =230, w=396, h=653)
frame=customtkinter.CTkFrame(master=root, fg_color="#FFFFFF", bg_color="#FFFFFF")
frame.place(x =1160,y =620, w=370, h=10)

#nagarkot
nagarkot_btn=CTkButton(master=root, text="Nagarkot",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#99B104",hover_color="#738600",bg_color="#99B104", corner_radius=0,command=nagarkot)
nagarkot_btn.place(x=0, y=250, w=380,h=117)
nagarkot_indicate=tk.Label( bg="#FFFFFF")
nagarkot_indicate.place(x=0, y=315, w=8, h=117)

#dhulikhel
dhulikhel_btn=CTkButton(master=root, text="Dhulikhel",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#738600",hover_color="#000000",bg_color="#99B104", corner_radius=0)
dhulikhel_btn.place(x=0, y=343, w=380,h=117)
dhulikhel_indicate=tk.Label( bg="#FFFFFF")
dhulikhel_indicate.place(x=0, y=430, w=8, h=117)

#shivapuri
shivapuri_btn=CTkButton(master=root, text="Shivapuri",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#99B104",hover_color="#738600",bg_color="#99B104", corner_radius=0,command=shivapuri)
shivapuri_btn.place(x=0, y=436, w=380,h=117)
shivapuri_indicate=tk.Label( bg="#FFFFFF")
shivapuri_indicate.place(x=0, y=546, w=8, h=117)

#Chitlang
Chitlang_btn=CTkButton(master=root, text="Chitlang",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#99B104",hover_color="#738600",bg_color="#99B104", corner_radius=0,command=chitlang)
Chitlang_btn.place(x=0, y=529, w=380,h=117)
Chitlang_indicate=tk.Label( bg="#FFFFFF")
Chitlang_indicate.place(x=0, y=662, w=8, h=117)

#chandragiri
Chandragiri_btn=CTkButton(master=root, text="Chandragiri",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#99B104",hover_color="#738600",bg_color="#99B104", corner_radius=0,command=chandragiri)
Chandragiri_btn.place(x=0, y=622, w=380,h=117)
chandragiri_indicate=tk.Label( bg="#FFFFFF")
chandragiri_indicate.place(x=0, y=779, w=8, h=117)

#RECEIPT
label1 = CTkLabel(master=root, text="Ghumna Jau", font=("Inter", 20,"bold"), text_color="#FFFFFF", fg_color="#153519")
label1.place(x=100, y=65, w=150, h=36)

#Distance:
label1 = CTkLabel(master=root, text="Distance:", font=("Jost", 20,"bold"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=310, y=510, w=120, h=50)
label1 = CTkLabel(master=root, text="31 Kms (19 miles)", font=("Jost", 20,), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=410, y=510, w=210, h=50)

#vehicle
label1 = CTkLabel(master=root, text="Vehicle:", font=("Jost", 20,"bold"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=310, y=550, w=108, h=50)
label1 = CTkLabel(master=root, text="Pathao Taxi", font=("Jost", 20,), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=390, y=550, w=150, h=50)

#stay
label1 = CTkLabel(master=root, text="Stay:", font=("Jost", 20,"bold"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=310, y=590, w=70, h=50)
label1 = CTkLabel(master=root, text="2 Days & 1 Night", font=("Jost", 20), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=365, y=590, w=200, h=50)

#Hotel
label1 = CTkLabel(master=root, text="Hotel:", font=("Jost", 20,"bold"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=310, y=630, w=80, h=50)
label1 = CTkLabel(master=root, text="Dhulikhel Resort", font=("Jost", 20), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=370, y=630, w=220, h=50)

#activity
label1 = CTkLabel(master=root, text="Activity:", font=("Jost", 20,"bold"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=310, y=670, w=110, h=50)
label1 = CTkLabel(master=root, text="Sunset & Sunrise View, SPA, SONA,", font=("Jost", 20), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=392, y=670, w=430, h=50)
label1 = CTkLabel(master=root, text="Yoga, Trek", font=("Jost", 20), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=390, y=700, w=150, h=50)

#Enter the date
label1 = CTkLabel(master=root, text="To book the package:", font=("Jost", 20,"bold"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=315, y=780, w=250, h=50)
entry1=CTkEntry(master=root, placeholder_text="Enter the date",text_color="#FFFFFF",fg_color="#000000")
entry1.place(x=530, y=785, w=407,h=40)

#Receipt
label1 = CTkLabel(master=root, text="Receipt", font=("Jost", 28,"bold"), text_color="#FFFFFF", fg_color="#3F452F")
label1.place(x=1160, y=250, w=150, h=50)

# Pathao Fare:   
label1 = CTkLabel(master=root, text="Pathao Fare:    1800 -", font=("Jost", 17,"bold"), text_color="#FFFFFF", fg_color="#3F452F")
label1.place(x=1160, y=300, w=300, h=50)

# Hotel     :   
label1 = CTkLabel(master=root, text="Hotel           :    4250 -", font=("Jost", 17,"bold"), text_color="#FFFFFF", fg_color="#3F452F")
label1.place(x=1160, y=350, w=300, h=50)

label1 = CTkLabel(master=root, text="Activity       :     800 -", font=("Jost", 17,"bold"), text_color="#FFFFFF", fg_color="#3F452F")
label1.place(x=1160, y=400, w=300, h=50)

label1 = CTkLabel(master=root, text="Tax 18%        :    350 -", font=("Jost", 17,"bold"), text_color="#FFFFFF", fg_color="#3F452F")
label1.place(x=1160, y=450, w=300, h=50)

label1 = CTkLabel(master=root, text="Total           :    7250 -", font=("Jost", 17,"bold"), text_color="#FFFFFF", fg_color="#3F452F")
label1.place(x=1160, y=640, w=300, h=50)

#BOOK NOW
def booknow():
    messagebox.showinfo ("BOOKED!","Your hotel, activities and cab are booked.                                \
                         Thankyou for choosing us!")

btn=CTkButton(master=root, text="BookNow",command=booknow,font=("Archivo",22,"bold"),text_color="#000000",fg_color="#FFFFFF",bg_color="#3F452F", hover_color="#99B104")
btn.place(x=1300, y=690, w=180,h=40)

#logout button
btn=CTkButton(master=root, text="Log out",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#000000",bg_color="#FFFFFF",command=logout)
btn.place(x=1350, y=780, w=132,h=34)



root.mainloop()