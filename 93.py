from tokenize import Intnumber


a, b, c, d = input("네 수를 입력하세요 : ").split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
aver = (a+b+c+d)/4
disp = ((a-aver)*(a-aver)+(b-aver)*(b-aver)+(c-aver)*(c-aver)+(d-aver)*(d-aver))/4
print("평균 : ", aver)
print("분산 : ", disp)