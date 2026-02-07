import requests

# Random Technology Facts API
url = "https://uselessfacts.jsph.pl/random.json?language=en"

# Function to get a random technology fact
def get_random_technology_fact():
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Random Technology Fact:")
        print(f"Did you know? {data['text']}")
        print("\n")
    else:
        print("Failed to retrieve a random technology fact.")

# Main loop to interact with the user
while True:
    key = input("Press Enter to get a random technology fact or type 'q' to quit: ")

    if key.lower() == 'q':
        print("Goodbye!")
        break
    else:        
        get_random_technology_fact()