# Let's create 2 sets or 2 lists that anything can be iterated.
print("******Nested for Loop**************")
l1 = ["Rahul", "Rajeev", "Mukhesh"]
l2 = ["Python", "Java", "JS"]
for i in l1:  # Outer Loop.
    for j in l2:  # Inner Loop.
        print(i + " " + j)

print("\n\n*********3 For Loops******")
l1 = ["Rahul", "Rajeev", "Mukhesh"]
l2 = ["Python", "Java", "JS"]
l3 = ["India", "US", "German"]
for a in l1:
    for b in l2:
        for c in l3:
            print(a + " " + b + " " + c)
# We will be using such kind of loops once we start reading an Excel file in a nested format.
