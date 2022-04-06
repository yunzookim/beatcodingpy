A = {1, 3, 4, 6}
B = {2, 3, 5, 6}

print(A^B)
print(A | B)
print((A ^ B) | (A&B))
print(A <= {1, 3, 4, 5, 6})
print(A.difference(B) <= {1, 2, 4})