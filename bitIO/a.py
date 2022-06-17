from tkinter import *


def loadImage(fname):
  global inImage,XSIZE,YSIZE
  fp=open(fname,'rb')

  for i in range(0,XSIZE):
    tempList=[]
    for k in range(0,YSIZE):
      data=int(ord(fp.read()))
      tempList.append(data)
  inImage.append(tempList)

  fp.close()

def display(image):
  global XSIZE,YSIZE
  for i in range(0,XSIZE):
    for k in range(0,YSIZE):
      data=image[i][k]
      paper.put("#%02x%02x%02x" % (data,data,data),(k,i))


window=None
canvas=None
XSIZE,YSIZE=256,256
inImage=[]

window=Tk()
window.title("흑백 사진 보기")
canvas=Canvas(window,height=XSIZE,width=YSIZE)

paper=PhotoImage(width=XSIZE,height=YSIZE)
canvas.create_image((XSIZE/2,YSIZE/2), image=paper,state="normal")

# filename="RAW/tree.raw"
filename="/Users/baejunsu/Documents/python/bitIO/flower1024.raw"
loadImage(filename)

display(inImage)


canvas.pack()
window.mainloop()