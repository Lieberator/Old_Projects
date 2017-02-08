class Person():
	#simple attempt to model a human
	
	def __init__(self, name, age, height, weight):
		self.name = name
		self.age = age
		self.height = height
		self.weight = weight
		self.numb_of_kids = 0
		
		
	def talk(self):
		print(self.name.title() + " is trying to say something.")
		
	def walk(self):
		print(self.name.title() + " is now walking.")
	
	def gloat(self):
		if self.numb_of_kids != 0 :
			print("\nMy " + str(self.numb_of_kids) + " kids are the best.")
		else:
			print("I'm the best!")

class Kid(Person):
	def __init__(self, name, age, height, weight):
		super().__init__(name, age, height, weight)
	def describe_self(self):
		print("I'm under 18 so thats why I'm still a kid.")
meg = Kid('Megan', 17, 64, 117)
mom = Person('Ann', 49, 68, 132)
dad = Person('David', 51, 69, 185)

mom.numb_of_kids = 2
dad.numb_of_kids = 2

print("My Mom's name is " + mom.name.title() + ".")

Person.talk(mom)

print("Sorry no one was listening please walk away")

Person.walk(mom)

print("\n" + mom.name.title() + " and " + dad.name.title() + " have been together for 20+ years.")

Person.gloat(mom)

Kid.describe_self(meg)
