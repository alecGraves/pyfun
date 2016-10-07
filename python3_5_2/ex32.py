the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This for-loop goes through a list.
for number in the_count:
	print("This is count %d" % number)

# Same as above
for fruit in fruits:
	print("A fruit of type: %s" % fruit)

# Also we can go through mixed lists
# Notice the change to %r because we don't know what is in it.
for i in change:
	print("I got %r" % i)

# We can also build empty lists
elements = []

# Then use the range function to do 0 to 5 counts
for i in range(0,6):
	print("Adding %d to the list." % i)
	# append is used with lists
	elements.append(i)

# Now, we can print them out too
for i in elements:
	print("Element was: %d" % i)
