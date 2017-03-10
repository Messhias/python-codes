from car import Car

newCar = Car('audi','a4',2010)

print(newCar.get_description())

newCar.odometer = 2000

newCar.read_odometer()
