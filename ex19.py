def ip_address(first,second,third,fourth)
    print(f"{first},{second}.{third}.{fourth}")
    print(f"Network Summary: {first}.{second}.{third}.0 /24")

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("that be a lot of crackers.")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers -2)

