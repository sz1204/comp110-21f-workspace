"""Example of looping through all characters in a string."""

user_string: str = input("Give me a string! ")

# The variable "i" is a common counter variable name in programming.
# i can be thought of as short for "iteration"
i: int = 0

while i < len(user_string):
    print(user_string[i])
    i = i + 1

# You can select multiple lines and press tab to indent
# To delte indents, hold shift and click tab.

print("Done!")