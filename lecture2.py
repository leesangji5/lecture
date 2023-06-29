# if elif else

name = input("your name?")
age = input("your age?")
phone = input("your phone number?")

if name == "sangji":
    print("Hello, Sangji")
elif name == "hyongmin":
    print("Hello, Hyongmin")
else:
    print("Sorry, I dont know")

myAge = 19
if myAge < age:
    print("older than me")
elif myAge > age:
    print("younger than me")
else:
    print("same age")

myPhone = "010-1234-5678"
if myPhone == phone:
    print("impossible")

