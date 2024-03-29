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
    - model (str): The model to use (openai, mistral, etc...)

    Returns:
    - dict: A dictionary containing the API's response if successful. In case of failure, returns a dictionary with an error message.

    Raises:
    - ValueError: If the OPENAI_API_KEY is not set in the environment variables.
    """
    # Check for API key in environment variables
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set in the .env file.")

    # Prepare the headers for the request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Prepare the payload with the model and prompt information
    payload = {
        "model": "gpt-3.5-turbo" if model == 'openai' else "current_model", # Choose model based on input
        "messages": [{"role": "user", "content": prompt}], # Encapsulate prompt in the required structure
    }

    # Set the URL for the API request, based on the model selected
    url = "https://api.openai.com/v1/chat/completions" if model == 'openai' else "MISTRAL_API_ENDPOINT"

    # Send the request to the API
    response = requests.post(url, headers=headers, json=payload)

    # Check the response status code to determine if the request was successful
    if response.status_code == 200:
        # Return the JSON response from the API if successful
        return response.json()
    else:
        # Return an error message if the request was not successful
        return {"error": f"Failed to get response: {response.status_code} {response.text}"}

# Example usage to demonstrate how the function can be called
if __name__ == "__main__":
    prompt = "Tell me a joke."
    response = send_prompt(prompt, model='openai')
    print(response)  # Print the response from the API to the console
