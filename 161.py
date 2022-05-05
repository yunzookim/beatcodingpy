import random

a, b = map(int, input().split())

c = random.randrange(a, b)

print(c) if a != b else print('no integer between two numbers')