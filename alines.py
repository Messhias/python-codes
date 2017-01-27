alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

print("The alien color is " + alien_0['color'] + ".")

alien_0['color'] = "yellow"

print("the alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position':0, 'y_position': 25, 'speed':"medium"}

print("Original x position: " + str(alien_0['x_position'])

#Move the alien to right
#Set the distance what the alien has to move by your actual speed
#actual speed
if alien_0['speed'] = "slow":
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#that's must be a faster alien!
	x_increment = 3

#the new position is the older position sum with increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print('New x-position: ' + str(alien_0['x_poisition'])
	
	
