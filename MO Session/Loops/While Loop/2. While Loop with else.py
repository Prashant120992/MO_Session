print("********Else Condition is evaluated to True************")
num = 10
while num < 15:  # 10 is less than 15. Yes.
    print(num)  # It is printing 10 and incrementing by 1 in the next step. It will continue till 14
    num = num + 1  # There is a requirement for incrementing by 1, 2 or 3. We can increment by any number.
else:
    print("The above condition is not true anymore.")
# Here, once the while condition is evaluated to false, it will execute the else statement.

print("\n\n\n********Else Condition is evaluated to False************")
num = 100
while num < 15:  # Is 100 less than 15. No! So automatically the else print statement executes.
    print(num)
    num = num + 1
else:
    print("The above condition is not true anymore.")
# Here, once the while condition is evaluated to True, it will execute the else print statement.
# The else statement is optional. If we don't have an else statement, that is fine.
