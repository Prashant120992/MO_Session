# Whenever we are writing if, we need to write a condition.
# If this condition is evaluated to true, then it will execute the next set of statements.
# Otherwise, it will continue.
print("Welcome")
if True:  # The "if" statement must end with colon(:)
    print("Hi")  # 4 White spaces.
print("Thanks for watching Videos")

print("False Block")
if False:  # The "if" statement must end with colon(:)
    print("Hi")  # 4 White spaces.
print("Thanks for watching False Videos")

print("**************If statement is True**************** ")
print("The 'a' Value")
a = 80
if a > 50:  # The value of 'a' is greater than the assigned value.
    print("Hello")
print("Thanks for making a Value")

print("**************If statement is False**************** ")
print("The 'a' Value")
a = 80
if a < 50:  # The value of 'a' is greater than the assigned value.
    print("Hello")
print("Thanks for making a Value")

print("**************Else Statement**************** ")
print("The 'a' Value")
a = 80
if a < 50:  # The value of 'a' is greater than the assigned value.
    print("Hello")
else:
    print("Bye")
print("Thanks for making a Value")

print("*********Example :1 for if else block************")
name = "Python1"
if name == "Python":
    print("Python Found")
else:
    print("Python Not Found")
print("Block Completed")

print("*********Example :2 for if else block************")
name = "Python"
if name == "Python":
    print("Python Found")
else:
    print("Python Not Found")
print("Block Completed")
