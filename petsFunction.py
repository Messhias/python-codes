def describe_pet(animal_type='dog',pet_name):
	""" SHOW SOME INFORMATION ABOUT A ANIMAL """
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster',pet_name='harry')
