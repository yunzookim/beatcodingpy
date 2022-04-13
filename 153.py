# a = int(input('enter 1st number : '))
# b = int(input('enter 2nd number : '))

# if a + b >= 0.5 * a * b :
#     print('Nice')
# else :
#     print('Bad')


a, b = map(int, input('enter 1st, 2nd number : ').split())

print('Nice') if a + b >= 0.5 * a * b else print('Bad')