import tkinter as tk
from tkinter import *
import customtkinter 
from customtkinter import*
import sqlite3
from tkinter import messagebox
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
    import userloginpage 


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

def adm_signup():   #Function to open security page after sigining up
   
    conn = sqlite3.connect('ghumnajaau.db')   #creating database
    c = conn.cursor()  #'cursor()' for executing the queries
    c.execute("""
              CREATE TABLE IF NOT EXISTS admin (
                 first_name TEXT,
                 last_name TEXT,
                 email TEXT,
                 phone_number INT,
                 password TEXT
                 sec_ans1 TEXT,
                 sec_ans2 TEXT
                 
                 
                 
              )
           
              """)
   
    global adm_emails
    c.execute("SELECT email FROM admin")
    adm_emails = c.fetchall()
    a=[]
   
    for email in adm_emails:
    #saving the changes made in the database
     a.append(email[0])
    conn.commit()
    conn.close()
 
    #checking if the entry boxes are filled and entered the valid credentials
    if entry1.get() == '' or entry2.get() == '' or entry3.get() == '' or entry4.get() == '' or entry.get() == '' or entry1.get() == 'firstname' or entry2.get() == 'lastname' or entry3  .get() == 'example@gmail.com':
            messagebox.showerror("Error", "Please fill all the required fields!")
    elif (entry1.get()).isalpha() == False or (entry2.get()).isalpha() == False:
           messagebox.showerror("Error", "Please enter valid first and last names!")    #show error for first and last names
    elif '@gmail.com' not in entry3.get() or len(entry3.get()) <= 10 or ' ' in entry3.get():
            messagebox.showerror("Error", "Please enter a valid email address!")     #show error for email entry
    elif len(entry4.get())!= 10 or entry4.get().isdigit()==False:
            messagebox.showerror("Error", "Please enter valid phone number!")       #show error for phone entry
    elif entry.get() != entry6.get():     #Checking if password is same in password and confirm password entry
            messagebox.showerror("Error", "Passwords do not match!")
    elif len(entry.get()) < 8 :
            messagebox.showerror("Error", "Password should be at least 8 characters long!")
   
    else:
            if entry3.get() in a:
                #show error
                messagebox.showerror("Error", "Email already exists!")
            else:
               messagebox.showinfo("Sucessful sign up!"," Now you need to fill the security questions for future security,incase you forget your password by filling the questions . ")
            #    adm_sign_fr.place_forget()
            #    security_pg_frm()  
               root.destroy()
               import securitypage
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
btn=CTkButton(master=root, text="Next",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#000000",bg_color="#EEF52F",command=adm_signup)
btn.place(x=575, y=570, w=132,h=34)




root.mainloop()