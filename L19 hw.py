import requests
import random

# Joke API endpoint
url = "https://official-joke-api.appspot.com/jokes/random" 

# Send a GET requsest to fetch a joke
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    joke = response.json()
    answer = input("Do you want to hear a joke? (yes/no): ").strip().lower()
    if answer == "yes":
        print(f"Here's a joke for you:\n{joke['setup']}\n{joke['punchline']}")
    else:
        print("Okay, maybe next time!")
        answer2 = input("Would you like to hear a motivational quote instead? (yes/no): ").strip().lower()
        if answer2 == "yes":
            quote = [
                "The best way to get started is to quit talking and begin doing. - Walt Disney",
                "Don't let yesterday take up too much of today. - Will Rogers",
                "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
                "If you are working on something exciting, it will keep you motivated. - Unknown",
                "Success is not in what you have, but who you are. - Bo Bennett",
                "East or west, home is best. - Unknown",
                "The journey of a thousand miles begins with a single step. - Lao Tzu",
                "Prepare for the worst, hope for the best, and expect the unexpected. - Denis Waitley",
                "Believe you can and you're halfway there. - Theodore Roosevelt",
                "Your time is limited, so don't waste it living someone else's life. - Steve Jobs"
            ]
            print("Here's a motivational quote for you:")
            print(random.choice(quote))
        else:
            print("Alright, have a great day!")
            answer3 = input("Would you like to receive a fun fact instead? (yes/no): ").strip().lower()
            if answer3 == "yes":
                fun_facts = [
                    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
                    "Bananas are berries, but strawberries aren't.",
                    "A group of flamingos is called a 'flamboyance'.",
                    "Octopuses have three hearts.",
                    "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion of the metal.",
                    "Wombat poop is cube-shaped.",
                    "There are more stars in the universe than grains of sand on all the world's beaches.",
                    "A day on Venus is longer than a year on Venus.",
                    "Some turtles can breathe through their butts.",
                    "The shortest war in history lasted just 38 to 45 minutes between Britain and Zanzibar on August 27, 1896."
                ]
                print("Here's a fun fact for you:")
                print(random.choice(fun_facts))
            else:
                print("No problem! Have a wonderful day!")
                answer= input("Do you want to hear a joke? (yes/no): ").strip().lower()
                if answer == "yes":
                    print(f"Here's a joke for you:\n{joke['setup']}\n{joke['punchline']}")
                else:
                    print("Alright, take care!")
else:
    print("Failed to fetch a joke. Please try again later.")