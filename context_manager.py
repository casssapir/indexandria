from api_handler import send_prompt

def get_more_context(prompt, api_details):
    """
    Manages the interaction loop with the language model, requesting more context when needed.
    
    Parameters:
    - prompt (str): The initial text prompt to send to the language model.
    - api_details (dict): Dictionary containing details required to send the request to the API.
    
    Returns:
    - dict: The final response from the API after any necessary context has been provided.
    """
    # Flag to indicate whether to request context from the LLM
    request_context = True

    while True:
        # Send the initial or updated prompt to the API
        response = send_prompt(prompt, api_details, request_context)

        # Assuming the model's response can indicate the need for more context,
        # check the response here and break the loop if no more context is needed
        if not "more context is required" in response.get('choices', [{}])[0].get('message', '').lower():
            break  # Exit the loop if no more context is requested by the model
        
        # Request additional context from the user
        additional_context = input("Please provide more context to help with your request: ")
        prompt += f" Additional context: {additional_context}"  # Append the additional context to the prompt

        # Optionally, turn off the request_context flag if you don't want the model to keep asking for more context
        request_context = False  # Adjust based on your logic and needs

    return response