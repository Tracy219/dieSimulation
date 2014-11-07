#!/usr/bin/env python

from random import randint
from specialInput import int_input

diceNumber = int_input("How many dice would you like to roll? ")
sides = int_input("How many sides on your die? ")

for i in range(1, diceNumber + 1):
	result = randint(1, sides)
	print("Die {} shows: {}".format (i, result))