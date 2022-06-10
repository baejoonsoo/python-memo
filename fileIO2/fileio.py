file=open('/Users/baejunsu/Documents/python/fileIO2/data.txt',encoding="UTF-8")

inList=file.readlines()

for i,str in enumerate(inList):
  print(i+1, str,end='')