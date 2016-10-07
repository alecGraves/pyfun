#ex11.py
#basic input
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print("So you're %r old, %r tall, and %r heavy." % (
	age, height, weight))

print("I want an integer!!")
number = int(input())
print("Thank you for %d." % number)
