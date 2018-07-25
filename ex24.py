print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')

poem = """
\tThe lovely world
with logic 
cannot discern \n the needs of love
nor comprehend passion from the institution\n\t where this is none.
"""

print("------------")
print(poem)
print("============")

five = 10-2+3-6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 5
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
#! sending the value of 10,000 to the secret_forumla function.  the returned value of the function will be
#! set to beans, jars, and crates
beans, jars, crates = secret_formula(start_point)

print("With a starting point of {}" .format(start_point))

print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

print("this will put {} {} {}  at the end" .format(beans, jars, crates))

start_point = start_point/10

print("We can also do that this way:")
formula = secret_formula(start_point)
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))