def city_country(city = '', country = ''):
	""" CALL CITIES COUNTRY """
	return {
		'city'		: city,
		'country'	: country
	}

while True:
	city = input("\nDigite a cidade")
	country = input("\nDigite o pais")
	interation = city_country(city,country)
	for data in interation:
		print(data)
