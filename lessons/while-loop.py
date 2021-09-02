"""An example of a while loop statement."""

counter: int = 0
maximum: int = int(input("Count up to, but not including what? "))

# If the condition of the counter is true, then the program will go into the loop.
while counter < maximum:
    counter_squared: int = counter ** 2
    print("The square of " + str(counter) + " is " + str(counter_squared))
    counter = counter + 1

print("Done!")