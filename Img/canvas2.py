from tkinter import *

window=Tk()

photo=PhotoImage(file="/Users/baejunsu/Documents/python/Img/gif/cat2.gif")

label1=Label(window,image=photo)
label1.pack()

window.mainloop()