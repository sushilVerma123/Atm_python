from tkinter import*
from PIL import Image,ImageTk
root=Tk()
root.geometry("1600x1000")
root.title("Amount Deposit")

image1=Image.open('C:\\Users\\Dell\\OneDrive\\Pictures\\Saved Pictures\\17520.jpg')
Photo=ImageTk.PhotoImage(image1)
label1=Label(root,image=Photo)
label1.pack()

def back():
    root.destroy()
    import Atm_front_page


Label(root,text=" Help page ",font="Arial 25 bold",borderwidth=49,relief="groove",justify="center",background="#208ff7",width=40).place(x=300,y=10)

Button(root,text="<<",command=back,bg="#208ff7").place(x=0,y=0)

string='''Create_Pin :-
This option helps to create your ATM pin and Account\n
Withdraw_Money:-
This option helps to withdraw the Money. When you click this option, new page will be open and enter your valid detail and withdraw the money\n
Balance:-
This option helps to check your balance amount in your account\n
History:-
This option helps to see your transaction History\n
Deposit:-
This option helps to deposit the money in your account\n
'''

Label(root,text=string,font='comicsansms 15 bold',borderwidth=10,relief="ridge" ,justify="center").place(x=100,y=200)





root.mainloop()