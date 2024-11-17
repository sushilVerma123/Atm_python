# befor run this program start xamp (apache, mysql)

import pymysql as my
import datetime
import maskpass

conn=my.connect(
    host='localhost',
    user='root',
    password='',
    database='atm_machine')
mysql=conn.cursor()


def create_pin(card_num):
    name=input("enter your name: ")
    pin=int(maskpass.askpass(prompt="Enter the pin: ",mask="*"))
    inn="INSERT into atm_card(Name,Card_number,Pin_number) values(%s,%s,%s)"
    t=(name,card_num,pin)
    mysql.execute(inn,t)
    conn.commit()
    print('******** your pin is created ********')
    n=int(input("press 1 for withdraw the money \n otherwise press any key "))
    if(n==1):
        withdraw(card_num)


def withdraw(card_num):
    user_amount=int(input("enter your amount which you want to withdraw: "))
    for i in range(1,4):
        user_pin=int(maskpass.askpass(prompt="Enter the pin: ",mask="*"))
        pin="select Pin_number from atm_card where Card_number=%s"
        t=(card_num)
        mysql.execute(pin,t)
        pin1=mysql.fetchall()[0][0]
        if(user_pin==pin1):
           pin_right(user_amount)
           break
        else:
            print("your pin is not valid")


def pin_right(user_amount):
    total="Select Sum(Type_Note*Number_Note) From note_details "
    mysql.execute(total)
    total_amount=mysql.fetchall()[0][0]
    note=[2000,500,200,100]
    if(user_amount>total_amount):
        p="****** Atm does not have that amount *******"

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
            p="**** Atm does not provid this amount *******"
    else:
        p= "******* money not withdrew ******"
    if(type(p)!=str):
        update_Atm_rupees(p,numnote,note)
        tansaction_detail(card_num,amount)
    display(p,note)



def update_Atm_rupees(p,numnote,note):
    
    for i in range(len(p)):
        new_numNote='update note_details set Number_Note=%s where Type_note=%s'
        x=numnote[i]-p[i]
        y=note[i]
        t=(x,y)
        mysql.execute(new_numNote,t)
        conn.commit()



def display(p,note):
    if(type(p)==str):
        print(p,"\n")
    else:
        for i in range(len(p)):
            if(p[i]==0):
                continue
            print(f'\n ***** {p[i]} note for {note[i]} ****')
        
def tansaction_detail(card_num,user_amount):
    now=datetime.datetime.now()
    inn="INSERT into transaction(Card_number,user_amount,Date_time) values(%s,%s,%s)"
    t=(card_num,user_amount,now)
    mysql.execute(inn,t)
    conn.commit()


    

try:
    card_num=int(input("enter your atm_number: "))     
    data="select Card_number from atm_card"
    mysql.execute(data)
    data_tuple=mysql.fetchall()
    a=False
    for i in data_tuple:
        if(card_num == i[0]):
            a=True
            break
    if(a==False):
        create_pin(card_num)
    else:
        withdraw(card_num)
except:
    print("Enter the valid Card Number")
    