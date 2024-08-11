def print_names(fname, *args, **kwargs):
    print(fname)
    print(args)
    print(kwargs)


print_names(10, 20, 30, name="Python", City="Bangalore")
# Here the first argument will be received as fname, and later one received as args and kwargs.
