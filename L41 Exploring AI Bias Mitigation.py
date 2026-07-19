# Choose ONE proider by importint it:

# Change groq --> hf to use hugging face API
# Change hf --> groq to use groq API
from groq import generate_response
#from hf import generate_response

def bias_mitigation_activity():
    print("\n=== Bias Mitigation Activity ===")
    prompt = input("Enter a prompt to explore bias (e.g., 'Describe the ideal doctor'): ").strip()
    if not prompt:
        print("Please enter a prompt to run the activity.")
        return
    
    initial_response = generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInitial AI Response:\n{initial_response}\n")

    modified_prompt = input("Modify the prompt to make it more neutral (e.g., 'Describe the qualities of a doctor'): ").strip()

    if modified_prompt:
        modified_response = generate_response(modified_prompt, temperature=0.3, max_tokens=1024)
        print(f"\nModified AI Response (Neutral):\n{modified_response}\n")
    else:
        print("No modified prompt provided. Skipping modified response.\n")

def token_limit_activity():
    print("\n=== Token Limit Activity ===")
    long_prompt = input("Enter a long prompt (more than 300 words, e.g., 'A detailed story or description'): ").strip()
    
    if long_prompt:
        long_response = generate_response(long_prompt, temperature=0.3, max_tokens=1024)
        preview = (long_response[:500]+ "...")
        print(f"\nAI Response to Long Prompt:\n{preview}\n")
    else:
        print("No long prompt entered. Skipping long Prompt response")

    short_prompt = input("Now, condense the prompt to be more concise: ").strip()

    if short_prompt:
        short_prompt_response = generate_response(short_prompt, temperature=0.3, max_tokens=1024)
        print(f"\nAI Response to Condensed Prompt:\n{short_prompt}\n")
    else:
        print("No short prompt entered. Skipping condensed Prompt response")

def run_activity():
    print("\n ===AI learning Activity===")
    print("Choose an activity")
    print("1. Bias Mitigation")
    print("2. Token Limits")

    choice = input("> ").strip()

    if choice == "1":
        bias_mitigation_activity()
    elif choice == "2":
        token_limit_activity()
    else:
        print("Invalid choice. Please choose 1 or 2")
      
if __name__ == "__main__":
    run_activity()