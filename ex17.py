from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying {from_file} to {to_file}!")
#! open the from file and assign to in_file
in_file = open(from_file)
#! read the contents of in_file that opened the from_file
in_data = in_file.read()

print(f"The input file is {len(in_data)} bytes long.")

print(f"Does the output file exists? {exists(to_file)}")
print("Hit return to continue.")
input()

#! open the dest file in write mode
out_file = open(to_file, 'w')
#! write the src file contents in indata to the dst file, out_file
out_file.write(in_data)

print("Alright, done.")

#! close the connections to each of the files.
out_file.close()
in_file.close()


