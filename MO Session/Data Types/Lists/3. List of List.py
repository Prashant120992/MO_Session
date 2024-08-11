print("*******************LIST OF LIST****************************")
# Can we create a list of list? or list of list of list?
# Ans: Yes we can.
mylist1 = [1, 2, 3, 4, ["Prashant", "Python", "Selenium"]]
# Create a list called mylist, and within that we need to create one more list.
print(mylist1)
# If we need to access the first value then:
print(mylist1[4])
# In the above example "["Prashant", "Python", "Selenium"]" the entire content is considered as List.
# If we need to access the element within the list, then give the list first then within the index later.
print(mylist1[4][1])
