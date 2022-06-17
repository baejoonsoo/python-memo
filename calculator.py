sum=0

while True:
  print(f"\n현재값 : {sum}")
  st=input('작업 명령 입력: ')

  if st=='x':
    break
  if len(st.split())!=2:
    print('잘못된 작업 명령!!')
  else:
    op,num=st.split()

    if op=='+':
      sum+=int(num)
    elif op=='*':
      sum*=int(num)
    elif op=='/':
      if int(num)==0:
        print('잘못된 작업 명령(0으로 나누기)!!')
      else:
        sum/=int(num)
    elif op=='%':
      sum%=int(num)
    elif op=='=':
      sum=int(num)
    else:
      print('잘못된 작업 명령!!')
