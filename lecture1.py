# print
print("Hello World!")
print(1234567890)
print(3.1415)

# variables
string = "Hello World!"
integer = 1234567890
floatnum = 3.1415

print(string)
print(integer)
print(floatnum)
print(string, integer, floatnum)

# input
name = input("your name?")
age = input("your age?")
phone = input("your phone number?")

print("Your name: " + name)
print("You age: " + age)
print("Your phone numbe: " + phone)

# if elif else
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