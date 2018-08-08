the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#the first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count: {number}")

# same as above
for fruit_list in fruits:
    print(f"A fruit_list of type: {fruit_list}")

#print only the third item in the list
print(f"This is the third item in fruits {fruits[2]}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(3,6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)
#now we can print them out too
for i in elements:
    print(f"Element was: {i}")
#print the entire list in elements
print(elements)


for j in range(10,50):
    print(f"This is number i created {j}")
    elements.append(j)

for j in elements:
    print(f"new func: {j}")

print (elements)