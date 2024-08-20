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
    root.destroy()
    import inputboard  

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

def a_db_edit():

        global win1, a_db_etrr1, a_db_etrr2
        win1=tk.Toplevel()
        win1.title("Edit Price")
        win1.iconbitmap("logo.ico")
        win1.geometry("500x250")
        win1.resizable(0,0)
        win1_main_frame=tk.Frame(win1,bg="#33303C")
        win1_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl1=tk.Label(win1_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl1.place(relx=0.05,rely=0.08)
        a_db_etrr1=CTkEntry(win1_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Nagarkot",placeholder_text_color="#33303c")
        a_db_etrr1.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl2=tk.Label(win1_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl2.place(relx=0.05,rely=0.33)
        a_db_etrr2=CTkEntry(win1_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.7250",placeholder_text_color="#33303C")
        a_db_etrr2.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn1=CTkButton(win1_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win1_cancel)
        a_db_btnn1.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn2=CTkButton(win1_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2, command = update_food1)
        a_db_btnn2.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)
def win4_cancel():
        win1.destroy()

def a_db_edit():

        global win1, a_db_etrr1, a_db_etrr2
        win2=tk.Toplevel()
        win2.title("Edit Price")
        win2.iconbitmap("logo.ico")
        win2.geometry("500x250")
        win2.resizable(0,0)
        win2_main_frame=tk.Frame(win1,bg="#33303C")
        win2_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl1=tk.Label(win2_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl1.place(relx=0.05,rely=0.08)
        a_db_etrr1=CTkEntry(win2_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Nagarkot",placeholder_text_color="#33303c")
        a_db_etrr1.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl2=tk.Label(win2_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl2.place(relx=0.05,rely=0.33)
        a_db_etrr2=CTkEntry(win2_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.7250",placeholder_text_color="#33303C")
        a_db_etrr2.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn1=CTkButton(win2_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win1_cancel)
        a_db_btnn1.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn2=CTkButton(win2_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2, command = update_food1)
        a_db_btnn2.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)
def win4_cancel():
        win1.destroy()



def update_location1():
        if a_db_etrr1.get() == '' or a_db_etrr2.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr2.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('ghumnajaau.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_price =? where rowid = ?", (a_db_etrr1.get(), 1))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Price updated successfully")


def update_location2():
        if a_db_etrr1.get() == '' or a_db_etrr2.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr2.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('ghumnajaau.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_price =? where rowid = ?", (a_db_etrr1.get(), 1))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Price updated successfully")



def update_location3():
        if a_db_etrr1.get() == '' or a_db_etrr2.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr2.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('ghumnajaau.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_price =? where rowid = ?", (a_db_etrr1.get(), 1))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Price updated successfully")

def update_location4():
        if a_db_etrr1.get() == '' or a_db_etrr2.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr2.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('ghumnajaau.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_price =? where rowid = ?", (a_db_etrr1.get(), 1))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Price updated successfully")

def update_location5():
        if a_db_etrr1.get() == '' or a_db_etrr2.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr2.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('ghumnajaau.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_price =? where rowid = ?", (a_db_etrr1.get(), 1))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Price updated successfully")




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