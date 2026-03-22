"""
L2: Voice Analysis & Comparison
Record → Analyze Properties → Compare Two Recordings
Prepares students to CONTROL these properties in L3 (TTS)

============== DEPENDENCY SETUP ==============

CHECK IF INSTALLED (run in terminal):
    pip show SpeechRecognition pyaudio numpy matplotlib

INSTALL - WINDOWS:
    pip install SpeechRecognition pyaudio numpy matplotlib

INSTALL - macOS:
    brew install portaudio
    pip install SpeechRecognition pyaudio numpy matplotlib

Note: macOS requires portaudio BEFORE installing pyaudio
==============================================
"""

import threading
import sys

# Dependency check
try:
    import pyaudio
    import numpy as np
    import matplotlib.pyplot as plt
    import speech_recognition as sr
    from speech_recognition import AudioData
    
except ImportError as e:
    print(f"❌ Missing library: {e.name}")
    print("\n📦 Install commands:")
    print("   Windows: pip install SpeechRecognition pyaudio numpy matplotlib")
    print("   macOS:   brew install portaudio && pip install SpeechRecognition pyaudio numpy matplotlib")
    sys.exit(1)

stop_event = threading.Event()

def wait_for_enter():
    input()
    stop_event.set()

def record_audio(label):
    stop_event.clear()
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                    input=True, frames_per_buffer=1024)
    frames = []
    
    print(f"\n🎤 {label}")
    print("   Press Enter to stop...")
    threading.Thread(target=wait_for_enter, daemon=True).start
    ()
    
    print("🔴 Recording", end="", flush=True)
    while not stop_event.is_set():
        frames.append(stream.read(1024, exception_on_overflow=False))
        print(".", end="", flush=True)
    print(" ✅")
    
    stream.stop_stream()
    stream.close()
    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()
    return b''.join(frames), 16000, width

def analyze_audio(data, rate):
    samples = np.frombuffer(data, dtype=np.int16)
    return {
        'duration': len(samples) / rate,
        'avg_volume': np.mean(np.abs(samples)),
        'max_volume': np.max(np.abs(samples)),
        'samples': samples
    }

def transcribe(data, rate, width):
    recognizer = sr.Recognizer()
    try:
        return recognizer.recognize_google(AudioData(data, rate, width))
    except:
        return "[Could not transcribe]"

def display_stats(stats, text, label):
    print(f"\n{'─' * 35}")
    print(f"📊 {label}")
    print(f"{'─' * 35}")
    print(f"⏱️  Duration:   {stats['duration']:.2f} sec")
    print(f"📈 Avg Volume: {stats['avg_volume']:.0f}")
    print(f"🔊 Max Volume: {stats['max_volume']:.0f}")
    print(f"📝 Text: {text}")

def compare(s1, s2):
    print("\n" + "=" * 40)
    print("🔬 COMPARISON RESULTS")
    print("=" * 40)

    longer = "1" if s1['duration'] > s2['duration'] else "2"
    print(f"⏱️  Recording {longer} is longer ({s1['duration']:.1f}s vs {s2['duration']:.1f}s)")

    louder = "1" if s1['avg_volume'] > s2['avg_volume'] else "2"
    print(f"🔊 Recording {louder} is louder ({s1['avg_volume']:.0f} vs {s2['avg_volume']:.0f})")

    print("\n💡 In L3, you'll CONTROL rate & volume when AI speaks!")

def plot_both(s1, s2, rate):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5))
    t1 = np.linspace(0, len(s1['samples']) / rate, len(s1['samples']))
    ax1.plot(t1, s1['samples'], color='blue')
    ax1.set_title("Recording 1 (Normal)")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True, alpha=0.3)

    t2 = np.linspace(0, len(s2['samples']) / rate, len(s2['samples']))
    ax2.plot(t2, s2['samples'], color='red')
    ax2.set_title("Recording 2 (Modified)")
    ax2.set_xlabel("Time (seconds)")
    ax2.set_ylabel("Amplitude")
    ax2.grid(True, alpha=0.3)
    ax2.plot("Time (seconds)")
    ax2.set_ylabel("Amplitude")
    ax2.grid(True, alpha=0.3)
    
    t2 = np.linspace(0, len(s2['samples']) / rate, len(s2['samples']))
    ax2.plot(t2, s2['samples'], color='red')    
    ax2.set_title("Recording 2 (Modified)")
    ax2.set_xlabel("Time (seconds)")
    ax2.set_ylabel("Amplitude")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

def main():
    print("=" * 40)
    print("🔬 VOICE ANALYSIS LAB")
    print("=" * 40)
    print("Record twice and compare your voice!")
    
    audio1, rate, width  = record_audio("Recording 1: Speak NORMALLY")
    stats1, text1 = analyze_audio(audio1, rate), transcribe(audio1, rate, width)
    display_stats(stats1, text1, "Recording 1")
    
    input("\n🔄 Press Enter, then speak LOUDER or FASTER...")
    audio2, rate, width = record_audio("Recording 2: CHANGE your voice")
    stats2, text2 = analyze_audio(audio2, rate), transcribe(audio2, rate, width)
    display_stats(stats2, text2, "Recording 2")
    
    compare(stats1, stats2)
    plot_both(stats1, stats2, rate)

if __name__ == "__main__":
    main()