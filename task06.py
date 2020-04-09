#!/usr/bin/python3.7

from common import calculate_mean, \
                   make_abs, \
                   sum_of_digits, \
                   point, \
                   sticks, \
                   filter_words, \
                   create_array

from area import area_of_shape

# mean value
print('numbers mean test:', calculate_mean(0,1,2,3,4))

# abs value
print('abs value -1:', make_abs(-1))

# shape area
area_of_shape()

# digits sum
print('intiger digits sum:')
print(sum_of_digits())

# distance between points
p1 = point(3, 4)
p2 = point(0, 0)
print('distance between points: \n  {}\n  {}\n  is {}'.format(p1, p2, p1 - p2))

# 21 sticks
sticks()

# filter words
filter_words('HELLO CAN YOU HEAR ME')

# fix create_array
print('create array', create_array(5))
