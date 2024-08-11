# As discussed in earlier, the loops are used to repeat the task efficiently.
# Whenever we have a multiple statement to execute, instead of executing statement by statement, we can run in a loop.
# The first step while creating a while loop is initialized. Because while loop works on conditions.

print("***************Demo 1**********************")
x = 1
# Need to write while after that need to write a condition.
# If this condition is evaluated to true, it will execute while loop, otherwise it will not execute while loop.
# If I want "x" to print for 10 times then.
while x < 10:  # 1<10, 2<10, 3<10...... it will print when the x value is <10
    print("The Value of x :", x)  # 1,2,3...........
    x = x + 1  # 1= 1+1=2..............
# The output will be 1...9 because we have assigned less than(<)

print("\n\n***************Demo 2**********************")
y = 1
while y <= 10:
    print("The Value of y :", y)
    y = y + 1
# The output will be 1…10 as we have assigned less than equal to(<=).

print("\n\n***************Demo 3**********************")
y = 3
while y <= 10:
    print("The Value of y :", y)
    y = y + 1
print("Bye Bye")
# The output will be 3…10 as we have initialized the value as 3 starting points.

# Whenever we are not making any increment or decrement, the loop will execute infinitely.
# 2 Ways to stop the infinite loop execution either press the stop icon or Ctrl+c
# x=5
# while x<10: → This condition will never get false, so loop will execute infinitely. Here 5 is always less than 10.
#  print("Python")
# The moment if we don't increment or decrement, the condition will always be true. It will always run an infinite loop.
'''The use case is like a monitor server that is up & running or not. For that we need to keep on ping request.
 It should be done 24*7 where we dont want our program to stop & run continuously.'''
