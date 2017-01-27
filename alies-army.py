aliens =[]

#create 30 green aliens
for alien_number in range(30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)

#show the 5 firts aliens 
for alien in aliens[:5]:
	print(alien)

print("...")

#show how many aliens has been created
print("Total number of aliens: " + str(len(aliens)))
