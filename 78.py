from email.policy import strict


string = "Hello, My name is Haemin Park"
print(string.upper())
print(string.lower())
print(string.title())
print(len(string))
print()
print(string.count('i'))
print(string.endswith('k'))
print(string.startswith('h'))
print(string.lower().startswith('h'))
print()

string_1 = string.split()
string_2 = string.split(',')
print(string_1)
print(string_2)