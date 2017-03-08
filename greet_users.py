def greet_users(names):
	""" GREET USERS LIST """
	for name in names:
		print("Hello, " + name.title() + "!")
		
usernames = ['William','Maria','Fabio']

greet_users(usernames)
