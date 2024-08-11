# Let's create a function that will create some data.
def helloworld():
    """The def is a keyword. Helloworld() is a method. Whatever written within the below indentation is considered as
    part of this function."""
    print("Hello Python")
    c = 10 + 90
    print(c)
    print("Bye")


'''The moment when we run the above program we wont get any output. The reason is we have defined a function but we 
have not called.'''
# The moment we write a function, we need to call them.
# To call the function, we need to come out of indentation and write the function method name.
helloworld()
'''The moment When we call the helloworld, the control is coming back to the 5th line it will print & it will execute 
sequentially.'''
# The above example is a basic function that doesn't expect any argument.
