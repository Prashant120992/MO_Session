def check_Even_Number(list1):
    even_Number = []
    for x in list1:

        if x % 2 == 0:
            even_Number.append(x)
        else:
            pass
    return even_Number


result = check_Even_Number([1, 3, 13, 77])
print(result)

# If the list has an empty even number(No even number) then print some message says a list is empty.
# For that, we can use if condition with len inbuilt method.

if len(result) < 0:
    print(result)
else:
    print("Sorry No even numbers found in the list.")
