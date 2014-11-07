#!/usr/bin/env python

from random import randint
from specialInput import int_input

sides = int_input("How many sides on your die? ")
result = randint(1, sides)

print("The die shows: {}".format(result))