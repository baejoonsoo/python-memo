from tkinter import *

def blue():
    global color
    color = "blue"

def red():
    global color
    color = "red"

def thin():
    global pensize
    pensize = 1

def thick():
    global pensize
    pensize = 7

def onStart(e): #e 객체의 속성인 x, y값을 이용하여 좌표값 계산, 다른함수에서도 사용해서 전역함수로
    global prevx, prevy
    prevx = e.x
    prevy = e.y

def onDraw(e):
    global prevx, prevy, canvas, color, pensize
    curx = e.x
    cury = e.y
    canvas.create_line(prevx, prevy, curx, cury, width=pensize, fill=color)
    prevx = curx
    prevy = cury

w = Tk()
w.geometry("400x400+10+10") #낙서장의 크기 400x400, (10,10)위치에 뜨게 함

canvas = Canvas(w, width=400, height=350, bg="beige")
canvas.grid(row=0, column=0, columnspan=4)

bb = Button(w, text="파랑펜", bg="blue", fg="white", command=blue)
rb = Button(w, text="빨강펜", bg="red", fg="white", command=red)#command=red blue는 함수를 만들어야 사용가능
nb = Button(w, text="가는펜", command=thin)
kb = Button(w, text="굵은펜", command=thick)
bb.grid(row=1,column=0)
rb.grid(row=1,column=1)
nb.grid(row=1,column=2)
kb.grid(row=1,column=3)

canvas.bind('<ButtonPress-1>', onStart)
canvas.bind('<B1-Motion>', onDraw)
w.mainloop()