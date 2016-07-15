invite_names = ['Maria','Doido','Lolko']

for names in invite_names:
	print(names + " you're invited to a dinner")


refuse_invite = invite_names.pop(1)

invite_names.insert(1,'Novo')

print('\n The ' + refuse_invite + ' cant\' go anymore')


for names in invite_names:
	print(names + " you're invited to a dinner")

