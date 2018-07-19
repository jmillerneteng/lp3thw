from sys import argv
first = input("what firstvar?: ")
second = input("what is the secondvar?: ")
third = input("third var?: ")

script, first, second, third = argv

print("this script is called:", script)
print("the first var is:", first)
print("the second var is:", second)
print("the third var is:", third)