def check_Odd_Even_Number(list1):
    Odd_Number = []
    Even_Number = []
    for x in list1:
        if x % 2 == 0:
            Even_Number.append(x)

        else:
            Odd_Number.append(x)
    return Odd_Number


result = check_Odd_Even_Number([1, 50, 12, 3, 8, 13, 76, 77])  # Passing numbers in the form of a list
print(result)
