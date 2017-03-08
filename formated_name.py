def formated_name(name='',middleName='', lastname=''):
	""" RETURN THE NAME NOMATED """
	fullName = name.title() + " " + middleName.title() + " " + lastname.title()
	return fullName
	
print(formated_name('Fabio','William','Conceição'))
