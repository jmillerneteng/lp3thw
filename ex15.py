from sys import argv
prompt= "holla here>> "
script, filename = argv

txt = open(filename)

print(f"here's your filename:", filename)
print(txt.read())

print("Type the filename again:")
file_again=input(prompt)

txt_again = open(file_again)
print(txt_again.read())