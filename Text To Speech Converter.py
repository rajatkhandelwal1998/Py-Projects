import pyttsx3
from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("Text To Speech Converter ")
root.geometry("430x150+100+100")

def show():
    engine = pyttsx3.init()
    engine.say(e1.get())
    engine.setProperty('rate', 60)
    engine.setProperty('volume', 0.9)
    engine.runAndWait()
def cancel():
    a = tkinter.messagebox.askyesno(title="Cancel", message="Do you Want to Cancel ?")
    print(a)
    if (a == True):
        root.destroy()
def clear():
    e1.delete("0",END)

l1=Label(text="Please Enter your Text:",font=('cambria',15,'italic'))
l1.place(x=0,y=5)
e1=Entry( font=('cambria',15,'italic'),bd=3)
e1.place(x=15,y=50,width=400,height=30)
b1=Button(text="OK",width=10,height=1,bd=4,command=show,bg="silver")
b1.place(x=35,y=100)
b2=Button(text="Clear",width=10,height=1,bd=4,command=clear,bg="silver")
b2.place(x=170,y=100)
b3=Button(text="Cancel",width=10,height=1,bd=4,command=cancel,bg="silver")
b3.place(x=305,y=100)

root.mainloop()