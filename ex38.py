ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("There are not 10 things in that list.  Let's fix it...")

stuff = ten_things.split(' ')

print(f"here is the split from_ten_things \n {stuff}")

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("Adding: " , next_one)
	stuff.append(next_one)
	print(f"There are {len(stuff)} items now.")

print("There we go: ",stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #whoa, yeah
print(stuff.pop())
print(" ".join(stuff)) # umm what?
print("#".join(stuff[3:5])) #roxtar

