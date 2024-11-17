from tkinter import*
import tkinter.messagebox as msg
from PIL import Image,ImageTk
root=Tk()
root.geometry("1600x1000")
root.title("Withdraw")

# setup the connection with database
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


Amount=IntVar()
pin=IntVar()
card_num=IntVar()

def check_card():
    try:
        data="select Card_number from atm_card"
        mysql.execute(data)
        data_tuple=mysql.fetchall()
        a=False
        card=card_num.get()
        if(len(str(card))==16):
            for i in data_tuple:
                if(card == i[0]):
                    a=True
                    break
            if(a==False):
                root.destroy()
                import Atm_create_pin
            else:
                withdraw()
        else:
            msg.showerror("Error","Please enter valid Card number")
            card_num.set(0)
    except:
        msg.showerror("Error","Please enter valid things")
        card_num.set(0)

def withdraw():
    try:
        user_amount=Amount.get()
        user_pin=pin.get()
        pin_d="select Pin_number from atm_card where Card_number=%s"
        t=(card_num.get())
        mysql.execute(pin_d,t)
        pin1=mysql.fetchall()[0][0]
        if(user_pin==pin1):
           pin_right(user_amount)
        else:
            # my1.config(text="******** Your pin is not valid ********")
            msg.showwarning("Pin"," Your pin is not valid")
    except:
        # my1.config(text="****** please enter valid number ******")
        msg.showerror("Error","Please enter valid number")



def pin_right(user_amount):
    total="Select Sum(Type_Note*Number_Note) From note_details "
    mysql.execute(total)
    total_amount=mysql.fetchall()[0][0]
    note=[2000,500,200,100]

    num="select Amount from atm_card where Card_number=%s"
    t=(card_num.get())
    mysql.execute(num,t)
    Addaccount=mysql.fetchall()[0][0]

    if(user_amount>total_amount or user_amount>Addaccount):
        p="Atm does not have that amount"

    elif(user_amount<=20000 and user_amount%100==0):
        amount=user_amount
        p=[] 
        numnote=[] 
        numNote="select Number_Note from note_details ORDER BY Type_Note DESC"
        mysql.execute(numNote)
        num_Note=mysql.fetchall()
        for i in num_Note:
            numnote.append(i[0])  
        i=0
        while(user_amount!=0 and i<4):
            p.append(user_amount//note[i]) 
            if(p[i]>numnote[i]):
                p[i]=numnote[i]
            user_amount=user_amount-p[i]*note[i]
            i=i+1
        if(user_amount!=0):
            p="Atm does not provid this amount"
    else:
        p= "Atm does not provid this amount"

    if(type(p)!=str):
        update_Atm_rupees(p,numnote,note)
        tansaction_detail(amount)
        update_atm_cade(amount,Addaccount)
    display(p,note)

# update in Note_detail table
def update_Atm_rupees(p,numnote,note):
    for i in range(len(p)):
        new_numNote='update note_details set Number_Note=%s where Type_note=%s'
        x=numnote[i]-p[i]
        y=note[i]
        t=(x,y)
        mysql.execute(new_numNote,t)
        conn.commit()

#update in atm_cade table 
def update_atm_cade(amount,Addaccount):
    new_numNote='update atm_card set Amount=%s where Card_number=%s'
    x=Addaccount-amount
    t=(x,card_num.get())
    mysql.execute(new_numNote,t)
    conn.commit()

#display the withdrow notes

def display(p,note):
    if(type(p)==str):
        # my1.config(text=p)
        msg.showinfo("Information",p)
    else:
        # reslut=""
        # for i in range(len(p)):
        #     if(p[i]==0):
        #         continue
        #     s=f'\n ***** {p[i]} note for {note[i]} ****'
        #     reslut+=s
        # my2.config(text=reslut) 
        b=zip(note,p)
        e=Label(my2,width=20,text="Notes",borderwidth=2, relief='ridge',anchor='w',bg='yellow',font=20)
        e.grid(row=0,column=0)
        e=Label(my2,width=20,text='Number_of_Note',borderwidth=2, relief='ridge',anchor='w',bg='yellow',font=20)
        e.grid(row=0,column=1)
        i=1
        for k in b: 
            for j in range(len(k)):
                e = Label(my2,width=20, text=k[j],borderwidth=2,relief='ridge', anchor="w",font=20) 
                e.grid(row=i, column=j) 
            i=i+1 


#update the transaction table
def tansaction_detail(user_amount):
    now=datetime.datetime.now()
    inn="INSERT into transaction(Card_number,user_amount,Date_time) values(%s,%s,%s)"
    t=(card_num.get(),user_amount,now)
    mysql.execute(inn,t)
    conn.commit()




# go back to front page
def back():
    root.destroy()
    import Atm_front_page
Button(root,text="<<",command=back,bg="#208ff7").place(x=0,y=0)
Label(root,text="  Withdraw_Money  ",font="Arial 25 bold",borderwidth=49,relief="groove",justify="center",width=40,bg="#208ff7").place(x=300,y=50)



Label(root,text="Enter the Card_Number :",font='comicsansms 20 bold',borderwidth=20,relief="ridge" ,justify="center",width=20).place(x=300,y=250)
Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="ridge" ,justify="center",width=20,textvariable=card_num).place(x=770,y=250)


Label(root,text=" Enter the Amount :",font='comicsansms 20 bold',borderwidth=20,relief="ridge" ,justify="center",width=20).place(x=300,y=350)
Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="groove" ,justify="center",width=20,textvariable=Amount).place(x=770,y=350)



Label(root,text="Enter the pin :",font='comicsansms 20 bold',borderwidth=20,relief="ridge",width=20,justify="center").place(x=300,y=450)
Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="groove" ,justify="center",width=20,show="*",textvariable=pin).place(x=770,y=450)


Button(root,text=" Withdraw ",borderwidth=10,relief="ridge" ,justify="center", width=20,font='comicsansms 15 bold',command=check_card).place(x=600,y=550)

# my1=Label(root,text="",fg="red",font=20)
# my1.place(x=500,y=650)

my2=Label(root,text="",fg="green",font=20)
my2.place(x=550,y=630)

root.mainloop()