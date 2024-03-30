from context_manager import get_more_context

# Define the initial prompt and API details
prompt = "I can't log in to my account. Can you help?"
api_details = {
    "api_key_env_variable": "OPENAI_API_KEY",
    "url": "https://api.openai.com/v1/chat/completions",
    "model_name": "gpt-3.5-turbo",
}

# Call the function to get more context and handle the interaction
response = get_more_context(prompt, api_details)

# Print the final response from the language model
print(response)
