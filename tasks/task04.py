#!/usr/bin/python3.7

from common import get_integer_from_input, \
                   factorial_recursion, \
                   get_integers_digits, \
                   string_words_reverse, \
                   make_wellcome_message

# test bigger
a = get_integer_from_input("enter integer 'a' for biggest test ")
b = get_integer_from_input("enter integer 'b' for biggest test ")

if(a == b):
    pass
elif(a < b):
    print(b, " is bigger ")
else:
    print(a, " is bigger ")

# test odd
a = get_integer_from_input("enter integer for parity check ")

if a % 2:
    print(a, "even")
else:
    print(a, "odd")

n = 5
print('n = {}, n! = {}'.format(n, factorial_recursion(n)))

# number to string
number = 2135
print('number =', number, 'digits =', get_integers_digits(number))

# reverse words in string
print(string_words_reverse('hello world this is program'))

# secret message
print(make_wellcome_message('johnny'))
