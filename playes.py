players = ['michael','lol','maria','fabio','roger']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[:-3])

print("Here's are the first three players of my team: ")
for player in players[:3]:
	print(player.title())
