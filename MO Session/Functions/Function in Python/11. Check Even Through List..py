# Let's make our function accept not only 1 number but number which are in a list.
def check_Even_Number(list1):  # Accepting list.
    even_Number = []  # Creating a list type variable which is a blank list.
    for x in list1:  # All the values will be stored in x.
        # using for loop, I can get value one by one.
        if x % 2 == 0:
            even_Number.append(x)

        # If the X%2==0 evaluates true, then I will add it to the list by using an append method.
        else:
            pass
    return even_Number


result = check_Even_Number([1, 50, 12, 3, 8, 13, 76, 77])  # Passing numbers in the form of a list
print(result)
