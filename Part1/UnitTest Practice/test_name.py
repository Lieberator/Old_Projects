import unittest
"""
from person import Person


from name_function import get_formated_name

class NamesTestCase(unittest.TestCase):
	
	
	def test_first_last_name(self):
		
		formatted_name = get_formated_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
"""
from person import Person

class TestPerson(unittest.TestCase):
	
	def test_store_single_person(self):
		ptest = Person('Joe', 19, 72, 183)
		self.assertEqual(ptest.age, 19)
	
unittest.main()
