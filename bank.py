from tkinter import *
from tkinter.font import BOLD, ITALIC
import smtplib
import random

window=Tk()
window.title("Banking App")
root=Frame(window)
root.pack()
label=Label(root,text="-----------------------Login-----------------------",font=("Forte",15,ITALIC),fg="#5E4352")
label.grid(row=0)
global lastFrame,lastrow
lastFrame=root
window.geometry("320x300")
lastlabel=Label()
window.resizable(True,True)


def customer():
    global lastFrame,cuser,cpswrd,lastrow
    lastFrame.forget()
    frame=Frame(window)
    frame.pack()
    lastFrame=frame
    l1=Label(frame,text="Username:",font=("Rockwell",15,ITALIC))
    l1.grid(row=0,columnspan=2)
    cuser=Entry(frame,width=45)
    cuser.grid(row=1,columnspan=2)
    l2=Label(frame,text="Password:",font=("Rockwell",15,ITALIC))
    l2.grid(row=2,columnspan=2)
    cpswrd=Entry(frame,width=45,show="*")
    cpswrd.grid(row=3,columnspan=2)
    c1=Checkbutton(frame,command=showPassword1)
    c1.grid(row=4)
    passLabel=Label(frame,text="Show Password",font=("Arial",9,))
    passLabel.grid(row=4,columnspan=2)
    btn=Button(frame,text="Continue",command=userCallFunc1,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    btn.grid(row=5,column=0,padx=10, pady=10,ipadx=3)
    btn1=Button(frame,text="Main Menu",command=mainMenu,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    btn1.grid(row=5,column=1,padx=10,pady=10,ipadx=3)
    lastrow=5
def bank():
    global lastFrame,pswrd,user,lastrow
    lastFrame.forget()
    frame=Frame(window)
    frame.pack()
    lastFrame=frame
    l1=Label(frame,text="ID:",font=("Rockwell",15,ITALIC))
    l1.grid(row=0,columnspan=2)
    user=Entry(frame,width=45)
    user.grid(row=1,columnspan=2)
    l2=Label(frame,text="Password:",font=("Rockwell",15,ITALIC))
    l2.grid(row=2,columnspan=2)
    pswrd=Entry(frame,width=45,show="*")
    pswrd.grid(row=3,columnspan=2)
    c1=Checkbutton(frame,command=showPassword2)
    c1.grid(row=4)
    passLabel=Label(frame,text="Show Password")
    passLabel.grid(row=4,columnspan=2)
    btn=Button(frame,text="Continue",command=bankCallFunc1,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    btn.grid(row=5,column=0,padx=10,pady=10,ipadx=3)
    btn1=Button(frame,text="Main Menu",command=mainMenu,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    btn1.grid(row=5,column=1,padx=10,pady=10,ipadx=3)
    lastrow=5

def checkUser(id,p):
    global lastrow
    check=0
    f=open("UserDatabase.txt","r")
    for i in f.readlines():
        lis=i.split()
        if(lis[0]==id):
            if lis[1]==encrypt(p):
                f.close()
                verifiedUser(id)
                check=1
                break
        elif(lis[0]==""):
            check=0
    f.close()            
    if check==0:
        label=Label(lastFrame,text="Incorrect user id or password",fg="red",font=("Copperplate Gothic Light",10,BOLD))
        label.grid(row=lastrow+1,columnspan=2) 
                
def checkEmployee(id,p):
    global lastrow
    check=0
    f=open("EmployeeDatabase.txt","r")
    for i in f.readlines():
        lis=i.split()
        if(lis[0]==id):
            if lis[1]==encrypt(p):
                check=1
                break
        elif(lis[0]==""):
            check=0
    f.close()          
    if check==0:
        label=Label(lastFrame,text="Incorrect id or password",fg="red",font=("Copperplate Gothic Light",10,BOLD))
        label.grid(row=lastrow+1,columnspan=2) 
    else:
        verifiedEmployee()

def verifiedUser(id):
    global lastFrame
    lastFrame.forget()
    frame=Frame(window)
    frame.pack()
    lastFrame=frame
    label=Label(frame,text="",bg="green",fg="white",font=("Copperplate Gothic Light",10,BOLD))
    label.pack(side="top")
    btn=Button(frame,text="Send Money",command=showAmount(id),font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    btn.pack(side="top",ipadx=3)

def showAmount(id):
    global current,sid,lastrow
    f=open("UserDatabase.txt","r")
    for i in f.readlines():
        lis=i.split()
        if(lis[0]==id):
            current=lis[2]
    sid=id
    f.close()
    global lastFrame,rid,ramt
    lastFrame.forget()
    frame=Frame(window)
    frame.pack()
    lastFrame=frame
    label1=Label(frame,text="Recipient ID:",font=("Rockwell",15,ITALIC))
    label1.grid(row=0,columnspan=2)
    rid=Entry(frame,width=45)
    rid.grid(row=1,columnspan=2)
    label2=Label(frame,text="Amount:",font=("Rockwell",15,ITALIC))
    label2.grid(row=2,columnspan=2)
    ramt=Entry(frame,width=45)
    ramt.grid(row=3,columnspan=2)
    btn=Button(frame,text="Get OTP",command=sendMoney,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    btn.grid(row=4,column=0,padx=10,pady=10,ipadx=3)
    btn1=Button(frame,text="Main Menu",command=mainMenu,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    btn1.grid(row=4,column=1,padx=10,pady=10,ipadx=3)
    label3=Label(frame,text="Balance: Rs "+current,font=("Rockwell",15,BOLD))
    label3.grid(row=5,columnspan=2)
    lastrow=5

def verifiedEmployee():
    global lastFrame,cid,lastrow
    lastFrame.forget()
    frame=Frame(window)
    frame.pack()
    lastFrame=frame
    label=Label(frame,text="Enter customer id",font=("Rockwell",15,ITALIC))
    label.grid(row=0)
    lastrow=0
    cid=Entry(frame,width=45)
    cid.grid(row=1)
    btn=Button(frame,text="Get OTP",command=bankCallFunc2,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    btn.grid(row=2,ipadx=3,pady=30)
    lastrow=2
    
def deposit(cid):
    global lastFrame,lastrow
    f=open("UserDatabase.txt","r+")
    lis=()
    for i in f.readlines():
        lis=i.split()
        if(lis[0]==cid):
            break
    f.close()
    global newAmt,dep,id
    id=cid
    newAmt=float(lis[2])
    lastFrame.forget()
    frame=Frame(window)
    frame.pack(side="top")
    lastFrame=frame
    labelU=Label(frame,text="User: "+lis[0]+"\nBalance: Rs."+lis[2]+"\nEnter deposit amount: ",font=("Baskerville Old Face",10,BOLD))
    labelU.pack(side="top")
    dep=Entry(frame,width=45)
    dep.pack(side="top")
    btn=Button(frame,text="Done",command=updateAmount,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    btn.pack(side="top",ipadx=3)
        
def bankCallFunc1():
    global user,pswrd,lastrow
    id=user.get()
    pas=pswrd.get()
    checkEmployee(id,pas)
def userCallFunc1():
    global cuser,cpswrd,lastrow
    id=cuser.get()
    pas=cpswrd.get()
    checkUser(id,pas)
def bankCallFunc2():
    global cid,lastrow,lastFrame,otp,otpEntry,receiver,ch
    ch=2
    if verifyUser(cid.get())!=0:
        lastFrame.forget()
        frame=Frame(window)
        frame.pack()
        lastFrame=frame
        label=Label(frame,text="Enter OTP",font=("Rockwell",15,ITALIC))
        label.grid(row=0,columnspan=3)
        otpEntry=Entry(frame,width=45)
        otpEntry.grid(row=1,columnspan=3)
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        password='hxdjcjrabhqntnkz'
        server.login("bankofpython2022@gmail.com",password)
        otp=random.randint(100000,999999)
        msg='Hello, Your OTP is '+str(otp)
        sender='bankofpython2022@gmail.com'  
        receiver=sender
        server.sendmail(sender,receiver,msg)
        server.quit()
        btn=Button(lastFrame,text="Submit",command=checkOtpBank,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
        btn.grid(row=2,column=0,padx=10,pady=10)
        btn=Button(lastFrame,text="Resend OTP",command=resendOtp,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
        btn.grid(row=2,column=1,padx=10,pady=10)
        btn=Button(lastFrame,text="Main Menu",command=mainMenu,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
        btn.grid(row=2,column=2,padx=10,pady=10)

def updateAmount():
    global newAmt,lastFrame,id
    lastFrame.forget()
    frame=Frame(window)
    frame.pack()
    lastFrame=frame
    f=open("UserDatabase.txt","r+")
    newAmt+=float(dep.get())
    dataEntries=list()
    l = f.readlines()
    for i in l:
        lis=i.split()
        if id == lis[0]:
            oldAmt=lis[2]
            Replacement = i.replace(oldAmt, str(newAmt)+"0")
            dataEntries.append(Replacement)
        else:
            dataEntries.append(i)
    f.close()
    f=open("UserDatabase.txt","w")
    for i in dataEntries:
        f.write(i)
    f.close()
    label=Label(frame,text="Deposit Success.",fg="green",font=("Copperplate Gothic Light",10,BOLD))
    label.pack(side="top")
    btn=Button(frame,text="Main Menu",command=mainMenu,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    btn.pack(side="top",ipadx=3)
    
def sendMoney():
    global rid,ramt,sid,lastFrame,lastrow,dataEntries2,Replacement,cntr,cntr1,otp,receiver,ch,phNo
    ch=1
    check=0
    if sid==rid.get():
        label=Label(lastFrame,text="Sender id and recipient id cannot be same",fg="red",font=("Copperplate Gothic Light",9,BOLD))
        label.grid(row=lastrow+1,columnspan=2)
        lastrow=lastrow+1
                
    elif rid.get()=="" or ramt.get()=="":
        label=Label(lastFrame,text="Any input field cannot be empty",fg="red",font=("Copperplate Gothic Light",9,BOLD))
        label.grid(row=lastrow+1,columnspan=2)
        lastrow=lastrow+1
                
    elif int(ramt.get())==0:
        label=Label(lastFrame,text="Amount cannot be 0",fg="red",font=("Copperplate Gothic Light",9,BOLD))
        label.grid(row=lastrow+1,columnspan=2)
        lastrow=lastrow+1
               
    elif float(ramt.get())<=float(current):
        f=open("UserDatabase.txt","r+")
        dataEntries2=list()
        cntr=-1
        for i in f.readlines():
            lis=i.split()
            cntr+=1
            if(lis[0]==rid.get()):
                Replacement=i.replace(lis[2],str(float(ramt.get())+float(lis[2]))+"0")
                check=1
                f.close()
                break
        f.close() 
        f=open("UserDatabase.txt","r+")
        for i in f.readlines():
            lis=i.split()      
            if lis[0]==sid:
                receiver=lis[3]
                phNo=lis[4]
        f.close()
        if check==0:
            label=Label(lastFrame,text="Incorrect user id",fg="red",font=("Copperplate Gothic Light",10,BOLD))
            label.grid(row=lastrow+1,columnspan=2) 
        else:
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            password='hxdjcjrabhqntnkz'
            server.login("bankofpython2022@gmail.com",password)
            otp=random.randint(100000,999999)
            msg='OTP for funds transfer of Rs. '+ramt.get()+' is '+str(otp)
            sender='bankofpython2022@gmail.com'  
            server.sendmail(sender,receiver,msg)
            server.quit()
            try:
                from twilio.rest import Client
            except:
                print ("Twilio package doesn't exist on the system\nTrying to install Twilio...")
                try:
                    import os
                    os.system("pip install twilio")
                    os.system("cls")
                    from twilio.rest import Client
                except:
                    print("Couldn't install twilio")
                    ch=0
                else:
                    print("Package installed successfully!")
                
            finally:
                try:
                    c=Client("AC1e086b5ae02cbae5d739c46bd9233cd4", "a8a753157a036b2c645c2c753951e87b")
                    c.messages.create(body="OTP for funds transfer of Rs. "+ramt.get()+" is "+str(otp),from_="+14247897182",to=phNo)
                except:
                    import os
                    os.system("cls")
                    print("Couldn't send otp to Sender's Phone number\nVerify the number first at twilio website\nOTP SENT TO EMAIL SUCCESSFULLY")
            global otpEntry
            lastFrame.forget()
            frame=Frame(window)
            frame.pack()
            lastFrame=frame
            enOtp=Label(lastFrame,text="Enter OTP:",font=("Rockwell",15,ITALIC))
            enOtp.grid(row=0,columnspan=3)
            otpEntry=Entry(lastFrame,width=45)
            otpEntry.grid(row=1,columnspan=3,padx=10,pady=10)
            btn=Button(lastFrame,text="Submit",command=checkOtp,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
            btn.grid(row=2,column=0,padx=10,pady=10)
            btn=Button(lastFrame,text="Resend OTP",command=resendOtp,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
            btn.grid(row=2,column=1,padx=10,pady=10)
            btn=Button(lastFrame,text="Main Menu",command=mainMenu,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
            btn.grid(row=2,column=2,padx=10,pady=10)
            
    else:
        label=Label(lastFrame,text="Insufficient funds.\nEnter an amount within "+current,fg="red",font=("Copperplate Gothic Light",10,BOLD))
        label.grid(row=lastrow+1,columnspan=2) 
        lastrow=lastrow+1
        
def newRegistration():
    global lastFrame
    lastFrame.forget()
    frame=Frame(window)
    frame.pack()
    lastFrame=frame
    nUser=Button(frame,text="New User",command=newUser,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    nUser.grid(row=0,padx=5,pady=30,ipadx=5,ipady=5)
    nEmployee=Button(frame,text="New Employee",command=newEmployee,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    nEmployee.grid(row=1,padx=5,pady=10,ipadx=5,ipady=5)
    btn1=Button(frame,text="Main Menu",command=mainMenu,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    btn1.grid(row=2,padx=5,pady=30,ipadx=5,ipady=5)
    
def newUser():
    global nupswrd,nuid,lastFrame,lastrow,email,phN
    lastFrame.forget()
    frame=Frame(window)
    frame.pack()
    lastFrame=frame
    l1=Label(frame,text="User ID:",font=("Rockwell",15,ITALIC))
    l1.grid(row=0,columnspan=2) 
    nuid=Entry(frame,width=45)
    nuid.grid(row=1,columnspan=2)
    l2=Label(frame,text="Password:",font=("Rockwell",15,ITALIC))
    l2.grid(row=2,columnspan=2)
    nupswrd=Entry(frame,width=45,show="*")
    nupswrd.grid(row=3,columnspan=2)
    c1=Checkbutton(frame,command=showPassword3)
    c1.grid(row=4)
    passLabel=Label(frame,text="Show Password")
    passLabel.grid(row=4,columnspan=2)
    notification=Label(frame,text="*Password must contain atleast one-upper case, special and numeric character",font=("Calibri",7,ITALIC),fg="red")
    notification.grid(row=5,columnspan=2)
    emL=Label(frame,text="Email ID: ",font=("Rockwell",15,ITALIC))
    emL.grid(row=6,columnspan=2)
    email=Entry(frame,width=45)
    email.grid(row=7,columnspan=2)
    phL=Label(frame,text="Contact Number: ",font=("Rockwell",15,ITALIC))
    phL.grid(row=8,columnspan=2)
    phN=Entry(frame,width=45)
    phN.grid(row=9,columnspan=2)
    cont=Button(frame,text="Continue",command=addUser,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    cont.grid(row=10,column=0,padx=10,pady=10,ipadx=3)
    btn1=Button(frame,text="Main Menu",command=mainMenu,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    btn1.grid(row=10,column=1,padx=10,pady=10,ipadx=3)
    lastrow=10

def newEmployee():
    global nepswrd,neid,lastFrame,lastrow
    lastFrame.forget()
    frame=Frame(window)
    frame.pack()
    lastFrame=frame
    l1=Label(frame,text="Employee ID:",font=("Rockwell",15,ITALIC))
    l1.grid(row=0,columnspan=2)
    neid=Entry(frame,width=45)
    neid.grid(row=1,columnspan=2)
    l2=Label(frame,text="Password:",font=("Rockwell",15,ITALIC))
    l2.grid(row=2,columnspan=2)
    nepswrd=Entry(frame,width=45,show="*")
    nepswrd.grid(row=3,columnspan=2)
    c1=Checkbutton(frame,command=showPassword4)
    c1.grid(row=4)
    passLabel=Label(frame,text="Show Password")
    passLabel.grid(row=4,columnspan=2)
    notification=Label(frame,text="*Password must contain atleast one-upper case, special and numeric character",font=("Calibri",7,ITALIC),fg="red")
    notification.grid(row=5,columnspan=2)
    cont=Button(frame,text="Continue",command=addEmployee,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    cont.grid(row=6,column=0,padx=10,pady=10,ipadx=3)
    back=Button(frame,text="Main Menu",command=mainMenu,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    back.grid(row=6,column=1,padx=10,pady=10,ipadx=3)
    lastrow=6

def addUser():
    global nuid,nupswrd,lastFrame,lastrow,lastlabel,email,phN
    f=open("UserDatabase.txt","r")
    check=0
    if checkPas(nupswrd.get())==0:
        lastlabel.destroy()
        lastlabel=Label(lastFrame,text="Invalid password",fg="red",font=("Copperplate Gothic Light",10,BOLD))
        check=1
        lastlabel.grid(row=lastrow+1,columnspan=2)
    else:
        for i in f.readlines():
            if i=="\n":
                break
            if list(i.split())[0]==nuid.get():
                lastlabel.destroy()
                lastlabel=Label(lastFrame,text="User ID already taken!",fg="red",font=("Copperplate Gothic Light",10,BOLD))
                check=1
                f.close()
                lastlabel.grid(row=lastrow+1,columnspan=2)
                break
    f.close()
    if nupswrd.get()=="" or nuid.get()=="" or email.get()=="" or phN.get()=="":
        lastlabel.destroy()
        lastlabel=Label(lastFrame,text="Any input field cannot be empty",fg="red",font=("Copperplate Gothic Light",10,BOLD))
        check=1
        lastlabel.grid(row=lastrow+1,columnspan=2)
        
    
    if check==0:
        f=open("UserDatabase.txt","a")
        f.write(nuid.get()+" "+encrypt(nupswrd.get())+" 0.00 "+email.get()+" +91"+phN.get()+"\n")
        f.close()
        lastFrame.forget()
        frame=Frame(window)
        frame.pack()
        lastFrame=frame
        l=Label(frame,text="Registration Successful",fg="green",font=("Copperplate Gothic Light",10,BOLD))
        l.pack(side="top")
        btn=Button(frame,text="Main Menu",command=mainMenu,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
        btn.pack(side="top",ipadx=3)

def addEmployee():
    global neid,nepswrd,lastFrame,lastrow,lastlabel
    f=open("EmployeeDatabase.txt","r")
    check=0
    if checkPas(nepswrd.get())==0:
        lastlabel.destroy()
        lastlabel=Label(lastFrame,text="Invalid password",fg="red",font=("Copperplate Gothic Light",10,BOLD))
        check=1
        lastlabel.grid(row=lastrow+1,columnspan=2)
        
    else:
        for i in f.readlines():
            if i=="\n":
                break
            if list(i.split())[0]==neid.get():
                lastlabel.destroy()
                lastlabel=Label(lastFrame,text="User ID already taken!",fg="red",font=("Copperplate Gothic Light",10,BOLD))
                check=1
                f.close()
                lastlabel.grid(row=lastrow+1,columnspan=2)
                break
    f.close()
    if nepswrd.get()=="" or neid.get()=="":
        lastlabel.destroy()
        lastlabel=Label(lastFrame,text="ID or password cannot be empty",fg="red",font=("Copperplate Gothic Light",10,BOLD))
        check=1
        lastlabel.grid(row=lastrow+1,columnspan=2)
        
    if check==0:
        f=open("EmployeeDatabase.txt","a")
        f.write(neid.get()+" "+encrypt(nepswrd.get())+"\n")
        f.close()
        lastFrame.forget()
        frame=Frame(window)
        frame.pack()
        lastFrame=frame
        l=Label(frame,text="Registration Successful",fg="green",font=("Copperplate Gothic Light",10,BOLD))
        l.pack(side="top")
        btn=Button(frame,text="Main Menu",command=mainMenu,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
        btn.pack(side="top",ipadx=3)

def encrypt(s):
    a=""
    lis=["a","e","i","o","u"]
    for i in s:
        if i.lower() in ("a","e","i","o"):
            if i.islower():
                a+=lis[lis.index(i.lower())+1]
            else:
                a+=lis[lis.index(i.lower())+1].upper()
        elif i.lower()=="u":
            if i.islower():
                a+="a"
            else:
                a+="A"
        else:
            a+=chr(ord(i)-2)
    return a

def mainMenu():
    global lastFrame
    lastFrame.forget()
    frame=Frame(window)
    frame.pack()
    label=Label(frame,text="-----------------------Login-----------------------",font=("Forte",15,ITALIC),fg="#5E4352")
    label.grid(row=0)
    lastFrame=frame
    btn1=Button(frame,text="Customer",command=customer,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    btn1.grid(row=1,padx=10,pady=10,ipadx=5,ipady=5)
    btn3=Button(frame,text="New Registration",command=newRegistration,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    btn3.grid(row=2,padx=10,pady=10,ipadx=5,ipady=5)
    btn2=Button(frame,text="Bank Login",command=bank,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    btn2.grid(row=3,padx=10,pady=10,ipadx=5,ipady=5)
    btn4=Button(frame,text="Exit",command=exit,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
    btn4.grid(row=4,padx=10,pady=10,ipadx=10,ipady=5)
    lastrow=4

def checkPas(s):
    cap=special=num=0
    for i in s:
        if ord(i)>=65 and ord(i)<=90:
            cap=1
        elif i in "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
            special=1
        elif i in "1234567890":
            num=1
        if cap==special==num==1:
            return 1
    return 0

def showPassword1():
    global cpswrd
    if cpswrd.cget("show")=="*":
        cpswrd.config(show="")
    else:
        cpswrd.config(show="*")

def showPassword2():
    global pswrd
    if pswrd.cget("show")=="*":
        pswrd.config(show="")
    else:
        pswrd.config(show="*")
    
def showPassword3():
    global nupswrd
    if nupswrd.cget("show")=="*":
        nupswrd.config(show="")
    else:
        nupswrd.config(show="*")

def showPassword4():
    global nepswrd
    if nepswrd.cget("show")=="*":
        nepswrd.config(show="")
    else:
        nepswrd.config(show="*")

def checkOtp():
    global otpEntry,lastFrame,dataEntries2,Replacement,cntr,cntr1,otp
    if otpEntry.get()==str(otp):
        f=open("UserDatabase.txt","r+")
        cntr1=-1
        for i in f.readlines():
            cntr1+=1
            lis=i.split()
            if(lis[0]==sid):
                Replacement2=i.replace(lis[2],str(float(lis[2])-float(ramt.get()))+"0")
                dataEntries2.append(Replacement2)
            elif(cntr1==cntr):
                dataEntries2.append(Replacement)
            else:
                dataEntries2.append(i)
        f.close()
        f=open("UserDatabase.txt","w")
        for i in dataEntries2:
            f.write(i)
        f.close()
        lastFrame.forget()
        frame=Frame(window)
        frame.pack()
        lastFrame=frame
        label=Label(lastFrame,text="Success :)",bg="green",fg="white",font=("Copperplate Gothic Light",10,BOLD))
        label.pack(side="top",padx=10,pady=10) 
        btn=Button(frame,text="Main Menu",command=mainMenu,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
        btn.pack(side="top",ipadx=3,padx=10,pady=10)
    else: 
        label=Label(lastFrame,text="Invalid otp!",fg="red",font=("Copperplate Gothic Light",10,BOLD))
        label.grid(row=3,columnspan=3)

def resendOtp():
    global receiver,otp,phNo,ramt
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    password='hxdjcjrabhqntnkz'
    server.login("bankofpython2022@gmail.com",password)
    otp=random.randint(100000,999999)
    if ch!=2:
        msg='OTP for funds transfer of Rs. '+ramt.get()+' is '+str(otp)
    elif ch==2:
        msg='Hello, Your OTP is '+str(otp)
    sender='bankofpython2022@gmail.com'  
    server.sendmail(sender,receiver,msg)
    server.quit()
    if ch==1:
        try:
            from twilio.rest import Client
            c=Client("AC1e086b5ae02cbae5d739c46bd9233cd4", "a8a753157a036b2c645c2c753951e87b")
            c.messages.create(body="OTP for funds transfer of Rs. "+ramt.get()+" is "+str(otp),from_="+14247897182",to=phNo)
        except:
            import os
            os.system("cls")
            print("Couldn't send otp to Sender's Phone number\nVerify the number first at twilio website\nOTP SENT TO EMAIL SUCCESSFULLY")

def checkOtpBank():
    global otp,otpEntry,cid,lastFrame
    if str(otp)==otpEntry.get():
        id=cid.get()
        deposit(id)
    else:
        label=Label(lastFrame,text="Invalid otp!",fg="red",font=("Copperplate Gothic Light",10,BOLD))
        label.grid(row=3,columnspan=3)

def verifyUser(cid):
    check=0
    f=open("UserDatabase.txt","r+")
    lis=()
    for i in f.readlines():
        lis=i.split()
        if(lis[0]==cid):
            check=1
            break
    f.close()
    if check==0:
        label=Label(lastFrame,text="Incorrect Customer ID",fg="red",font=("Copperplate Gothic Light",10,BOLD))
        label.grid(row=lastrow+1) 
    return check

btn1=Button(root,text="Customer",command=customer,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
btn1.grid(row=1,padx=10,pady=10,ipadx=5,ipady=5)
btn3=Button(root,text="New Registration",command=newRegistration,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
btn3.grid(row=2,padx=10,pady=10,ipadx=5,ipady=5)
btn2=Button(root,text="Bank Login",command=bank,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
btn2.grid(row=3,padx=10,pady=10,ipadx=5,ipady=5)
btn4=Button(root,text="Exit",command=exit,font=("Algerian",10,ITALIC,UNDERLINE),bg="#9A91A8")
btn4.grid(row=4,padx=10,pady=10,ipadx=10,ipady=5)
lastrow=4

window.mainloop()