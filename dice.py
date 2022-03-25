import random


attempts = 0

while True:
  attempts+=1
  n1 = random.randint(1,6)
  n2 = random.randint(1,6)
  n3 = random.randint(1,6)

  if n1==n2==n3:
    print(n1,n2,n3)
    print(attempts)
    break