from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def post_answers_to_slack(answers, slack_token, slack_channel):
    client = WebClient(token=slack_token)
    message = "\n".join([f"Q: {q}\nA: {a}" for q, a in answers.items()])
    try:
        response = client.chat_postMessage(
            channel=slack_channel,
            text=message
        )
    except SlackApiError as e:
        raise ValueError(f"Error posting to Slack: {e.response['error']}")


