# Dictionary to hold API details for each LLM service
llm_api_details = {
    "openai": {
        "api_key_env_variable": "OPENAI_API_KEY",
        "url": "https://api.openai.com/v1/chat/completions",
        "model_name": "gpt-3.5-turbo",
    },
    "mistral": {
        "api_key_env_variable": "MISTRAL_API_KEY",
        "url": "https://api.mistral.ai/v1/chat/completions",
        "model_name": "open-mixtral-8x7b",
    },
    # Add other LLM services here as needed
}
