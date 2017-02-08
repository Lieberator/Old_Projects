import unittest
from employees import Employee

#doesnt work yet, and not super important so moving on

class TestRaise(unittest.TestCase):
	
	def setUp(self):
		self.first_name = 'Joe'
		self.last_name = 'Lieberman'
		self.A_salary = 100000
		
	def test_give_default_raise(self):
		value = self.give_raise()
		self.assertEqual(105000, value)
	
	def test_give_custom_raise(self):
		self.give_raise(100000)
		self.assertEqual(200000, self.A_salary)

unittest.main()
		
