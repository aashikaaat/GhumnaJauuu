import tkinter as tk
from tkinter import *
import customtkinter 
import customtkinter as CTK
from customtkinter import*
import sqlite3
from tkinter import ttk
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

def dash():
    root.destroy()
    import admindash
 

def clients():
    root.destroy()
    import clientdetails   

# upperframe
frame=customtkinter.CTkFrame(master=root, fg_color="#153519", corner_radius=0)
frame.place(x =0,y =0, w=1920, h=160)


#insert image
pil_image1 = Image.open("dashicon.png")

# imageresize
pil_image1 = pil_image1.resize((150,150))

# Convert the PIL image to a PhotoImage object
photo_image = ImageTk.PhotoImage(pil_image1)

# Create a Label widget to display the image
label = tk.Label(root, image=photo_image)
label.place(x=20, y=14, w=133, h=133)

#to prevent images from being garbage collected
label=pil_image1


#possible destination frame
frame=customtkinter.CTkFrame(master=root, fg_color="#000000", corner_radius=0)
frame.place(x =0,y =128, w=380, h=130)

#destinations frame
frame=customtkinter.CTkFrame(master=root, fg_color="#99B104",corner_radius=0)
frame.place(x =0,y =232, w=380, h=818)

# “I now walk into the wild.”
label1 = CTkLabel(master=root, text="“I now walk into the wild.”", font=("Bold Italic", 20, "bold"), text_color="#000000",fg_color="#FFFFFF")
label1.place(x=330, y=130, w=310, h=68)

#Hi, User*
label1 = CTkLabel(master=root, text="Hi, User*", font=("Calibri", 35, "bold"), text_color="#FFFFFF", fg_color="#153519")
label1.place(x=1300, y=50, w=182, h=38)

#  ― Jon Krakauer,
label1 = CTkLabel(master=root, text=" ― Jon Krakauer,", font=("Bold Italic", 20, ), text_color="#000000",fg_color="#FFFFFF")
label1.place(x=1143, y=172, w=200, h=25)

#  Into the Wild
label1 = CTkLabel(master=root, text="Into the Wild", font=("Bold Italic", 20, "underline"), text_color="#000000",fg_color="#FFFFFF")
label1.place(x=1300, y=172, w=168, h=28)

#welcome back
label1 = CTkLabel(master=root, text="Welcome back!", font=("Inter", 26, "bold"), text_color="#FFFFFF", fg_color="#000000")
label1.place(x=10, y=145, w=360, h=36)

#BOSS
label1 = CTkLabel(master=root, text="BOSS", font=("Inter", 26, "bold"), text_color="#FFFFFF", fg_color="#000000")
label1.place(x=10, y=185, w=360, h=36)

#Welcome to
label1 = CTkLabel(master=root, text="Welcome to", font=("Inter", 20), text_color="#FFFFFF", fg_color="#153519")
label1.place(x=100, y=40, w=150, h=36)

#Ghumna Jau
label1 = CTkLabel(master=root, text="Ghumna Jau", font=("Inter", 20,"bold"), text_color="#FFFFFF", fg_color="#153519")
label1.place(x=100, y=65, w=150, h=36)


