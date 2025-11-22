print("Hello! I'm your friendly chatbot.")
name = input("What's your name? ")

print(f"Nice to meet you, {name}!")

print()

feeling = input("How are you feeling today? ").lower()

if "good" in feeling or "great" in feeling or "fine" in feeling or "happy" in feeling or "excitement" in feeling: #positive tone
    print("I'm glad to hear that!")
elif "bad" in feeling or "sad" in feeling or "Loneliness" in feeling or "anger" in feeling: #negative tone
    print("I'm sorry to hear that, hope things will get better")
else:
    print("I see. Sometimes its hard to put feelings into word")

print()
hobby = input("What's your favorite hobby? ")

print(f"Wow, {hobby} sounds fun!")
print()

print()
color = input("What's your favorite color? ")

print(f"Nice, {color} is beautiful.")
print()

print()
subject = input("So What's your favorite subject in school?" )
 
print(f"Cool, {subject} is interesting!")
print()

stop = input("Do you want to continue conversation? ")

if "yes" in stop or "okay" in stop or "ok" in stop:
    type = input("What type of animal do you like? ").lower()
    if "mammals" in type: 
        print("I'm glad to hear that you like mammals!")
    elif "birds" in type :
        print("How interesting!")
    elif "fish" in type :
        print("Nice , I like fish too!")
    elif "reptiles" in type :
        print("Oh scary but interesting")
    elif "insert" in type :
        print("Oh it is little scary")
    else:
        print("I see. Sometimes we invent new names for our pets.")
    
    print()
    juck = input("What do think of juck food? ")
 
    print(f"Yeah, juck food is {juck}.")
    print()

    print()
    paper = input("What do think of paper cutting? ")
 
    print(f"Yeah, paper cutting is {paper}. what's more I love paper cuttting")
    print()

    print()
    print("Let me write small introduction about you")

    print()
    print(f"Your name is {name}, and you’re absolutely passionate about {hobby}—it's your favorite hobby! {color} has always been your go-to favorite color; you love how it brightens up your day. At school, {subject} stands out as your all-time favorite subject—you could talk about it for hours! When it comes to animals, you’re a total fan of {type} creatures—they’re so charming (or fascinating, depending on the animal!). As for junk food? You think {juck}—whether that means indulging in it occasionally, craving it nonstop, or preferring to stick to healthier snacks. And paper cutting? You find {paper}—it might feel like a fun, creative challenge, a calming way to unwind, or even a little tricky but super rewarding!")

    print(f"It was nice chatting with you, {name}. Goodbye")

else:
    print(f"It was nice chatting with you, {name}. Goodbye")
