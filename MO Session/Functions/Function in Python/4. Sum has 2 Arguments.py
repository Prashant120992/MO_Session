# Let's create a function method called sum() that expect 2 arguments.
def summ(num1, num2):
    result = num1 + num2  # Doing arithmetic operation here.
    print("The result is :", result)
    # If I want to call this, then I want to call it through function method name.


summ(10, 30)
# Value 10 will be stored in num1, and value 30 will be stored in num2
# It will store the value in a result and finally it will print.


# When we call function summ() function with only 1 Argument, it will throw an error (Positional argument missing).
# The below code throws an error.
# summ(10)
# Because the summ() function is expecting 2, but we are passing only 1. In this case, it is mandatory to give 2 args.
