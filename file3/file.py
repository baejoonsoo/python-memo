outFile=None
outStr=''

outFile=open('/Users/baejunsu/Documents/python/file3/myData2.txt',"w")

outStr="abc"
outFile.writelines(outStr+"\n")

outStr="qwert"
outFile.writelines(outStr+"\n")

outStr="zxcv"
outFile.writelines(outStr+"\n")

outFile.close()