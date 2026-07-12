import requests


DEFAULT_MODEL = "google/pegasus-xsum"
HF_API_URL = "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"

def build_api_url(model_name):
    #return f"https://api-inference.huggingface.co/models/{model_name}"
    return f"https://router.huggingface.co/hf-inference/models/{model_name}"

def query(payload, model_name=DEFAULT_MODEL):
    # Sends a POST request to the Hugging Face API using the specified model.
    api_url = build_api_url(model_name)
    headers = {"Authorization": f"Bearer {HF_API_URL}"}
    response = requests.post(api_url, headers=headers, json=payload)

    return response.json()

def summarize_text(text, min_length, max_length, model_name=DEFAULT_MODEL):
    payload = {
        "inputs": text,
        "parameters": {
            "min_length": min_length,"max_length": max_length}
        }
    print(f"\n???? Performing summarization using model: {model_name}...")
    result = query(payload, model_name)

    # Check if the response has the expected format
    if isinstance(result, list) and result and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        print("❌Error❌ in summarization response:", result)
        return None
if __name__ == "__main__":
    # Ask for user'S name
    print("Welcome to the AI Text Summarization Tool!")
    print("Hi there! What's your name?")
    user_name = input("Please enter your name: ").strip()

    if not user_name:
        user_name = "User"
    print(f"Welcome, {user_name}! Let's give text some AI-powered summarization magic! ✨")

    # Prompt the ueser for input text
    print("\nPlease enter the text you want to summarize:")
    input_text = input("> ").strip()
    if not input_text:
        print("❌No text provided. Exiting")
    else:
        # Ask for user preferences for model
        print("\nWhich summarization model would you like to use?(e.g., facebook/bart-large-cnn)")
        model_choice = input("Model (press Enter for default): ").strip()

        if not model_choice:
            model_choice = DEFAULT_MODEL
        # Ask for user summary style preferences
        print("\nWhat summary style do you prefer?")
        print("1. Concise (Quick & Concise)")
        print("2. Detailed (More Detailed & Refined)")
        style_choice = input("Choose 1 or 2: ").strip()

        if style_choice == "2":
            min_length = 80
            max_length = 200
            print("Enabling detailed summary style...")
        else:
            min_length = 50
            max_length = 150
            print("Using Standard summarization style...")
        # Generate the summary
        summary = summarize_text(input_text, min_length, max_length, model_name=model_choice)
        if summary:
            print(f"\nHere is your summary, {user_name}")
            print("✨" + summary + "✨")
        else:
            print("Sorry, something went wrong with the summarization process.")