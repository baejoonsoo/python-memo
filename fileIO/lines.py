inFile=None
inList=[]

inFile=open('/Users/baejunsu/Documents/python/fileIO/data/myData1.txt',encoding="UTF-8")


inList=inFile.readlines()

for inStr in inList:
  print(inStr)

inFile.close()