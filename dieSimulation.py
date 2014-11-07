#!/usr/bin/env python

from random import randint
from specialInput import int_input
'''
	specialInput is three special input functions. int_input can convert what you enter to
	integer, if it failed, it will print "That's not a integer."
	This program simulate a die roll.

'''

print("This program simulates rolling several dice.\n" \
"The user can choose how many dice are rolled.\n")

diceNumber = int_input("How many dice would you like to roll? ")
sides = int_input("How many sides on your die? ")

for i in range(1, diceNumber + 1):
	result = randint(1, sides)
	print("Die {} shows: {}".format (i, result))