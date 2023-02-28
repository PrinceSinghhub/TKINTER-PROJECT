from tkinter import *
root = Tk()
root.geometry("1920x1080")
root.title("codex")
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
    d="available ammount ="+c
    result.set(d)

a=Label(root,text="ENTER YOUR AMMOUNT",fg="gray",font="arial 20 bold")
a.place(x=300,y=300)
a=Label(root,text="Your Transaction",fg="gray",font="arial 20 bold")
a.place(x=300,y=400)


a=Entry(root,fg="green",font="arial 20 bold",relief=GROOVE,justify=RIGHT,textvariable=ammount)
a.place(x=700,y=300)
b=Entry(root,fg="green",font="arial 20 bold",relief=GROOVE,justify=RIGHT,textvariable=result)
b.place(x=700,y=400)



c=Button(root,text="PROCEED",font="arial 20 bold",command=ak)
c.place(x=900,y=600)
root.mainloop()


