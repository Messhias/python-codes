from survey import AnnonymousSurvey

#define a question and create a search

question = "Waht language did you first learn to speak?"

survey = AnnonymousSurvey(question)

#show the question and get their answer
survey.show_question()

print("Enter 'q' to quit")

while True:
	response = input("Language: ")
	if response == 'q':
		break
	
	survey.store_response(response)
	
#show the research results
survey.show_results()
