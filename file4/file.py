outFile=None
outStr=''

outFile=open('/Users/baejunsu/Documents/python/file4/data1.txt','w')

while True:
  outStr=input("내용 입력 ==> ")
  if outStr !="":
    outFile.writelines(outStr+"\n")
  else:
    break;

outFile.close()