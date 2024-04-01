# Dictionary to hold API details for each LLM service
llms = {
    "openai": {
        "api_key": "OPENAI_API_KEY",
        "url": "https://api.openai.com/v1/chat/completions",
        "model_name": "gpt-3.5-turbo",
    },
    "mistral": {
        "api_key": "MISTRAL_API_KEY",
        "url": "https://api.mistral.ai/v1/chat/completions",
        "model_name": "open-mixtral-8x7b",
    },
    # Add other LLM services here as needed
}
