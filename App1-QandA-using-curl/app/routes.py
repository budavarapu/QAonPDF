from flask import Blueprint, request, jsonify
import os
import logging
from .pdf_extractor import extract_text_from_pdf
from .question_answering import get_answers_from_text
from .slack_integration import post_answers_to_slack

bp = Blueprint('main', __name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@bp.route('/answer-questions', methods=['POST'])
def answer_questions():
    try:
        if 'pdf' not in request.files or 'questions' not in request.form or 'slack_channel' not in request.form:
            return jsonify({"error": "Missing required parameters"}), 400

        pdf_file = request.files['pdf']
        questions = request.form.getlist('questions')
        slack_channel = request.form['slack_channel']

        openai_api_key = os.getenv('OPENAI_API_KEY')
        slack_token = os.getenv('SLACK_TOKEN')

        if not openai_api_key or not slack_token:
            logger.error("OpenAI API key and Slack token must be set as environment variables.")
            return jsonify({'error': 'OpenAI API key and Slack token must be set as environment variables.'}), 500

        pdf_path = f"/tmp/{pdf_file.filename}"
        pdf_file.save(pdf_path)

        logger.info("Extracting text from PDF")
        text = extract_text_from_pdf(pdf_path)

        logger.info("Getting answers from text")
        answers = get_answers_from_text(text, questions, openai_api_key)

        logger.info("Posting answers to Slack")
        post_answers_to_slack(answers, slack_token, slack_channel)

        logger.info("Returning JSON response")
        return jsonify({"questions_and_answers": answers})

    except Exception as e:
        logger.error(f"Error processing PDF: {e}")
        return jsonify({'error': str(e)}), 500

@bp.route('/answer-questions', methods=['GET'])
def get_message():
    return jsonify({'message': 'Use POST method to upload a PDF and get answers to your questions.'})



