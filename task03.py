#!/usr/bin/python3.7

from common import count_match, \
                   get_integers_digits, \
                   multiply_digits

zen = \
'''1.Beautiful is better than ugly.
2.Explicit is better than implicit.
3.Simple is better than complex. (Has been edited from the Command-line)
4.Complex is better than complicated
5.Flat is better than nested.
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea.'''

# count words
print('count better', count_match(zen, 'better'))
print('count never', count_match(zen, 'never'))
print('count is', count_match(zen, 'is'))

# count words
print('count better', zen.count('better'))
print('count never', zen.count('never'))
print('count is', zen.count('is'))

print(zen.upper())
print(zen.replace('i', '&'))

# get number digits
number = 2135
digits = get_integers_digits(number)
print('digits', digits)

# multiply digits
print('multiply digits result', multiply_digits(digits))

# reverse digits
digits.reverse()
print('reversed digits', digits)

#sort digits
digits.sort()
print('sorted digits', digits)

# switch values
x = 44
y = 55
print('x =', x, 'y =', y)
print('          x               y')
print('         ', id(x), id(y), )
x = x + y; print('x = x + y', id(x), id(y))
y = x - y; print('y = x - y', id(x), id(y))
x = x - y; print('x = x - y', id(x), id(y))
print('x =', x, 'y =', y)

# switch values
x, y = y, x
print('x =', x, 'y =', y)
