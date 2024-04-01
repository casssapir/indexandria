def craft_problem_understanding_prompt(user_issue):
    """
    Creates a prompt for the LLM, instructing it to act as a senior technical support engineer.
    
    Parameters:
    - user_issue: Brief description of the issue provided by the user.
    
    Returns:
    - A string containing the crafted prompt.
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
    
    Returns:
    - User input as a string.
    """
    print("Please describe the issue you're experiencing in a sentence or two:")
    user_issue = input("> ").strip()
    return user_issue

def main():
    user_issue = get_user_issue()
    prompt = craft_problem_understanding_prompt(user_issue)
    
    # For demonstration purposes, we'll print the prompt to the console.
    # In a real application, you would send this prompt to an LLM via an API call.
    print("\nCrafted Prompt for LLM:")
    print(prompt)

if __name__ == "__main__":
    main()
