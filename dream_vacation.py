local = {}

while True:
	name = input("Digite o seu nome\n")
	location = input("\nQual o local?\n")
	
	local[name] = location
	
	repeat = input("Deseja adicionar mais algum local? (s/n)")
	
	if repeat == "n":
		break;

for name, localation in local.items():
	print(name + " gostaria de ir para " + location + ".\n")
