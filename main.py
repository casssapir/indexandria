import logging
from dotenv import load_dotenv
from llm_handler import send_prompt

# Setup logging level and format for entire app
# Level options are DEBUG, INFO, WARN, ERROR, and CRITICAL
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(filename)s:%(lineno)d:%(message)s')

def main():
    # Load environment variables from a .env file
    load_dotenv()

    # Read the prompt from an external file
    with open("prompt.txt", "r") as file:
        prompt = file.read().strip()
    
    # Specify which LLM service to use ('openai' or 'mistral')
    llm = 'openai'

    # Call send_prompt from llm_handler
    response = send_prompt(prompt, llm)
    if response:
        # Print the response from the API
        print(response)

if __name__ == "__main__":
    main()
