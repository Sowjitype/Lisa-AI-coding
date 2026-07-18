# Choose ONE proider by importint it:

# Change groq --> hf to use hugging face API
# Change hf --> groq to use groq API
#from groq import generate_response
from hf import generate_response

def reinforcement_learning_activity():
    print("\n=== Reinforcement Learning Activity ===")
    prompt = input("Enter a prompt for AI model (e.g., 'Describe the lion'): ").strip()
    
    if not prompt:
        print("Please enter a prompt to run the activity.")
        return
    
    initial_response = generate_response(prompt, temperature=0.3, max_tokens=1024)

    print(f"\nInitial AI Response:\n{initial_response}\n")

    #Rating + feedback (simulated Rl)
    try:
        rating = int(input("Rate the response from 1 (poor) to 5 (excellent): "))
        if rating < 1 or rating > 5:
            print("Invalid raiting. Using 3")
            rating = 3
    except ValueError:
        print("Invalid input. Using 3")
        rating = 3
    
    feedback = input("Provide feedback for the AI response: ").strip()
    improved_response = f"{initial_response} (Improved with your feedback: {feedback})"
    print(f"\nImproved AI Response:\n{improved_response}\n")
    print()

    print("\nReflection:")
    print("1. how did the model's response improve with the feedback?")
    print("2. How does reinforcement learning help in its performance over time?")
    print()

def role_based_prompt_activity():
    print("\n=== Role-Based Prompt Activity ===")
    category = input("Enter category (e.g., 'science', 'history', 'math'): ").strip()
    item = input(f"Enter an item for the AI model as a {category}: ").strip()
    
    if not category or not item:
        print("Please fill in both fields to run the activity.")
        return
    
    teacher_prompt = f"You are a teacher. Explain {item} in simple terms."
