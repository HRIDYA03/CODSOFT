from tkinter import *

# Function for Done Button
def doneTask(event):
    taskNo=event.widget.cget("text")
    del l[int(taskNo[5:])-1]
    global viewTaskFrame
    viewTaskFrame.destroy()
    viewTaskFrame=Frame(root,background="#7C3626")
    viewTaskFrame.configure(width=367,height=390)
    viewTaskFrame.grid_propagate(0)
    viewTaskFrame.pack(padx=4,pady=4)
    view()
    
# Function to Add Task
l=[]
task=""
def addTask():
    task=task_var.get()
    l.append(task)
    view()
    task_var.set("")
    task_input.update()

# Function to show all the tasks
def view():
    for i in range(len(l)):
        op="{0}) {1}".format(i+1,l[i])
        flag="Done-{0}".format(i+1)
        viewTask=Label(viewTaskFrame,text=op,justify="left",fg="#F5853F",font=("Helvetica 20 bold"),width=16)
        viewTask.grid(row=i,column=0,columnspan=5,padx=4,pady=4,sticky="w")
        done=Button(viewTaskFrame,text=flag,bg="#7C3626",fg="#FFCDBC",font=("Helvetica 13 bold"))
        done.grid(row=i,column=10,columnspan=1,padx=4,pady=4)
        done.bind("<Button-1>",doneTask)
    viewTaskFrame.pack(padx=4,pady=4)


# Code for GUI
root=Tk()
root.configure(background="#FFCDBC")
root.geometry("400x600")
root.maxsize(400,600)
root.title("To-Do List")

name=Label(root,text="To-Do List",bg="#FFCDBC",fg="#7C3626",font=("Helvetica 50 bold"))
name.pack(padx=20,pady=30)

addTaskFrame=Frame(root,background="#7C3626")
task_var=StringVar()
task_input=Entry(addTaskFrame,textvariable=task_var,fg="#F5853F",font=("Helvetica 20"))
task_input.grid(row=0,column=0,columnspan=5,padx=4,pady=4)
add=Button(addTaskFrame,text="+",bg="#7C3626",fg="#FFCDBC",font=("Helvetica 13 bold"),command=addTask)
add.grid(row=0,column=6,columnspan=1,padx=4,pady=4)
addTaskFrame.pack(padx=4,pady=4)

viewTaskFrame=Frame(root,background="#7C3626")
viewTaskFrame.configure(width=367,height=390)
viewTaskFrame.grid_propagate(0)
viewTaskFrame.pack(padx=4,pady=4)

# Command to Run the Code
root.mainloop()