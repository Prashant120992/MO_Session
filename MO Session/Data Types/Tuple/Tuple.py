# Tuple is a collection of an items like list, set and dictionary.

"""It is ordered and indexed. Means we can have tuple values in a proper order,
 and we can access them with the help of an index value"""

# Since we have an indexing, we can do indexing and slicing operation.

'''Though the tuple has same property as list the Tuple is immutable (We cannot change the value), but a list is 
mutable. In the list, we can override the values.'''

# Syntax 1:
# (value1, value2)
# Example :
# (1,"Python", 2, "Selenium") --> 4 Values. Integer and String Values.
# Syntax 2: Like a list, set and dictionary, we can use tuple constructor by using tuple() constructor.
# Example :
# tup1=tuple([1,"Python", 2, "Selenium"]) --> In the constructor we need to pass tuple values.

print("*******************Example 1****************************")
tup1 = (1, "Python", 10.5, "True")
print("The values of Tup1:", tup1)  # Same order it will print.

# Since it is order-based, we can access a specific element through their index value.
print(tup1[1])

tup2 = (1, "Python", 10.5, True, 1, 1, 1, "QA")
print("The values of Tup2:", tup2)

# It supports negative index as well.
print("***********Accessing an element through -ve Index****************")
print(tup2[-2])
print(tup2[-1])

print("********No.of Occurrences of specific element in a tuple********************")
print(tup2.count(1))  # The result will be 5, though there are 4 1's. Because there is a value called True in the list.
# Internally, the value of True is considered as 1, so it results 5.
print(tup2.count("QA"))

print("***********Finding an index of any element in the tuple*************")
print("The Index Value of 10.5 is : ", tup2.index(10.5))

print("*********Slicing**********")
print(tup2[0:5])  # It should only include till 4th element, not 5th element.

# The Major difference between a list and tuple is that in tuple object assignment(tup1[0]="Prashant) is not allowed.
# Because the tuple is immutable.

# Is there any way to convert from Tuple into List?
# Yes. It is possible with the help of their constructor.
print("*********Converting Tuple into List**********")
tup3 = (1, "Python", 90.0, True, 1, 1, 1, "QA", 2, 2, 2)
print(type(tup3))
# Is there any way to convert from Tuple into Set?

# Tuple is a collection of an items like list, set and dictionary.
"""It is ordered and indexed. Means we can have tuple values in a proper order,
 and we can access them with the help of an index value"""
# Since we have an indexing, we can do indexing and slicing operation.
'''Though the tuple has same property as list the Tuple is immutable (We cannot change the value), but a list is 
mutable. In the list, we can override the values.'''
# Syntax 1:
# (value1, value2)
# Example :
# (1,"Python", 2, "Selenium") --> 4 Values. Integer and String Values.
# Syntax 2: Like a list, set and dictionary, we can use tuple constructor by using tuple() constructor.
# Example :
# tup1=tuple([1,"Python", 2, "Selenium"]) --> In the constructor we need to pass tuple values.

print("*******************Example 1****************************")
tup1 = (1, "Python", 10.5, "True")
print("The values of Tup1:", tup1)  # Same order it will print.

# Since it is order-based, we can access a specific element through their index value.
print(tup1[1])

tup2 = (1, "Python", 10.5, True, 1, 1, 1, "QA")
print("The values of Tup2:", tup2)

# It supports negative index as well.
print("***********Accessing an element through -ve Index****************")
print(tup2[-2])
print(tup2[-1])

print("********No.of Occurrences of specific element in a tuple********************")
print(tup2.count(1))  # The result will be 5, though there are 4 1's. Because there is a value called True in the list.
# Internally, the value of True is considered as 1, so it results 5.
print(tup2.count("QA"))

print("***********Finding an index of any element in the tuple*************")
print("The Index Value of 10.5 is : ", tup2.index(10.5))

print("*********Slicing**********")
print(tup2[0:5])  # It should only include till 4th element, not 5th element.

# The Major difference between a list and tuple is that in tuple object assignment(tup1[0]="Prashant) is not allowed.
# Because the tuple is immutable.

# Is there any way to convert from Tuple into List?
# Yes. It is possible with the help of their constructor.
print("*********Converting Tuple into List**********")
tup3 = (1, "Python", 90.0, True, 1, 1, 1, "QA", 2, 2, 2)
print(type(tup3))
# To convert into list type "list" and inside list constructor pass tuple name. Then it will return a list.
li = list(tup3)
print(type(li))
print(li)
# Is there any way to convert from Tuple into Set?
# Yes. It is possible with the help of their constructor.
print("*********Converting Tuple into Set**********")
se = set(tup3)
print(type(se))
print(se)

'''When we convert into a set, the duplicate values will be discarded. 
Also set unordered so it will print in random order.'''

# Can we convert tuple into a dictionary?
# No, We cannot as dictionary needs a key value pair.

# Imp: When we are pass single string value within tuple without a comma, it will read character by character.
tup4 = ("Prashant")
print("Length of a tup4 without comma :", len(tup4))
# Returns length as 8 as it will read character by character since there is no comma after one string.

tup4 = ("Prashant",)
print("Length of a tup4 with comma :", len(tup4))
tup4 = ("Prashant", "Python")
print("Length of a tup4 with comma after adding one more value :", len(tup4))
# Returns length as 1 as it will be considered as 1 String since there is no comma after one string.

# Can we create a list of Tuples?
# Yes. We can create.
print("*******Tuples inside the List******************")
li1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]  # In the list, we can have multiple tuples those are separated by commas.
print("Tuples inside the list :", li1)
# In the above list(li1) we have 3 tuples.
# 1st Tuple --> (1, 2, 3)
# 2nd Tuple --> (4, 5, 6)
# 3rd Tuple --> (7, 8, 9)
# If I need to access Tuple 1 then
print("Accessing Tuple 1 : ", li1[0])  # Accessing 1st Tuple through index value 0.
print("Accessing Tuple 2 : ", li1[1])  # Accessing 2nd Tuple through index value 1.
# Since it is tuple, again tuple supports indexing, we can access specific value from index.
print("Accessing specific value from Tuples : ", li1[1][1])
print("Accessing specific value from Tuples : ", li1[0][1])
