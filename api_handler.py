import requests
from dotenv import load_dotenv
import os

# Load environment variables from a .env file located in the same directory.
load_dotenv()

def send_prompt(prompt, api_details, request_context=False):  # Added request_context parameter
    """
    Sends a text prompt to a specified language model API and returns the response.

    Parameters:
    - prompt (str): The text prompt to send to the language model.
    - api_details (dict): A dictionary containing details required to send the request,
                          including the API key, URL, model name, and any other necessary information.
    - request_context (bool): Optional flag indicating whether more context is being requested.

    Returns:
    - dict: A dictionary containing the API's response if successful. In case of failure, returns a dictionary with an error message.
    """
    api_key = os.getenv(api_details['api_key_env_variable'])
    if not api_key:
        raise ValueError(f"API key for {api_details['model']} is not set in the .env file.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    
    # Optional: Modify the prompt based on the request_context flag if necessary
    if request_context:
        # Here you can adjust the prompt or take other actions based on request_context
        pass

    payload = {
        "model": api_details['model_name'],
        "messages": [{"role": "user", "content": prompt}],
    }

    # Send the request to the API
    response = requests.post(api_details['url'], headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to get response: {response.status_code} {response.text}"}


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
