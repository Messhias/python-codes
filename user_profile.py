def build_profile(first,last, **user_info):
	""" CONSTRUCT DICTIONARY OF USER INFO """
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('Fabio',' William',
	city='Cubatão', field='development', role='programmer')

print(user_profile)
