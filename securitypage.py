import tkinter as tk
from tkinter import *
import customtkinter 
from customtkinter import*
from PIL import Image, ImageTk

root = customtkinter.CTk() #window
root.iconbitmap("logo.ico")
root.title("घुम्न जाऔँ") #page title

def loginpage():
    root.destroy()
    import loginpage 

def inputboard():
    root.destroy()
    import inputboard    

#window resolution
screenwidth= root.winfo_screenwidth()
screenheight= root.winfo_screenheight()
root.geometry(f'{screenwidth}x{screenheight}+0+0')

#appearence mode
customtkinter.set_appearance_mode("dark")

#background
pil_image = Image.open("signupbgoverlay.png")

#image resize
pil_image = pil_image.resize((1920, 1080))

#Convert the PIL image to a PhotoImage object
photo_image = ImageTk.PhotoImage(pil_image)


# Create a Label widget to display the image
label = tk.Label(root, image=photo_image)
label.pack()

#Sign Up
label1 = CTkLabel(master=root, text="Sign Up", font=("Be Vietnam", 40,"bold"), text_color="#000000", fg_color="#EEF52F")
label1.place(x=160, y=250, w=190, h=82)

#green frame
frame=customtkinter.CTkFrame(master=root, fg_color="#00FF29", bg_color="#eef52f", corner_radius=20, border_color="#000000", border_width=2 )
frame.place(x =150,y = 310, w=680, h=310)

#Security Questions
label1 = CTkLabel(master=root, text="Security Questions", font=("Be Vietnam", 18,"bold"), text_color="#000000",bg_color="#00FF29")
label1.place(x=160, y=314, w=220, h=50)

#who was ypur childhood hero?
label1 = CTkLabel(master=root, text="Qn. Who was your childhood hero?", font=("Be Vietnam", 15,"bold"), text_color="#000000",bg_color="#00FF29")
label1.place(x=160, y=350, w=330, h=50)

#Answer
entry4=CTkEntry(master=root, placeholder_text="Answer",fg_color="#000000",bg_color="#00FF29")
entry4.place(x=160, y=390, w=650,h=34)

#where did you complete your highschool from?
label1 = CTkLabel(master=root, text="Qn. Where did your complete your highschool from?", font=("Be Vietnam", 15,"bold"), text_color="#000000",bg_color="#00FF29")
label1.place(x=160, y=435, w=500, h=50)

#Answer
entry4=CTkEntry(master=root, placeholder_text="Answer",fg_color="#000000",bg_color="#00FF29")
entry4.place(x=160, y=475, w=650,h=34)

#Back
btn=CTkButton(master=root, text="Back",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#000000",bg_color="#EEF52F", command = loginpage)
btn.place(x=160, y=570, w=132,h=34)
#Next
btn=CTkButton(master=root, text="Next",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#000000",bg_color="#EEF52F", command=inputboard)
btn.place(x=575, y=570, w=132,h=34)




root.mainloop() 