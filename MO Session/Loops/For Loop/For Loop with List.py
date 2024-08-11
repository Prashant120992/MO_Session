# Let's create a list that picks marks one by one each time from the list.
marks = [44, 56, 65, 87, 92, 35]
for m in marks:
    print(m)

    # We can also write the above statements like:
print("\n\n********************Other way of writing a for loop************")
for m in [47, 58, 68, 87, 96, 38]:
    print(m)
print("Bye")

print("\n\n********************Print the final value of list or sum of list element**************************")
sumOfValues = 0
for m in [50, 50, 50, 100, 100, 100]:
    sumOfValues = sumOfValues+m
print("Final Value is ", sumOfValues)
print("Bye")
