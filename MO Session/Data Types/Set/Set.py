# A set is collection of an objects.
# Dynamic in nature. Means it does not have any size restriction. We can store as many as values.
# It can have any type of values. It means it can have integer, float, string, etc. together.
# It does not follow an index approach, hence slicing is not possible like list and strings.
# Cannot have duplicate elements.

"""List                                                   Set"""
"""1. Have an Index and slicing                      Cannot have indexing and slicing."""
"""2. Allows duplicate                               Does not allow duplicate."""

# There are 2 ways to create a set in python
# Syntax 1:
# {value1, value2}
# Example 1: {10,20,30}
# Example 3: {12, "Prashant" 71.5} --> Set of different values such as integer, string and float.

# Another way to create a set using set constructor.
# Syntax 2:
# Using set() constructor
# MySet=set([1,2,4])

MySet = {90, 89, 76, 12}
print(MySet)  # It will print the elements in random order. Output --> {89, 90, 76, 12}
MySet1 = {90, 89, 76, 12, 2, 888, 90, 90}
print(MySet1)  # It will eliminate the duplicate values.

# Adding an element to existing set.
print("***********************ADDING AN ELEMENT**************************")
MySet2 = {90, 89, 76, 12}
print("Before adding an element:", MySet2)
MySet2.add(55555)
print("After adding an element:", MySet2)

# Removing an element to existing set.
print("***********************REMOVING AN ELEMENT**************************")
MySet3 = {90, 89, 76, 12, 42, 57, 88}
print("Before removing an element:", MySet3)
MySet3.remove(76)  # The "remove" is used to remove a specific value from a set.
print("After removing an element:", MySet3)
# When we are trying to remove the value which does not exist, it will give key error.
'''We have a method called discard, which will remove if the element is there and if element is not there,
 it will not throw any error.'''
MySet3.discard(100)
print("After Discarding an element:", MySet3)

"""The pop() is also used to remove the random element from the set. But in the list,
 it is used to remove the last element."""
print("***********************POP METHOD**************************")
MySet3.pop()
print("After pop() method :", MySet3)

print("***********LENGTH**********************")
MySet4 = {90, 89, 76, 12, 42, 57, 88}
print(len(MySet4))  # Returns the length of the list.

print("*****************CLEAR THE SET********************")
MySet5 = {1, 2, 3, "Prashant", 12.5}
print(MySet5)
MySet5.clear()
print(MySet5)

print("******************CREATING A COPY OF SET**************************")
MySet6 = {1, 2, 3, "Prashant", 12.5}
print(MySet6)
MySetCopy = MySet6.copy()
MySet6.clear()
print(MySet6)
print(MySetCopy)

# 2nd way to create a set.
print("************2nd Way to Create a Set*******************")
print("************Set Creation using list*******************")
set1 = set([1, 2, 3, 4]) # Created with the help of list.
print(set1)

set2 = set(["Prashant", 65.4, 1, 2, 3, 4])
print(set2)  # Created with the help of list.

print("************Set Creation using tuple*******************")
set3=set(("Python", 65.4, 1, 2, 3, 4))
print(set3)
