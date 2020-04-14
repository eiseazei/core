#!/usr/bin/python3.7

from common import summation, \
                   list_animals, \
                   double_chars

# summation
print('sum is {:d}'.format(summation(100)))

# list animals
print('{:s}'.format(list_animals(['dog', 'cat', 'elephant'])))

# repeat message characters
print(double_chars('String'))