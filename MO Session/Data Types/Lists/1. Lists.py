# List: Collection of values or objects.
# Dynamic in nature.
"""Dynamic in nature means, we don't need to give an exact value in list that how many values we want to store
within the list."""
# It can have any type of values. It means it can have Integer, Float, String or together.
# The List is indexed.
# It can have duplicate elements.
# Syntax: [Value1, Value2]
# Example :
# 1. [10,20,30]
# 2. [10, "Prashant" 60.0]
# 2. [10, "Prashant" 60.0]

list1 = [10, 20, 30, 70, 31]
print(list1)  # It will give output in the same sequence.
list2 = ["Prashant", 31, 95000.0, True]
print(list2)
# To calculate the length
print(len(list2))

# We can also concatenate both lists
print("***********************CONCATENATING 2 LISTS*******************************")
list3 = list2 + list1
print(list3)
print(len(list3))

print("*****************INDEXING********************")
list4 = [12, 89, 78, 90]
print(list4[-1])
print(list4[1])  # To get a last value from the list. It is also fetching the value from reverse order.

# When we give the index which does not exist, then it will return an error "IndexError: list index out of range".

# When the list has duplicate value.
print("**************DUPLICATE VALUES******************")
list5 = [12, 89, 78, 90, 90, 90, 89]
print(list5)  # The list allows duplicate values & it will print the way it is ordered.

# To count the number of occurrences of a specific object from the list, we have 2 ways.
# 1. Writing a custom logic
# 2. Using inbuilt function.
print("**************NUMBER OF OCCURRENCES******************")
list5 = [12, 89, 78, 90, 90, 90, 89]
print(list5.count(90))
# When checking the object which is not in a list.
list5 = [12, 89, 78, 90, 90, 90, 89]
print(list5.count(100))  # It will return result as 0.

print("***********SLICING******************")
list6 = [12, 89, 78, 90, 90, 90, 89]
print(list6[::])  # Returns all the objects from the list.
print(list6[1::])  # Returns the objects from 2nd element.
print(list6[1::-1])
print(list6[1:4])
# print(list6[1:4]) here the 4 is stop counter. It will not include the 4th element that is 90.
# It will only include till 3.

print("************METHODS*****************")
list7 = [12, 89, 78, 90, 90, 90, 89]
list7[0] = 222  # Replacing value of 0th index(12) with 222
print(list6)
list7.append(888)  # Appending the last value with 888
print(list7)
# We can append any type of value.
list7.append("Prashant")
print(list7)

# Not appending the value at last, but we can make it in between as well. We can make it by "insert" method.
list7.insert(0, 555)
print(list7)
