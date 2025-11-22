print("Hello! I'm your friendly chatbot.")
name = input("What's your name? ")

print(f"Nice to meet you, {name}!")

print()

feeling = input("How are you feeling today? ").lower()

if "good" in feeling or "great" in feeling or "fine" in feeling: #positive tone
    print("I'm glad to hear that!")
elif "bad" in feeling or "sad" in feeling: #negative tone
    print("I'm sorry to hear that, hope things will get better")
else:
    print("I see. Sometimes its hard to put feelings into word")

print()
hobby = input("What's your favorite hobby? ")

print(f"Wow, {hobby} sounds fun!")
print()

print(f"It was nice chatting with you, {name}. Goodbye")