#Dashboard
bookingdate_btn=CTkButton(master=root, text="Dashboard",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#99B104",hover_color="#738600",bg_color="#99B104", corner_radius=0,command=dash)
bookingdate_btn.place(x=0, y=250, w=380,h=117)
bookingdate_indicate=tk.Label( bg="#FFFFFF")
bookingdate_indicate.place(x=0, y=315, w=8, h=117)

#Client
clientid_btn=CTkButton(master=root, text="Client",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#99B104",hover_color="#738600",bg_color="#99B104", corner_radius=0, command=clients)
clientid_btn.place(x=0, y=343, w=380,h=117)
clientid_indicate=tk.Label( bg="#FFFFFF")
clientid_indicate.place(x=0, y=430, w=8, h=117)

#Location
location_btn=CTkButton(master=root, text="Location",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#738600",hover_color="#000000",bg_color="#99B104", corner_radius=0)
location_btn.place(x=0, y=436, w=380,h=117)
location_indicate=tk.Label( bg="#FFFFFF")
location_indicate.place(x=0, y=546, w=8, h=117)

#nagarkot
pil_image1=Image.open("nagarkothotel.png")#insert image
pil_image1=pil_image1.resize((362,168))#resize
photo_image1=ImageTk.PhotoImage(pil_image1)#pil to photo image
label1 = tk.Label(root, image=photo_image1)#label
label1.place(x=457, y=300, w=362, h=168)
label1=pil_image1

#Nagarkot
label1 = CTkLabel(master=root, text="Nagarkot: Himalayan Range View Hotel", font=("Inter", 16), text_color="#FFFFFF", fg_color="#153519")
label1.place(x=365, y=380, w=365, h=36)
label1 = CTkLabel(master=root, text="NRs 7250", font=("Inter", 14, "underline"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=365, y=410, w=90, h=36)
btn=CTkButton(master=root, text="Edit",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#FF0000",bg_color="#FFFFFF")
btn.place(x=550, y=410, w=132,h=34)

# dhulikhel
pil_image2=Image.open("dhulikhelhotel.png")#insert image
pil_image2=pil_image2.resize((362,168))#resize
photo_image2=ImageTk.PhotoImage(pil_image2)#pil to photo image
label2 = tk.Label(root, image=photo_image2)#label
label2.place(x=969, y=300, w=362, h=168)
label2=pil_image2

# dhulikhel
label1 = CTkLabel(master=root, text="Dhulikhel: Dhulikhel Resort", font=("Inter", 16), text_color="#FFFFFF", fg_color="#153519")
label1.place(x=775, y=380, w=365, h=36)
label1 = CTkLabel(master=root, text="NRs 7200", font=("Inter", 14, "underline"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=775, y=410, w=90, h=36)
btn=CTkButton(master=root, text="Edit",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#FF0000",bg_color="#FFFFFF")
btn.place(x=960, y=410, w=132,h=34)

# shivapuri
pil_image3=Image.open("shivapurihotel.png")#insert image
pil_image3=pil_image3.resize((362,168))#resize
photo_image3=ImageTk.PhotoImage(pil_image3)#pil to photo image
label3 = tk.Label(root, image=photo_image3)#label
label3.place(x=1481, y=300, w=362, h=168)
label3=pil_image3

# shivapuri
label1 = CTkLabel(master=root, text="Shivapuri: Fulbari Resort", font=("Inter", 16), text_color="#FFFFFF", fg_color="#153519")
label1.place(x=1185, y=380, w=365, h=36)
label1 = CTkLabel(master=root, text="NRs 7120", font=("Inter", 14, "underline"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=1185, y=410, w=90, h=36)
btn=CTkButton(master=root, text="Edit",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#FF0000",bg_color="#FFFFFF")
btn.place(x=1370, y=410, w=132,h=34)


# chitlang
pil_image4=Image.open("chitlanghotel.png")#insert image
pil_image4=pil_image4.resize((362,168))#resize
photo_image4=ImageTk.PhotoImage(pil_image4)#pil to photo image
label4 = tk.Label(root, image=photo_image4)#label
label4.place(x=730, y=650, w=362, h=168)
label4=pil_image4


# chitlang
label1 = CTkLabel(master=root, text="Chitlang: Kulekhani View Resort", font=("Inter", 16), text_color="#FFFFFF", fg_color="#153519")
label1.place(x=583, y=660, w=365, h=36)
label1 = CTkLabel(master=root, text="NRs 7050", font=("Inter", 14, "underline"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=580, y=690, w=90, h=36)
btn=CTkButton(master=root, text="Edit",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#FF0000",bg_color="#FFFFFF")
btn.place(x=765, y=690, w=132,h=34)

# chandragiri
pil_image5=Image.open("chandragirihotel.png")#insert image
pil_image5=pil_image5.resize((362,168))#resize
photo_image5=ImageTk.PhotoImage(pil_image5)#pil to photo image
label5 = tk.Label(root, image=photo_image5)#label
label5.place(x=1300, y=650, w=362, h=168)
label5=pil_image5

# chandragiri
label1 = CTkLabel(master=root, text="Chandragiri: Chandragiri Resort", font=("Inter", 16), text_color="#FFFFFF", fg_color="#153519")
label1.place(x=1040, y=660, w=365, h=36)
label1 = CTkLabel(master=root, text="NRs 6650", font=("Inter", 14, "underline"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=1040, y=690, w=90, h=36)
btn=CTkButton(master=root, text="Edit",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#FF0000",bg_color="#FFFFFF")
btn.place(x=1225, y=690, w=132,h=34)




#Exit
transport_btn=CTkButton(master=root, text="EXIT",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#99B104",hover_color="#738600",bg_color="#99B104", corner_radius=0,command=logout)
transport_btn.place(x=0, y=529, w=380,h=117)
transport_indicate=tk.Label( bg="#FFFFFF")
transport_indicate.place(x=0, y=662, w=8, h=117)


root.mainloop()
