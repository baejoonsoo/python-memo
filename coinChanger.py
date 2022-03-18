money = int(input('교환할 돈은 얼마? : '))

coin500 = (money//500)
money -= (coin500*500)

coin100 = (money//100)
money -= (coin100*100)

coin50 = (money//50)
money -= (coin50*50)

coin10 = (money//10)
money -= (coin10*10)

print(f'500원짜리 --> {coin500}개')
print(f'100원짜리 --> {coin100}개')
print(f'50원짜리 --> {coin50}개')
print(f'10원짜리 --> {coin10}개')
print(f'바꾸지 못한 돈 --> {money}개')