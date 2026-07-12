import speech_recognition as sr
import pyttsx3
from datetime import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print(f"✅ You said: {command}")

            return command.lower()
        
        except sr.UnknownValueError:
            print("❌ Sorry, I did not understand that. Can you please repeat?")
            
        except sr.RequestError as e:
            print("❌ Sorry, API Error. Please try again later.")

    return ""

def respond_to_command(command):
    if "hello" in command:
        speak("Hello! I am your voice assistant. How can I assist you today?")

    elif "your name" in command:
        speak(f"My name is Python Voice Assistant. I am here to help you.")

    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"分秒必争, 现在才{now}点钟. Let's make the most of our time!")

    elif "date" in command:
        today = datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}. I hope you have a productive day!")

    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a great day!")
        return False
    
    else:
        speak("Sorry, I don't understand that command. Can you please repeat?")

    return True

def main():
    speak("Hello! I am your voice assistant. I am here to help you. Say something to get started.")
    
    while True:
        command = get_audio()
  
        if command and not respond_to_command(command):
             break
        
if __name__ == "__main__":
    main()