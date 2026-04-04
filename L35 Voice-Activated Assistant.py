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
            print("❌ Sorry, I did not understand that.")
            
        except sr.RequestError as e:
            print("❌ Sorry, API Error: {e}")

    return ""

def respond_to_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")

    elif "your name" in command:
        speak(f"My name is Python Voice Assistant.")

    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}.")

    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        return False
    
    else:
        speak("Sorry, I don't understand that command.")

    return True

def main():
    speak("Hello! I am your voice assistant. Say something to get started.")
    
    while True:
        command = get_audio()
  
        if command and not respond_to_command(command):
             break
        
if __name__ == "__main__":
    main()