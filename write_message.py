filename = 'programming.txt'

with open(filename,'a') as file_object:
	file_object.write("I love programming.\n")

with open(filename) as file:
	print(file.read())
