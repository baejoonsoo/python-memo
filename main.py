import random

chose=input("가위, 바위, 보 ==>")


botChose=random.choice(['가위','바위','보'])

if (chose=="가위" and botChose=="보") or (chose=="바위" and botChose=="가위") or (chose=="보" and botChose=="바위"):
  print('이김')
elif (chose==botChose) or (chose== botChose) or (chose==botChose):
  print('비김')
else:
  print('짐')

