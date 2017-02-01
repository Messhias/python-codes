prompt 	= "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' where you are finished.\n"

while True:
	city = input(prompt)
	if city == "quit":
		break;
	else:
		print("I'd love to go " + city.title() + "!")	
		
	
