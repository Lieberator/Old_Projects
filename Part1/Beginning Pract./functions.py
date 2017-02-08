def choose_toppings():
	prompt="What topping would you like, enter one at a time (enter done to stop adding toppings): "
	topping = input(prompt)
	
	return topping
	
def make_pizza(toppings, crust):
	#print list of toppings that are requested
	
	print("\n Making pizza with " + crust + " crust and the following toppings:")
	
	for topping in toppings:
		print("- " + topping)
		
		
toppings = []

print("Welcome to Joe's Dough!")

while True:
	top_req = choose_toppings()
	if top_req == 'done':
		break
	else:
		toppings.append(top_req)

crust = input("What kind of crust would you like? (Thin, Thick, Sicilian): ")
 
make_pizza(toppings, crust)
	

	

