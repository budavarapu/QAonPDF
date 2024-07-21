from flask import Blueprint, request, jsonify, current_app
from .text_processing import extract_text_from_pdf
from .question_answering import get_answers_from_text
from .database import cache_answer, get_cached_answer
from .slack_integration import post_answers_to_slack
import logging

logger = logging.getLogger(__name__)

api = Blueprint('api', __name__)

@api.route('/answer-questions', methods=['POST'])
def answer_questions():
    logger.info("Received request to /answer-questions")
    try:
        pdf_file = request.files.get('pdf')
        questions = request.form.getlist('questions')
        slack_channel = request.form.get('slack_channel')

        if not pdf_file or not questions or not slack_channel:
            logger.warning("Missing required parameters in request")
            return jsonify({'error': 'Missing required parameters'}), 400

        openai_api_key = current_app.config['OPENAI_API_KEY']
        slack_token = current_app.config['SLACK_TOKEN']

        if not openai_api_key or not slack_token:
            logger.error("OpenAI API key or Slack token is missing")
            return jsonify({'error': 'OpenAI API key and Slack token must be set as environment variables.'}), 500

        pdf_path = f"/tmp/{pdf_file.filename}"
        pdf_file.save(pdf_path)
        logger.info(f"Saved PDF file to {pdf_path}")

        logger.info("Extracting text from PDF")
        text = extract_text_from_pdf(pdf_path)
        
        logger.info("Getting answers from text")
        answers = get_answers_from_text(text, questions, openai_api_key)

        # Post answers to Slack (assuming you have a Slack integration function)
        logger.info("Posting answers to Slack")
        post_answers_to_slack(answers, slack_token, slack_channel)

        logger.info("Returning answers to the request")
        return jsonify({"questions_and_answers": answers})

    except Exception as e:
        logger.error(f"Exception occurred: {e}")
        return jsonify({'error': str(e)}), 500

@api.route('/answer-questions', methods=['GET'])
def get_message():
    return jsonify({'message': 'Use POST method to upload a PDF and get answers to your questions.'})



