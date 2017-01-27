favorite_languages = {
	'jim'	:	['python'],
	'sarah'	:	['c']	,
	'edward':	['ruby']	,	
	'phil'	:	['python'],
}

for name, languages in favorite_languages.items():
	print("\n" + name.title() +"'s favorite languages are: ")
	for languages in languages:
		print("\t" + languages.title())
