# QAonPDF

## Overview
QAonPDF is an application designed to perform question and answer (Q&A) tasks on PDF documents using OpenAI's GPT-3.5-Turbo. The application allows users to extract text from a PDF, answer questions based on the extracted content, and post the results to a specified Slack channel.

Contribution to the project is as follows 
### **Project Concept and Strategy**

- **Idea Formation**: Conceptualized and initiated the project with a mission to conduct QA on PDFs without using traditional frameworks.
- **Expectation Management**: Defined clear objectives and outcomes to guide the project's development and ensure alignment with desired goals.

### **AI Collaboration**
- **Prompt Design**: Developed effective prompts for ChatGPT to generate code and functions that meet the project's requirements.
- **Optimization**: Identified areas for improvement, such as:
  - Implementing caching mechanisms to store answers and reduce redundant computations.
  - Minimizing computational costs through efficient processing strategies.

### **Component Development and Validation**
- **Task Decoupling**: Decomposed the project into distinct, manageable tasks to simplify development and troubleshooting.
- **Functionality Testing**: Rigorously tested each section of the pipeline independently to ensure reliability and seamless integration.
- **Document Handling**: Implemented batch processing for documents to enhance performance with large files.

### **Integration and Communication**
- **Slack API Integration**: Validated the integration of Slack API to facilitate automatic notifications and updates through Slack, enhancing communication and workflow.
  
### **System Testing and Deployment**

- **End-to-End Verification**: Conducted comprehensive testing to ensure the entire solution operates smoothly, whether accessed via curl commands or as part of Slack interactions.

## Features

### App1-QandA-using-curl
- **Interact with App Using POST/GET**: This version of the app allows you to interact with the application via HTTP POST and GET requests. Users must provide path to PDF along with questions, and specify a Slack channel to post the questions and answers.

### App1-QandA-using-GUI
- **Perform Q&A Using Tkinter-Based GUI**: This version of the app provides a graphical user interface (GUI) using Tkinter. Users can upload a PDF, enter questions, and view answers on a slack channel.

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
