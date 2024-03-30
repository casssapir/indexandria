import requests
from dotenv import load_dotenv
import os
import logging
from requests.exceptions import RequestException

# Initialize logging
# set log level to DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s:%(name)s:%(filename)s:%(lineno)d:%(message)s')

# Load environment variables from a .env file
load_dotenv()

def send_prompt(prompt, api_details, request_context=False):
    logging.info(f"Sending prompt to API: {prompt[:50]}...")

    api_key = os.getenv(api_details['api_key_env_variable'])
    if not api_key:
        raise ValueError(f"API key for {api_details['model']} is not set in the .env file.")

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    payload = {"model": api_details['model_name'], "messages": [{"role": "user", "content": prompt}]}

    try:
        response = requests.post(api_details['url'], headers=headers, json=payload)
        response.raise_for_status()  # This will raise an HTTPError for bad responses
        logging.info("Received response successfully.")
        return response.json()
    except RequestException as e:
        logging.error(f"Failed to get response: {e}")
        return None

# Example usage should ideally be in a separate file or entry point
if __name__ == "__main__":
    prompt = "I can't log in to my account. Can you help?"
    openai_details = {
        "api_key_env_variable": "OPENAI_API_KEY",
        "url": "https://api.openai.com/v1/chat/completions",
        "model_name": "gpt-3.5-turbo",
    }
    mistral_details = {
        "api_key_env_variable": "MISTRAL_API_KEY",
        "url": "https://api.mistral.ai/v1/chat/completions",
        "model_name": "open-mixtral-8x7b",
    }
    # Try changing 'openai_details' to 'mistral_details' to test with Mistral AI
    response = send_prompt(prompt, openai_details)
    print(response)
