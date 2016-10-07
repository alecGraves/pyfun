#This is an import:
from sys import argv

#Script, the first variable unpacked from argv,
#	returns the name of the file! (ex13.py)
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
