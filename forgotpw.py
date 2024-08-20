from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import customtkinter

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

def login():
    root.destroy()
    import login

def userlogin():
    root.destroy()  
    import userloginpage  
    



pil_image = Image.open("forgotpwbg.png")

#image resize
pil_image = pil_image.resize((1920, 1080))

#Convert the PIL image to a PhotoImage object
photo_image = ImageTk.PhotoImage(pil_image)


# Create a Label widget to display the image
label = tk.Label(root, image=photo_image)
label.pack()


#frame
frame=customtkinter.CTkFrame(master=root, fg_color="#C9CD00",corner_radius=0)
frame.place(x = 610,y = 270, w=400, h=550)


# show password function
def showPassword():
    if newPasswordEntry.cget("show") == "*":
        newPasswordEntry.config(show="")
    else:
        newPasswordEntry.config(show="*")


# show password function2
def showPassword2():
    if confirmPasswordEntry.cget("show") == "*":
        confirmPasswordEntry.config(show="")
    else:
        confirmPasswordEntry.config(show="*")



# password reset function
def resetPassword():
    username = usernameEntry.get()
    newPassword = newPasswordEntry.get()
    confirmPassword = confirmPasswordEntry.get()
    if usernameEntry != "" and newPassword != "" and confirmPassword != "":
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        if newPassword == confirmPassword:
            selectusername = """SELECT * FROM admins WHERE username=?"""
            cursor.execute(selectusername, [(username)])
            if cursor.fetchall():
                passwordUpdate = """UPDATE admins SET password=? WHERE username=?"""
                cursor.execute(passwordUpdate, [(newPassword), (username)])
                messagebox.showinfo(
                    title="info", message="Password succcessfully updated."
                )
                usernameEntry.delete(0, END)
                newPasswordEntry.delete(0, END)
                confirmPasswordEntry.delete(0, END)
            else:
                messagebox.showerror(title="error", message="invalid credentials")
                usernameEntry.delete(0, END)
                newPasswordEntry.delete(0, END)
                confirmPasswordEntry.delete(0, END)
        else:
            messagebox.showerror(title="error", message="Passwords do not match")
            usernameEntry.delete(0, END)
            newPasswordEntry.delete(0, END)
            confirmPasswordEntry.delete(0, END)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror(title="error", message="invalid credentials")
        usernameEntry.delete(0, END)
        newPasswordEntry.delete(0, END)
        confirmPasswordEntry.delete(0, END)


# LABEL

# login
resetPasswordLabel = customtkinter.CTkLabel(master= frame, text="RESET PASSWORD", font=("ariel", 20, "bold"))
resetPasswordLabel.place(x=40, y=50)

# username
usernamelabel =customtkinter.CTkLabel(master=frame, text="Username", font=("ariel", 18))
usernamelabel.place(x=30, y=105)


# create password
newPasswordLabel = customtkinter.CTkLabel(master=frame, text="New Password", font=("ariel", 18))
newPasswordLabel.place(x=30, y=170)

# confirm password
confirmPasswordLabel = customtkinter.CTkLabel(master=frame, text="Confirm Password", font=("ariel", 18))
confirmPasswordLabel.place(x=30, y=255)

# ENTRY
# username
usernameEntry = Entry(root, width=24, font=("ariel", 15), relief=SUNKEN)
usernameEntry.place(x=800, y=500)

# create password
newPasswordEntry = Entry(root, width=24, font=("ariel", 15), show="*", relief=SUNKEN)
newPasswordEntry.place(x=800, y=580)

# confirm password
confirmPasswordEntry = Entry(root, width=24, font=("ariel", 15), show="*", relief=SUNKEN)
confirmPasswordEntry.place(x=800, y=690)


# BUTTONS
# back button
backBtn = customtkinter.CTkButton(master=root,text="BACK",hover_color="#99B104",command=userlogin)
backBtn.place(x=780, y=640)

# reset button
resetBtn = customtkinter.CTkButton(master=root,text="RESET",command=resetPassword,hover_color="#99B104")
resetBtn.place(x=620, y=640)


# CHECKBUTTON
# show password
var = IntVar()
checkbtn1 = Checkbutton(root,text="Show Password",variable=var,command=showPassword,bg="#2b2b2b",font=("ariel", 10),fg="white",)
checkbtn1.place(x=800, y=620)

var2 = IntVar()
checkbtn2 = Checkbutton(root,text="Show Password",variable=var2,command=showPassword2,bg="#2b2b2b",font=("ariel", 10),fg="white")
checkbtn2.place(x=800, y=730)

root.mainloop()