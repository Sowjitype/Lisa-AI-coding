import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json
import datetime

# Define audio parameters
samplerate = 16000  # Vosk models typically use 16kHz
channels = 1
dtype = 'int16'
blocksize = 8000  # Adjust as needed for responsiveness vs. processing load

# Load the Vosk model
model_path = "Python\L34\vosk-model-small-en-us-0.15"
model = Model(model_path)
recognizer = KaldiRecognizer(model, samplerate)

print("Listening...")

# Audio callback function
def callback(indata, frames, time, status):
    if status:
        print(status) # Handle potential issues
    if bytes(indata):
        if recognizer.AcceptWaveform(bytes()):
            result = json.loads(recognizer.Result())
            if result['text']:
                print("You said:", result['text'])
                
                #voice assistant logic here based on the recognized text
                result = process_query(result['text'])
                print(f"VA: {result}")

def process_query(query):
    query = query.lower()
    if "time" in query:
        now = datetime.datetime.now().strftime("%H:%M")
        response = f"The current time is {now}."
    elif "date" in query:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        response = f"Today's date is {today}."
    else:
        response = "I'm sorry, I didn't understand that."
    return response

# Start audio stream
try:
    with sd.RawInputStream(samplerate=samplerate, blocksize=blocksize,
                           dtype=dtype, channels=channels, callback=callback):
        while True:
            sd.sleep(1000) # Keep the stream alive
except KeyboardInterrupt:
    print("\nStopping voice assistant.")
except Exception as e:
    print(f"An error occurred: {e}")