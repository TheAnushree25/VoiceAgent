"""Sarvam: cloud speech services built for Indian languages."""

import base64
import io
import os

import httpx
import soundfile
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["SARVAM_API_KEY"]
SPEECH_TO_TEXT_URL = "https://api.sarvam.ai/speech-to-text"
TEXT_TO_SPEECH_URL = "https://api.sarvam.ai/text-to-speech"
CHAT_URL = "https://api.sarvam.ai/v1/chat/completions"
SPEAKER = os.environ.get("SARVAM_SPEAKER", "priya")


def speech_to_text(audio, sample_rate, language):
    """Send recorded sound to Sarvam and get the words back. language is "hi" or "bn"."""
    buffer = io.BytesIO()
    soundfile.write(buffer, audio, sample_rate, format="WAV")

    response = httpx.post(
        SPEECH_TO_TEXT_URL,
        headers={"api-subscription-key": API_KEY},
        data={"model": "saaras:v4", "language_code": f"{language}-IN"},
        files={"file": ("speech.wav", buffer.getvalue(), "audio/wav")},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["transcript"]