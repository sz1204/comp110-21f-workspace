"""Finding duplicate letters in a word."""

__author__ = "730490960"

word: str = input("Enter a word: ")
i: int = 0
dupe: bool = False

while i < len(word):
    j: int = 0
    while j < len(word):
        if i == j:
            j = j + 1
        else:
            if word[i] == word[j]:
                dupe = True
            j = j + 1

    i = i + 1

print("Found duplicate: " + str(dupe))
