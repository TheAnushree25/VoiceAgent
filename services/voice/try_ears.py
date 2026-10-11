# try_ears.py: record 5 seconds, then let both "ears" write down what you said.

import time

import soundfile

from voice.ears import SAMPLE_RATE, load_model, record, transcribe
from voice.sarvam import speech_to_text

language = input("Language? Type hi for Hindi or bn for Bengali: ").strip()

print("Loading Whisper...")
model = load_model()

input("Press Enter, then speak for 5 seconds.")
print("Listening...")
audio = record(5)
soundfile.write("last_recording.wav", audio, SAMPLE_RATE)

if abs(audio).max() < 0.01:
    print("I heard almost nothing. Check your microphone.")

start = time.perf_counter()
text = speech_to_text(audio, SAMPLE_RATE, language)
print(f"\nSarvam heard:  {text}  ({time.perf_counter() - start:.1f} s)")

start = time.perf_counter()
text = transcribe(model, audio, language)
print(f"Whisper heard: {text}  ({time.perf_counter() - start:.1f} s)")