import random


for i in range(10):
  computerNumber = random.randint(1,5)
  userNum=int(input('컴퓨터가 정한 숫자를 찾아보세요!! -> '))

  if userNum==computerNumber:
    print('찾음')
    exit()
  else:
    continue

print('기회 끝')