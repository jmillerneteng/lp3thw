from sys import argv

script, filename = argv

print(f"We are going to erase", {filename})
print("If you don't want to erase, hit ctr-c (^c)")
print("if you do want to destroy, hit RETURN.")

input("decision...? ")
print("Opening the file...")
target = open(filename, 'w')
print("Truncating the file.  See yah!")
target_read = open(filename, 'r')

target.truncate()

print("Now we are going to insert three lines.")
#line1 = input("Line1: ")
#line2 = input("Line2: ")
#line3 = input("Line3: ")
line = input(""" Write here: """)
print("I'm going to write these to the file")

target.write(line)

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("And we now close the file")
target.close()

print("Here is what you just typed, by opening the file again in read mode")
print(target_read.read())