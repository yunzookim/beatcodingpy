import random
from traceback import print_tb

a = []

while len(a) <= 3:
    i = random.randrange(10, 20)
    a.append(i)
    if len(a) > 3:
        print('4가지 수: ', a)
        break

average = sum(a)/4
print('평균: ', average)

print('Big') if average >= 15 else print('Small')