# QAonPDF

## Overview
QAonPDF is an application designed to perform question and answer (Q&A) tasks on PDF documents using OpenAI's GPT-3.5-Turbo. The application allows users to extract text from a PDF, answer questions based on the extracted content, and post the results to a specified Slack channel.

## Features

### App1-QandA-using-curl
- **Interact with App Using POST/GET**: This version of the app allows you to interact with the application via HTTP POST and GET requests. You can upload a PDF, provide questions, and specify a Slack channel to receive the answers.

### App1-QandA-using-GUI
- **Perform Q&A Using Tkinter-Based GUI**: This version of the app provides a graphical user interface (GUI) using Tkinter. Users can upload a PDF, enter questions, and view answers in a user-friendly interface.

## Approach

### Input Handling
- **PDF Upload**: Users upload a PDF document.
- **Question Submission**: Users provide a list of questions to be answered.
- **Slack Channel Specification**: Users specify the Slack channel where the answers will be posted.

### Text Extraction
- **PDF Parsing**: Text is extracted from the uploaded PDF using the PyMuPDF library.

### Question Answering
- **Split Text to Chunks and Database creation using Embeddings**: Text is converted to chunks. Embeddings were integrated along with Database store the queries and implement caching technique to serve the queries efficiently.
- **GPT-3.5-Turbo Integration**: OpenAI's GPT-3.5-Turbo model is used to generate answers based on the extracted text and user-provided questions.

### Slack Integration
- **Posting Answers**: The answers are posted to the specified Slack channel using the Slack API.

## Installation

### Requirements
- Python 3.8 or higher
- Required libraries:
  - flask
  - PyMuPDF
  - openai
  - slack_sdk
  - scikit-learn
  - numpy

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/budavarapu/QAonPDF.git
   cd QAonPDF
