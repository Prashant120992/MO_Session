# Module is just a python file. Any file with .py extension can be considered as module.

"""The module can contain
multiple functions, we can have classes, can have variables, and also it can have runnable code."""

'''There can be a Call existing module from python, user defined modules, 
external module which are not available in python. '''

# Combination of multiple packages we can make a package.

'''Lets say if I need to develop bank application, 
currently assume that there are modules available separately called carload, homeland and personal loan. 
We can make use of these ready made modules and build an application.'''

# Module will help when it comes to reusability and make code as readable as well.
# When we combine multiple modules, it is officially considered as python package.
# When we create a python package, it will create a standard __init__py file.
# Let's use existing module here.

# Lets use calender module.
# One module can also import another module.

# When we are using any ib built module, then we can start with import and later module name. Here calendar is a module.

import calendar

result = calendar.month(2024, 9)


class Yes:
    pass


Yes

print(result)
