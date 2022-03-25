sum = 0

while True:
  cmd, num = input('실행할 연산과 피연산자를 입력하세요 -> ').split()
  num=int(num)

  if cmd=='+':
    sum+=num
  elif cmd=='-':
    sum-=num
  elif cmd=='/':
    sum/=num
  elif cmd=='//':
    sum //=num
  elif cmd=='*':
    sum*=num
  elif cmd == '**':
    sum **=num
  elif cmd =='%':
    sum %=num
  
  print(f'현재 값 : {sum}')