formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "five", "four"))
print(formatter.format(True, False, False, True, False))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or Lyla can write a song",
    "will the 5th print out?"
))
print(formatter.format(formatter, formatter, formatter, formatter))
