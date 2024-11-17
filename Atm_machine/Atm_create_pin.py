from tkinter import*
import tkinter.messagebox as msg
root=Tk()
root.geometry("1600x1000")
root.title("Create_pin")

from PIL import Image,ImageTk
import validate_email as ve

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

name=StringVar()
Email=StringVar()
Pin=IntVar()
card_num=IntVar()

def create_pin():
    try:
        if(name.get() and Pin.get() and card_num.get() and len(str(card_num.get()))==16 and len(str(Pin.get()))==4 and ve.validate_email(Email.get())):
            inn="INSERT into atm_card(Name,Email,Card_number,Pin_number) values(%s,%s,%s,%s)"
            t=(name.get(),Email.get(),card_num.get(),Pin.get())
            mysql.execute(inn,t)
            conn.commit()
            # my1.config(text="******** Pin is created ********")
            msg.showinfo("Successfully","**** Pin is created *****")
            empty()
        else:
            # my2.config(text="******* Please Fill valid things *******")
            msg.showerror("error","please Fill valid things ")
            empty()
    except:
        # my2.config(text="******* Please Enter valid things******* ")
        msg.showerror("error","please Fill valid things ")
        empty()


def empty():
    name.set("")
    card_num.set(0)
    Pin.set(0)
    Email.set("")

def back():
    root.destroy()
    import Atm_front_page

Label(root,text="  Create Pin  ",font="Arial 25 bold",borderwidth=49,relief="groove" ,justify="center",width=40,bg="#208ff7").place(x=300,y=50)

Button(root,text="<<",command=back,bg="#208ff7").place(x=0,y=0)



Label(root,text="Enter your Card_Number :",font='comicsansms 20 bold',borderwidth=20,relief="ridge" ,justify="center",width=20).place(x=300,y=250)
Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="ridge" ,justify="center",width=20,textvariable=card_num).place(x=770,y=250)



Label(root,text=" Enter your Name :",font='comicsansms 20 bold',borderwidth=20,relief="ridge" ,justify="center",width=20).place(x=300,y=350)
Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="ridge" ,justify="center",width=20,textvariable=name).place(x=770,y=350)



Label(root,text=" Enter your Email:",font='comicsansms 20 bold',borderwidth=20,relief="ridge" ,justify="center",width=20).place(x=300,y=450)
Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="ridge" ,justify="center",width=20,textvariable=Email).place(x=770,y=450)



Label(root,text=" Enter your pin :",font='comicsansms 20 bold',borderwidth=20,relief="groove" ,justify="center",width=20).place(x=300,y=550)
Entry(root,show="*",font='comicsansms 30 bold',borderwidth=10,relief="ridge" ,justify="center",width=20,textvariable=Pin).place(x=770,y=550)


Button(root,text=" Submit ",borderwidth=10,relief="ridge" ,justify="center", width=20,font='comicsansms 15 bold',command=create_pin,activebackground = "green", activeforeground = "blue").place(x=600,y=650)

# my1=Label(root,text="",fg="green",font=20)
# my1.place(x=550,y=750)

# my2=Label(root,text="",fg="red",font=20)
# my2.place(x=550,y=750)

root.mainloop()