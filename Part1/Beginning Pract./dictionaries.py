"""alien_0 = {'color': 'green', 'points': 5}
alien_points = alien_0['points']

alien_0['x-pos'] = 0
alien_0['y-pos'] = 25

print("The alien's x position is: " + str(alien_0['x-pos']))

alien_0['x-pos'] = 15

print("The alien's x position is now: " + str(alien_0['x-pos']))

del alien_0['color']
print(alien_0)
"""
"""
user_0={
	'username' : 'balls18118@gmail.com',
	'password' : 'Tootsie2',
	'cell_num' : '7249916509',
	'pass' : 'Tootsie2',
	}

for key, value in sorted(user_0.items()):
	print("\nKey: " + key)
	print("Value: " + value)
	
for key in sorted(user_0.keys()):
	print("Key: " + key)

for value in sorted(set(user_0.values())):
	print("Value: " + value)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points':10}
alien_2 = {'color': 'red', 'points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)
	
aliens = []
 
for alien_number in range(30):
	new_alien = {'color':'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
	
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'
		print(alien)

for alien in aliens[25:]:
	if alien['color'] == 'green':
		alien['color'] = 'red'
		alien['points'] = 15
		alien['speed'] = 'fast'
		print(alien)
	
	
print("\nTotal number of aliens created: " + str(len(aliens)))"""

users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'jlieberman': {
		'first': 'joe',
		'last': 'lieberman',
		'location': 'gibsonia',
		},
	}
	
for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())



