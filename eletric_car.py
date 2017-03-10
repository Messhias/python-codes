class Car():
	""" CAR CLASS """
	
	def __init__(self,make,model,year,odometer=0):
		""" CLASS CONSTRUCTOR """
		self.make = make
		self.model = model
		self.year = year
		self.odometer = odometer
		
	def get_description(self):
		""" GET CAR DESCRIPTION """
		long_name = str(self.year) + " " + self.make.title() +" " + self.model.title()
		return long_name.title()
		
	def read_odometer(self):
		""" READ CAR ODOMETER """
		print("This car has " + str(self.odometer) + " miles on  it")
	
	def update_odometer(self,mileage):
		""" UPDATE ODOMETER MILES """
		if self.odometer <= mileage:
			self.odometer = mileage
		else:
			print("You can't rollback the odometer")
		
	def increment_odometer(self,miles):
		""" INCREMENT ODOMETER WITH A VALUE """
		self.odometer += miles

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



tesla = EletricCar('tesl','model s',1900)

print(tesla.get_description())

tesla.battery.describe_battery()

tesla.fill_gas_tank()
