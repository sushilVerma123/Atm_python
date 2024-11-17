from tkinter import*
import tkinter.messagebox as msg
from PIL import Image,ImageTk
root=Tk()
root.geometry("1600x1000")
root.title("Amount Deposit")

import pymysql as my
import datetime
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
notes100=IntVar()
notes200=IntVar()
notes500=IntVar()
notes2000=IntVar()
Pin=IntVar()
def check():
    try:
        card=card_num.get()
        data="select Card_number from atm_card"
        mysql.execute(data)
        data_tuple=mysql.fetchall()
        a=False
        if(len(str(card))==16):
            for i in data_tuple:
                if(card == i[0]):
                    a=True
                    break
            if(a==False):
                root.destroy()
                import Atm_create_pin
            else:
                Pin_rigth()
        else:
            msg.showerror("Error","Please enter valid Card number")
            card_num.set(0)
    except:
        # my1.config(text=" ******** please enter valid number *******")
        msg.showerror("error","please enter valid number")

# check the pin is rigth
def Pin_rigth():
    try:
        user_pin=Pin.get()
        pin_d="select Pin_number from atm_card where Card_number=%s"
        t=(card_num.get())
        mysql.execute(pin_d,t)
        pin1=mysql.fetchall()[0][0]
        if(user_pin==pin1):
            card=card_num.get()
            deposit(card)
        else:
            # my1.config(text="******** Your pin is not valid ********")
            msg.showwarning("Pin"," Your pin is not valid")
    except:
        # my1.config(text="****** please enter valid number ******")
        msg.showerror("Error","Please enter valid number")
# Add amount in atm_card table        
def deposit(card):
    numnoteuser=[notes2000.get(),notes500.get(),notes200.get(),notes100.get()]
    notes=[2000,500,200,100]
    sum=0
    for i in range(0,4):
        if(numnoteuser[i]==0):
            continue
        sum+=numnoteuser[i]*notes[i]
    num="select Amount from atm_card where Card_number=%s"
    t=(card)
    mysql.execute(num,t)
    Addaccount=mysql.fetchall()[0][0]
    new_numNote='update atm_card set Amount=%s where Card_number=%s'
    x=Addaccount+sum
    t=(x,card)
    mysql.execute(new_numNote,t)
    conn.commit()
    depoit_Details(card,sum)
    depoit_note_detail(numnoteuser,notes)
    empty()

# add amount in deposit table
def depoit_Details(card,sum):
    now=datetime.datetime.now()
    inn="INSERT into deposit(Card_number,Amount,Date_time) values(%s,%s,%s)"
    t=(card,sum,now)
    mysql.execute(inn,t)
    conn.commit()

# add amount in note_detail table
def depoit_note_detail(numnoteuser,notes):
    for i in range(0,4):
            num="select Number_Note from note_details where Type_Note=%s"
            t=(notes[i])
            mysql.execute(num,t)
            numnote=mysql.fetchall()[0][0]

            new_numNote='update note_details set Number_Note=%s where Type_note=%s'
            x=numnote+numnoteuser[i]
            y=notes[i]
            t=(x,y)
            mysql.execute(new_numNote,t)
            conn.commit()
    # my1.config(text="***** successfully deposit *****")
    msg.showinfo("successfully","successfully deposit")

def empty():
    card_num.set(0)
    notes100.set(0)
    notes200.set(0)
    notes500.set(0)
    notes2000.set(0)
    Pin.set(0)


Label(root,text="Amount deposit",font="Arial 25 bold",borderwidth=49,relief="groove",justify="center",background="#208ff7",width=40).place(x=300,y=10)

Button(root,text="<<",command=back,bg="#208ff7").place(x=0,y=0)

Label(root,text="Enter the Card_Number :",font='comicsansms 20 bold',borderwidth=20,relief="ridge" ,justify="center",width=20).place(x=300,y=170)
Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="ridge" ,justify="center",width=20,textvariable=card_num).place(x=770,y=170)


Label(root,text=" 100Rs notes :",font='comicsansms 20 bold',borderwidth=20,relief="ridge" ,justify="center",width=15).place(x=400,y=260)
Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="ridge" ,justify="center",width=10,textvariable=notes100).place(x=800,y=260)


Label(root,text="200Rs notes :",font='comicsansms 20 bold',borderwidth=20,relief="ridge" ,justify="center",width=15).place(x=400,y=350)
Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="ridge" ,justify="center",width=10,textvariable=notes200).place(x=800,y=350)


Label(root,text="500Rs notes :",font='comicsansms 20 bold',borderwidth=20,relief="ridge" ,justify="center",width=15).place(x=400,y=440)
Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="ridge" ,justify="center",width=10,textvariable=notes500).place(x=800,y=440)


Label(root,text="2000Rs notes :",font='comicsansms 20 bold',borderwidth=20,relief="ridge",justify="center",width=15).place(x=400,y=530)
Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="ridge" ,justify="center",width=10,textvariable=notes2000).place(x=800,y=530)

Label(root,text=" Pin :",font='comicsansms 20 bold',borderwidth=20,relief="ridge" ,justify="center",width=15).place(x=400,y=620)
Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="ridge" ,justify="center",width=10,show="*",textvariable=Pin).place(x=800,y=620)


Button(root,text=" Deposit ",borderwidth=10,relief="ridge" ,justify="center", width=20,font='comicsansms 15 bold',command=check,activebackground = "green", activeforeground = "blue").place(x=600,y=700)

# my1=Label(root,text="",fg="green",font=20)
# my1.place(x=600,y=750)

root.mainloop()