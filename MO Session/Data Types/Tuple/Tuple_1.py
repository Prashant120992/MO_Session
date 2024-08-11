# By using Tuple Constructor or tuple class.
t1 = tuple([1, "Prashant", 10.1, True])  # Created tuple constructor and inside that passed values in the form of list.
print(type(t1))
print(t1)
# We can access with the help of an index.
print(t1[1])

# Tuple Unpacking → Making all the values of tuple into variables by creating a variables.
t2 = tuple([1, "Prashant", 10.1, True])
x, y, z, a = t2  # Assigns each variable to each value of tuple.
# x --> 1
# y --> Prashant
# z --> 10.1
# a -->True
print(a)
print(z)

# Note: We need to assign the same number of variables that matches the number of elements in the Tuple.
