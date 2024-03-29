import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def send_prompt(prompt, model='openai'):
    # Check for API key in environment variables
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

    # Prepare the headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Prepare the payload
    payload = {
        "model": "gpt-3.5-turbo" if model == 'openai' else "current_model",  # Update as needed for 'mistral'
        "messages": [{"role": "user", "content": prompt}],
    }

    # URL for OpenAI or Mistral API
    url = "https://api.openai.com/v1/chat/completions" if model == 'openai' else "MISTRAL_API_ENDPOINT"

    # Send the request
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        # Return the JSON response if successful
        return response.json()
    else:
        # Return an error message if the request was not successful
        return {"error": f"Failed to get response: {response.status_code} {response.text}"}

# Example usage
if __name__ == "__main__":
    prompt = "Tell me a joke."
    response = send_prompt(prompt, model='openai')
    print(response)
