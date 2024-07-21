from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import logging

logger = logging.getLogger(__name__)

def post_answers_to_slack(answers, slack_token, slack_channel):
    client = WebClient(token=slack_token)
    message = "\n".join([f"Q: {q}\nA: {a}" for q, a in answers.items()])
    try:
        logger.info(f"Posting answers to Slack channel: {slack_channel}")
        response = client.chat_postMessage(
            channel=slack_channel,
            text=message
        )
        logger.info("Successfully posted answers to Slack")
    except SlackApiError as e:
        logger.error(f"Error posting to Slack: {e.response['error']}")
        raise ValueError(f"Error posting to Slack: {e.response['error']}")

