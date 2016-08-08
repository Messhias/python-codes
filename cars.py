cars = [ 'bmw','audi', 'toyota', 'subaru' ]


for car in cars:
	if car == "bmw":
		print(car.upper())
	else:
		print(car.title())

cars.sort()

print(cars)


cars.sort(reverse=True)

print(cars)

cars = [ 'bmw','audi', 'toyota', 'subaru' ]

print("here's the original list: ")
print(cars)

print("here's the sorted list: ")
print(sorted(cars))

print ("here's the original list again " )
print(cars)

cars.reverse()
print(cars)


