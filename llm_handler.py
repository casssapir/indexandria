import logging
import requests
from requests.exceptions import RequestException
import os
from llms import llms

# Send prompt to an llm. Receive a JSON response.
def send_prompt(prompt, llm):
    logging.info(f"Sending prompt to {llm} API: {prompt[:50]}...")

    api_details = llms.get(llm)
    if not api_details:
        raise ValueError(f"API details for {llm} are not in llms.py")

    api_key = os.getenv(api_details['api_key'])
    if not api_key:
        raise ValueError(f"API key for {llm} is not set in the .env file.")

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    payload = {"model": api_details['model'], "messages": [{"role": "user", "content": prompt}]}

    try:
        response = requests.post(api_details['url'], headers=headers, json=payload)
        response.raise_for_status()
        logging.info("Received response successfully from {llm}.")
        return response.json()
    except RequestException as e:
        logging.error(f"Failed to get response from {llm}: {e}")
        return None
