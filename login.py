import tkinter as tk
from tkinter import *
import customtkinter 
from customtkinter import*
from PIL import Image, ImageTk



root = customtkinter.CTk() #window
root.iconbitmap("logo.ico")     
root.title("घुम्न जाऔँ") #page title
    

# window resolution
screenwidth= root.winfo_screenwidth()
screenheight= root.winfo_screenheight()
root.geometry(f'{screenwidth}x{screenheight}+0+0')


#appearence mode
customtkinter.set_appearance_mode("dark") 

def adminlogin():
    root.destroy()
    import adminlogin

def userlogin():
    root.destroy()
    import userloginpage   
    

# #insert image
pil_image = Image.open("loginpagebg.jpg")

# # imageresize
pil_image = pil_image.resize((1920, 1080))


# # Convert the PIL image to a PhotoImage object
photo_image = ImageTk.PhotoImage(pil_image)


# # Create a Label widget to display the image
label = tk.Label(root, image=photo_image)
label.pack()


# Keep a reference to the image to prevent it from being garbage collected
label.image = photo_image

#login frame
frame=customtkinter.CTkFrame(master=root, fg_color="#FCD419", bg_color="#000000", corner_radius=32 )
frame.place(x = 1050,y = 20, w=500, h=350)

#welcome to 
label1 = CTkLabel(master=root, text="Welcome to", font=("Archivo", 20), text_color="#000000", fg_color="#FCD419")
label1.place(x=1100, y=20, w=150, h=60)

# ghumna jaau
label2 = CTkLabel(master=root, text="Ghumna Jaau", font=("Arial Black", 20), text_color="#000000", fg_color="#FCD419")
label2.place(x=1220, y=20, w=200, h=60)

#Your
label3 = CTkLabel(master=root, text="Your", font=("Be Vietnam", 50), text_color="#FFFFFF", fg_color="#000000")
label3.place(x=400, y=35, w=134, h=94)

#Time
label4 = CTkLabel(master=root, text="Time", font=("Be Vietnam", 50,"bold"), text_color="#FFFFFF", fg_color="#000000")
label4.place(x=520, y=35, w=138, h=94)

#Our
label5 = CTkLabel(master=root, text="Our", font=("Be Vietnam", 50), text_color="#FFFFFF", fg_color="#000000")
label5.place(x=400, y=92, w=134, h=94)

#Plan.
label6 = CTkLabel(master=root, text="Plan.", font=("Be Vietnam", 50,"bold"), text_color="#FFFFFF", fg_color="#000000")
label6.place(x=520, y=92, w=134, h=94)


#admin login
btn=CTkButton(master=root, text="Admin Login",font=("Calibri",28, "bold"),text_color="#FFFFFF",fg_color="#000000",bg_color="#FCD419",hover_color="#008000",command=adminlogin)
btn.place(x=1170, y=85, w=220,h=70)

#user login
btn=CTkButton(master=root, text="User Login",font=("Calibri",28, "bold"),text_color="#FFFFFF",fg_color="#000000",bg_color="#FCD419", hover_color="#008000",command=userlogin)
btn.place(x=1170, y=180, w=220,h=70)



root.mainloop()