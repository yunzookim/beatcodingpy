a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = []

# 리스트 a의 요소에 대한 반복문. 이 경우, i는 a의 요소가 된다.
for i in a :
    if (len(i) == 5):
        b.append(i)

print(b)
        