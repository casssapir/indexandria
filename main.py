from api_handler import send_prompt

def main():
    prompt = ("My electric vehicle isn't charging when I plug it into the charging station. "
              "I've checked that the charging cable is securely connected to both my vehicle and the charging station, "
              "but the charging process doesn't start. What are some steps I can take to troubleshoot this issue?")
    model = 'openai'  # Specifying to use the OpenAI model

    response = send_prompt(prompt, model=model)
    if response:
        # Assume response processing including cost calculation is handled within send_prompt or elsewhere as needed
        pass

if __name__ == "__main__":
    main()
