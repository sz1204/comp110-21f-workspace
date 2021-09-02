"""Repeating a beat in a loop."""

__author__ = "730490960"


# Begin your solution here...

i: int = 0

beat: str = input("What beat do you want to repeat? ")
times: int = int(input("How many times do you want to repeat it? "))

rep: str = beat

if times <= 0:
    print("No beat...")
else:
    while i < times - 1:
        rep = rep + " " + beat
        i = i + 1
    print(rep)
