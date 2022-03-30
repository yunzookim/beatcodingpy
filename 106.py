from cgi import print_arguments
from tempfile import SpooledTemporaryFile


sports = ['soccer']
print(sports)
sports.extend(['baseball', 'hockey'])
print(sports)
sports.insert(1, 'tennis')
print(sports)
sports.sort()
print(sports)
print(sports[-1])
sports.remove('tennis')
print(sports)