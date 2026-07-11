# Choose ONE proider by importint it:

# Change groq --> hf to use hugging face API
# Change hf --> groq to use groq API
from hf import generate_response
# From groq import generate_response

import time

def temperature_prompt_activity():
  print("=" * 70)
  print("ADVAN PROMPT ENGINEERING: TEMPERATURE + INSTRUCTIONS")
  print("=" * 70)

  # Part 1: Temperature
  print("\nPart 1: Temperature Exploration")
  base = input("Enter a creative prompt: ").strip()

  for t, label in [(0.1, "LOW(0.1) - Deterministic"),
                   (0.5, "MEDIUM(0.5) - Balanced"),
                   (0.9, "HIGH(0.9) - Creative")]:
    print(f"\n---{label}---")
    print(generate_response(base, temperature=t, max_tokens=512))
    time.sleep(1)

  # part 2: Instructions based prompt
  print("\nPart 2: Instructions-based Prompts")
  topic = input("Choose a topic (e.g., climate change, AI ethics, space exploration): ").strip()
  prompts = [
      f"Summarize key facts about {topic},in 3-4 sentences.",
      f"Explain {topic} as if I'm a 10-year-old child.",
      f"Write a pro/con list about {topic}.",
      f"Create a fictional new headlines from 2050 about {topic}.",
  ]

  for i, p in enumerate(prompts, 1):
    print(f"\n---Instruction {i}---\n{p}")
    print(generate_response(p, temperature=0.7, max_tokens=512))
    time.sleep(1)

  #part 3: your promt
  print("\nPart 3: Your own instructions Prompt")
  custom = input("Enter your own instruction-based prompt: ").strip()
  try:
    temp = float(input("Set temperature value (0.0 to 1.0): ").strip())
    if not (0.1 <= temp <= 1.0): raise ValueError
  except ValueError:
    print("Invalid temperature value. Using 0.7.")
    temp = 0.7

  print(f"\n---Your Custom Prompt---\n{temp}---")
  print(generate_response(custom, temperature=temp, max_tokens=512))

  # Reflection + Challenge
  print("\nReflection:")
  print("1. What changed when the prompts more specific?")
  print("2. How improved when context was added?")
  print("3. Which prompt felt the useful and why?")
  print("\nChallenge: Create a prompt chain")
  print("Generate a content -> rewrite with constraints -> create a sequel (try different temperatures)")

if __name__ == "__main__":
  temperature_prompt_activity()