animals = {'cat', 'dog'}
print('cat' in animals)
print('fish' in animals)

animals.add('fish')
print(len(animals))

animals.add('cat')
print(len(animals)) # 중복은 더해지지 않음