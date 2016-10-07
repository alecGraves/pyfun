from sys import argv

script, user_name = argv
prompt = '> '

print("Hi {0}, I'm the {1} script.".format(user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me {0}?".format(user_name))
likes = input(prompt)

print("Where do you live {0}?".format(user_name))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said {0} about liking me.
You live in {1}. Not sure where that is.
And you have a {2} computer. Nice.
""".format(likes, lives, computer))
