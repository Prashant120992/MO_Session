print("************Without Break**************")
# Creating a boolean variable which is False by default.
Status = False
# Let's create a list of Languages
names = ["Java", "Selenium", "Python", "CSharp"]
# I want to search a specific tool within the list. If that exists, then say True. Otherwise, print some junk message.
# So for that first, we need to traverse the list.
# We can traverse it through for loop.
for name in names:  # Syntax of creating a for loop.
    # The "name" is a variable where we store the values in each iteration.
    # In the for loop, the list values are got one by one and stored into name.
    # So in the list if there are 4 names, it will run for 4 times.
    # Each time it will give a value.
    if name == "Python":
        # Here I want to check if Python is available in the list.
        Status = True
        # If the value is available, then change the Status flag as "True".
    else:
        print("Please wait, We are still searching.")
# If the status is evaluated as true, then print the valid message.
if Status:
    print("We are glad that we are able to find the record.\n\n")
# In case if we don't find, print message.
else:
    print("Sorry, we are unable to find\n\n\n")
# The above example is without break. Without break, the loop still continues though the value is found.

print("************With Break**************")
# Creating a boolean variable which is False by default.
Status = False
# Let's create a list of Languages
names = ["Java", "Selenium", "Python", "CSharp"]
# I want to search a specific tool within the list. If that exists, then say True. Otherwise, print some junk message.
# So for that first, we need to traverse the list.
# We can traverse it through for loop.
for name in names:  # Syntax of creating a for loop.
    # The "name" is a variable where we store the values in each iteration.
    # In the for loop, the list values are got one by one and stored into name.
    # So in the list if there are 4 names, it will run for 4 times.
    # Each time it will give a value.
    if name == "Python":
        # Here I want to check if Python is available in the list.
        Status = True
        break
        # If the value is available, then change the Status flag as "True".
    else:
        print("Please wait, We are still searching.")
# If the status is evaluated as true, then print the valid message.
if Status:
    print("We are glad that we are able to find the record.")
# In case if we don't find, print message.
else:
    print("Sorry, we are unable to find")
# The above example is without break. Without break, the loop still continues though the value is found.
