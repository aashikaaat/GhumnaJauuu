import tkinter as tk
from tkinter import *
import customtkinter 
from customtkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox

root = customtkinter.CTk() #window
root.iconbitmap("logo.ico")     
root.title("घुम्न जाऔँ") #page title


def logout():
    root.destroy()
    import login

def dash():
    if combobox1.get() == 'Select here.' or combobox2.get() == 'Select here.' or entry1.get() == '' or entry2.get() == '' :
        tk.messagebox.showerror('Error', 'Enter all fields!' )
        
    else:

        root.destroy()
        import nagarkot   
        
# window resolution
screenwidth= root.winfo_screenwidth()
screenheight= root.winfo_screenheight()
root.geometry(f'{screenwidth}x{screenheight}+0+0')

#appearence mode
customtkinter.set_appearance_mode("dark") 

# #insert image
pil_image = Image.open("inputboardbg.png")

# # imageresize
pil_image = pil_image.resize((1920, 1080))


# # Convert the PIL image to a PhotoImage object
photo_image = ImageTk.PhotoImage(pil_image)


# # Create a Label widget to display the image
label = tk.Label(root, image=photo_image)
label.pack()


# Keep a reference to the image to prevent it from being garbage collected
label.image = photo_image



# #insert image
pil_image = Image.open("searchbutton.png")

# # imageresize
pil_image = pil_image.resize((36, 38))


# # Convert the PIL image to a PhotoImage object
photo_image = ImageTk.PhotoImage(pil_image)


# # Create a Label widget to display the image
label = tk.Label(root, image=photo_image)
label.pack()


# Keep a reference to the image to prevent it from being garbage collected
label.image = photo_image

    
#fill in these blanks
label1 = CTkLabel(master=root, text="Fill in the blanks", font=("Be Vietnam", 23), text_color="#000000", fg_color="#bec40a")
label1.place(x=200, y=290, w=270, h=50)

#to complete
label2 = CTkLabel(master=root, text="to complete", font=("Be Vietnam", 27, "bold"), text_color="#000000", fg_color="#bec40a")
label2.place(x=400, y=290, w=190, h=50)


#Your incomplete
label3 = CTkLabel(master=root, text="your incomplete", font=("Be Vietnam", 23), text_color="#000000", fg_color="#bec40a")
label3.place(x=200, y=320, w=270, h=50)

#wishes
label4 = CTkLabel(master=root, text="wishes.", font=("Be Vietnam", 27, "bold"), text_color="#000000", fg_color="#bec40a")
label4.place(x=398, y=325, w=118, h=40)

# your location
label5 = CTkLabel(master=root, text="Your location", font=("Be Vietnam", 18,"bold"), text_color="#000000", fg_color="#bec40a")
label5.place(x=170, y=370, w=270, h=38)

#search box
def search(location):
    value=location.widget.get()
    if value == '':
        combobox3['values']=list
    else:
        data=[]

        for item in list:
            if value.lower() in item.lower():
                data.append(item)
        combobox1['values']=data  

combobox3= CTkComboBox(master=root, values=["Bhaktapur","Kathmandu","Lalitpur"],bg_color="#FFFFFF", fg_color="#FFFFFF", text_color="#000000")
combobox3.set('Search')
combobox3.place(x=300, y=225, w=600, h=50)

combobox3.bind('<KeyRelease>',search)


#location entry box
combobox1= CTkComboBox(master=root, values=["Bhaktapur","Kathmandu","Lalitpur"],bg_color="#bec40a")
combobox1.set('Select here.')
combobox1.place(x=220, y=400, w=400, h=30)

# time you have allocated
label6 = CTkLabel(master=root, text="Travel time", font=("Be Vietnam", 18,"bold"), text_color="#000000", fg_color="#bec40a", bg_color="#000000")
label6.place(x=160, y=440, w=270, h=38)

#atleast 2 hrs
entry1=CTkEntry(master=root, placeholder_text="Atleast 2 hours.",fg_color="#343638",bg_color="#bec40a")
entry1.place(x=220, y=470, w=400,h=30)

#your budget
label7 = CTkLabel(master=root, text="Your Budget", font=("Be Vietnam", 18,"bold"), text_color="#000000", fg_color="#bec40a", bg_color="#000000")
label7.place(x=170, y=510, w=270, h=38)

#atleast 2 hrs
entry2=CTkEntry(master=root, placeholder_text="Atleast 4000 NRS.",fg_color="#343638",bg_color="#bec40a")
entry2.place(x=220, y=540, w=400,h=30)

#mode of transportation
label8 = CTkLabel(master=root, text="Mode of transportation", font=("Be Vietnam", 18,"bold"), text_color="#000000", fg_color="#bec40a", bg_color="#000000")
label8.place(x=215, y=580, w=270, h=38)

#transport entry box
combobox2= CTkComboBox(master=root, values=["Pathao Taxi"],bg_color="#bec40a")
combobox2.set('Select here.')
combobox2.place(x=220, y=610, w=400, h=30)


#submit

btn=CTkButton(master=root, text="Submit",font=("Archivo",25,"bold"),text_color="#FFFFFF",fg_color="#000000",bg_color="#bec40a",hover_color="#3BC100",command=dash)
btn.place(x=600, y=620, w=150,h=50)


btn=CTkButton(master=root, text="Log out",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#000000",bg_color="#bec40a",hover_color="#3BC100",command=logout)
btn.place(x=150, y=645, w=180,h=40)
root.mainloop()