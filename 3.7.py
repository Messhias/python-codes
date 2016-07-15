invite_names = ['Maria','Doido','Lolko']

for names in invite_names:
	print(names + " you're invited to a dinner")


refuse_invite = invite_names.pop(1)

invite_names.insert(1,'Novo')

print('\n The ' + refuse_invite + ' cant\' go anymore')


for names in invite_names:
	print(names + " you're invited to a dinner")

print('\nI noticed i will have a huge new dinner table\n')

invite_names.insert(4,'New invite')
invite_names.insert(1,'Another one')
invite_names.append('Appended one')

for names in invite_names:
	print(names + ' you\'re invited to a dinner')


print('\nSomething happening\n')

for names in invite_names:
	if(len(invite_names) >= 2):
		invite_names.remove(names)
		print(names + " you're still invited")

del invite_names[0]
del invite_names[1]
del invite_names[0]

print(invite_names)
