def build_person(name ='', lastname='',age=0):
	""" RETURN A DICTIONARY OF PERSONS """
	person = {
		"First": name.title(), 
		"Last name": lastname.title()
	}
	if age:
		person['age'] = age
	
	return print(person)
	
build_person("Fabio","William")
