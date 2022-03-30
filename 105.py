from cgi import print_arguments


myList = ['A', [5, 2], 'music']
print(len(myList))
print(myList[1])

myList.append(10)
print(myList.pop())
print(sum(myList[1]))
print(myList)