from tkinter import *
root =Tk()
root.geometry("1920x1080")
def clear():
    mtxt.delete(0.1,END)

mtxt=Text(root,width=60,height=20,font=("Helvetica",10))
mtxt.pack(pady=20)
pbuton=Frame(root)
pbuton.pack()
cb=Button(pbuton,text="clear screen",command=clear)
cb.grid(row=0,column=0)
root.mainloop()