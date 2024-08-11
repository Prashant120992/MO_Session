# The parameter and arguments, both are the same.
def greeting(firstname, lastname):
    print("Hello" + " " + firstname + " " + lastname)


greeting("Prashant", "Hiremath")
# What if I change the above order.
greeting("Hiremath", "Prashant")
# This time it will output as Hello Hiremath Prashant,
# So to avoid this, we can also pass keyword along with values.
greeting(firstname="Prashant", lastname="Hiremath")
greeting(lastname="Hiremath", firstname="Prashant")  # Now it will give proper order even there is random assignment.


# We can also add one more parameter.
def greeting1(firstname, lastname, marks):
    print("Welcome" + " " + firstname + " " + lastname + " " + str(marks))


greeting1(marks=65, lastname="Hiremath", firstname="Prashant")
