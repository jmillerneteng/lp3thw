from sys import argv

script, filename = argv

target = open(filename).read()
print(target)