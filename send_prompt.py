import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def send_prompt(prompt, model='openai'):
    if model == 'openai':
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",  # Use API key from .env
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-3.5-turbo-0125",  # Specify the model
                "messages": [
                    {"role": "user", "content": prompt}
                ],  # Updated to match expected structure
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
        data = response.json()
        # Extract and print the assistant's response
        assistant_message = data['choices'][0]['message']['content']
        print("\nAssistant's response:\n")
        print(assistant_message)
        return data  # Return the full response object for further use if needed
    else:
        print("Failed to get response:", response.text)
        return {"error": f"Failed to get response: {response.text}"}  # Handle errors

# Example usage
if __name__ == "__main__":
    prompt = ("My electric vehicle isn't charging when I plug it into the charging station. "
              "I've checked that the charging cable is securely connected to both my vehicle and the charging station, "
              "but the charging process doesn't start. What are some steps I can take to troubleshoot this issue?")
    model = 'openai'  # Specifying to use the OpenAI model
    
    send_prompt(prompt, model=model)  # Print the assistant's response
