# Lets create a tuple.
t1 = (2, 3, 4)
t2 = (10, 20, 30)
t3 = (100, 200, 300)
l1 = [t1, t2, t3]  # This list has 3 Tuples.
print(l1)

# If I want to this list of tuples,
for x in l1:
    print(x)

print("*****Accessing values based on Index*************")
for x in l1:
    print(x[0])
    print(x[1])
    print(x[2])

# instead of an index, there is one more way to get value with proper variable.
print("\n\n*****Unpacking*************")
for a, b, c in l1:  # Tuple Unpacking
    print(a)
    print(b)
    print(c)
