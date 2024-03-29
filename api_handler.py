import requests
from dotenv import load_dotenv
import os

# Load environment variables from a .env file located in the same directory.
load_dotenv()

def send_prompt(prompt, model='openai'):
    """
    Sends a text prompt to a specified language model API and returns the response.

    Parameters:
    - prompt (str): The text prompt to send to the language model.
    - model (str): The model to use ('openai' for OpenAI's models, 'mistral' for Mistral AI's models).

    Returns:
    - dict: A dictionary containing the API's response if successful. In case of failure, returns a dictionary with an error message.
    """
    # Determine which API key and endpoint to use based on the model parameter
    if model == 'openai':
        api_key = os.getenv('OPENAI_API_KEY')
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
        }
    elif model == 'mistral':
        api_key = os.getenv('MISTRAL_API_KEY')
        url = "https://api.mistral.ai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": "open-mixtral-8x7b",  # Or other Mistral model names as required
            "messages": [{"role": "user", "content": prompt}],
        }
    else:
        raise ValueError(f"Unsupported model: {model}")

    # Ensure API key is provided
    if not api_key:
        raise ValueError(f"API key for {model} is not set in the .env file.")

    # Send the request to the API
    response = requests.post(url, headers=headers, json=payload)

    # Check the response status code to determine if the request was successful
    if response.status_code == 200:
        # Return the JSON response from the API if successful
        return response.json()
    else:
        # Return an error message if the request was not successful
        return {"error": f"Failed to get response: {response.status_code} {response.text}"}

# Example usage
if __name__ == "__main__":
    prompt = "Tell me a joke."
    # Try changing 'openai' to 'mistral' to test with Mistral AI
    response = send_prompt(prompt, model='mistral')
    print(response)
