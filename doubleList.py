list1=[]
list2=[]
value=1

for i in range(3):
  for k in range(4):
    list1.append(value)
    value+=1
  list2.append(list1)
  list1=[]

for i in range(3):
  for k in range(4):
    print(f'{list2[i][k]}',end='')