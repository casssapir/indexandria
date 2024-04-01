import logging
import requests
from dotenv import load_dotenv
import os
from requests.exceptions import RequestException
from llm_config import llm_api_details  # Import the API details dictionary

def send_prompt(prompt, llm_service_key):
    logging.info(f"Sending prompt to {llm_service_key} API: {prompt[:50]}...")

    api_details = llm_api_details.get(llm_service_key)
    if not api_details:
        raise ValueError(f"API details for {llm_service_key} are not configured.")

    api_key = os.getenv(api_details['api_key_env_variable'])
    if not api_key:
        raise ValueError(f"API key for {llm_service_key} is not set in the .env file.")

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    payload = {"model": api_details['model_name'], "messages": [{"role": "user", "content": prompt}]}

    try:
        response = requests.post(api_details['url'], headers=headers, json=payload)
        response.raise_for_status()
        logging.info("Received response successfully from {llm_service_key}.")
        return response.json()
    except RequestException as e:
        logging.error(f"Failed to get response from {llm_service_key}: {e}")
        return None
