# PDF Question Answering AI Agent

## Overview
This AI agent extracts text from a PDF document, answers questions based on the extracted text using OpenAI's GPT-3.5-Turbo, and posts the answers on a specified Slack channel.

## Components
- **`app/__init__.py`**: Initializes the Flask app and sets up routes.
- **`app/routes.py`**: Defines the API endpoints for interacting with the application.
- **`app/text_processing.py`**: Handles PDF text extraction.
- **`app/question_answering.py`**: Manages question answering using OpenAI's API and caching.
- **`app/database.py`**: Manages database operations for caching answers and storing text chunks.

## Upgrades
- Cached Answers: Check if the query made is already answered and use the cahced answer. 
- Early Termination: As soon as an answer to a question is identified, the function stores it in the cache and discontinues any further chunk processing. 
- Answer Caching: Upon completion of processing, the answer is stored in the cache using the cache_answer(question, answer) method.

## Setup

### Prerequisites
- Python 3.7 or higher
- OpenAI API key
- Slack API token

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/budavarapu/QAUsingPDF.git
   cd App1-QandA-using-curl

   pip install -r requirements.txt
   export OPENAI_API_KEY='your_openai_api_key'
   export SLACK_TOKEN='your_slack_token'
   
2. Run the App
   flask run

3. Post Queries using curl
   curl -X POST   -F 'pdf=@path-to-Pdf' -F 'questions=Who is the CEO of the company?'   -F 'slack_channel=#general'   http://127.0.0.1:5000/answer-questions
   
	


