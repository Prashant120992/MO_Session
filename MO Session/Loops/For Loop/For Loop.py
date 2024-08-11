# In Python, we have while loop and for loops.
"""The loop as a name itself indicates, whenever we need to run one thing at multiple times instead of repeating the
same Statement multiple times, we can run a loop."""
# Iterating one thing multiple times depends on conditions.
# The list, set, dictionary, string and tuple are iterable with the help of for loop and while loop.
'''Real time examples : If I need to create 100 files. Instead of creating a file one by one, I can create a for loop
that will create 100 files.'''
# No.of links on webpage. Writing no.of records in an Excel sheet using this loop statements.
# Syntax:
# Let's talk about a string as per below example.
print("*********For Loop Example : 1*******************")
name = "Python"
# I want to traverse the above string, or I want to iterate it.
for x in name:
    # The "x" will be any variable name that is local. We can give any name.
    # The "name" will be an object name that we want to traverse or which we want to iterate.
    # In the current example, we want to iterate "name", which is a string type.
    # After name, there must be semicolon and hit enter. Then the cursor has to move 4 whitespaces.
    print(x)
    # Here when we say name, the string name is a sequence of charter.
    '''Here each character will be picked up by the variable x every time then printing. 
    It will continue this process until it reaches last character.'''

# Let's take below example.
print("\n\n*********For Loop Example : 2*******************")
name = "I Love Python"
for n in name:
    print(n)
# In the above example, the white spaces are also included as they are also considered as character.
