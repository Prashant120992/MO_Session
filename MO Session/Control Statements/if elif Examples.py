# What if there are multiple if else condition.That time we can use if elif statements, which is nothing but if else if.
print("*******Example 1 Elif**************")
lang = "Python1"
if lang == "Selenium":
    print("Selenium Found")
elif lang == "Java":
    print("Java Found")
elif lang == "Python":
    print("Python Found")
else:
    print("Sorry we could not found anything\n\n")

print("******Take input from user***************")
lan = input("Enter the language : ")
if lan == "Python":
    print("Python Found")
elif lan == "Java":
    print("Java Found")
elif lan == "Selenium":
    print("Selenium Found")
else:
    print("The", lan, "does not Found\n\n")
