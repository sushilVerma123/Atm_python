from tkinter import*
import tkinter.messagebox as msg
from PIL import Image,ImageTk
root=Tk()
root.geometry("1600x1000")
root.title("Admin_access")

image1=Image.open('C:\\Users\\Dell\\OneDrive\\Pictures\\Saved Pictures\\17520.jpg')
Photo=ImageTk.PhotoImage(image1)
label1=Label(root,image=Photo)
label1.pack()

def Deposit():
    pass
def Change_Pin():
    pass


Label(root,text="Admin",font="Arial 25 bold",borderwidth=49,relief="groove",justify="center",background="#208ff7",width=40).place(x=300,y=50)

button_create=Button(root,text="Deposit",font='comicsansms 19 bold',borderwidth=10,relief="ridge" ,justify="center",width=25,border="10",command=Deposit).place(x=250,y=300)

button_withdraw=Button(root,text="Change_pin",font='comicsansms 19 bold',borderwidth=10,relief="ridge" ,justify="center",width=25,command=Change_Pin).place(x=900,y=300)

root.mainloop()