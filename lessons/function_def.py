"""An example function definition."""


def my_max(a: int, b: int) -> int:
    # The above line is known as the signature, or contract line.
    # Says it will take in two integer values, but only result in one int value.
    """Returns the largest argument."""
    # Docstring describes how to use the function.

    if a >= b:
        return a
    else:
        return b
    
    # The if else is a block, or body component of the program.


print(my_max(10 + 1, 10))

result: int = my_max(-50, 100)
print(result)

# This has no impact on the program's output, but when looking at the memory it is different.
# You cannot call a function before it has been defined.

x: int = 6
y: int = 5 + 2
z: int = my_max(x, y)
print(z)