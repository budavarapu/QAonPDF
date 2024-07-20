# PDF Question Answering AI Agent

## Overview
This AI agent extracts text from a PDF document, answers questions based on the extracted text using OpenAI's GPT-4, and posts the answers on a specified Slack channel.

## Setup

### Prerequisites
- Python 3.7 or higher
- OpenAI API key
- Slack API token

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pdf-question-answering-agent.git
   cd pdf-question-answering-agent

   pip install -r requirements.txt

   export OPENAI_API_KEY='your_openai_api_key'
   export SLACK_TOKEN='your_slack_token'

2. Run the App
   flask run

3. Post Queries using curl
   curl -X POST   -F 'pdf=@path-to-Pdf' -F 'questions=What is the context?'   -F 'slack_channel=#general'   http://127.0.0.1:5000/answer-questions
	


