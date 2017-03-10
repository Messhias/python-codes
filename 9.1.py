class Restaurant():
	""" MODEL A DOG CLASS """
	def __init__(self, name,cuisine):
		self.name = name;
		self.cuisine = cuisine;
		
	def open(self):
		""" MAKING DOG SIT """
		print(self.name.title() + " is now open")
		
	def information(self):
		""" MAKING DOG ROLL OVER """
		print(self.name.title() + " we cook " + self.cuisine)
		
		
r = Restaurant("willie",'2x')

print(r.open())
print(r.information())
