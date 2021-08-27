"""This program asks the user to input two numbers and then compares them using relational operators."""
__author__ = "730490960"

left: int = int(input("Please enter a number for the left-hand side: "))
right: int = int(input("Please enter a number for the right-hand side: "))

print("Left-hand side: " + str(left))
print("Right-hand side: " + str(right))

print(str(left) + " < " + str(right) + " is " + (str(bool(left < right))))
print(str(left) + " >= " + str(right) + " is " + str(bool(left >= right)))
print(str(left) + " == " + str(right) + " is " + str(bool(left == right)))
print(str(left) + " != " + str(right) + " is " + str(bool(left != right)))