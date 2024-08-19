import tkinter as tk
from tkinter import *
import customtkinter 
from customtkinter import*
from PIL import Image, ImageTk

root = customtkinter.CTk() #window
root.iconbitmap("logo.ico")
root.title("घुम्न जाऔँ") #page title

#window resolution
screenwidth= root.winfo_screenwidth()
screenheight= root.winfo_screenheight()
root.geometry(f'{screenwidth}x{screenheight}+0+0')

def loginpage():
    root.destroy()
    import loginpage 


def securitypage():
    root.destroy()
    import securitypage    

#appearence mode
customtkinter.set_appearance_mode("dark")

#background
pil_image = Image.open("signupbgoverlay.png")

#image resize
pil_image = pil_image.resize((1920, 1080))

# Convert the PIL image to a PhotoImage object
photo_image = ImageTk.PhotoImage(pil_image)


# Create a Label widget to display the image
label = tk.Label(root, image=photo_image)
label.pack()

#Sign Up
label1 = CTkLabel(master=root, text="Sign Up", font=("Be Vietnam", 40,"bold"), text_color="#000000", fg_color="#EEF52F")
label1.place(x=160, y=250, w=190, h=82)

#First name
entry1=CTkEntry(master=root, placeholder_text="First Name",fg_color="#000000",bg_color="#EEF52F")
entry1.place(x=160, y=320, w=320,h=34)

#Last name
entry2=CTkEntry(master=root, placeholder_text="Last Name",fg_color="#000000",bg_color="#EEF52F")
entry2.place(x=440, y=320, w=320,h=34)

#Enter your email
entry3=CTkEntry(master=root, placeholder_text="Enter your Email",fg_color="#000000",bg_color="#EEF52F")
entry3.place(x=160, y=370, w=670,h=34)

#Enter your phone number
entry4=CTkEntry(master=root, placeholder_text="Enter your Phone Number",fg_color="#000000",bg_color="#EEF52F")
entry4.place(x=160, y=420, w=670,h=34)

entry=CTkEntry(master=root, placeholder_text="Create Password ",fg_color="#000000",bg_color="#EEF52F",show="*")
entry.place(x=160, y=470, w=550,h=34)

def show_password(entry, var):
    if var.get():
        entry.configure(show="")
    else:
        entry.configure(show="*")

show_password_var = tk.IntVar()
show_password_checkbox = CTkCheckBox( master=root, bg_color="#EEF52F", variable=show_password_var, command=lambda: show_password(entry, show_password_var))
show_password_checkbox.place(x=605, y=470, w=30,h=30)

#confirm password
entry6=CTkEntry(master=root, placeholder_text="Confirm Password",fg_color="#000000",bg_color="#EEF52F",show="*")
entry6.place(x=160, y=520, w=550,h=34)

def show_password(entry, var):
    if var.get():
        entry.configure(show="")
    else:
        entry.configure(show="*")

show_passwordd_var = tk.IntVar()
show_password_checkbox = CTkCheckBox( master=root, bg_color="#EEF52F", variable=show_passwordd_var, command=lambda: show_password(entry6, show_passwordd_var))
show_password_checkbox.place(x=605, y=520, w=30,h=30)

#Back
btn=CTkButton(master=root, text="Back",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#000000",bg_color="#EEF52F", command = loginpage)
btn.place(x=160, y=570, w=132,h=34)

#Next
btn=CTkButton(master=root, text="Next",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#000000",bg_color="#EEF52F",command=securitypage)
btn.place(x=575, y=570, w=132,h=34)




root.mainloop()