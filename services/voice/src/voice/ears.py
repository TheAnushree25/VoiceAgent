"""Ears: record speech from the microphone and turn it into text."""

import sounddevice
from faster_whisper import WhisperModel

SAMPLE_RATE = 16_000  # sound measurements per second; Whisper expects 16,000
MODEL_SIZE = "small"  # tiny, base, small, medium or large-v3-turbo: bigger is smarter but slower


def record(seconds):
    """Record from the default microphone and return the sound as a row of numbers."""
    frames = int(seconds * SAMPLE_RATE)
    audio = sounddevice.rec(frames, samplerate=SAMPLE_RATE, channels=1, dtype="float32")
    sounddevice.wait()
    return audio[:, 0]


def load_model():
    """Load Whisper into memory. This is slow, so do it once and reuse the result."""
    return WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")


def transcribe(model, audio, language):
    """Turn recorded sound into text. language is "hi" (Hindi) or "bn" (Bengali)."""
    segments, _info = model.transcribe(
        audio,
        language=language,
        vad_filter=True,
        temperature=0.0,
        condition_on_previous_text=False,
        max_new_tokens=100,
    )
    return " ".join(segment.text.strip() for segment in segments)