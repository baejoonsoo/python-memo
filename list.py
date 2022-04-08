
import random

winCount=[0,0,0]

for i in range(10000):
  com1= random.choice(['가위','바위','보'])
  com2= random.choice(['가위','바위','보'])

  # com1 win
  if (com1=='가위' and com2=='보') or (com1=='바위' and com2=='가위') or (com1=='보' and com2=='바위'):
    winCount[0]+=1
  elif (com2=='가위' and com1=='보') or (com2=='바위' and com1=='가위') or (com2=='보' and com1=='바위'):
    #com2 win
    winCount[1]+=1
  else:
    winCount[2]+=1


if winCount[0]>winCount[1]:
  print('com1 win!!')
elif winCount[0]<winCount[1]:
  print('com2 win!!')
else:
  print('no winner')

print(winCount)