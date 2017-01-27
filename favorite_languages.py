favorite_languages = {
	'jim'	:	'python',
	'sarah'	:	'c'		,
	'edward':	'ruby'	,	
	'phil'	:	'python',
}

print(
	"Sarah's farorite language is " + favorite_languages['sarah'].title() + "."
)


for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is : " + language.title() + "." )


for names in favorite_languages.keys():
	print(names.title())


friends = ['phil', 'sarah']

for name, language in favorite_languages.items():
	print(name.title())
	if name in friends:
		print(
			'hi ' + name.title() + ', i see you favorite language is ' +
			language.title()  + "."		)
		
if 'erin' not in favorite_languages.keys():
	print('please erin take our poll')
	
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thanks for take our poll")
	

print('the following languages have been mentioned')
for language in favorite_languages.values():
	print(language.title())



print('the following languages have been mentioned')
for language in set(favorite_languages.values()):
	print(language.title())
