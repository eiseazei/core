#!/usr/bin/python3.7

from common import is_travel_successfull, \
                   is_available_bus_sits, \
                   test_banjo_player_name, \
                   test_input_yes_no, \
                   counting_sheep, \
                   is_correct_tail, \
                   get_min_and_max, \
                   what_number, \
                   factorial_loop, \
                   make_login_procedure, \
                   parse_integers, \
                   parse_pack_integers, \
                   is_prime

# success
print('make it with {} galons? {}'.format(55, is_travel_successfull(55)))


print('is enought places?', is_available_bus_sits(10, 5, 5))
print('is enought places?', is_available_bus_sits(100, 60, 50))
print('is enought places?', is_available_bus_sits(20, 5, 5))

# banjo
print('banjo test: {}'.format(test_banjo_player_name()))

# yes/no
print('yes/no test for 3 is {}'.format(test_input_yes_no(3)))

# sheep
sheeps = [True,  True,  True,  False,
            True,  True,  True,  True,
            True,  False, True,  False,
            True,  False, False, True,
            True,  True,  True,  True,
            False, False, True,  True]
print('total sheeps {}'.format(counting_sheep(sheeps)))

# tail vs body
print('tail test Fox x', is_correct_tail('Fox', 'x'))
print('tail test Emu t', is_correct_tail('Emu', 't'))

# min max in range
print('min max test:')
get_min_and_max()

# testing integers
print('what number test:')
what_number()

# get fact
n = 5
print('n = {}, n! = {}'.format(n, factorial_loop(n)))

# parse login
print('login status:', make_login_procedure())

# test input integer
print('negative integer test:')
parse_integers()

# test pack input integer
print('pack integers test:')
parse_pack_integers()

# test prime
print('prime test:')
is_prime()
