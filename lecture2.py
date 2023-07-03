# for
for  i in range(5):
    print(i)

for i in range(0, 5, 2):
    print(i)

array = [1, 2, 3, 4, 5]
print(array[0])
print(array[1])
print(array[2])
print(array[3])
print(array[4])

for i in range(len(array)):
    print(array[i])

customers = ["sangji", 18, "010-1234-5678"]
for i in range(len(customers)):
    print(customers[i])

# while
i = 0
while i < 5:
    print(i)
    i += 1

# while True:
#     print(i)
#     i += 1

while True:
    print(i)
    i += 1
    if i == 5:
        break

while True:
    answer = input("your name?")
    if answer == "sangji":
        print("Hello, Sangji")
        break
    elif answer == "hyongmin":
        print("Hello, Hyongmin")
        break
    else:
        print("Sorry, I dont know")