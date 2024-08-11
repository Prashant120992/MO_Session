print("*********Only continue within if Block***************")
num = 1
while num < 10:
    num = num + 1
    if num == 5:  # This number skips and continues further.
        continue
    print(num)  # The output will be 2, 3, 4, 6,7,8,9,10, but it skips 5.
# Note that the indentation, within the "if", there is only 1 statement. That is "continue".
# The print after continue statement is part of while.
# The continuing basically says, if the condition meets true, then continue for while loop again.

print("\n\n*********print&continue within if Block***************")
num = 1
while num < 10:
    num = num + 1
    if num == 5:
        continue
        print("Python")
    print(num)
else:
    print("Condition is no more true")
