inFp,outFp=None,None
inStr=''

inFp=open('/Users/baejunsu/Documents/python/file5','r')
outFp=open('/Users/baejunsu/Documents/python/file5','w')

inList=inFp.readlines()
for inStr in inList:
  outFp.writelines(inStr)

inFp.close()
outFp.close()