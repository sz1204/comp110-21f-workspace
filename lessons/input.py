"""Examples of user input and variables."""
# Docstring. Serves as user documentation only. Best practice to use.

user_name: str = input("Who are you? ")
# Variable input! Order: variable name, colon, data type, assignment operator (=)

print("Wow, " + user_name + ", you rock!")
# String concatenation
print(user_name + ", have a great day!")

# The Stack occurs in the globals frame. The name has global meaning through the program when defined (user_name)).
# The output uses the globals to print out sentences in the terminal. (Wow, Sarah, you rock!)

# If you see the white circle on top, save first: CTRL + S 
# In order to run the program in the terminal, run a module: python -m lessons.input