requested_toppings = ["mushrooms","green peppers","extra cheese"]

if requested_toppings:		
	for requested_toppings in requested_toppings:
		if requested_toppings == "green peppers":
			print("sorry we out " + requested_toppings + "right now!")
		else:
			print("Adding " + requested_toppings)

	print("\nFinished making your pizza")
else:
	print("are you sure you want a plain pizza?")
