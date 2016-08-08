my_foods = ['pizza','hamburguer','carrot']
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite's' foods are: ")
for my_foods in my_foods:
	print(my_foods)

print("\nMy friend's favorite food are: ")
for friend_foods in friend_foods:
	print(friend_foods)
