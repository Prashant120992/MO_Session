print("************Example***********")
feedback = ""  # By default I am giving it as blank string.
while feedback not in ["1", "2", "3", "4", "5"]:  # Checking with list values.
    # Creating a while loop where I want to just check if the feedback within the list
    feedback = input("Please enter your feedback! : ")
    print("Thank you!")
# When we enter any number, the feedback will evaluate if the entered number is within the list of values.
'''Lets say if I enter 9, it will store into variable 9, then it will compare with a list, it will continue for 
another input to get from user. It will continue till the user provides the number which is within the list'''
# Example: The 4 is within the list. The Loop exits by printing only "Thank you!"
