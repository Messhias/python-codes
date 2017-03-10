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


newCar = Car("TOYOTA","COROLLA",2000,10)

print(newCar.get_description())

newCar.update_odometer(1300)

print(newCar.read_odometer())

newCar.update_odometer(10)

newCar.increment_odometer(400)

print(newCar.read_odometer())
