# function
# 8.1 basic of function

def printHello():
    print("Hello World!")
    a = 1
    b = 2
    print(a + b)

# error
#print(a)

printHello()

def main():
    printHello()

main()

# 7.2 parameter
def printName(name):
    print("Hello, " + name)

printName("sangji")

# 7.3 return
def returnName():
    return "sangji"

name = returnName()
print(name)


def printName(name):
    string = "Hello, " + name   
    return string

name = printName("sangji")
print(name)