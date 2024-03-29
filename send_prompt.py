import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI 
# Model Reference https://platform.openai.com/docs/models/overview
# Cost Reference https://openai.com/pricing

def send_prompt(prompt, model='openai'):
    if model == 'openai':
        response = requests.post(
            "https://api.openai.com/v1/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-3.5-turbo-0125",
                "prompt": prompt,
                "max_tokens": 100,
                "temperature": 0.7,
                "top_p": 1.0,
                "frequency_penalty": 0.0,
                "presence_penalty": 0.0,
            }
        )
    elif model == 'mistral':
        response = requests.post(
            "MISTRAL_API_ENDPOINT", # Replace with the actual Mistral API endpoint
            headers={
                "Authorization": f"Bearer {os.getenv('MISTRAL_API_KEY')}",
                "Content-Type": "application/json",
            },
            json={
                "model": "current_model", # Replace with actual model name if necessary
                "prompt": prompt,
                "max_tokens": 100,
                "temperature": 0.7,
                "top_p": 1.0,
            }
        )
    else:
        raise ValueError("Unsupported model. Choose 'openai' or 'mistral'.")

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to get response: {response.text}"}

# Example usage
if __name__ == "__main__":
    prompt = "Tell me a joke."
    model = 'openai' # or 'mistral'
    
    response = send_prompt(prompt, model=model)
    print(response)
