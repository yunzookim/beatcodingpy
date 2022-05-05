num = int(input('enter the number: '))
print('짝수' if num % 2 == 0 else '홀수')
if (num>0) :
    print('양수')
else : print('음수' if num<0 else '0') 
print('3의 배수' if num % 3 == 0 else '3의 배수 아님')
print('5의 배수' if num % 5 == 0 else '5의 배수 아님')