# Pop Method
# Removes the value from the list.
print("******************POP METHOD*********************")
list10 = [1, 2, 3, 4, 5]
list10.pop()
print(list10)
# The last value from the list will be removed when passing empty pop. It is applicable for string as well.
list11 = ["Bangalore", "Belagavi", "Shimoga", "Hubli", " "]
list11.pop()
print(list11)
# If we want to remove a specific element from the list, then we need to pass its index value.
list11 = ["Bangalore", "Belagavi", "Hubli", "Shimoga"]
list11.pop(2)
print(list11)

# When we are popping out the element which does not exist, then "pop index out of range" error populates.

'''In case if we don't aware of Index or if there is a huge number of values, then we can remove those with the help of
remove method.'''
list12 = ["Vijayanagar ", "Basavanagudi", "Kalasipalya", "Marathahalli"]
list12.remove("Kalasipalya")
print(list12)
