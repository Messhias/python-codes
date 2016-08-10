string  = 'teste'

if string == 'teste':
	print("true")

if string != 'oi':
	print("false")


string = 'TESTE'

if string.lower() == 'teste':
	print("true")
	
number = 10

if number == 10:
	print("true")
	
if number != 20:
	print("is not 20 the number")
	
if number > 0:
	print("the number is higher than 0")

if number < 100:
	print("the number is lower than 100")
	
if number == 10 and number != 20:
	print ("Yes, the number is 10 and different than 20")

if number > 0 and number < 100:
	print ("the number is highter than 0 and lower than 100")
	
	
itens = ['teste',10,200]

if 'teste' in itens:
	print("the 'teste' is in itens list")
	
if 300 not in itens:
	print("The '300' is not in itens list")
	
