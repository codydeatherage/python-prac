players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:2]) #for(i = 0; i < 2; i++){ print(); }

print('First three players:')
for player in players[:3]:
	print(player.title())

copy_players = players[:]
print(copy_players)