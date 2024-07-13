import random as rm
from tkinter import *

# FUNCTION FOR GENERATE BUTTON
def genwin():
    global lengthInput,v
    length=lengthInput.get()
    gen(eval(length),v.get())

# FUNCTION TO GENERATE PASSWORD
def gen(a,b):
    x="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$&_?|~"
    global pw,output
    password=""
    for i in range(a):
        if b==1:
            password+=rm.choice(x[:52])
        elif b==2:
            password+=rm.choice(x[:62])
        else:
            password+=rm.choice(x)
    pw.set(password)
    output.update()

# CODE FOR GUI
root=Tk()
root.geometry("400x250")
root.configure(background="light grey")
root.minsize(400,250)
root.maxsize(400,250)

name=Label(root,text="Random Password Generator",bg="light grey",font="Ariel 19 bold")
name.pack(padx=5,pady=5)

lengthVar=StringVar()
lengthVar="0"
lengthInput=Entry(root,textvariable=lengthVar,font=("Calibiri 10 bold"),width=40)
lengthInput.pack(padx=3,pady=4)
instruct=Label(root,text="Enter Length for the Password",bg="light grey",font="Ariel 10 bold")
instruct.pack(padx=3,pady=3)

difficultyFrame=Frame(root,background="light grey")
v = IntVar(difficultyFrame, 1)
values = {"Easy" : 1,"Medium" : 2,"Hard" : 3}
for (text, value) in values.items():
    Radiobutton(difficultyFrame, text = text, variable = v, value = value).pack(side = "left",pady = 3,padx=3)
difficultyFrame.pack(padx=3,pady=3)

generate=Button(root,text="GENERATE",font=("Ariel 10 bold"),command=genwin)
generate.pack(padx=3,pady=3)

pw=StringVar()
pw.set("")

outputFrame=Frame(root,background="light grey")
OutputLabel=Label(outputFrame,text="Password : ",bg="light grey",font="Ariel 10 bold")
OutputLabel.grid(row=0,column=0,padx=3,pady=3)
output=Entry(outputFrame,textvariable=pw,bg="light grey",font="Ariel 10")
output.grid(row=0,column=1,padx=3,pady=3)
outputFrame.pack(padx=3,pady=3)


# COMMAND TO RUN CODE
root.mainloop()