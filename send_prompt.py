import requests
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.text import Text
from rich import box
from rich.panel import Panel
from rich.table import Table

# Initialize a Rich console
console = Console()

# Load environment variables
load_dotenv()

# Define a dictionary to hold cost information for various models
MODEL_COSTS = {
    "gpt-3.5-turbo-0125": {
        "input_cost_per_million_tokens": 0.50,  # Cost per 1M input tokens in dollars
        "output_cost_per_million_tokens": 1.50,  # Cost per 1M output tokens in dollars
    }
}

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

def print_token_info(usage, model='gpt-3.5-turbo-0125'):
    model_costs = MODEL_COSTS.get(model, {})
    input_cost = model_costs.get("input_cost_per_million_tokens", 0)
    output_cost = model_costs.get("output_cost_per_million_tokens", 0)

    # Calculate the cost for the used tokens
    prompt_cost = usage['prompt_tokens'] / 1_000_000 * input_cost
    completion_cost = usage['completion_tokens'] / 1_000_000 * output_cost
    total_cost = prompt_cost + completion_cost

    table = Table(title="Token Usage and Costs", box=box.DOUBLE)
    table.add_column("Type", style="cyan", no_wrap=True)
    table.add_column("Tokens", style="magenta")
    table.add_column("Cost (USD)", style="green")

    table.add_row("Prompt Tokens", str(usage['prompt_tokens']), f"${prompt_cost:.4f}")
    table.add_row("Completion Tokens", str(usage['completion_tokens']), f"${completion_cost:.4f}")
    table.add_row("Total Tokens", str(usage['total_tokens']), f"${total_cost:.4f}")
    
    console.print(table)

# Example usage
if __name__ == "__main__":
    prompt = ("My electric vehicle isn't charging when I plug it into the charging station. "
              "I've checked that the charging cable is securely connected to both my vehicle and the charging station, "
              "but the charging process doesn't start. What are some steps I can take to troubleshoot this issue?")
    model = 'openai'  # Specifying to use the OpenAI model
    
    send_prompt(prompt, model=model)  # Print the assistant's response
