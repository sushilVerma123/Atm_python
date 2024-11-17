from tkinter import*
import tkinter.messagebox as msg
from PIL import Image,ImageTk
root=Tk()

root.geometry("1600x1000")
root.title("History")

v=Scrollbar(root,orient="vertical")
v.pack(side = RIGHT, fill = Y)

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
def withdraw_History():
    try:
        if(len(str(card_num.get()))==16):
            pin="select user_amount,Date_time from transaction where Card_number=%s"
            t=(card_num.get())
            mysql.execute(pin,t)
            accounthistory=mysql.fetchall()
    
            display_History(accounthistory,"withdraw_amount")
        
           
        else:
            msg.showerror("Error","Please enter the valid number")
    except:
        # my1.config(text="***** Please enter the valid number *****")
        msg.showerror("Error","Please enter the valid number")

def depoist_History():
    try:
        if(len(str(card_num.get()))==16):
            pin="select Amount,Date_time from deposit where Card_number=%s"
            t=(card_num.get())
            mysql.execute(pin,t)
            accounthistory=mysql.fetchall()

            display_History(accounthistory,"deposit_amount")
        else:
            msg.showerror("Error","Please enter the valid number")
    except:
        # my1.config(text="***** Please enter the valid number *****")
        msg.showerror("Error","Please enter the valid number")



def display_History(acc,type):
    e=Label(my1,width=20,text=type,borderwidth=2, relief='ridge',anchor='w',bg='yellow',font=20)
    e.grid(row=0,column=0)
    e=Label(my1,width=20,text='Date_time',borderwidth=2, relief='ridge',anchor='w',bg='yellow',font=20)
    e.grid(row=0,column=1)
    i=1
    for k in acc: 
        for j in range(len(k)):
            e = Label(my1,width=20, text=k[j],borderwidth=2,relief='ridge', anchor="w",font=20) 
            e.grid(row=i, column=j) 
        i=i+1

Label(root,text="Account History",font="Arial 25 bold",borderwidth=49,relief="groove",justify="center",background="#208ff7",width=40).place(x=300,y=50)

Button(root,text="<<",command=back,bg="#208ff7").place(x=0,y=0)

Label(root,text="Enter the Card_Number :",font='comicsansms 20 bold',borderwidth=20,relief="ridge" ,justify="center",width=20).place(x=300,y=250)
Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="ridge" ,justify="center",width=20,textvariable=card_num).place(x=770,y=250)

Button(root,text=" Withdraw History ",borderwidth=10,relief="ridge" ,justify="center", width=20,font='comicsansms 15 bold',command=withdraw_History,activebackground = "green", activeforeground = "blue").place(x=400,y=350)

Button(root,text=" Deposit History ",borderwidth=10,relief="ridge" ,justify="center", width=20,font='comicsansms 15 bold',command=depoist_History,activebackground = "green", activeforeground = "blue").place(x=800,y=350)

my1=Label(root,fg="green",font=20)
my1.place(x=500,y=450)
root.mainloop()