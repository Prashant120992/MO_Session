print("**********Without including 10*****************")
num = 5
while num < 10:
    print(num)
    num = num + 1
    if num == 10:
        break  # This is nothing but terminating.
        # The moment when we say break, it will break the current loop which is while loop in our current case.

# Ideally, the execution starts from 5-15.
# But we have added a condition here if the number is reaching 10 then break this.
# It will not execute anything after 9.
# If we want to print till 10,then, before break, we can print num so that it will include 10 as well.

print("\n\n**********Including 10*****************")
num = 5
while num < 10:
    print(num)
    num = num + 1
    if num == 10:
        print(num)  # It will include till 10.
        break

print("\n\n************When num value is greater than if condition***************")
num = 50
while num < 15:
    print(num)
    num = num + 1
    if num == 10:
        print(num)
        break
# It will not execute even while here. So we can add else part here.
else:
    print("Else part executes here")

print("\n\n************When num value is greater than if condition but lesser than while***************")
num = 11
while num < 15:
    print(num)
    num = num + 1
    if num == 10:
        print(num)
        break

else:
    print("Else part executes here")
