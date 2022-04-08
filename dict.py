import operator


trainDIc,trainList={},[]

trainDIc={'thomas':'토마스','edward':'애드워드','henry':'핸리'}
trainList=sorted(trainDIc.items(),key=operator.itemgetter(0))

print(trainList)