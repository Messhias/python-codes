class AnnonymousSurvey():
	""" CLASS TO COLLECT ANSWERS ABOUT SURVEY """
	def __init__(self,question):
		""" CLASS CONSTRUCTOR """
		self.question = question
		self.responses = []
		
	def show_question(self):
		""" SHOW THE QUESTION OF SEARCH """
		print(self.question)
		
	def store_response(self,new_response):
		""" STORE THE NEW RESPONSE """
		self.responses.append(new_response)
		
	def show_results(self):
		""" SHOW QUESTION RESPONSES """
		print("Survey results: ")
		for response in self.responses:
			print(" - " + response)
