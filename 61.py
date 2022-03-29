from cgitb import text


text_1 = '문자열에서 \n을 쓰면 줄바꿈이 되고 \t를 사용하면 탭 공백이 넣어진다'
text_2 = "문자열에서 '를 쓰려면 문자열을 큰 따옴표로 선언하거나 \'나 \"를 쓰면 된다"
text_3 = '마찬가지로 작은 따옴표 내에서 "는 그냥 출력된다'

print(text_1)
print(text_2)
print(text_3)