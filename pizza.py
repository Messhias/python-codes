def make_pizza(size,*toppings):
	""" LIST INGRIEDIENTS """
	print("\n The pizza's size is " + str(size))
	
	for toppings in toppings:
		print("\n- " + toppings)
