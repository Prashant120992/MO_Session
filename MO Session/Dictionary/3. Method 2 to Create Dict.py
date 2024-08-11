# Syntax 2:

emp = dict(QA="Prashant", Dev="Veer", DevOps="Prasanna")
print(emp)
# The dict is a class, and we are using dictionary class constructor.
# In the constructor, we are providing a key value pair separated by comma.
# In the above example, we can notice the keys are not in double quotes.
# By default, the keys are strings.
'''The emp = dict(1="Prashant", Dev="Veer", DevOps="Prasanna") and 
emp = dict(10.5="Prashant", Dev="Veer", DevOps="Prasanna") are invalid'''
# The keys are case-sensitive. We can differentiate QA, qa and Qa as keys.
# We cannot have a duplicate key in the dictionary.

emp = dict(QA="Prashant", Dev="Veer", DevOps="Prasanna", qa="AK", Qa="Akshay")
print(emp)

# Another way to create a dictionary is with a list of tuple.
newDict = dict([(1, "Python"), (2, "Selenium"), (3, "PlayWrite")])
print(newDict)
# Using dictionary constructor.
# Within the parenthesis, we are creating a list of tuples. Within that list we have multiple tuples.
# Within that tuple we can have multiple key value pairs.
# Inside the tuple we have key value are separated by comma.
# Also, each tuple is separated by comma.
