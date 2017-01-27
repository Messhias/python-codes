current_users  = ['Fabio','William','Maria', 'Ed','Naga' ] 
new_users = ['Jobson','tobão','William','Maria','Ed','Conceição','Fabio']

for new_users in new_users:
	if new_users in current_users:
		print("You can't use " + new_users + ", chose another")
	else:
		print("You can use " + new_users)
