import random

def getNum(numList):
  lottoNum=0
  while lottoNum in numList or not lottoNum :
    lottoNum=random.randint(1,45)
  return lottoNum

def randomNumber():
  numList=[]
  for i in range(6):
    numList.append(getNum(numList))
  return numList

num = randomNumber()

print(num)