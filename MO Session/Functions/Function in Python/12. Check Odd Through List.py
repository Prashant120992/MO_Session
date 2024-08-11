# Let's make our function accept not only 1 number but number which are in a list.
def check_Odd_Number(list1):  # Accepting list.
    Odd_Number = []  # Creating a list type variable which is a blank list.
    for x in list1:  # All the values will be stored in x.
        # using for loop, I can get value one by one.
        if x % 2 == 0:
            pass
        else:
            Odd_Number.append(x)
    return Odd_Number


result = check_Odd_Number([1, 50, 12, 3, 8, 13, 76, 77])  # Passing numbers in the form of a list
print(result)
