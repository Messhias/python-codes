age 	= 0
city 	= ''

print("Digite 'quit' para sair")

city 	= input("Digite sua cidade\n")
while True:
	
	age 	= input("Digite sua idade\n")
	
	if city == "quit" or str(age) == "quit":
		break	
	
	if int(age) >= 0 and int(age) <= 2:
		print("Sua idade é: " + str(age) + ". O ingresso é gratuito")
	elif int(age) >= 3 and int(age) <= 12:
		print("Sua idade é: " + str(age) + ". O ingresso é 10 dolares")
	else:
		print("Sua idade é: " + str(age) + ". O ingresso é 15 dolares")
