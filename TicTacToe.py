from tkinter import *
import tkinter.messagebox
tk=Tk()
tk.title("TicTacToe")
#tk.geometry("600x800+400+400")
click=True
def checker(buttons):
    global click
    if buttons["text"]==" " and click ==True:
      buttons["text"]="X"
      click=False
    elif buttons["text"] ==" " and click == False:
      buttons["text"]="o"
      click=True
    elif(button1["text"]=="X"and button2["text"]=="X"and button3["text"]=="X" or
        button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
        button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
        button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" ):
        tkinter.messagebox.showinfo(title="Winner X",message="You Won This Game ")
    elif(button1["text"]=="o"and button2["text"]=="o"and button3["text"]=="o" or
        button4["text"] == "o" and button5["text"] == "o" and button6["text"] == "o" or
        button7["text"] == "o" and button8["text"] == "o" and button9["text"] == "o" or
        button3["text"] == "o" and button5["text"] == "o" and button7["text"] == "o" or
        button1["text"] == "o" and button5["text"] == "o" and button9["text"] == "o" or
        button1["text"] == "o" and button4["text"] == "o" and button7["text"] == "o" or
        button2["text"] == "o" and button5["text"] == "o" and button8["text"] == "o" or
        button3["text"] == "o" and button6["text"] == "o" and button9["text"] == "o" ):
        tkinter.messagebox.showinfo(title="Winner O",message="You Won This Game")
buttons=StringVar()
button1=Button(tk,text=" ",font=('Arial', 30, 'bold'),bg='grey',fg='white',height=4,width=8,command=lambda :checker(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)
button2=Button(tk,text=" ",font=('Arial', 30, 'bold'),bg='grey',fg='white',height=4,width=8,command=lambda :checker(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)
button3=Button(tk,text=" ",font=('Arial', 30, 'bold'),bg='grey',fg='white',height=4,width=8,command=lambda :checker(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)
button4=Button(tk,text=" ",font=('Arial', 30, 'bold'),bg='grey',fg='white',height=4,width=8,command=lambda :checker(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)
button5=Button(tk,text=" ",font=('Arial', 30, 'bold'),bg='grey',fg='white',height=4,width=8,command=lambda :checker(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)
button6=Button(tk,text=" ",font=('Arial', 30, 'bold'),bg='grey',fg='white',height=4,width=8,command=lambda :checker(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)
button7=Button(tk,text=" ",font=('Arial', 30, 'bold'),bg='grey',fg='white',height=4,width=8,command=lambda :checker(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)
button8=Button(tk,text=" ",font=('Arial', 30, 'bold'),bg='grey',fg='white',height=4,width=8,command=lambda :checker(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)
button9=Button(tk,text=" ",font=('Arial', 30, 'bold'),bg='grey',fg='white',height=4,width=8,command=lambda :checker(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)
tk.mainloop()

