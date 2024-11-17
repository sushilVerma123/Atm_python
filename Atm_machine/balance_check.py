from tkinter import*
import tkinter.messagebox as msg
from PIL import Image,ImageTk
root=Tk()
root.geometry("1600x1000")
root.title("Balance_check")

import pymysql as my
conn=my.connect(
    host='localhost',
    user='root',
    password='',
    database='atm_machine')
mysql=conn.cursor()

image1=Image.open('C:\\Users\\Dell\\OneDrive\\Pictures\\Saved Pictures\\17520.jpg')
Photo=ImageTk.PhotoImage(image1)
label1=Label(root,image=Photo)
label1.pack()

def back():
    root.destroy()
    import Atm_front_page

card_num=IntVar()

def Balance():
    try:
        if(len(str(card_num.get()))==16):
            pin="select Amount from atm_card where Card_number=%s"
            t=(card_num.get())
            mysql.execute(pin,t)
            amount=mysql.fetchall()[0][0]
            my1.config(text=f'Amount of your account: {amount}')
        else:
            msg.showerror("Error","Please enter valid Card Number")
            card_num.set(0)
    except:
        # my1.config(text="******* This Card number not in data base *******")
        msg.showwarning("Warning","This Card number not in data base")
        card_num.set(0)


Label(root,text="Balance",font="Arial 25 bold",borderwidth=49,relief="groove",justify="center",background="#208ff7",width=40).place(x=300,y=50)

Button(root,text="<<",command=back,bg="#208ff7").place(x=0,y=0)

Label(root,text="Enter the Card_Number :",font='comicsansms 20 bold',borderwidth=20,relief="ridge" ,justify="center",width=20).place(x=300,y=250)
Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="ridge" ,justify="center",width=20,textvariable=card_num).place(x=770,y=250)

Button(root,text=" Submit ",borderwidth=10,relief="ridge" ,justify="center", width=20,font='comicsansms 15 bold',command=Balance,activebackground = "green", activeforeground = "blue").place(x=600,y=350)

my1=Label(root,text="",fg="green",font=20)
my1.place(x=600,y=450)

root.mainloop()