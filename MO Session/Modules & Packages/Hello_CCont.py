# What if I don't want to mention module name each time.
from Hello import hello_world
from Hello import calEMI
# The below statement shows how to import multiple functions in a single statement.
from Hello import hello_world, calEMI
# If we have more function to import then, we can use import *. The following statement shows the same.
from Hello import *
# Using *(Wildcard), we can import.
from ModulesPackages1.Hello import *      # Coming from different package.
# Here we are saying from Hello which function to mention.

hello_world()
calEMI()
personalLoanEMI()

# However, this approach is not much effective as we are importing all the functions one by one.
'''There is a way to 
import multiple functions with one statement. We can pass multiple function names separated with comma.'''

# This approach will work when everything is within the same working directory. What if there is different package.
