list1 = [12, 89, 78, 90]
list2 = ["Prashant", "Hiremath", "Python"]
list3 = "Prashant"
list1.extend(list3)
print(list1)
list1.extend(list3)  # String is iterable. When we extend a string, it will display character by character.
print(list1)
