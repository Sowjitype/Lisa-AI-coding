# Chooes ONE provider by importing it:

# Change groq --> hf to use hugging face API
#Change hf --> groq to use groq API
from groq import generate_response

def prompt_engineer_activity():
  print("Welcome to the API Prompt Engineer Tutorial!")

  vague = input("Enter a vague prompt: ")
  print("\nAI's response to vague prompt:")
  print(generate_response(vague))

  specific = input("\nNow, make it more specific: ")
  print("\nAI's response to specific prompt:")
  print(generate_response(specific))

  context = input("\nNow, add context to your specific prompt: ")
  print("\nAI's response to contextual prompt:")
  print(generate_response(context))

  print("\n--- Reflection ---")
  print("1. How did the AI's responses change when the prompt was made more specific?")
  print("2. How did the AI's responses improve with the added context?")
  print("3. Which prompt produced the most relevant and tailored response? Why?")

if __name__ == "__main__":
  prompt_engineer_activity()