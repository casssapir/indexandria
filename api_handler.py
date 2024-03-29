import requests
from dotenv import load_dotenv
import os

from rich.console import Console
from rich.text import Text
from rich import box
from rich.panel import Panel
from rich.table import Table

from utils import print_token_info

# Initialize a Rich console for api_handler
console = Console()

load_dotenv()

def send_prompt(prompt, model='openai'):
    # Using Rich for headers and prompts
    console.print(Panel(Text(prompt, style="bold green"), title="Prompt", box=box.DOUBLE))

    console.print(Text("\nSending message to OpenAI (awaiting response)...\n", style="bold yellow"))
    
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

    # Inside send_prompt function, after receiving response and before printing token info:
    if response.status_code == 200:
        console.print(Text("Response received from OpenAI.\n", style="bold blue"))
        data = response.json()
        # Extract and print the assistant's response using Rich
        assistant_message = data['choices'][0]['message']['content']
        console.print(Panel(Text(assistant_message, style="italic"), title="Response", box=box.DOUBLE))

        # Displaying token usage information and calculate costs
        print_token_info(data['usage'], model="gpt-3.5-turbo-0125")  # Pass the model parameter
        
        return data
    else:
        console.print(Text("Failed to get response: " + response.text, style="bold red"))
        return {"error": f"Failed to get response: {response.text}"}
