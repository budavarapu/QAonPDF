import logging
import time
import os

LOG_FILE_PATH = 'app_logs.log'
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()

def setup_logging():
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        level=LOG_LEVEL,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def log_event(message, level='INFO'):
    if level == 'INFO':
        logging.info(message)
    elif level == 'WARNING':
        logging.warning(message)
    elif level == 'ERROR':
        logging.error(message)

def log_execution_time(start_time, end_time, operation):
    duration = end_time - start_time
    log_event(f"Execution time for {operation}: {duration:.2f} seconds")

def log_openai_cost(api_usage):
    cost_per_token = 0.02 / 1000  # Example cost
    total_cost = api_usage['total_tokens'] * cost_per_token
    log_event(f"OpenAI API usage cost: ${total_cost:.4f}")


