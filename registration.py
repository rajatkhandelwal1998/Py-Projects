from tkinter import *
import pymysql
import tkinter.messagebox

tk=Tk()
tk.geometry("600x400+100+100")
tk.title("Registration page")

def save():
    n=e1.get()
    m = e2.get()
    e = e3.get()
    un = e4.get()
    ps = e5.get()
    repass = e6.get()
    if(len(n)==0 or len(m)==0 or len(e)==0 or len(un)==0 or len(ps)==0 or len(repass)==0):
        tkinter.messagebox.showerror("error", "Empty fields not allowed!!")
    else:
        if(ps==repass):
            #database connection
            con=pymysql.connect("localhost","root","rat","pnpythondb")
            cur=con.cursor()
            query="insert into registration values('%s','%s','%s','%s','%s','%s')"%(0,n,m,e,un,ps)
            i=cur.execute(query)
            if(i==1):
                tkinter.messagebox.showinfo("Success","Registration done!!")
                reset()
            else:
                tkinter.messagebox.showerror("error", "Registration failed!!")
            con.commit()
        else:
            tkinter.messagebox.showerror("error", "password and repass didn't match!!")


def reset():
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)

l=Label(text="Registration form",font=40)
l1=Label(text="Enter Name")
l2=Label(text="Enter MobileNo.")
l3=Label(text="Enter Email")
l4=Label(text="Enter Username")
l5=Label(text="Enter Password")
l6=Label(text="Retype Password")

e1=Entry()
e2=Entry()
e3=Entry()
e4=Entry()
e5=Entry()
e6=Entry()

b1=Button(text="SAVE",command=save)
b2=Button(text="RESET",command=reset)


l.place(x=220,y=10)
l1.place(x=180,y=70)
e1.place(x=300,y=70)

l2.place(x=180,y=100)
e2.place(x=300,y=100)

l3.place(x=180,y=100+30)
e3.place(x=300,y=100+30)


l4.place(x=180,y=100+30+30)
e4.place(x=300,y=100+30+30)


l5.place(x=180,y=190)
e5.place(x=300,y=190)

l6.place(x=180,y=220)
e6.place(x=300,y=220)

b1.place(x=180,y=250,width=100)
b2.place(x=300,y=250,width=130)

tk.mainloop()