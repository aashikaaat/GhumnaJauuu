import tkinter as tk
from tkinter import *
import customtkinter 
from customtkinter import*
import sqlite3
from PIL import Image, ImageTk



root = customtkinter.CTk() #window
root.iconbitmap("logo.ico")     
root.title("घुम्न जाऔँ") #page title

def signup():
    root.destroy()
    import signuppage

def login():
    root.destroy()
    import login    

def input():

    conn = sqlite3.connect('ghumnajaau.db')
    c = conn.cursor()
    c.execute('SELECT * FROM user WHERE email = ? and password = ?',(entry1.get(), entry2.get()))
    user_data = c.fetchone()
    print(user_data)
    if user_data != None:
        if (entry1.get() and entry2.get()) in user_data :
            tk.messagebox.showinfo('Successful','Login Successful!')

            root.destroy()
            import inputboard 
        else:
            tk.messagebox.showerror ('Error','Invalid credentials! ')
    else:
            tk.messagebox.showerror ('Error','Invalid credentials! ')

def forgotpw():
    root.destroy()
    import forgotpw      
    



# window resolution
screenwidth= root.winfo_screenwidth()
screenheight= root.winfo_screenheight()
root.geometry(f'{screenwidth}x{screenheight}+0+0')

# root.resizable(False, False)
# root.after(1, lambda: root.state("zoomed"))

#appearence mode
customtkinter.set_appearance_mode("dark") 

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
frame.place(x = 950,y = 20, w=700, h=350)

#Login 
label1 = CTkLabel(master=root, text="Log In", font=("Britannic Bold", 35), text_color="#000000", fg_color="#FCD419")
label1.place(x=970, y=50, w=150, h=80)

#welcome to 
label1 = CTkLabel(master=root, text="Welcome to", font=("Archivo", 15), text_color="#000000", fg_color="#FCD419")
label1.place(x=1100, y=20, w=150, h=60)

# ghumna jaau
label2 = CTkLabel(master=root, text="Ghumna Jaau", font=("Arial Black", 15), text_color="#000000", fg_color="#FCD419")
label2.place(x=1205, y=20, w=150, h=60)

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

#email
label7 = CTkLabel(master=root, text="Email:", font=("Archivo", 15), text_color="#000000", fg_color="#FCD419")
label7.place(x=970, y=110, w=100, h=50)
entry1=CTkEntry(master=root, placeholder_text="Enter your email",fg_color="#000000",bg_color="#FCD419")
entry1.place(x=1065, y=118, w=407,h=34)

# password
label7 = CTkLabel(master=root, text="Password:", font=("Archivo", 15), text_color="#000000", fg_color="#FCD419")
label7.place(x=960, y=145, w=150, h=50)
entry2=CTkEntry(master=root, placeholder_text="Enter your password",fg_color="#000000",bg_color="#FCD419",show="*")
entry2.place(x=1065, y=150, w=407,h=34)



def show_password(entry, var):
    if var.get():
        entry.configure(show="")
    else:
        entry.configure(show="*")



show_password_var = tk.IntVar()
show_password_checkbox = CTkCheckBox(frame,text="Show Password",text_color="#FFFFFF", variable=show_password_var, command=lambda: show_password(entry2, show_password_var))
show_password_checkbox.place(x=444, y=132, w=30,h=30)

#login button
btn=CTkButton(master=root, text="Log in",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#000000",bg_color="#FCD419", command=input)
btn.place(x=1350, y=220, w=132,h=34)




#back button
btn=CTkButton(master=root, text="Back",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#000000",bg_color="#FCD419",command=login)
btn.place(x=1000, y=220, w=132,h=34)

# forgot password
btn=CTkButton(master=root, text="Forgot password?",font=("Archivo",13,"underline"),text_color="#000000",fg_color="#FCD419",bg_color="#FCD419", hover_color="#FCD419",command=forgotpw)
btn.place(x=1350, y=250, w=145,h=34)

#new user
label7 = CTkLabel(master=root, text="New user?", font=("Archivo", 15), text_color="#000000", fg_color="#FCD419")
label7.place(x=1200, y=180, w=150, h=50)

# register here
btn=CTkButton(master=root, text="Register here.",font=("Archivo",15,"bold", "underline"),text_color="#000000",fg_color="#FCD419",bg_color="#FCD419", hover_color="#FCD419", command=signup)
btn.place(x=1295, y=181, w=145,h=50)



root.mainloop()