import json 

def get_stored_username():
	""" GET THE STORED USERNAME IF EXISTS """
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
		
def greet_user():
	""" USER OUTPUT BY YOUR NAME """
	username = get_stored_username()
	if username:
		print("Welcome back, " + username)
	else:
		username = print("What's your name: ")
		filename = 'username.json'
		with open(filename,'w') as f_obj:
			json.dump(username,f_obj)
			print("We'll remember you when you come back, " + username)
			
greet_user()
