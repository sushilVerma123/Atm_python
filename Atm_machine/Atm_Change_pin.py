from tkinter import*
from PIL import Image,ImageTk
import tkinter.messagebox as msg
import datetime
root=Tk()
root.geometry("1600x1000")
root.title("ATM Machine")

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

OTP_input=IntVar()
new_pin=IntVar()
Card_number=IntVar()


def send_otp():
    from email.message import EmailMessage
    import smtplib
    import ssl
    import random
    
    try:
        otp=random.randint(1000,99999)

        email_sender="devil1392001@gmail.com"
        email_pass="iziwccaoqigbsbnn"

        email_rev="select Email from atm_card where Card_number=%s"
        t=(Card_number.get())
        mysql.execute(email_rev,t)
        email_receiver=mysql.fetchall()[0][0]
        subject="OTP"
        messages="Your OTP is {} for changing the pin ".format(otp)

        em=EmailMessage()
        em['From']=email_sender
        em['To']=email_receiver
        em['subject']=subject
        em.set_content(messages)

        context=ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context)as smtp:
            smtp.login(email_sender,email_pass)
            smtp.sendmail(email_sender,email_receiver,em.as_string())
            otp_enter(otp)
            msg.showinfo("successfully","OTP SEND SUCCESSFULLY")
    except:
        msg.showerror("error"," Invalid Card Number ")

def otp_enter(otp):
    card_num=Card_number.get()
    data="select card_number from otp_recoder"
    mysql.execute(data)
    data_tuple=mysql.fetchall()
    a=False
    for i in data_tuple:
        if(card_num == i[0]):
            a=True
            break
    if(a==False):
        now=datetime.datetime.now()
        otp_enter_database="INSERT into otp_recoder(card_number,otp,date_time) values(%s,%s,%s)"
        t=(card_num,otp,now)
        mysql.execute(otp_enter_database,t)
        conn.commit()
    else:
        otp_update='update otp_recoder set otp=%s where card_number=%s'
        t=(otp,Card_number.get())
        mysql.execute(otp_update,t)
        conn.commit()

def Change_pin():
    otp_fetch='select otp from otp_recoder where card_number=%s'
    t=(Card_number.get())
    mysql.execute(otp_fetch,t)
    otp_data=mysql.fetchall()[0][0]
    if(OTP_input.get()==otp_data):
        inn='update atm_card set Pin_number=%s where Card_number=%s'
        t=(new_pin.get(),Card_number.get())
        mysql.execute(inn,t)
        conn.commit()
    else:
        msg.showerror("Error","something worng")

Label(root,text=" Change Pin",font="Arial 25 bold",borderwidth=49,relief="groove",justify="center",background="#208ff7",width=40).place(x=300,y=50)
Button(root,text="<<",command=back,bg="#208ff7").place(x=0,y=0)


Label(root,text=" Enter Your Card Number :",font='comicsansms 20 bold',borderwidth=20,relief="ridge" ,justify="center",width=20).place(x=300,y=250)
Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="ridge" ,justify="center",width=20,textvariable=Card_number).place(x=770,y=250)

Button(root,text="Send OTP",font='comicsansms 10 bold',borderwidth=10,relief="ridge" ,justify="center",width=20,command=send_otp).place(x=650,y=350)

Label(root,text="Enter Your OTP :",font='comicsansms 20 bold',borderwidth=20,relief="ridge" ,justify="center",width=20).place(x=300,y=450)
Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="ridge" ,justify="center",width=20,textvariable=OTP_input).place(x=770,y=450)

Label(root,text=" Enter your new Pin :",font='comicsansms 20 bold',borderwidth=20,relief="groove" ,justify="center",width=20).place(x=300,y=550)
Entry(root,show="*",font='comicsansms 30 bold',borderwidth=10,relief="ridge" ,justify="center",width=20,textvariable=new_pin).place(x=770,y=550)


Button(root,text=" Submit ",borderwidth=10,relief="ridge" ,justify="center", width=20,font='comicsansms 15 bold',command=Change_pin,activebackground = "green", activeforeground = "blue").place(x=600,y=650)

root.mainloop()