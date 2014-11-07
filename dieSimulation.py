#!/usr/bin/env python

from random import randint
from specialInput import int_input
'''
	specialInput is three special input functions. int_input can convert what you enter to
	integer, if it failed, it will print "That's not a integer."
	This program simulate a die roll.

'''

diceNumber = int_input("How many dice would you like to roll? ")


for i in range(1, diceNumber + 1):
	sides = int_input("How many sides on your die #{}? ".format(i))
	result = randint(1, sides)
	print("Die {} shows: {}".format (i, result))