filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''	
for line in lines:
	pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

birthday = input("Enter your birthday, format (dd/mm/YYYY)")
if birthday in pi_string:
	print("In the file")
else:
	print("Not in file")
