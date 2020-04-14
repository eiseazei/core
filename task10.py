#!/usr/bin/python3.7

from common import Ball, Ghost, Man, Woman, make_humans, Person

# Ball class
b0 = Ball()
print(b0)

b1 = Ball('super')
print(b1)

# Ghost class
gh = Ghost()
print(gh)

# Humans
humans = make_humans()

print('human name is {} sex is {}'.format(humans[0].name, humans[0].sex))
print('human name is {} sex is {}'.format(humans[1].name, humans[1].sex))

# Person
pe = Person('john', 34)
print(pe.getPersonInfo())