pizza 			= ''
ingriedients 	= []

pizza = input("Digite o nome da pizza: \n")

print("Digite 'quit' para sair")

while True:
	ingriedients.append(input("Digite os ingrientes: \n"))
	if input("Digite os ingrientes: \n") == 'quit' :
		break
		
print("Você escolheu uma pizza de " + pizza.title() + " com os seguintes ingredientes: ")

for items in ingriedients:
	print("\t" + items)
