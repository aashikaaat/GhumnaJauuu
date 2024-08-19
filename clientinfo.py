import tkinter as tk
from tkinter import *
import customtkinter 
import customtkinter as CTK
from customtkinter import*
import database
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


#Client Info
bookingdate_btn=CTkButton(master=root, text="Client Info",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#738600",hover_color="#000000",bg_color="#99B104", corner_radius=0)
bookingdate_btn.place(x=0, y=250, w=380,h=117)
bookingdate_indicate=tk.Label( bg="#FFFFFF")
bookingdate_indicate.place(x=0, y=315, w=8, h=117)

#Booking
clientid_btn=CTkButton(master=root, text="Booking",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#99B104",hover_color="#738600",bg_color="#99B104", corner_radius=0)
clientid_btn.place(x=0, y=343, w=380,h=117)
clientid_indicate=tk.Label( bg="#FFFFFF")
clientid_indicate.place(x=0, y=430, w=8, h=117)

#Location
location_btn=CTkButton(master=root, text="Location",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#99B104",hover_color="#738600",bg_color="#99B104", corner_radius=0)
location_btn.place(x=0, y=436, w=380,h=117)
location_indicate=tk.Label( bg="#FFFFFF")
location_indicate.place(x=0, y=546, w=8, h=117)

#Activity
transport_btn=CTkButton(master=root, text="Activity",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#99B104",hover_color="#738600",bg_color="#99B104", corner_radius=0)
transport_btn.place(x=0, y=529, w=380,h=117)
transport_indicate=tk.Label( bg="#FFFFFF")
transport_indicate.place(x=0, y=662, w=8, h=117)

#Hotels
hotel_btn=CTkButton(master=root, text="Hotels",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#99B104",hover_color="#738600",bg_color="#99B104", corner_radius=0)
hotel_btn.place(x=0, y=622, w=380,h=117)
hotel_indicate=tk.Label( bg="#FFFFFF")
hotel_indicate.place(x=0, y=779, w=8, h=117)

#GhumnaJau's Clients
label1 = CTkLabel(master=root, text="GhumnaJau's Clients", font=("Jost", 35,"bold"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=320, y=220, w=450, h=64)

#Clients Info
label1 = CTkLabel(master=root, text="Client's Information", font=("Jost", 28,"bold"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=350, y=320, w=450, h=64)

#Frame for table
frame3=customtkinter.CTkFrame(master=root, fg_color="#D9D9D9", corner_radius=0)
frame3.place(x =406,y =380, w=993, h=485)


# Table
table=ttk.Treeview(frame3, columns=('first','last','ph. no','email'),show='headings')
table.heading('first', text='First name')
table.heading('last', text='Last name')
table.heading('ph. no', text='Phone no')
table.heading('email', text='email')
table.place(x =0,y =0, w=993, h=485)

#insert values into table
# table.insert(parent='',index=0,values=('John','Doe',"9876543210",'Johndoe@mail.com'))


root.mainloop()
