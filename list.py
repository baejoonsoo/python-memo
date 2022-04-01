myList = [30,10,20]
print(f'현재 리스트 : {myList}')

myList.append(40)
print(f'append(40) 후의 리스트 : {myList}')

print(f'pop()으로 추출한 값 : {myList.pop()}')
print(f'pop() 후의 리스트 : {myList}')

myList.sort()
print(f'sort() 후의 리스트 {myList}')

myList.reverse()
print(f'reverse() 후의 리스트 {myList}')

print(f'20값의 위치 : {myList.index(20)}')

myList.insert(2,222)
print(f'insert(2,222) 후의 리스트 : {myList}')

myList.remove(222)
print(f'remove(222) 후의 리스트 : {myList}')

myList.extend([77,88,77])
print(f'extend[77,88,77]) 후의 리스트 : {myList}')

print(f"77값의 개수 : {myList.count(77)}")