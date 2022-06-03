import math


toeic=[510,630,750,780,620,930,650,840,670]

def frequency(toeic):
  scoreList=[0 for _ in range(9)]

  for score in toeic:
    scoreList[(score//100)-1]+=1
  print(scoreList)
  return scoreList

def max_frequency(counters):
  maxCount = max(counters)
  # pass
  yield counters.index(maxCount)+1
  yield maxCount
  

def min_frequency(counters):
  minCount = min(filter(lambda score:score!=0, counters))
  
  yield counters.index(minCount)+1
  yield minCount


counters=frequency(toeic)

scoreBase,maxCount=max_frequency(counters)
print(f'가장 많은 빈도 : {scoreBase}, 빈도수 : {maxCount}')

scoreBase,minCount=min_frequency(counters)
print(f'가장 적은 빈도 : {scoreBase}, 빈도수 : {minCount}')
