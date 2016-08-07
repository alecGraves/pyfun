#ex11.py
#basic input
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall, and %r heavy." % (
	age, height, weight)

print "I want an integer!!"
number = int(raw_input())
print "Thank you for %d." % number
