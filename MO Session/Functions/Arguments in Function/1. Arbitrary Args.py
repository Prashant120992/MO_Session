# What if there is a situation if we don't know that how much argument will be passed to our function. How to handle it?
# We can do it from arbitrary Arguments.
# Let's create a function.
def print_names(name1, name2):
    print(name1, name2)


print_names("Python", "Java")  # Call the function print_names.
# In the above example, Python will be stored in name1 and Java will be stored in name2.
# What if I print one more argument called C, we will be getting an error called 2 Positional Argument but were given 3.
# To resolve this, we need to pass one more variable in function called name 3: def print_names(name1, name2, name3)
# Also we need to print: print(name1, name2, name3)
'''In this scenario we know the number of parameter so that we can easily change our no.of variable that are passed in 
function.'''


# What if I don't know no.of arguments which I will be receiving. So for that we will use *args.
# *args means, whatever values we will be passing, those will be stored into *args.
def print_names(*args):
    print(args)


print_names("Python", "C++", "Java")


# In this case, the output will be printing in the form of Tuple: ('Python', 'C++', 'Java')\
# The *args will accept n number of parameters that we pass.
# Let's print one more value.
def print_names(*args):
    print(args)


print_names("Python", "C++", "Java", "JS")
# The *args will receive the value in the form of Tuple.
# To retrieve the value from Tuple: we use index concept.
print("\n\n********Retrieve value from Tuple************")


def names(*args):
    print(args)
    print(args[1])


names("Python", "Java", "C++", "Java Script")

# We can pass n number of arguments with the help of Arbitrary Argument.
# Is it mandatory that we just want to use *args?
# The answer is no. We can use any convenient naming convention instead of args.
# Example:
print("\n\n*******Passing args as Prashant**************")


def naming(*Prashant):
    print(Prashant)
    print(Prashant[0])


naming("Belagavi", "Bangalore", "Delhi")

# What if I want to retrieve value from tuple.One way is to print the complete Tuple. Another way is using it for loop.
print("\n\n******Retrieve value from Tuple with the help of for loop************")


def for_loop(*args):
    print(args)
    for i in args:
        print(i)


for_loop("ID", "Name", "Gender")
