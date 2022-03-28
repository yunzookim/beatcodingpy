a = 0b11101100
b = 0b10111011

print(bin(a&b), a&b) # AND연산자: 각 자릿수를 비교하여 둘 다 1이면 1, 아니면 0을 변환
print(bin(a^b), a^b) # XOR연산자: 각 자릿수를 비교하여 다르면 1, 같으면 0을 변환
print(bin(a|b), a|b) # OR연산자: 각 자릿수를 비교하여 둘 중 하나만 1이면 1을 변환
print(bin((a+b)>>2), (a+b)>>2) 
print(bin(~a), ~a) # NOT연산자: 1을 0으로, 0은 1으로 변환

