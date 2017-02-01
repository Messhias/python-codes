sandwich_orders 	= ['atun']
finished_sandwich 	= []

while sandwich_orders:
	current_order = sandwich_orders.pop()
	
	finished_sandwich.append(current_order)
	
for finished_sandwich in finished_sandwich:
	print(finished_sandwich.title())	
