import openai
import time
import logging

logger = logging.getLogger(__name__)

def get_answers_from_text(text, questions, openai_api_key):
    openai.api_key = openai_api_key
    answers = {}
    for question in questions:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an intelligent assistant tasked with answering questions based on the provided text from a PDF document.If the answer to a question is an exact word-for-word match in the text, provide that exact match as the answer."
                        },
                    {"role": "user", "content": f"Text: {text}\n\nQuestion: {question}"}
                ],
                max_tokens=150
            )
            answer = response.choices[0].message['content'].strip()
            if "data not available" in answer.lower():
                answers[question] = "Data Not Available"
            else:
                answers[question] = answer
            logger.info(f"Successfully queried and processed OpenAI chat response : {answers[question]}")
        except Exception as e:
            logger.error(f"Error extracting text from PDF: {e}")
            answers[question] = f"Error fetching answer: {e}"
    return answers

