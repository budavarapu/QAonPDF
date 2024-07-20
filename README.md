# QAonPDF
Question and Answers on a PDF using OpenAI 

App1-QandA-using-curl
  Interact with app using POST/GET
App1-QandA-using-GUI
  Perform Q and A using Tkinter based GUI

#Approach
Input Handling:
	Users upload a PDF and provide questions.
	Users specify the Slack channel for posting answers.
Text Extraction:
	Extract text from the uploaded PDF using PyMuPDF.
Question Answering:
	Use OpenAI GPT-4 to answer the provided questions based on the extracted text.
Slack Integration:
	Post the answers to the specified Slack channel using the Slack API.
	
