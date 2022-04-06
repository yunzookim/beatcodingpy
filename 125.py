from cgi import print_arguments


myset = set([1, 2, 3, 4, 5])
print(myset)
B = {1, 3, 4, 7, 'Ferrari', 11}
C = myset ^ B
myset = C
print(myset)