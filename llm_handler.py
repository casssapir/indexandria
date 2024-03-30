import requests
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

def send_prompt(prompt, api_details, request_context=False):
    print(f"Sending prompt to API: {prompt[:50]}...")  # Print the first 50 characters of the prompt

    api_key = os.getenv(api_details['api_key_env_variable'])
    if not api_key:
        raise ValueError(f"API key for {api_details['model']} is not set in the .env file.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": api_details['model_name'],
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post(api_details['url'], headers=headers, json=payload)

    if response.status_code == 200:
        print("Received response successfully.")
    else:
        print(f"Failed to get response: {response.status_code} {response.text}")
    
    return response.json()


# Example usage
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
