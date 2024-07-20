# PDF Question Answering AI Agent

## Overview
This AI agent extracts text from a PDF document, answers questions based on the extracted text using OpenAI's GPT-3.5, and posts the answers on a specified Slack channel. The agent is implemented as a Flask web application.

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

python main.py

Opens a Tkinter based GUI, Upload a PDF, Post Queries, Provide Slack Channel and Execute
