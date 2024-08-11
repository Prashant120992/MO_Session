# 1. String is Immutable.
# 2. String is a sequence of Character.
# Python does not have Character Data Type.
# 3. String can be represented by "" or ''\
first_name = "Prashant"
last_Name = 'Hiremath'
print(first_name)
print(last_Name)

# Make Concatenation Operation
print(first_name + " " + last_Name)

name = "I don't know anyone in this session"  # Double quote should be ended with double quote.
print(name)
# If I want to print double quote, then use one escape Sequence by using backward slash
programming = "\"Python\""
print(programming)

# If I need to give a tab in between a sequence of Characters
name = "I Know\tPython"
print(name)

# If I need to print Python in new line :
name = "I Know\nPython"
print(name)
# a. \ --> Escape Sequence
# b. \t --> Tab
# c. \n --> New Line
# *Each datatype in python is a class.

# String Methods.
sent = "I love Python"
print(len(sent))  # Calculate the length of a string. When we call len() method, it also includes a white spaces.
print(sent.index('l'))  # Find the index of specific character in string.
print(sent.replace('P', 'J'))  # Replace P with J.
print(sent.replace('Py', 'Jk'))  # We can also replace a sequence of a character.
print(sent.split('P'))  # It will skip when P comes and returns a value as a list. Here we can find 2 values as List.
print(sent.split(' '))  # Make a list after a space
print(sent.upper())  # Convert to uppercase
print(sent.lower())  # Convert to lowercase.

print("**************************")
sent = "I love python"
print(sent.title())  # Title Case.

print(sent.islower())  # Returns boolean based on cases.
print(sent.count('o'))  # Count the number of occurrences of specific word.

print("********Slicing*************")
myLang = "I know {}".format("Python")  # Using Format method.
print(myLang)
myLang = "I know {} {} {}".format("Python", "Java", "SQL")  # Multiple braces are also allowed.
print(myLang)
myLang = "I know {0} {2} {1}".format("Python", "Java", "SQL")  # If we want to print a sequence in random order,
# we can address based on Index and pass Index number within {}
print(myLang)
# In the above case, there are only 3 values so that we can assign values and remember them easily.
# But wha if there are huge values?
# Then, to avoid this, we can use key associated with that value.
myLang = "I Know {p} {s} {j}".format(p="Python", j="Java", s="SQL")
print(myLang)
# In the above example, we should make sure that we are passing the same amount of argument in format method.

print("**********fStrings**************")
name = "Prashant"
print(f"My name is {name}")
print("******************************")
name = "Prashant"
programming = "Python"
print(f"My name is {name} and I love {programming}")

print("************Indexing**************")
# P     Y       T       H       O       N
# 0     1       2       3       4       5
# -6    -5      -4      -3      -2      -1     # Python also supports -ve index.
sent = "Python is very easy"
print(sent[0])
print(sent[6])  # Whitespace is also considered.
print(sent[-1])  # Get last character.

print("************Slicing**************")
sent = "Python is very easy"
print(sent[2:])
print(sent[2:4 + 1])
print(sent[::2])  # Step Count

print("*******How do you reverse a String ?**************")
print(sent[::-1])
