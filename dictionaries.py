
alien_0 = {'color': 'green', 'points': 5, 'position':(4, 20)}
alien_0['position'] = (3, 10)

#adds the species 'peepeeman' to dictionary
alien_0['species'] =  'peepeeman'

print(alien_0)

#deletes species from dictionary
del alien_0['species']
print(alien_0)

user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi'
}

for key, value in user_0.items():
	print(f"Key: '{key}', Value: '{value}'\n")
