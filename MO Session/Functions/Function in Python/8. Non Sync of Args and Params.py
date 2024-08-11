# What if I have 2 arguments but need to pass value for 1 parameter?
"""Then we can create a function with parameter 2 making one as an optional by assigning some value to it within the
parenthesis."""


def summ(num1, num2=0):
    result = num1 + num2
    return result


finalResult = summ(12)  # If I pass one more value, it will take that parameter as a mandatory one.
# If I don't pass it will consider as an optional. The 12 will be received as num1.
print("Final Result is:", finalResult)
finalResult = summ(12, 15)
print("Final Result after passing one more value is:", finalResult)


# What if I pass parameter 3 when I am expecting 2 arguments?
# In that case, it will throw an error.
# The following snippet will throw an error.
# finalResult = summ(12,15,30)

# For the above case to resolve, we can declare one more argument in function method.
# The "def summ(num1, num2=0, num3=0):" snippet does that.
# Example:
def values(num1, num2=0, num3=0, num4=0):
    result = num1 + num2 + num3 + num4
    return result


end = values(10, 20, 30, 40)
print("The values of all nums are ", end)
