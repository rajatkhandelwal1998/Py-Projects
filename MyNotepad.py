from tkinter import *
root=Tk()
root.geometry("1000x1000")
root.title("Notepad")
ta=Text()
ta.insert(INSERT,0)
ta.pack()
def show ():
    print("any item clicked")
mymenu=Menu()
list1=Menu()
list1.add_command(label="New",command=show)
list1.add_command(label="Open",command=show)
list1.add_command(label="Save",command=show)
list1.add_command(label="SaveAs",command=show)
list1.add_command(label="page setup",command=show)
list1.add_command(label="Print",command=show)
list1.add_command(label="exit",command=show)
mymenu.add_cascade(label="File",menu=list1)
list2=Menu()
list2.add_command(label="Undo",command=show)
list2.add_command(label="Cut",command=show)
list2.add_command(label="Copy",command=show)
list2.add_command(label="Paste",command=show)
list2.add_command(label="Delete",command=show)
list2.add_command(label="Find",command=show)
list2.add_command(label="Find Next",command=show)
list2.add_command(label="Replace",command=show)
list2.add_command(label="GoTo",command=show)
list2.add_command(label="SelectAll",command=show)
list2.add_command(label="Time/Date",command=show)
mymenu.add_cascade(label="Edit",menu=list2)
list3=Menu()
list3.add_command(label="Word Wrap",command=show)
list3.add_command(label="Font..",command=show)

mymenu.add_cascade(label="Format",menu=list3)
list4=Menu()
list4.add_command(label="Status Bar",command=show)

mymenu.add_cascade(label="View",menu=list4)
list5=Menu()
list5.add_command(label="View Help",command=show)
list5.add_command(label="About Notepapd",command=show)

mymenu.add_cascade(label="Help",menu=list5)
root.config(menu=mymenu)

e1=Entry()
e1.place(height=1000,width=1000)















root.mainloop()