import json

numbers = [2, 3, 4, 5, 6, 7, 8]


filename = 'numbers.json'

with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)

