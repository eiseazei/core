#!/usr/bin/python3.7

import sys
from task01 import get_integer

def success_traver(distance):
    rate = 25
    count = 2

    return True if rate * count >= distance else False

def enough(ca, on, wait):
    return 1 if (ca - on) >= wait else 0

def banjo():
    print('\ntesting name')
    name = input('Are you playing banjo? Enter your name: ')
    if len(name) == 0:
        exit("error: you doesn't provide name!")

    if name[0] == 'R' or name[0] == 'r':
        msg = ' plays banjo'
    else:
        msg = ' does not play banjo'
    
    return name + msg

def yes_no(val):
    print('\ntesting Yes No')
    return 'Yes' if val else 'No'

def sheep(sheeps):
    print('\ncounting sheeps')
    count = 0

    for sheep in sheeps:
        if sheep: count += 1
    
    return count

def correct_tail(body, tail):
    print('testing tail in', body, tail)
    if len(tail) > len(body):
        sys.exit("error: tail bigger than body")
    
    sub = body[-len(tail) : ]
    
    if sub == tail:
        return True
    else:
        return False

def get_min_max():
    print('testing 3 number for min and max')
    values = []

    for i in range(3):
        values.insert(i, get_integer("enter integer value: "))

    print('result is min = {}, max {}'.format(min(values), max(values)))
    
def what_numbers():
    print('testing values from 1 to 11')

    for i in range(1,11):
        if i % 2 == 0:
            print(i, 'even value')
        elif i % 3 == 0:
            print(i, 'multiple 3')
        else:
            print(i, 'not multiple 2 or 3')

def fact(number):
    # result = 1

    # for i in range(1, number + 1):
    #     result *= i

    result, i = 1, 1
    while i <= number:
        result *= i
        i += 1

    return result


if __name__ == "__main__":
    #---------------------------------------------------------------------------
    # success
    print('make it?', success_traver(55))

    #---------------------------------------------------------------------------
    print('enought', enough(10, 5, 5))
    print('enought', enough(100, 60, 50))
    print('enought', enough(20, 5, 5))

    #---------------------------------------------------------------------------
    # banjo
    # print(banjo())

    #---------------------------------------------------------------------------
    # yes/no
    print('yes no maybe i dont know', yes_no(3))
    
    #---------------------------------------------------------------------------
    # sheep
    array = [True,  True,  True,  False,
             True,  True,  True,  True,
             True,  False, True,  False,
             True,  False, False, True,
             True,  True,  True,  True,
             False, False, True,  True]
    print('sheeps', sheep(array))

    #---------------------------------------------------------------------------
    # tail vs body
    print(correct_tail('Fox', 'x'))
    print(correct_tail('Emu', 't'))

    #---------------------------------------------------------------------------
    # min max in range
    print()
    get_min_max()
    
    #---------------------------------------------------------------------------
    # testing numbers
    print()
    what_numbers()

    #---------------------------------------------------------------------------
    # get fact
    number = 5
    print('\nfactorial of', number, 'is', fact(number))

