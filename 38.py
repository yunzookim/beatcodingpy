from doctest import REPORTING_FLAGS


a = 0b10110101 # 0b 2진수 변환 
b = 0b11011001 # 0b 2진수 변환 
c = a + b
print(a, b, c) 
print(bin(a&b), a&b) # 각 자릿 수를 비교하여 둘 다 1 이면, 1, 아니면 0을 변환
print(bin(a|b), a|b) # 각 자릿 수를 비교하여 둘 중 하나만 1이면 1을 변환
print(bin(a^b), a^b) # 각 자릿수를 비교하여 다르면 1, 같으면 0을 변환
print(bin(a >> 2), a >> 2) # 각 비트를 오른쪽으로 2번 옮긴다
print(bin(a >> 3), a >> 3) # 각 비틀르 오른쪽으로 3번 옮긴다
print(bin(a << 2), a << 2) # 각 비트를 왼쪽으로 2번 옮긴다
print(bin(-a), -a) # 1는 0으로, 0은 1으로 변환
