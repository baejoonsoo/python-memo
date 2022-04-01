import random

attempts = 5

userName=input('네 이름은 뭐니?\n')
print(f'반가워. {userName}. 내가 1부터 30사이의 수를 가지고 있어.\n맞춰봐')

while True:
  computerNumber = random.randint(1,30)
  gameClear=False

  print(f'\n\n{attempts}번 안에 맞혀야 돼')

  for i in range(attempts):
    userNum=int(input('추측한 숫자를 입력하세요->'))

    if userNum==computerNumber:
      print(f'{i+1}번만에 맞췄어요!! 축하해요')
      gameClear=True
      break
    elif userNum >30 or userNum<1:
      print('...내가 분명 1부터 30사이라고 했을텐데?')
    elif userNum > computerNumber:
      print('추측한 숫자가 컴퓨터가 가진 숫자보다 커요')
    else:
      print('추측한 숫자가 컴퓨터가 가진 숫자보다 작아요')
  
  isTry= input('\n\n게임을 다시 할까요?(YES or NO) : ')
  
  if isTry=='YES':
    if gameClear:
      attempts-=1
    else:
      attempts+=1
    
    continue
  elif isTry=="NO":
    break
  else:
    print('허용되지 않는 입력')
    exit()
    