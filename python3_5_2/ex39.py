# Dictionaries

things = ['a', 'b', 'c', 'd']
print(things[1])

things[1] = 'z'
print(things[1])

things

stuff = {'name' : 'Alec', 'age' : 17, 'height' : 6 * 12 - 1}

print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

stuff['city'] = "Atlanta"

print(stuff['city'])

stuff[1] = "cool"
stuff[2] = "awesome"

print(stuff[1])
print(stuff[2])

stuff

del stuff['city']
del stuff[1]
del stuff[2]

stuff

# create mapping of states to abbreviations
states = {
	'Oregon' : 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every city in state
print('-' *  10)
for state, abbrev in list(states.items()):
	print("%s is abbreviated %s" % (state, abbrev))

# print every city in the state
print('-' * 10)
for abbrev, city in list(cities.items()):
	print("%s has the city %s" % (abbrev, city))

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
	print("%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev]))
# safely get abbreviation by state that may not be there
print('-' * 10)
state = states.get('Texas')

if not state:
	print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is : %s" % city)
