invite_names = ['Maria','Doido','Lolko']

for names in invite_names:
	print(names + " you're invited to a dinner")


refuse_invite = invite_names.pop(1)

invite_names.insert(1,'Novo')

print('\n The ' + refuse_invite + ' cant\' go anymore')


for names in invite_names:
	print(names + " you're invited to a dinner")

print('\nI noticed i will have a huge new dinner table\n')

invite_names.insert(0,'New invite')
invite_names.insert(1,'Another one')
invite_names.append('Appended one')

for names in invite_names:
	print(names + ' you\'re invited to a dinner')
