def get_formatted_name(first,last, midlle = ''):
	""" RETURN THE FULL NAME """
	if midlle :
		full_name = first + ' ' + midlle + ' ' + last
	else:
		full_name = first + ' ' + last
		
	return full_name.title()
	
