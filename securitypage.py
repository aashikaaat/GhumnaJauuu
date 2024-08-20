import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customtkinter 
from customtkinter import*
from PIL import Image, ImageTk
import sqlite3

root = customtkinter.CTk() #window
root.iconbitmap("logo.ico")
root.title("घुम्न जाऔँ") #page title

def loginpage():
    root.destroy()
    import userloginpage 

def inputboard():
    root.destroy()
    import inputboard    

#window resolution
screenwidth= root.winfo_screenwidth()
screenheight= root.winfo_screenheight()
root.geometry(f'{screenwidth}x{screenheight}+0+0')

#appearence mode
customtkinter.set_appearance_mode("dark")



def security_info():
        '''
        this function is made to show a message when user clicks submit on the security question page
        '''



        #----------------------------DATABASE--------------------------#




        #checking if the entry is filled or not
        if entry1.get() == '' or entry2.get() == '':
            tk.messagebox.showerror("Error", "Please fill all the required fields!")
        elif entry1.get().isdigit() == False:
            tk.messagebox.showerror("Error", "Please enter a number in the first field!")
        else:

           #inserting security answers to the database
            conn = sqlite3.connect("mealmate.db")
            c = conn.cursor()
            
            #updating security questions
            #inserting data into the database
            c.execute('''INSERT INTO user (first_name, last_name, email,phone_number, password, sec_ans1, sec_ans2) 
                         VALUES (?,?,?,?,?,?,?)''',
                         ((entry1.get()).capitalize(),(entry2.get()).capitalize(),entry3.get(),entry.get(),usec_entry1.get(), usec_entry2.get(), usec_entry3.get())
                     )
            conn.commit()
            conn.close()
            usign_sec_qsn_frame.place_forget()  
            userloginpage()       
            tk.messagebox.showinfo("Successful Message ","Security questions Entry Successful !")




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
entry1=CTkEntry(master=root, placeholder_text="Answer",fg_color="#000000",bg_color="#00FF29")
entry1.place(x=160, y=390, w=650,h=34)

#where did you complete your highschool from?
label1 = CTkLabel(master=root, text="Qn. Where did your complete your highschool from?", font=("Be Vietnam", 15,"bold"), text_color="#000000",bg_color="#00FF29")
label1.place(x=160, y=435, w=500, h=50)

#Answer
entry2=CTkEntry(master=root, placeholder_text="Answer",fg_color="#000000",bg_color="#00FF29")
entry2.place(x=160, y=475, w=650,h=34)

#Back
btn=CTkButton(master=root, text="Back",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#000000",bg_color="#EEF52F", command = loginpage)
btn.place(x=160, y=570, w=132,h=34)
#Next
btn=CTkButton(master=root, text="Next",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#000000",bg_color="#EEF52F", command=inputboard)
btn.place(x=575, y=570, w=132,h=34)




root.mainloop() 