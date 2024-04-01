import logging
from dotenv import load_dotenv
import json
from llm_handler import send_prompt

def craft_issue_understanding_prompt(issue_details, additional_context=""):
    """
    Enhances the initial prompt with user responses to clarifying questions and issue details,
    instructing the LLM to directly ask clarifying questions in the persona of a support person.
    """
    prompt_template = f"""
    You are a senior technical support engineer with extensive experience. 
    A customer has contacted support with an issue, and your task is to ask direct clarifying questions to the customer 
    to fully understand their issue. Use the details provided so far and any additional context from the customer 
    to formulate your questions.

    Details provided so far:
    Who is experiencing the issue: {issue_details['Who']}
    What is the issue: {issue_details['What']}
    Where is the issue happening: {issue_details['Where']}
    When the issue started: {issue_details['When']}
    Why is the issue occurring: {issue_details['Why']}

    Additional context from the customer:
    {additional_context}

    Directly ask one or two clarifying questions to the customer to help further diagnose the issue.
    """

    return prompt_template.strip()


def extract_clarifying_questions(llm_response):
    """
    Extracts clarifying questions from the LLM's response.
    """
    try:
        content = llm_response['choices'][0]['message']['content']
        return content
    except KeyError:
        return "I'm sorry, I couldn't generate a response. Could you please provide more details or clarify your question?"


def initialize_issue(user_issue):
    """
    Initializes the issue with the user's initial description of the issue.
    """
    return {
        "Who": "Unspecified",
        "What": user_issue,
        "Where": "Unspecified",
        "When": "Unspecified",
        "Why": "Unspecified"
    }

def update_issue_details(issue_details, llm_response):
    """
    Updates the issue details based on the LLM's response.
    """
    # Placeholder for the logic to parse llm_response and update issue_details
    # This logic will depend on the structure of the LLM's response
    # For demonstration, let's assume llm_response contains directly applicable updates
    pass

def save_issue_details_to_json(issue_details, filename='issue_details.json'):
    """
    Saves the issue details to a JSON file.

    Parameters:
    - issue_details: The dictionary containing the issue information.
    - filename: The name of the file to save the issue details to.
    """
    with open(filename, 'w') as file:
        json.dump(issue_details, file, indent=4)

def main():
    load_dotenv()
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(filename)s:%(lineno)d:%(message)s')

    print("Please describe the issue you're experiencing:")
    user_issue = input("> ").strip()
    additional_context = ""

    llm = 'openai'  # Specify the LLM service to use

    # Initialize the issue with the user's issue
    issue_details = initialize_issue(user_issue)

    while True:
        prompt = craft_issue_understanding_prompt(issue_details, additional_context)
        response = send_prompt(prompt, llm)
        clarifying_questions = extract_clarifying_questions(response)

        print("\nLLM's Response:")
        print(clarifying_questions)

        user_input = input("\nYour response (or type 'exit' to finish): ").strip()
        if user_input.lower() == 'exit':
            break

        # Update issue details based on user's response and save to a JSON file
        # Assume all responses go into 'What' for simplicity
        issue_details['What'] += f" {user_input}"

        # Save the updated issue details to a JSON file
        save_issue_details_to_json(issue_details)

        # Add user's response to the context for the next round of clarification
        additional_context += f"\nCustomer's Response:\n{user_input}\n"

if __name__ == "__main__":
    main()
