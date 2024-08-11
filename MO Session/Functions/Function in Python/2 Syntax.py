# Syntax: Without Argument
"""def function():
    statement 1
    statement2"""

# Syntax 2: With Argument
# We can also pass an arguments to function.
'''def function(param1, param2):
    statement 1
    statement 2'''
# We can pass n number of parameters within the parenthesis.

# Syntax 3: With Default Argument
'''def function(param1, param2="default"):
    statement 1
    statement 2'''
# We can also have a function with a default argument.
# Here, param 1 is mandatory and param 2 I have made default.
# Default means, if I don't pass any value for the 2nd parameter, it will take default value.

# Syntax 4: Arbitrary Argument
'''def function(*args):
    statement1
    statement2'''
'''When we dont have fixed number of arguments we can use this where we can pass n number of parameter & it will 
take all the parameters dynamically'''

# Syntax 4: Arbitrary Keyword Argument
'''def function(*kwargs):
    statement1
    statement2'''
# Here we are passing dynamic parameters when the number of parameters is not fixed, but here we also pass with keyword.
