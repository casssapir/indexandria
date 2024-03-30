from api_handler import send_prompt
from issue_tracker import SupportIssue

def needs_more_context(message_content):
    # List of phrases that might indicate more context is needed
    indicative_phrases = [
        "can you",
        "not sure",
        "could you",
        "are you"
    ]
    # Check if any of the indicative phrases are in the message content
    return any(phrase in message_content for phrase in indicative_phrases)

def get_more_context(prompt, api_details):
    """
    Manages the interaction loop with the language model, requesting more context when needed.
    
    Parameters:
    - prompt (str): The initial text prompt to send to the language model.
    - api_details (dict): Dictionary containing details required to send the request to the API.
    
    Returns:
    - dict: The final response from the API after any necessary context has been provided.
    """
   # Placeholder for determining the issue category dynamically or from initial user input
    issue_category = "General Inquiry"  # This could be dynamically set based on user input
    
    support_issue = SupportIssue(
        user_id="",  # Placeholder for user ID
        issue_category=issue_category,
        specific_details=prompt,
        hardware_software_details="",
        steps_already_taken=""
    )
   
    # Flag to indicate whether to request context from the LLM
    request_context = True

    while True:
        response = send_prompt(prompt, api_details, request_context)
        
        message_content = response.get('choices', [{}])[0].get('message', {}).get('content', '').lower()
        print(f"Analyzing response for additional context needs: {message_content[:100]}...")  # Print part of the response

        if not needs_more_context(message_content):
            print("No further context requested by the model.")
            break
        
        additional_context = input("Please provide more context to help with your request: ")
        print(f"User provided additional context: {additional_context}")
        
        # Update the SupportIssue object with additional context
        support_issue.hardware_software_details += f" {additional_context}"  # Example of updating details
        support_issue.add_interaction(f"User said: {additional_context}")  # Log interaction

        prompt += f" Additional context: {additional_context}"
        request_context = False

    # After exiting the loop, you can display or log the final state of the support issue
    print(support_issue)
    return response
