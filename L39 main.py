# Choose ONE proider by importint it:

# Change groq --> hf to use hugging face API
# Change hf --> groq to use groq API
#from groq import generate_response
from hf import generate_response

def run_activity():
    print("ZERO-SHOT, ONE-SHOT & FEW-SHOT ACTIVITY")

    category = input("Enter a category (e.g., 'sports', 'politics', 'technology'): ").strip()
    item = input(f"Enter a specific {category} to classify: ").strip()

    if not category or not item:
        print("Please fill in both fields to run the activity.")
        return
    
    # Zero shot example
    zero_shot = f"Is {item} a {category}? Answer with 'yes' or 'no'."
    print("\nZero-Shot Learning:")
    print(f"Response: {generate_response(zero_shot, temperature=0.3, max_tokens=1024)}")

    # One shot example
    one_shot = f"""Example:
                    Category: sports
                    Item: football
                    Answer: Yes, football is a sport.

                    Now, you try:
                    Category: {category}
                    Item: {item}
                    Answer: """
    print("\nOne-Shot Learning:")
    print(f"Response: {generate_response(one_shot, temperature=0.3, max_tokens=1024)}")

    # Few shot example( kept same as your original prompt format)
    few_shot = f"""Example 1:
                    Category: fruit
                    Item: apple
                    Answer: Yes, apple is a fruit.
                    
                    Example 2:
                    Category: vehicle
                    Item: car
                    Answer: Yes, car is a vehicle.
                    
                    Now, you try:
                    Category: {category}
                    Item: {item}
                    Answer: """
    print("\nFew-Shot Learning:")
    print(f"Response: {generate_response(few_shot, temperature=0.3, max_tokens=1024)}")

    #Creative_prompt
    creative_prompt = f"""Write a short story about the word given.
                        Example 1 : Word: moon
                        Story: THe moon winked at the lovers as they walked along the beach. 
                        
                        Word: {item}
                        Story: """
    print("\nCreative Prompt:")
    print(f"Response: {generate_response(creative_prompt, temperature=0.7, max_tokens=1024)}")

    #Reflection question
    print("\nReflection Question:")
    print("1. How did the responses differ between zero-shot, one-shot, and few-shot learning?")
    print("2. Which approach gave you the most helpful response and why?")
    print("3. How did the examples influence the model's output")

if __name__ == "__main__":
    run_activity()