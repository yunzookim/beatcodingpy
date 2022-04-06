dict_D = {'수학': 76, '과학': 89, '영어': 93}
dict_J = {'수학': 88, '과학': 87, '영어': 100}
dict_S = {'수학': 86, '과학': 93, '영어': 82}

a = sum(dict_D.values()) / len(dict_D)
b = sum(dict_J.values()) / len(dict_J)
c =sum(dict_S.values()) / len(dict_S)

d = (a+b+c) /3

print(a)
print(b)
print(c)
print(d)