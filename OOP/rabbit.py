class Rabbit:


  def __init__(self):
    self.x=0
    self.y=0

  def moveRabbit(self,x,y):
    self.x+=x
    self.y+=y
    
    yield self.x
    yield self.y

rabbit=Rabbit()

while True:
  x=int(input("토끼가 이동할 X좌표 ==> "))
  y=int(input("토끼가 이동할 Y좌표 ==> "))
  x,y =rabbit.moveRabbit(x,y)

  print(f"토끼가 이동한 좌표({x}, {y})")