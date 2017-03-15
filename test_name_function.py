import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	""" UNIT TESTS CASE CLASS """
	def test_first_last_name(self):
		""" TEST FUNCTION GET_FORMATTED_NAME """
		formatted_name = get_formatted_name('Janis','Joplin')
		self.assertEqual(formatted_name,'Janis Joplin')
		
	def test_first_midlle_last_name(self):
		""" TEST FULL NAME """
		formatted_name = get_formatted_name('Fabio','Conceição','William')
		self.assertEqual(formatted_name,'Fabio William Conceição')
		
unittest.main()
