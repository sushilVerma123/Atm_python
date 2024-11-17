from tkinter import*
import tkinter.messagebox as msg
from PIL import Image,ImageTk
root=Tk()
root.geometry("600x500")
root.title("Admin_login ")

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


ID=StringVar()
password=IntVar()

def Admin_login():
    num="select * from admin_login"
    mysql.execute(num)
    numnote=mysql.fetchall()[0]
    if(numnote[0]==ID.get() and password.get()==numnote[1]):
        root.destroy()
        import Admin_access
    else:
        msg.showerror("Error","Please enter valid ID and password")
    conn.commit()

def back():
    root.destroy()
    import Atm_front_page

Button(root,text="<<",command=back,bg="#208ff7").place(x=0,y=0)

Label(root,text="Admin ID:",font='comicsansms 10 bold',borderwidth=15,relief="ridge" ,justify="center",width=10).place(x=50,y=150)
Entry(root,font='comicsansms 20 bold',borderwidth=10,relief="ridge" ,justify="center",width=20,textvariable=ID).place(x=200,y=150)

Label(root,text="Password:",font='comicsansms 10 bold',borderwidth=15,relief="ridge" ,justify="center",width=10).place(x=50,y=250)
Entry(root,font='comicsansms 20 bold',borderwidth=10,relief="ridge" ,justify="center",width=20,textvariable=password,show='*').place(x=200,y=250)


Button(root,text=" Login ",borderwidth=10,relief="ridge" ,justify="center", width=10,font='comicsansms 15 bold',command=Admin_login,activebackground = "green", activeforeground = "blue").place(x=300,y=350)
root.mainloop()