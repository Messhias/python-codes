pizzas = ['queijo','portuguesa','carne']

pizzas.append("outra pizza")

friend_pizzas = pizzas[:]

friend_pizzas.append("brocolis")

print("Minhas pizzas favoritas são:")

for pizzas in pizzas:
	print(pizzas)
	
print("\nas pizzas favoritas do meu amigo são: ")

for friend_pizzas in friend_pizzas:
	print(friend_pizzas)
