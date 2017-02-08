"""
Joe Lieberman
12/22
nested dictionary and loop practice
"""

pets = { 
	'Big dog': {
		'owner':'joe',
		'weight': 75.2,
		'age': 5,
		'type': 'bermise mountain'
		},
	'Medium dog': {
		'owner': 'meg',
		'weight': 56,
		'age': 12,
		'type': 'hound',
		},
	'cat': {
		'owner': 'bryan',
		'weight': 9.6,
		'age': 8,
		'type': 'tabby',
		},
	}


for pet, info in pets.items():
	print('\nOwner: ' + info['owner'].title())
	
	print("\tCategory: " + pet)
	print("\tType: " + info['type'].title())
	print("\tAge/Weight: " + str(info['age']) + "/" + str(info['weight']))
	
	
			
		
