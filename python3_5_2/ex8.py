#ex8.py
formatter = "{0} {1} {2} {3}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"I had this thing.",
	"That you could type up right",
	"But it didn't sing.",
	"So I said goodnight."
))

#end ex8.py

