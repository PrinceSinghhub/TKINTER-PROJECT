from tkinter import *
root = Tk()
root.geometry("1920x1080")
root.title("ajeet atm")
# todo variable
ammount=IntVar()
result=StringVar()
command=IntVar()
# todo logic
def ak():
    a=10000
    b=ammount.get()
    c=a-b
    c=str(c)
    d="available ammount =",c
    result.set(d)
def ajeet():
    if command.get()==0:
        a=Toplevel()
        a.geometry("1920x1080")

        a2 = Label(a, text="ENTER YOUR AMMOUNT", fg="gray", font="arial 20 bold")
        a2.place(x=300, y=300)
        a3 = Label(a, text="Your Transaction", fg="gray", font="arial 20 bold")
        a3.place(x=300, y=400)

        x = Entry(a, fg="red", font="arial 20 bold", relief=GROOVE)
        x.place(x=700, y=300)
        x = Entry(a, fg="red", font="arial 20 bold", relief=GROOVE)
        x.place(x=700, y=400)
        a.mainloop()

a=Label(root,text="ENTER YOUR AMMOUNT",fg="gray",font="arial 20 bold")
a.place(x=300,y=300)
a=Label(root,text="Your Transaction",fg="gray",font="arial 20 bold")
a.place(x=300,y=400)
a=Label(root,text="command",fg="gray",font="arial 20 bold")
a.place(x=300,y=500)

a=Entry(root,fg="green",font="arial 20 bold",relief=GROOVE,justify=RIGHT,textvariable=ammount)
a.place(x=700,y=300)
b=Entry(root,fg="green",font="arial 20 bold",relief=GROOVE,justify=RIGHT,textvariable=result)
b.place(x=700,y=400,width=450)

c=Entry(root,fg="green",font="arial 20 bold",relief=GROOVE,justify=RIGHT,textvariable=command)
c.place(x=700,y=500)

c=Button(root,text="PROCEED",font="arial 20 bold",command=ak)
c.place(x=900,y=600)

c=Button(root,text="Go",font="arial 20 bold",activebackground="green",command=ajeet)
c.place(x=500,y=600)
root.mainloop()


