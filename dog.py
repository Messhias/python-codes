class Dog():
	""" MODEL A DOG CLASS """
	def __init__(self, name,age):
		self.name = name;
		self.age = age;
		
	def sit(self):
		""" MAKING DOG SIT """
		print(self.name.title() + " is now sitting")
		
	def roll_over(self):
		""" MAKING DOG ROLL OVER """
		print(self.name.title() + " rolled over")
		
		
my_dog = Dog("willie",10)

print("My dog name's " + my_dog.name.title())
print("\nHis age's " + str(my_dog.age))
