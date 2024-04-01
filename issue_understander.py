import logging
from dotenv import load_dotenv
from llm_handler import send_prompt

def craft_issue_understanding_prompt(user_issue, additional_context=""):
    """
    Enhances the initial prompt with user responses to clarifying questions.
    """
    prompt_template = f"""
    As a senior technical support engineer with extensive experience, your task is to review the customer's issue described below and ensure you understand it fully. Based on your understanding, ask one or two clarifying questions to further comprehend the issue.

    Customer's Issue:
    "{user_issue}"

    {additional_context}

    Please provide:
    a) A brief understanding of the issue.
    b) One or two clarifying questions to further understand the issue.
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

def main():
    load_dotenv()
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(filename)s:%(lineno)d:%(message)s')

    print("Please describe the issue you're experiencing:")
    user_issue = input("> ").strip()
    additional_context = ""

    llm = 'openai'  # Specify the LLM service to use

    while True:
        prompt = craft_issue_understanding_prompt(user_issue, additional_context)
        response = send_prompt(prompt, llm)
        clarifying_questions = extract_clarifying_questions(response)

        print("\nLLM's Response:")
        print(clarifying_questions)

        user_input = input("\nYour response (or type 'exit' to finish): ").strip()
        if user_input.lower() == 'exit':
            break

        # Add user's response to the context for the next round of clarification
        additional_context += f"\nCustomer's Response:\n{user_input}\n"

if __name__ == "__main__":
    main()
