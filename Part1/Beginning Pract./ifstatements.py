"""fam = ['David', 'Ann', 'Joe', 'Meg']

print('Test of equality:')
for member in fam:
	if member == 'David': #checking for equality is case sensitive
		print(member.upper())
	else:
		print(member.lower())

print('\nTest of inequality:')
for member in fam:
	if member != 'Joe':
		print(member.upper())
	else:
		print(member.lower())


#checking if an item is not in a list
member = 'Bryan'
if member not in fam:
	print(str(member) + " is not in the Lieberman family")"""

'''alien = ['green', 'red', 'yellow']
alien.insert(0, 'yellow')

if 'green' in alien[0]:
	print(" The alien is Green! You're awarded 10 points")
elif 'red' in alien[0]:
	print(" The alien is Red! You're awarded 5 points")
else:
	print("The alien is not Green or Red:( Sorry you're awarded 0 points")'''
	
req_toppings = ['pepperoni', 'squash'] 
available_toppings=['pepperoni', '', 'cheese', 'pineapple']

if req_toppings: #checks to make sure the list isn't empty
	for req_topping in req_toppings:
		if req_topping in available_toppings:
			print('Adding: ' + str(req_topping))
		else:
			print("Sorry we don't have: " + str(req_topping))
else:
	print("are you sure you want plain pizza?")
	
