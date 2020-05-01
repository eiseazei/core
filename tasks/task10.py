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

class A:
    """Dummy class."""
    def func1(self) -> None:
        """"""
        print('func1')

class B(A):
    """Class inherited from parent A."""
    def func2(self) -> None:
        """Instance initialization."""
        super().func1()
        print('func2')

# class B instance
b = B()
b.func2()

# format key 'f' test
s = f'aaa'
print(s)