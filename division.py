print("give me 2 number's and i will divide then for your")
print("Enter 'q' to quit")

while True:
	first_number = input("\nDigit a number")
	if first_number == 'q' or first_number == "Q":
		break
	second_number = input("Digit a second number")
	if second_number == "q" or second_number == "Q":
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero")
	else:
		print(answer)
