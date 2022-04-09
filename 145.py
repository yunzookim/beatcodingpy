# num = 13
# # 변수 num에 저장된 값 2 또는 3의 배수인가?
# result1 = (num % 2 == 0) | (num % 3 == o)
# print("2 또는 3의 배수인가? ", result1)

# num = 13
# result1 = (num % 2 == 0) | (num % 3 == 0)
# print("2 또는 3의 배수인가? ", result1)

# num = 13
# if ((num % 2 == 0) | (num % 3 == 0)) :
#     print("2 또는 3의 배수인가? True")
# else :
#      print("2 또는 3의 배수인가? False")

num = 13
print("2 또는 3의 배수인가? ", end="")
if (num % 2 == 0) | (num % 3 == 0) :
    print("True")
else: print("False")
