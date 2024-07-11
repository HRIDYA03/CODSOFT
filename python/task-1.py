# CODE BY HRIDYA HIRAWAT

from tkinter import *

# CODE FOR CLICK EVENT
def click(event):
    r=event.widget.cget("text")
    if r == "=":
        output.set(eval(output.get()))
        screen.update()
    elif r=="C":
        output.set("")
        screen.update()
    else:
        output.set(output.get()+r)
        screen.update()

# CODE FOR GUI
root=Tk()
root.geometry("350x410")
root.minsize(350,410)
root.title("Calculator")
root.configure(background="grey")
output=StringVar()
output.set("")
screen=Entry(root,textvariable=output,font=("7SEG",40))
screen.pack(fill=X,padx=20,pady=20)

# CODE FOR BUTTONS
buttons_frame=Frame(root)
buttons_frame.columnconfigure(0,weight=1)
buttons_frame.columnconfigure(1,weight=1)
buttons_frame.columnconfigure(2,weight=1)
buttons_frame.columnconfigure(3,weight=1)
b1=Button(buttons_frame,text="7",font=("7SEG",25))
b1.grid(row=0,column=0,sticky="news")
b1.bind("<Button-1>",click)
b2=Button(buttons_frame,text="8",font=("7SEG",25))
b2.grid(row=0,column=1,sticky="news")
b2.bind("<Button-1>",click)
b3=Button(buttons_frame,text="9",font=("7SEG",25))
b3.grid(row=0,column=2,sticky="news")
b3.bind("<Button-1>",click)
b4=Button(buttons_frame,text="+",font=("7SEG",25))
b4.grid(row=0,column=3,sticky="news")
b4.bind("<Button-1>",click)
b5=Button(buttons_frame,text="4",font=("7SEG",25))
b5.grid(row=1,column=0,sticky="news")
b5.bind("<Button-1>",click)
b6=Button(buttons_frame,text="5",font=("7SEG",25))
b6.grid(row=1,column=1,sticky="news")
b6.bind("<Button-1>",click)
b7=Button(buttons_frame,text="6",font=("7SEG",25))
b7.grid(row=1,column=2,sticky="news")
b7.bind("<Button-1>",click)
b8=Button(buttons_frame,text="-",font=("7SEG",25))
b8.grid(row=1,column=3,sticky="news")
b8.bind("<Button-1>",click)
b9=Button(buttons_frame,text="1",font=("7SEG",25))
b9.grid(row=2,column=0,sticky="news")
b9.bind("<Button-1>",click)
b10=Button(buttons_frame,text="2",font=("7SEG",25))
b10.grid(row=2,column=1,sticky="news")
b10.bind("<Button-1>",click)
b11=Button(buttons_frame,text="3",font=("7SEG",25))
b11.grid(row=2,column=2,sticky="news")
b11.bind("<Button-1>",click)
b12=Button(buttons_frame,text="*",font=("7SEG",25))
b12.grid(row=2,column=3,sticky="news")
b12.bind("<Button-1>",click)
b13=Button(buttons_frame,text="0",font=("7SEG",25))
b13.grid(row=3,column=0,sticky="news")
b13.bind("<Button-1>",click)
b14=Button(buttons_frame,text="C",font=("7SEG",25))
b14.grid(row=3,column=1,sticky="news")
b14.bind("<Button-1>",click)
b15=Button(buttons_frame,text="=",font=("7SEG",25))
b15.grid(row=3,column=2,sticky="news")
b15.bind("<Button-1>",click)
b16=Button(buttons_frame,text="/",font=("7SEG",25))
b16.grid(row=3,column=3,sticky="news")
b16.bind("<Button-1>",click)
buttons_frame.pack(fill="both",padx=20,pady=20)

# COMMAND TO RUN CODE
root.mainloop()