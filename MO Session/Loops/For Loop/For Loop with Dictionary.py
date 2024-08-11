# Can we traverse the dictionary with the help of for loop?
print("************Example 1**************")
myDict = {1: "Prashant", 2: "Python"}
for n in myDict:
    print(n)  # It will print only keys of dictionary but not values.

print("\n\n*******Example 2***********")
myDict1 = {1: "Prashant", 2: "Python", "name": "Akshay"}
for md in myDict1:
    print(md)

# If we need to get the full set of dictionary (Combination of key and value, the use items() method.
print("\n\n*******Print full dict***********")
for md in myDict1.items():
    print(md)

'''If we need to segregate Key with value while printing, 
then we need to create 2 local variables and print them separately.'''
print("\n\n*******Key Value Segregation***********")
for a, b in myDict1.items():
    print(a)
    print(b)

# If we need to print only values, then declare only any local variable and call values() methods.
print("\n\n*******Print only values***********")
for a in myDict1.values():
    print(a)
