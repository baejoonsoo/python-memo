inFile=None
inStr=''

inFile=open('/Users/baejunsu/Documents/python/fileIO/data/myData1.txt',encoding="UTF-8")


while True:
  inStr=inFile.readline()
  if inStr=="":
    break
  print(inStr,end='')

inFile.close()