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
   git clone https://github.com/budavarapu/QAUsingPDF/tree/main/App2-QandA-using-GUI.git
   cd App2-QandA-using-GUI
2. pip install -r requirements.txt
3. export OPENAI_API_KEY='your_openai_api_key', export SLACK_TOKEN='your_slack_token'
4. python main.py
5. Opens a Tkinter based GUI, Upload a PDF, Post Queries, Provide Slack Channel and Execute
