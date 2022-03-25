import random

computerNumber = random.randint(0,100)
attempts = 0

while True:
  userNum=int(input('컴퓨터가 정한 숫자를 찾아보세요!! -> '))
  attempts+=1

  if userNum==computerNumber:
    print(f'컴퓨터가 정한 숫자는 {computerNumber}였습니다!!\n 찾기까지 걸린 횟수 : {attempts}')
    exit()
  else:
    if userNum>computerNumber:
      print('컴퓨터의 숫자 보다 큽니다!!\n')
    else:
      print('컴퓨터의 숫자 보다 작습니다!!\n')