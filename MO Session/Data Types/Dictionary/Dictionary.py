# Dictionaries are collection of an items.

"""Each item in the Dictionary is in key value pair just like a map.
Whenever we provide any value, make sure that we associate with a key."""

# It is dynamic in nature. It means we can have n number of Key-Value pairs here.

"""It is Unordered like a set. 
We don't have an index feature here hence whenever we want to get any specific value,
we need to provide the key then we get the value."""

# Using Dictionaries, we can fetch the values with a key.
# Keys in Dictionaries should be unique, but values can be duplicate.
# Syntax1:
# {key1:value1, key2:value2}
# Example1: {1:"Python", 2:"Selenium"} Integer as a key and value as a string.
# Example2: {"Pyselium":"Testing Team", "PyDev":"Dev Team"} # Both key and values are string.
# There is no type restriction.
# Syntax2 using dict() constructor. The dict is separate class.
# myDict=dict("Pyselium":"Testing Team", "PyDev":"Dev Team")
# Syntax3:(Development Project)
# myDict = dict([("Pyselium", "Testing Team"), ("PyDev", "Dev Team")])

print("**************Example 1**************************")
emp = {"QA": "Prashant", "Dev": "Veer", "DevOps": "Prasanna"}
print(emp)
# There are 2 ways to access the value from dictionary.
# 1st one is passing value.

print("**************1st Way to access an element from Dictionary**************************")
print(emp["QA"])
# Dictionaries are collection of an items.
"""Each item in the Dictionary is in key value pair just like a map.
Whenever we provide any value, make sure that we associate with a key."""
# It is dynamic in nature. It means we can have n number of Key-Value pairs here.
"""It is Unordered like a set. 
We don't have an index feature here hence whenever we want to get any specific value,
we need to provide the key then we get the value."""
# Using Dictionaries, we can fetch the values with a key.
# Keys in Dictionaries should be unique, but values can be duplicate.
# Syntax1:
# {key1:value1, key2:value2}
# Example1: {1:"Python", 2:"Selenium"} Integer as a key and value as a string.
# Example2: {"Pyselium":"Testing Team", "PyDev":"Dev Team"} # Both key and values are string.
# There is no type restriction.
# Syntax2 using dict() constructor. The dict is separate class.
# myDict=dict("Pyselium":"Testing Team", "PyDev":"Dev Team")
# Syntax3:(Development Project)
# myDict = dict([("Pyselium", "Testing Team"), ("PyDev", "Dev Team")])
emp = {"QA": "Prashant", "Dev": "Veer", "DevOps": "Prasanna"}
print(emp)
# There are 2 ways to access the value from dictionary.
# 1st one is a passing key. The key here is QA
print(emp["QA"])
# The accessing of non-existing value will return Key Error.
# 2nd way to access is from get() method.
print(emp.get("DevOps"))
# We can provide any type of values in the dictionary.
emp1 = {"QA": "Prashant", "Dev": "Veer", "DevOps": "Prasanna", "Security": 20, 50: "Python"}
print(emp1)

"""If there are multiple values for one key, lets say as per the example, if someone is joining in QA Team later, 
then we can create a list within a Dictionary"""
emp2 = {"QA": ["Prashant", "Akshay"], "Dev": "Veer", "DevOps": "Prasanna"}

'''In the above example, one key returns a list of values and then 
once we get a list of value and totally it is a list.'''
print(emp2)

"""We can get the value 1st value from the QA as it represents a list, we can iterate them. 
We can make them through index."""

emp3 = {"QA": ["Prashant", "Akshay"], "Dev": "Veer", "DevOps": "Prasanna"}
print(emp2["QA"][1])

# Creating a dictionary within a dictionary.
print("***************Dictionary within the Dictionary********************")
emp4 = {"QA": "Prashant", "Dev": {"Front_End": "Veer", "Backend": "Neha"}, "DevOps": "Prasanna"}
# Here we have one dictionary and within that there is one more dictionary called Dev.
print(emp4)

# What if we want to access the value from inside the dictionary.
print(emp4.get("Dev"))
print(emp4.get("Dev").get("Front_End"))
# We can also write the "print(emp4.get("Dev").get("Front_End"))" as shown below.
print(emp4["Dev"]["Backend"])

# Adding a value to Dictionary
print("----------------------------Adding value to a dictionary------------------------- ")

emp5 = {"QA": "Prashant", "Dev": {"Front_End": "Veer", "Backend": "Neha"}, "DevOps": "Prasanna"}
print("Before adding:", emp5)
emp5["Manager"] = "Manish"
print("After adding:", emp5)
# If we need to update the manager name again, then provide the exact key name and the value that needs to be modified.
emp5["Manager"] = "Dhanush"
print("After updating:", emp5)

print("**************Deleting***************")
# The Pop method will ask which key we want to delete.
emp5.pop("QA")
print("After deleting :", emp5)

print("*************Pop Item*********************")
# There is one more method that will remove LIFO order. It will remove the last-in item.
emp5["Manager"] = "Satya"
print("After adding Manager :", emp5)
emp5.popitem()
print("After Pop Item:", emp5)

# Interview Q. Difference between pop and pop Item.

print("**********Length of the Dictionary**********")
print(len(emp5))  # Returns the length of key value pair records we have.

print("**********Display only Keys**********")
print(emp5.keys())  # Returns only keys of dictionary.

print("**********Display only Keys**********")
print(emp5.values())  # Returns only values of dictionary.

print("**********Returns key value pair**********")
print(emp5.items())  # Returns the key value pair in terms of tuples.

print("******************Deleting record from Dictionary************************")
names = {'Pratik': 21, 'Prasanna': 21, 'Pramod': 22, 'Mani': 21}
print("Before removing an items :", names)
del names["Pramod"]
print("After removing an items :", names)

'''print("**********To delete the complete dictionary**********")
name1 = {'Anuradha': 21, 'Kashyap': 21, 'Pramod': 22, 'Mani': 21}
del name1
print("After deleting the complete dictionary :", name1)  # It will return name error as it deletes dictionary name.'''
