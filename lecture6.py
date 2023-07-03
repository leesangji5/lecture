# class

# basic of class

class person():
    pass

person1 = person()

# class variable
class person():
    def __init__(self):
        self.name = "sangji"
        self.age = 19

person1 = person()
person2 = person()

person1.money = 1000
person2.money = 2000

print(person1.money)
print(person2.money)

# class function
class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("hi my name is", self.name)
        other = input("what your name")
        print("hi", other)
        return other
    
person1 = person("sangji", 19)
myname = person1.say_hello()