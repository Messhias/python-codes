pizza = {
	'crust'		:	'trick',
	'toopings'	:	['mushrooms','extra cheese'],
}

print ("You ordered a " + pizza['crust'] + "-crust pizza " + 
		"with the following toppings: ")
		
for toopings in pizza['toopings']:
	print("\t" + toopings)
