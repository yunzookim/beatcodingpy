int_1=0
int_2=3
long_1=12345678
long_2=0x142
float_1=0.0
float_2=1.35
complex_1=1j
complex_2=1+3j

print("변수 int_1과 int_2의 자료형은", type(int_1), type(int_2))
print('변수 long_1과 long_2의 자료형은', type(long_1), type(long_2))
print('변수 float_1과 float_2의 자료형은', type(float_1), type(float_2))
print('변수 complex_1과 complex_2의 자료형은', type(complex_1), type(complex_2))

# 0x로 시작하는 수는 16진수를, 0o로 시작하는 수는 8진수를 의미
# type() 괄호 안 변수의 자료형 파악 함수