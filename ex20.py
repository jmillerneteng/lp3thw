from sys import argv
# script is the filename that you are executing and the input file is static in the same line
script, input_file = argv

# funtion to print the input_file that was specified.
def print_all(f):
    print(f.read())
# reset the file back to the 0 position, since i had printed the current_file earlier.  this will reset for the next cmd
def rewind(f):
    f.seek(0)
# print each line of the specified file (f) that was passed in argv
def print_a_line(line_count, f):
    print(line_count, f.readline())
### end of functions ###

#this input_file was passed in the argv
current_file = open(input_file)

print("first let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like tape.")
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)