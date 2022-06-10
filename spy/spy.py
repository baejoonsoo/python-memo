secureFile=None
inStr,secure="",""

secureFile=open('/Users/baejunsu/Documents/python/spy/secure.txt','w',encoding="UTF-8")
origin=open('/Users/baejunsu/Documents/python/spy/origin.txt','r',encoding="UTF-8")

isStr=origin.readline()

for c in list(isStr):
  ordC=ord(c)
  secure+=chr(ordC+100)

secureFile.writelines(secure)

secureFile.close()
origin.close()