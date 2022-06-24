from operator import length_hint


class Line:
  length=0
  def __init__(self,length):
    self.length=length
  
  def __add__(self,line):
    return self.length+line.length

l1= Line(1)
l2= Line(2)

print(l1+l2)