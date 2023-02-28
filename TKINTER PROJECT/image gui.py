from tkinter import *
root=Tk()
root.geometry("1080x720")
photo=PhotoImage(file="h.png")
lable=Label(image=photo)
lable.pack()
root.mainloop()