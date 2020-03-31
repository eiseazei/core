#!/usr/bin/python3.7

import sys

def success_traver(distance):
    rate = 25
    count = 2

    return True if rate * count >= distance else False

def enough(ca, on, wait):
    return 1 if (ca - on) >= wait else 0

def banjo():
    name = input('Are you playing banjo? Enter your name: ')
    if len(name) == 0:
        exit("error: you doesn't provide name!")

    if name[0] == 'R' or name[0] == 'r':
        msg = ' plays banjo'
    else:
        msg = ' does not play banjo'
    
    return name + msg

def yes_no(val):
    return 'Yes' if val else 'No'

def sheep(sheeps):
    count = 0

    for sheep in sheeps:
        if sheep: count += 1
    
    return count

def correct_tail(body, tail):
    if len(tail) > len(body):
        sys.exit("error: tail bigger than body")
    
    sub = body[-len(tail) : ]
    
    if sub == tail:
        return True
    else:
        return False

if __name__ == "__main__":
    # --------------------------------------------------------------------------
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
