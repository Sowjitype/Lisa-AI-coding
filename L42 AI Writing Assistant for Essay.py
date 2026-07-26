# Choose ONE proider by importint it:

# Change groq --> hf to use hugging face API
# Change hf --> groq to use groq API
from hf import generate_response
#from groq import generate_response

def get_essay_details():
  print("\n===AI Writing Assistant===")

  topic = input("What is topic of essay of your essay").strip()
  essay_type = input("What type of essay are you writing?").strip()
  print()

  lengths = ["300 words", "900 words", "1200 words", "2000 words"]

  print("Select essay word count:")

  for i,l in enumerate(lengths, 1):
    print(f"{i}) {l}")

  try:
    idx = int(input(">").strip())
    length = lengths[idx - 1] if 1 <= idx <= len(lengths) else "300 words"
  except ValueError:
    length = "300 words"

  target_audience = input("Target audience (e.g., High School students): ").strip()

  return {"topic": topic, "essay_type": essay_type, "length": length, "target_audience": target_audience}

def generate_essay_content(details):
  try:
    temp = float(input("Enter tempertaure (0.1 structured, 0.7 creative):").strip())

    if not (0.0 <= temp <= 1.0):
      raise ValueError

  except ValueError:
    print("Invalid temperature. Using 0.3.")
    temp = 0.3

  intro_p = f"Write an introduction for an {details['essay_type']} essay about {details['topic']} on the topic of {details['length']}."

  intro = generate_response(intro_p, temperature=temp, max_tokens=1024)

  print("\n=== Generated Introduction ===\n")
  print(intro)
  print()

  print("Would you like the body written as a full draft or step-by-step?")
  print("1) Full draft")
  print("2) Step-by-step")

  choice = input("> ").strip()
