"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730490960"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says...")

random: int = randint(1, 4)
if random == 1:
    print("A dream you have will come true.")
else:
    if random == 2:
        print("A thrilling time is in your immediate future.")
    if random == 3:
        print("Fortune favors the brave.")
    if random == 4:
        print("Never give up. Always find a reason to keep trying.")

print("Now, go spread positive vibes!")