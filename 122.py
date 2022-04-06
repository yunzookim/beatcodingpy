from doctest import REPORTING_FLAGS
from re import M


mySet = {1, 3, 5}
print(mySet)
mySet.add('A')
print(mySet)
mySet.update({1, 3}, [2, 3])
print(mySet)
print() # update는 각 객체의 요소를 셋에 추가한다

print(mySet.pop())
print(mySet)
print(mySet.pop())
mySet = {'apple', 'melon', 'strawberry', 'grape'}
print(mySet)
print()

mySet.discard('strawberry')
print(mySet)
mySet.remove('grape')
print(mySet)

mySet.clear() # A.issuperset({20, 30, 50}) 과 동일
print(mySet)