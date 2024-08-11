def print_names(**kwargs):  # For arbitrary keyword arguments use **(2star).
    # We can use any other naming convention instead of kwargs. But kwargs is standard.
    print(kwargs)  # Retrieving value from a dictionary.
    # If I need to retrieve the Address, then.
    print(kwargs["Address"])  # Traversing of dictionary


print_names(name="Prashant", Address="Bangalore", Mobile=8867055859)
# Keyword arguments will receive values in the form of dictionary.
# The values we pass to kwargs will be received as a dictionary.

'''Arbitrary Args                                                     Arbitrary Keyword Arguments'''
''' 1. Pass the values and it will be received as Tuples.       Pass the values and it will be received as Dictionary'''
''' 2. *args                                                                          **kwargs'''
