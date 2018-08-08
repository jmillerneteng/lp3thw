i = 0
numbers = []
factor = int(input("What*? > "))

while i < 6:
    print(f"At top is {i}")
    numbers.append(i)
    i = i + factor
    print("Number now:", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

range_low=3
range_var=8
for random_number in range (range_low,range_var):
    print(f"This is the new number: {random_number}")

input_low = int(input("Low end?: >"))
input_high = int(input("High end? >"))

for ran_number in range (input_low, input_high):
    print(f"User selected number: {ran_number}")
