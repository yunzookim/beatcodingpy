from cgi import print_arguments


A = {1, 2, 3, 5, 6, 8}
B = {1, 3, 4, 5, 6, 7}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))