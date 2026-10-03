# check_setup.py: makes sure the voice service's tools are ready.

from importlib.metadata import version

import ollama
import sounddevice

LIBRARIES = ["faster-whisper", "sounddevice", "soundfile", "edge-tts", "ollama", "fastapi"]

print("Installed libraries:")
for name in LIBRARIES:
    print(f"  {name:<15} {version(name)}")

print("\nYour microphones and speakers:")
print(sounddevice.query_devices())

print("\nAI models in Ollama:")
for model in ollama.list().models:
    print(f"  {model.model}")

print("\nEverything is ready!")