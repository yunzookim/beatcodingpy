from lib2to3.pgen2.token import RPAR
from traceback import print_tb


X, Y, Z = 1, 2, 1.5

print(X)
print(X+Y)
print(X+Y+Z)
#print(2X) 곱셈을 하고 싶다면 * 를 사용해야 함
print(2*X)
print(2.0*X)
print(X -1.0)
print(X-1)
print(Z-0.5)
#print(XZ) 문자열끼리 곱셈은 불가능?
print(X*Z)