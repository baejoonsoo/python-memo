from tkinter import *
from tkinter import messagebox

def clickImage(e):
  messagebox.showinfo("마우스","마우스 왼쪽 버튼이 클릭됨")

window=Tk()
window.geometry("400x400")


photo=PhotoImage(file="gif/cat2.gif")
label1=Label(window,image=photo)

label1.bind("<Button>",clickImage)

label1.pack(expand=1,anchor=CENTER)
window.mainloop()