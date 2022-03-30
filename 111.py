a = (10, 20, 30, 20 , 30, 40)
print(a.index(10), a.index(20), a.index(30))
print(a.count(20), a.count(30), a.count(40))
print(10 in a)
b = tuple(i for i in range(0) if i % 2 == 0)
# 반복문과 조건문에 대해서는 뒤에서 배운다
# 0 부터 10 미만 수 중에서  2로 나누어 떨어지는 주슬 구하는 문장이다.
print(b)
