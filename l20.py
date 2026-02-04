import requests

# Trivia API endpoint
url = "https://opentdb.com/api.php?amount=10&type=multiple"  # Fetch 5 questions

# Send GET request to fetch trivia questions
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
  score = 0
  name = input("Enter your name: ")
  age = input("Enter your age: ")
  print(f"Welcome to the Trivia Game, {name}!")
  print()
  print("Name and Age have been recorded.")
  print("Your score will be displayed at the end of the game.")
  print()
  print(f"Hello {name}, age {age}! Get ready to test your knowledge.")
  print("Let's get started with some trivia questions!")
  print()
  print("SCORE BOARD - Each correct answer gives you 1 point. No negative points for wrong answers.")
  print("SCORE: ",score)
  print("Fetching trivia questions...")
  print()
  trivia_data = response.json()
  
  # Loop through each trivia question
  for i, question_data in enumerate(trivia_data["results"]):
    print(f"Question {i + 1}: {question_data['question']}")
    options = question_data["incorrect_answers"] + [question_data["correct_answer"]]  # Add correct answer to options
    options = sorted(options)  # Shuffle options
    
    for j, option in enumerate(options):
      print(f"{j + 1}. {option}")

    # Collect user's answer
    user_answer = input(f"Please enter your answer (1/2/3/4) {name}: ")

    # Check if the answer is correct
    if options[int(user_answer) - 1] == question_data["correct_answer"]:
      print(f"Correct!, Congratulations! {name}")
      print("Well done!, you got it right.")
      score += 1
    else:
      print(f"Wrong! The correct answer was: {question_data['correct_answer']}")
      print("Better luck next time!")
      print(f"Keep trying, you'll get it ,{name}!")

    print()

  print(f"Your final score: {score}/{len(trivia_data['results'])}")
  print(f"Thanks for playing!, {name}.")
  print("Visit https://opentdb.com/ for more trivia questions!")
else:
  print("Failed to retrieve trivia")
  print(f"Please check your internet connection or try again later.")