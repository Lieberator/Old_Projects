class Employee():
	
	def __init__(self, fname, lname, salary):
		self.first_name = fname
		self.last_name = lname
		self.A_salary = salary
		
	def give_raise(self, raze=0):
		if raze==0:
			self.A_salary += 5000
		else: 
			self.A_salary += raze
	

One = Employee('joe', 'lieberman', 100000)

One.give_raise(10000)

print(One.A_salary)
