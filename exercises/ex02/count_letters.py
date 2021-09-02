"""Counting letters in a string."""

__author__ = "730490960"


# Begin your solution here...

letter: str = input("What letter do you want to seach for? ")
word: str = input("Enter a word: ")
i: int = 0
count: str = " "
counting: int = 0

while i < len(word):
    count = word[i]

    if count == letter:
        counting = counting + 1

    i = i + 1

print("Count: " + str(counting))