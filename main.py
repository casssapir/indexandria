import logging
from dotenv import load_dotenv
from llm_handler import send_prompt

# Setup logging config for entire app
def setup_logging(level=logging.INFO):
    logging.basicConfig(level=level,
                        format='%(levelname)s:%(name)s:%(filename)s:%(lineno)d:%(message)s')

def main():
    # Initialize logging with desired level
    setup_logging(level=logging.DEBUG)

    # Load environment variables from a .env file
    load_dotenv()

    # Prompt to send to an LLM
    prompt = ("My electric vehicle isn't charging when I plug it into the charging station. "
              "I've checked that the charging cable is securely connected to both my vehicle and the charging station, "
              "but the charging process doesn't start. What are some steps I can take to troubleshoot this issue?")
    
    # Specifying which LLM service to use ('openai' or 'mistral')
    llm = 'openai'  # Change this key based on the service you want to use

    # Call send_prompt from llm_handler with the specified LLM service
    response = send_prompt(prompt, llm)
    if response:
        # Print the response from the API
        print(response)

if __name__ == "__main__":
    main()
