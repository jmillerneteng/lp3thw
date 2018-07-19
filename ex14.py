from sys import argv

script, user_name = argv
prompt = '>!>!>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like ferrets, {user_name}?")
likes = input(prompt)

print(f"Where you eat?, {user_name}? ")
lives = input(prompt)

print(f"{user_name}, what kind of computer you have?")
computer = input(prompt)

print(f"""
ok, you said you {likes} me and you live
in {lives}.  Not sure about that, but 
you also have a {computer} that you code on.
""")