responses = {}

polling_active = True

while polling_active:
	name = input("\nWhat's your name?")
	response = input("Which mountain would you like to climb someday?")
	
	responses[name] = response
	
	repeat = input("Would you like to let another person response? (yes/no)")
	
	if repeat == 'no':
		polling_active = False
	
print("\n --- Poll results --")

for name, response  in responses.items():
	print(name + " would like to climb " + response + ".")
	
