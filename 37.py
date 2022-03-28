int_1 = 1
int_2 = 3
long_1 = 2
float_1 = 0.5
complex_1 = 1 + 1j

A = int_1 + long_1
B = int_2 + float_1
C = float_1 + complex_1

print(A, type(A)) #int + int 
print(B, type(B)) # int + float
print(C, type(C)) # float + complex

# 보다 상위 개념의 변수가 최종 선언됨