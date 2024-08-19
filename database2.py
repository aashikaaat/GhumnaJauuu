import tkinter as tk
from tkinter import *
import customtkinter 
import customtkinter as CTK
from customtkinter import*
from tkinter import messagebox

app=customtkinter.CTk()

app = customtkinter.CTk() #window
app.iconbitmap("logo.ico")     
app.title("घुम्न जाऔँ") #page title


# window resolution
screenwidth= app.winfo_screenwidth()
screenheight= app.winfo_screenheight()
app.geometry(f'{screenwidth}x{screenheight}+0+0')

font1=('Arial',20,'bold')
font2=('Arial',12,'bold')

id_label=customtkinter.CTkLabel(app,font=font1,text='ID:',text_color="#fff",bg_color="#000000")
id_label.place(x=20,y=20)

id_entry=customtkinter.CTkEntry(app,font=font1,text_color="#000",bg_color="#000000",fg_color="#fff",width=180)
id_entry.place(x=100,y=20)


app.mainloop()