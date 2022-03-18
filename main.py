americano=2500
latte=3000
cappuccino=3000


americanoNumber=int(input('americano를 얼마나 사실건가요? : '))
latteNumber=int(input('latte를 얼마나 사실건가요? : '))
cappuccinoNumber=int(input('cappuccino를 얼마나 사실건가요? : '))

money= int(input('돈을 넣어주세요!! : '))

needfulMoney= (americano*americanoNumber)+(latte*latteNumber)+(cappuccino*cappuccinoNumber)

if needfulMoney>money:
  print(f'돈이 부족합니다!!\n부족한 금액 :{needfulMoney-money}')
else:
  returnMoney= format((money-needfulMoney), ',')
  print(f'잔돈은 ₩{returnMoney} 입니다')