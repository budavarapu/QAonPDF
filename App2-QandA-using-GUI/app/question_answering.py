import openai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from .database import get_cached_answer, cache_answer
import logging

logger = logging.getLogger(__name__)
def split_text(text, max_tokens=4000):
    logger.info("Splitting text into chunks.")
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        if len(current_chunk) + len(word.split()) <= max_tokens:
            current_chunk.append(word)
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    logger.info(f"Text split into {len(chunks)} chunks.")
    return chunks

def get_embeddings(texts, openai_api_key):
    openai.api_key = openai_api_key
    embeddings = []
    for text in texts:
        try:
            response = openai.Embedding.create(
                model="text-embedding-ada-002",
                input=text
            )
            embeddings.append(np.array(response['data'][0]['embedding']))
        except Exception as e:
            logger.error(f"Error getting embeddings for text: {e}")
    logger.info(f"Generated embeddings for {len(texts)} texts.")
    return embeddings

def get_question_embeddings(questions, openai_api_key):
    openai.api_key = openai_api_key
    embeddings = []
    for question in questions:
        try:
            response = openai.Embedding.create(
                model="text-embedding-ada-002",
                input=question
            )
            embeddings.append(np.array(response['data'][0]['embedding']))
        except Exception as e:
            logger.error(f"Error getting embeddings for question: {e}")
    logger.info(f"Generated embeddings for {len(questions)} questions.")
    return embeddings

def find_most_relevant_chunks(question_embeddings, text_embeddings, chunks):
    logger.info("Finding most relevant chunks for each question.")
    similarities = cosine_similarity(question_embeddings, text_embeddings)
    most_relevant_chunks = {}
    for i, question_embedding in enumerate(question_embeddings):
        best_chunk_idx = np.argmax(similarities[i])
        most_relevant_chunks[i] = chunks[best_chunk_idx]
    logger.info("Determined most relevant chunks for all questions.")
    return most_relevant_chunks

def get_answers_from_text(text, questions, openai_api_key):
    chunks = split_text(text)
    text_embeddings = get_embeddings(chunks, openai_api_key)
    question_embeddings = get_question_embeddings(questions, openai_api_key)
    most_relevant_chunks = find_most_relevant_chunks(question_embeddings, text_embeddings, chunks)

    answers = {}
    for i, question in enumerate(questions):
        cached_answer = get_cached_answer(question)
        if cached_answer:
            logger.info(f"Found cached answer for question: {question}")
            answers[question] = cached_answer
            continue

        relevant_chunk = most_relevant_chunks[i]
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an intelligent assistant tasked with answering questions based on the provided text from a PDF document."},
                    {"role": "user", "content": f"Context: {relevant_chunk}\n\nQuestion: {question}\n\nYou should also aggregate any relevant information from the following chunks: {chunks}. If the information is not found, please respond with 'Data Not Available'."}
                ],
                max_tokens=150
            )
            answer = response.choices[0].message['content'].strip()
            if "data not available" in answer.lower():
                answer = "Data Not Available"
            cache_answer(question, answer)
            answers[question] = answer
            logger.info(f"Successfully fetched and cached answer for question: {question}")
        except Exception as e:
            logger.error(f"Error fetching answer for question '{question}': {e}")
            answers[question] = f"Error fetching answer: {e}"
    return answers

