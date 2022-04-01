numList=[]

for i in range(5):
  num=int(input('넣고 싶은 숫자를 입력하세요 : '))
  numList.append(num)

sum=0

for num in numList:
  sum+=num

print(sum)