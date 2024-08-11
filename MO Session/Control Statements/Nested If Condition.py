# The Nested if, will check for one condition. If that evaluates to true, it will check another condition.
salary = int(input("Enter the Salary : "))
if salary > 40000:
    print("Eligible for Personal Loan")
    if salary > 60000:
        print("Eligible for Car Loan ")
        if salary > 80000:
            print("Eligible for Home Loan")
            if salary > 100000:
                print("Premium Customer and eligible for all type of loans.")
else:
    print("Sorry we could not serve you any type of loans.")
