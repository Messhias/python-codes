from car import Car

class EletricCar(Car):
	""" A TYPE OF CAR """
	def __init__(self,make,model,year):
		""" CLASS CONSTRUCTOR """
		super().__init__(make,model,year)
		self.battery = Battery()
		
		
	def fill_gas_tank(self):
		""" FILL GAS TANK """
		print("This car dont have a gas tank")

class Battery():
	""" BATTERY CLASS """
	def __init__(self,batterySize=90):
		""" CLASS CONSTRUCTOR"""
		self.batterySize = batterySize
		
	def describe_battery(self):
		""" DESCRIBE BATTERY """
		print("This car has a " + str(self.batterySize) + "-kwh battery")
	
f	def get_range(self):
		""" SHOW A RANGE LIST """
		if self.batterySize == 70:
			range = 240
		else:
			range = 270
		
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge"
		print(message)
