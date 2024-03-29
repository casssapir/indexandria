import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI 
# Model Reference https://platform.openai.com/docs/models/overview
# Cost Reference https://openai.com/pricing
# in general, 
# English: 1 word ≈ 1.3 tokens
# Spanish: 1 word ≈ 2 tokens
# French: 1 word ≈ 2 tokens

def send_prompt(prompt, model='openai'):
    if model == 'openai':
        response = requests.post(
            "https://api.openai.com/v1/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",  # Use API key from .env
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-3.5-turbo-0125",  # Specify the model
                "prompt": prompt,  # The input text to generate a response for
                "max_tokens": 100,  # Maximum length of the model's response
                "temperature": 0.7,  # 0.0 (more repetitious) - 1.0 (more random) (0.7 is a balanced choice)
                "top_p": 1.0,  # 1.0 = considers all tokens (promotes diversity)
                "frequency_penalty": 0.0,  # 0.0 = no penalty for repeated tokens
                "presence_penalty": 0.0,  # 0.0 = no penalty for new token presence
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
        return response.json()  # Return the model's response
    else:
        return {"error": f"Failed to get response: {response.text}"}  # Handle errors

# Example usage
if __name__ == "__main__":
    prompt = "Tell me a joke."
    model = 'openai'  # Specify the model to use ('openai' or 'mistral')
    
    response = send_prompt(prompt, model=model)
    print(response)  # Print the model's response
