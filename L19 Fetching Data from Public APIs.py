import requests

# Joke API endpoint
url = "https://official-joke-api.appspot.com/random_joke" 

# Send a GET requsest to fetch a joke
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    joke = response.json()
    print(f"Here's a joke for you:\n{joke['setup']}\n{joke['punchline']}")
    
else:
    print("Failed to fetch a joke. Please try again later.")