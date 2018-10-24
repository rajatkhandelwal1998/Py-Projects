from tkinter import *
import math
tk=Tk()                     #obj of TK class to create a blank window
tk.resizable(0,0)
tk.title("Scientific Calc")
tk.geometry("288x400")
i=0
def fac():
    a = float(e1.get())
    b = math.factorial(a)
    clear()
    e1.insert(0, b)
def power():
    a = float(e1.get())
    b = math.pow(a, 2)
    clear()
    e1.insert(0, b)
def sqrt():
    a = float(e1.get())
    b = math.sqrt(a)
    clear()
    e1.insert(0, b)
def pie():
    e1.insert(END, 3.14)
def clear():
    e1.delete(0, END)

def sin():
    a = float(e1.get())
    b = math.sin(a)
    clear()
    e1.insert(0, b)
def open():
    e1.insert(END, "(")
def close():
    e1.insert(END, ")")
def e2():
    a= float(e1.get())
    b = math.pow(2.303, a)
    clear()
    e1.insert(0, b)
def Del():
    a = e1.get()
    clear()
    b = len(a)
    for i in range(0, b - 1):
        e1.insert(END, a[i])

def cos():
    a = float(e1.get())
    b = math.cos(a)
    clear()
    e1.insert(0, b)
def type7():
    e1.insert(END, "7")
def type8():
    e1.insert(END, "8")
def type9():
    e1.insert(END, "9")
def divide():
    e1.insert(END, "/")

def tan():
    a = float(e1.get())
    b = math.tan(a)
    clear()
    e1.insert(0, b)
def type4():
    e1.insert(END, "4")
def type5():
    e1.insert(END, "5")
def type6():
    e1.insert(END, "6")
def multiply():
    e1.insert(END, "*")

def ln():
    a = float(e1.get())
    b = math.log(a, 10)
    c = 2.303 * b
    clear()
    e1.insert(0, c)
def type1():
    e1.insert(END, "1")
def type2():
    e1.insert(END, "2")
def type3():
    e1.insert(END, "3")
def sub():
    e1.insert(END, "-")

def log():
    a = float(e1.get())
    b = math.log(a, 10)
    clear()
    e1.insert(0, b)
def type0():
    e1.insert(END, "0")
def type():
    e1.insert(END, ".")
def equal():
    try:
        ans = eval(e1.get())
        e1.delete(0, END)
        e1.insert(0, ans)
    except SyntaxError:
        e1.delete(0, END)
        e1.insert(0, "Syntax Error")
    except ZeroDivisionError:
        e1.delete(0, END)
        e1.insert(0, "You cann't divide by zero!")
def add():
    e1.insert(END, "+")

e1=Entry(width=44, font=('arial',20,'bold'), bd=10,justify=RIGHT)
e1.place(x=10, y=10, width=270, height=70)

b1=Button(text="!",width=5,bg="grey",command=fac,bd=4)
b1.place(x=10,y=100)
b2=Button(text="^",width=5,bg="grey",command=power,bd=4)
b2.place(x=65,y=100)
b3=Button(text="√",width=5,bg="grey",command=sqrt,bd=4)
b3.place(x=120,y=100)
b4=Button(text="π",width=5,bg="grey",command=pie,bd=4)
b4.place(x=175,y=100)
b5=Button(text="C",width=5,bg="grey",command=clear,bd=4)
b5.place(x=230,y=100)

b6=Button(text="sin",width=5,bg="grey",command=sin,bd=4)
b6.place(x=10,y=150)
b7=Button(text="(",width=5,bg="grey",command=open,bd=4)
b7.place(x=65,y=150)
b8=Button(text=")",width=5,bg="grey",command=close,bd=4)
b8.place(x=120,y=150)
b9=Button(text="e", width=5, bg="grey", command=e2, bd=4)
b9.place(x=175,y=150)
b10=Button(text="DEL",width=5,bg="grey",command=Del,bd=4)
b10.place(x=230,y=150)

b11=Button(text="cos",width=5,bg="grey",command=cos,bd=4)
b11.place(x=10,y=200)
b12=Button(text="7",width=5,bd=4,command=type7)
b12.place(x=65,y=200)
b13=Button(text="8",width=5,bd=4,command=type8)
b13.place(x=120,y=200)
b14=Button(text="9",width=5,bd=4,command=type9)
b14.place(x=175,y=200)
b15=Button(text="/",width=5,bg="grey",bd=4,command=divide)
b15.place(x=230,y=200)

b16=Button(text="tan",width=5,bd=4,bg="grey",command=tan)
b16.place(x=10,y=250)
b17=Button(text="4",width=5,bd=4,command=type4)
b17.place(x=65,y=250)
b18=Button(text="5",width=5,bd=4,command=type5)
b18.place(x=120,y=250)
b19=Button(text="6",width=5,bd=4,command=type6)
b19.place(x=175,y=250)
b20=Button(text="*",width=5,bd=4,bg="grey",command=multiply)
b20.place(x=230,y=250)

b21=Button(text="ln",width=5,bd=4,bg="grey",command=ln)
b21.place(x=10,y=300)
b22=Button(text="1",width=5,bd=4,command=type1)
b22.place(x=65,y=300)
b23=Button(text="2",width=5,bd=4,command=type2)
b23.place(x=120,y=300)
b24=Button(text="3",width=5,bd=4,command=type3)
b24.place(x=175,y=300)
b25=Button(text="-",width=5,bd=4,command=sub,bg="grey")
b25.place(x=230,y=300)

b26=Button(text="log",width=5,bd=4,command=log,bg="grey")
b26.place(x=10,y=350)
b27=Button(text="0",width=5,bd=4,command=type0)
b27.place(x=65,y=350)
b28=Button(text=".",width=5,bd=4,command=type)
b28.place(x=120,y=350)
b29=Button(text="=",width=5,bd=4,bg="red",command=equal)
b29.place(x=175,y=350)
b30=Button(text="+",width=5,bd=4,bg="grey",command=add)
b30.place(x=230,y=350)

tk.mainloop()                    #to hold the window
print("End of program!!")
