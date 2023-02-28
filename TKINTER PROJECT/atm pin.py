from tkinter import *
root = Tk()
root.geometry("1920x1080")
root.title("codex")
# todo variable
aj=StringVar()
Balance=StringVar()
# todo logic
def ak():
    x="aj123"
    bal=str(10000)
    y=aj.get()
    if x == y:
        z="BALANCE: "+bal
        Balance.set(z)
a=Label(root,text="ENTER YOUR PIN",fg="gray",font="arial 20 bold")
a.place(x=300,y=300)
a=Label(root,text="Your Balance",fg="gray",font="arial 20 bold")
a.place(x=300,y=400)


a=Entry(root,fg="green",font="arial 20 bold",relief=GROOVE,justify=RIGHT,textvariable=aj)
a.place(x=700,y=300)
b=Entry(root,fg="green",font="arial 20 bold",relief=GROOVE,justify=RIGHT,textvariable=Balance)
b.place(x=700,y=400)


c=Button(root,text="PROCEED",font="arial 20 bold",command=ak)
c.place(x=900,y=600)
root.mainloop()

