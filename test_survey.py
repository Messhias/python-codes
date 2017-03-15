import unittest
from survey import AnnonymousSurvey

class TestAnnonymousSurvey(unittest.TestCase):
	""" UNIT TEST FOR ANNONYMOUS SURVEY CLASS """
	
	def setUp(self):
		""" CREATE A RESEARCH AND A LIST OF RESPONSES WICH COULD 
		USED BY IN ALL TESTS METHODS """
		question = "Waht language did you first learn to speak?"
		self.survey = AnnonymousSurvey(question)
		self.responses = ['English','PT','ES']
		
	
	def test_store_single_response(self):
		""" TEST A SINGLE RESPONSE TO SURVEY """
		self.survey.store_response(self.responses[0])
		self.assertIn(self.responses[0],self.survey.responses)
		
	def test_tree_answer(self):
		""" TEST """
		for response in self.responses:
			self.survey.store_response(response)
		
		for response in self.responses:
			self.assertIn(response,self.survey.responses)
		

unittest.main()
