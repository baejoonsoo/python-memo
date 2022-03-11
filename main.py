menu={
  "coffee":{
    "buy":500,
    "sell":1800
  },
  "kimBab":{
    "buy":900,
    "sell":1400
  },
  "bbaU":{
    "buy":800,
    "sell":1800
  },
  "doSirock":{
    "buy":3500,
    "sell":4000
  },
  "cola":{
    "buy":700,
    "sell":1500
  },
  "saeOuKkang":{
    "buy":500,
    "sell":1800
  }
}

def getMenu():
  return 1,2

def sell():
  menu, price = input().split()
  price = int(price)

# def buy():

  
while True:
  action = input()

  # if action == 'buy':
    # buy()
  if action == 'sell':
    sell()
  elif action == 'break':
    exit()
  else:
    print('unknown input')


