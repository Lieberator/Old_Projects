Pets = ['Dottie', 'Daisey', 'Rosie', 'Cheeto', 'Carley']
counter = 0

#for pet in Pets:
	#counter = counter + 1
	#print(str(pet) + " is number: " + str(counter) + " in the order") 


squares = []
for value in range(2,12,2): #does even numbers
	square = value**2
	squares.append(square)
	
print(min(squares))
print(max(squares))
print(sum(squares))

#this creates the same list as above:

values_squared = [value**2 for value in range(2,12,2)]
print(values_squared)

print(values_squared[0:2]) #[beggining index: end index] to obmit parts of the list
print(values_squared[2:])

for values in values_squared[:2]:
	square = values**2
	print(square)
	
#how to copy a list

friends_food= ['pizza', 'candy', 'chips', 'dip']
my_food=friends_food[:]

del my_food[-1]
friends_food.insert(0, 'soda')

for food in my_food:
	print(food)
for food in friends_food:
	print("Friend food:" + str(food))

