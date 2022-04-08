num=list()

for i in range(5):
  num.append(int(input('평가 점수 : ')))

sum=0
for n in num:
  sum+=n

print(sum/len(num))
