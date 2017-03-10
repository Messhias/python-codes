from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jim'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, languages in favorite_languages.items():
	print("\n" + name.title() +"'s favorite languages are: ")
	for languages in languages:
		print("\t" + languages.title())
