import logging
from dotenv import load_dotenv
from llm_handler import send_prompt  # Import send_prompt from llm_handler

def craft_problem_understanding_prompt(user_issue):
    """
    Creates a prompt for the LLM, instructing it to act as a senior technical support engineer.
    """
    prompt_template = f"""
    As a senior technical support engineer with extensive experience, your task is to review the customer's issue described below and ensure you understand it fully. After reviewing the issue, share a brief understanding of the issue and ask one or two clarifying questions to further comprehend the issue.

    Customer's Issue:
    "{user_issue}"

    Based on your expertise, please provide:
    a) A brief understanding of the issue.
    b) One or two clarifying questions to further understand the issue.
    """

    return prompt_template.strip()

def get_user_issue():
    """
    Prompts the user to describe their issue in a sentence or two.
    """
    print("Please describe the issue you're experiencing in a sentence or two:")
    user_issue = input("> ").strip()
    return user_issue

def main():
    # Setup environment and logging
    load_dotenv()
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(filename)s:%(lineno)d:%(message)s')

    user_issue = get_user_issue()
    prompt = craft_problem_understanding_prompt(user_issue)

    # Specify which LLM service to use ('openai', 'mistral', etc.)
    llm = 'openai'

    # Sending the crafted prompt to the LLM and receiving the response
    response = send_prompt(prompt, llm)
    if response:
        # Process and display the LLM's response
        print("\nLLM's Response:")
        print(response)  # Modify as needed to extract and display relevant information from the response

if __name__ == "__main__":
    main()
