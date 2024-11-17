from tkinter import*
from PIL import Image,ImageTk
root=Tk()
root.geometry("1600x1000")
root.title("ATM Machine")

image1=Image.open('C:\\Users\\Dell\\OneDrive\\Pictures\\Saved Pictures\\17520.jpg')
Photo=ImageTk.PhotoImage(image1)
label1=Label(root,image=Photo)
label1.pack()


def admin():
    root.destroy()
    import Admin_page

yourmember=Menu(root)
m1=Menu(yourmember,tearoff=0)
m1.add_command(label="Client")
m1.add_command(label="Admin",command=admin)
root.config(menu=yourmember)
yourmember.add_cascade(label="Setting",menu=m1)



def display(page):
    root.destroy()
    if(page==1):
        import Atm_create_pin
    elif(page==2):
        import Atm_withdraw_page
    elif(page==3):
        import balance_check
    elif(page==4):
        import History_page
    elif(page==5):
        import Amount_Deposit
    elif(page==6):
        import Help_page
    elif(page==7):
        import Atm_Change_pin


Label(root,text="ATM MACHINE",font="Arial 25 bold",borderwidth=49,relief="groove",justify="center",background="#208ff7",width=40).place(x=300,y=50)


# card=Label(root,text="Enter the Card_Number :",font='comicsansms 20 bold',borderwidth=5,relief="ridge" ,justify="center").place(x=300,y=300)
# Entry(root,font='comicsansms 30 bold',borderwidth=10,relief="groove" ,justify="center",width=20).place(x=700,y=290)

button_create=Button(root,text="Create Pin",font='comicsansms 19 bold',borderwidth=10,relief="ridge" ,justify="center",width=25,border="10",command=lambda:display(1)).place(x=250,y=300)

button_withdraw=Button(root,text="Withdraw Money",font='comicsansms 19 bold',borderwidth=10,relief="ridge" ,justify="center",width=25,command=lambda:display(2)).place(x=900,y=300)

button_blance=Button(root,text=" Check Balance",font='comicsansms 19 bold',borderwidth=10,relief="ridge" ,justify="center",width=25,command=lambda:display(3)).place(x=250,y=400)

button_Histroy=Button(root,text="History",font='comicsansms 19 bold',borderwidth=10,relief="ridge",justify="center",width=25,command=lambda:display(4)).place(x=900,y=400)

button_Deposite=Button(root,text="Deposit",font='comicsansms 19 bold',borderwidth=10,relief="ridge" ,justify="center",width=25,command=lambda:display(5)).place(x=250,y=500)

button_Help=Button(root,text="Help!",font='comicsansms 19 bold',borderwidth=10,relief="ridge" ,justify="center",width=25,command=lambda:display(6)).place(x=900,y=500)

button_Change_pin=Button(root,text="Change pin",font='comicsansms 19 bold',borderwidth=10,relief="ridge" ,justify="center",width=25,command=lambda:display(7)).place(x=250,y=600)

root.mainloop()