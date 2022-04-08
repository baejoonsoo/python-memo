dict={}

while True:
  name=input('입력 물품 => ')
  if name=='z':
    break;
  num=int(input('재고량 => '))
  dict[name]=num

print("=== 물품의 재고량 확인 ===")

while True:
  name=input('칮을 물품 => ')

  if name in dict:
    print(f'{dict.get(name)}개 남았어요')
  else:
    print('그 물품은 없어요')