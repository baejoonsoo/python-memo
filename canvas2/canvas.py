from curses import window
import imp
from tkinter import *

window = Tk()

def quit():
  pass

button1=Button(window,text="파이썬 종료",fg="red",command=quit)
button1.pack()

window.mainloop()