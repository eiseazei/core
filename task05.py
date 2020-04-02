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
    print('\ntesting 3 values for min and max')
    values = []

    for i in range(3):
        values.insert(i, get_integer("enter integer value: "))

    print('result is min = {}, max {}'.format(min(values), max(values)))
    
def what_number():
    print('\ntesting values from 1 to 11')

    for i in range(1,11):
        if i % 2 == 0:
            print(i, 'even value')
        elif i % 3 == 0:
            print(i, 'multiple 3')
        else:
            print(i, 'not multiple 2 or 3')

def fact(value):
    # result = 1

    # for i in range(1, value + 1):
    #     result *= i

    result, i = 1, 1
    while i <= value:
        result *= i
        i += 1

    return result

def parse_login():
    print('\nparsing login')
    
    state = False
    count = 3
    login = 'abc123'

    while count > 0:
        print("enter login (you have", count, "tries): ")
        value = input()
        count -= 1

        if login == value:
            state = True
            break
    else:
        print("you failed to login")
    
    return state

def parse_integers():
    print('\ntesting input numbers')
    value = 1

    while value > 0:
        value = get_integer()
    else:
        print('got number less than 1')

def parse_pack_integers():
    print('\ntesting up to 5 integers')

    count = get_integer("enter how many integers need to be tested: ")

    if count > 0 and count < 6:
        i = 0
        value = 1

        while count > i and value > 0:
            value = get_integer()
            count -= 1
    else:
        print('provided invalid count value')

def test_prime():
    print('\ntesing for prime')
    for i in range(10, 31):
        prime = True

        for j in range(2, 10):    
            if i % j == 0:
                print('{} not prime, {} * {}'.format(i, j, i // j))
                prime = False
                break
        if prime:
            print('{} is prime'.format(i))

def trick_sort():
    s = 'hello world this is program'
    l = s.split()
    l.sort(key = lambda chunk : len(chunk))
    # print(l)

    li = [0,4,6,1,3]

    # for i in range(len(li) - 1):
    #     for j in range(i + 1):
    #         if li[j] > li[j + 1]:
    #             li[j], li[j + 1] = li[j + 1], li[j]

    
    # dd = [ li[ li.index(li[j + 1]) ]
    #     for i in range(len(li) - 1)
    #         for j in range(i + 1)
    #             if li[j] > li[j + 1]
    # ] 


    
    print(li)



if __name__ == "__main__":
    #---------------------------------------------------------------------------
    # success
    # print('make it?', success_traver(55))

    #---------------------------------------------------------------------------
    # print('enought', enough(10, 5, 5))
    # print('enought', enough(100, 60, 50))
    # print('enought', enough(20, 5, 5))

    #---------------------------------------------------------------------------
    # banjo
    # print(banjo())

    #---------------------------------------------------------------------------
    # yes/no
    # print('yes no maybe i dont know', yes_no(3))
    
    #---------------------------------------------------------------------------
    # sheep
    array = [True,  True,  True,  False,
             True,  True,  True,  True,
             True,  False, True,  False,
             True,  False, False, True,
             True,  True,  True,  True,
             False, False, True,  True]
    # print('sheeps', sheep(array))

    #---------------------------------------------------------------------------
    # tail vs body
    # print(correct_tail('Fox', 'x'))
    # print(correct_tail('Emu', 't'))

    #---------------------------------------------------------------------------
    # min max in range
    # get_min_max()
    
    #---------------------------------------------------------------------------
    # testing integers
    # what_number()

    #---------------------------------------------------------------------------
    # get fact
    # value = 5
    # print('\nfactorial of', value, 'is', fact(value))
    
    #---------------------------------------------------------------------------
    # parse login
    # print('login status:', parse_login())

    #---------------------------------------------------------------------------
    # test input integer
    # parse_integers()
    
    #---------------------------------------------------------------------------
    # test pack input integer
    # parse_pack_integers()

    #---------------------------------------------------------------------------
    # test prime
    # test_prime()

    #---------------------------------------------------------------------------
    # trick sort
    trick_sort()