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

name_label=customtkinter.CTkLabel(app,font=font1,text='ID:',text_color="#fff",bg_color="#161C25")
name_label.place(x=20,y=20)

name_entry=customtkinter.CTkEntry(app,font=font1,text_color="#000",fg_color="#fff",border_color='#0C9295',border_width=2,width=180)
name_entry.place(x=100,y=20)

phoneno_label = customtkinter.CTkLabel(app,font=font1,text='Name:', text_color='#000',fg_color='#fff',bg_color='#161C25')
phoneno_label.place(x=20, y=80)

phoneno_entry=customtkinter.CTkEntry(app,font=font1,text_color="#000",fg_color="#fff",border_color='#0C9295',border_width=2,width=180)
phoneno_entry.place(x=100,y=80)

_label = customtkinter.CTkLabel(app,font=font1,text='Name:', text_color='#000',fg_color='#fff',bg_color='#161C25')
name_label.place(x=20, y=80)

bookingdate_label=()


app.mainloop()