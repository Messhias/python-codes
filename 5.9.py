users = ['william','maria','admin']

if users:		
	for users in users:
		if users == 'admin':
			print("\nHello " + users + ", did you like status report?")
		else:
			print("Hello " + users + ", thanks for login again")
else:
	print("No users to login")


