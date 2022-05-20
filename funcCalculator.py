def plus(acc, num):
  return acc+num

def minus(acc,num):
  return acc-num

def multiply(acc,num):
  return acc*num

def division(acc, num):
  if num==0:
    print('0으로는 나눌 수 없습니다')
    exit()
  return acc%num

def squared(acc,num):
  return acc**num

def Calculation():
  sign=input('계산 입력(+, -, *, /) : ')

  num1=int(input('첫 번째 숫자 입력 : '))
  num2=int(input('두 번째 숫자 입력 : '))

  res=0

  if sign=='+':
    res=plus(num1,num2)
  elif sign=='-':
    res=minus(num1,num2) 
  elif sign=='*':
    res=multiply(num1,num2) 
  elif sign=='/':
    res=division(num1,num2) 
  # elif sign=='^':
  #   plus(num1,num2)

  print(f'계산 결과 : {res}')


Calculation()
