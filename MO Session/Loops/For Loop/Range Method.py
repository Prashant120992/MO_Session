# Let's say if I want to print the values from 0-100, instead of creating a list, I can use Range method.
print("******************Given start & Stop counters********************")
for x in range(0, 100):  # We can provide start & stop within the brackets.
    # The above line generates the number from 0-100 where the 99 is stop counter. It will not include 100 here.
    # Range() is predefined class.
    print(x)

print("\n\n******************Given only Stop counters********************")
for x in range(100):  # Given only stop counter. It will start from 0 even when we don't provide start counter.
    print(x)

# I need to calculate even and odd numbers falling in between 0-30.
# I want to print even number separately and odd numbers separately.
# For that, we need numbers. So those numbers will be generated by for i in range(0,30).
# To find even and odd, we use %(mod) operator which generally gives us a remainder.
# If the remainder == 0 then it is even, otherwise it is an odd number.
# Create 2 empty lists. 1. evenNumbers 2. oddNumbers.
print("\n\n\n**********Print even and odd Separately******************")
evenNumbers = []  # To store even numbers. By the moment we get even values, we keep on appending into here.
oddNumbers = []  # To store odd numbers. By the moment we get odd values, we keep on appending into here.

for i in range(30):  # Get 0-100 numbers from here.
    if i % 2 == 0:  # Logic to find even and odd.
        evenNumbers.append(i)  # Append even numbers to evenNumbers list.
    else:
        oddNumbers.append(i)  # Append odd numbers to oddNumbers list.
print("evenNumbers = ", evenNumbers)  # Print even a number list.
print("oddNumbers", oddNumbers)  # Print odd number list.
