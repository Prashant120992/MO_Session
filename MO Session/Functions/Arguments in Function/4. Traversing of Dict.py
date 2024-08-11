# It is possible to pass both *args and *kwargs.
def print_names(*args, **kwargs):
    print(args)
    print(kwargs)


print_names(1, 2, 3, name="Python", country="India")  # Here we need to pass Arbitrary Args and Arbitrary Keyword Args
# The 1, 2, 3 are stored as args and ame="Python", country="India" stored as kwargs.
# Here we can pass multiple values and based on the values the function will receive as a tuple and dictionary.
