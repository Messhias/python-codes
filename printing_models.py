def print_models(unprinted_designs, completed_models):
	"""
		SIMULATE THE PRINTING DESIGN UNTIL HAS NO NE.
		TRANSFER EACH DESIGN FOR COMPLETED_MODELS AFTER THE PRINT
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		
		#SIMULATE THE CREATION OF A 3D IMPRENSION AT DESIGN
		print("Printing model: " + current_design)
		completed_models.append(current_design)
		
def show_completed_models(completed_models):
	""" SHOW ALL PRINTED MODELS """
	print("\nThe following models have been printed")
	for completed_models in completed_models:
		print(completed_models)
	
unprinted_design = ['iphone case', 'robot pendant', 'something']
completed_models = []
print_models(unprinted_design,completed_models)
show_completed_models(completed_models)
