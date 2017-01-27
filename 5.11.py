numbers = [1,2,3,4,5,6,7,8,9]

for numbers in numbers:
	if numbers > 0 and numbers < 2:
		print(str(numbers) + "st")
	elif numbers > 1 and numbers < 4:
		print(str(numbers) + "nd")
	elif numbers >= 4:
		print(str(numbers) + "th")	
