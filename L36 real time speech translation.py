import speech_recognition as sr
import pyttsx3
from googletrans import Translator  # Google Translate API

# Initialize text-to-speech engine
def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Speed of speech

    voices = engine.getProperty('voices')

    # Set voice for English or other language if supported by pyttsx3
    if language == "en":
        engine.setProperty('voice', voices[0].id)  # Default English voice
    else:
        engine.setProperty('voice', voices[1].id)  # Fallback to another voice if available

    engine.say(text)
    engine.runAndWait()

# Speech-to-Text: Recognize spoken language (English)
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
         

    try:
        print("🎤 Listening... Please speak in English.")
        text = recognizer.recognize_google(audio, language="en-US")
        # Use English for speech recognition

        print(f"✅ You said: {text}")
        return text

    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")

    except sr.RequestError as e:
        print(f"❌ API error: {e}")

    return "" 

# Translate text using Google Translate API
def translate_text(text, target_language="es"):  # Default target language is Spanish (es)
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"???? Translated text: {translation.text}")
    return translation.text

# Display language options to the user
def display_language_options():
    print("???? Available translation languages: ")
    print("1. Hindi (hi)")
    print("2. Chinese (zh)")
    print("3. Japanese (ja)")
    print("4. Indonesian (id)")
    print("5. Arabic (ar)")
    print("6. French (fr)")
    print("7. Korean (ko)") 

    # User selects language
    choice = input("Please select the target language number (1-7): ")

    language_dict = {
        "1": "hi",
        "2": "zh",
        "3": "ja",
        "4": "id",
        "5": "ar",
        "6": "fr",
        "7": "ko"
    }    

    return language_dict.get(choice, "es")  # Default to Spanish if invalid input 

# Main function to combine all steps
def main():
    # Step 1: Display language options and get user's choice
    target_language =  display_language_options()

    speak("say something in English!")   

    # Step 2: Speech-to-Text (recognizing English speech)
    original_text =  speech_to_text() 

    if original_text:
        # Step 3: Translate to selected target language
        translated_text = translate_text(original_text, target_language=target_language)        

        # Step 4: Text-to-Speech (Translate output and speak it)
        speak(translated_text, language=target_language)  # Speak the translation in the targeted language

        print("✅ Translation spoken out") 

if __name__ == "__main__":
    main()