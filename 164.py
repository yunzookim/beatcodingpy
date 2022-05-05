import random

cars = ['Hyundai', 'Kia', 'BMW', 'Benz']
print('original: ',cars)
random.shuffle(cars)
print('change: ', cars)
print('Ture!') if cars[0] == 'Hyundai' else print('False!')

