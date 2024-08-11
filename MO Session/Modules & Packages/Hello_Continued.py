# Here we are calling the module that we have created(Hello.py).
import Hello

Hello.hello_world()  # This is coming from the function "hello_world()" which is in Hello.py
Hello.calEMI()  # This is coming from the function "calEMI()" which is in Hello.py


# We can also have our own function in this file.

def home_EMI():
    print("The Home EMI is 50K INR/Month")


home_EMI()
