"""Mouth: turn text into speech with Microsoft Edge's free online voices (for learning only)."""

import asyncio
import io

import edge_tts
import sounddevice
import soundfile

VOICES = {"hi": "hi-IN-SwaraNeural", "bn": "bn-IN-TanishaaNeural"}


async def _collect_mp3(text, voice):
    chunks = []
    async for chunk in edge_tts.Communicate(text, voice).stream():
        if chunk["type"] == "audio":
            chunks.append(chunk["data"])
    return b"".join(chunks)


def text_to_mp3(text, language):
    """Return the spoken text as MP3 bytes. language is "hi" or "bn"."""
    # The free service sometimes never answers: give up after 30 seconds, never wait forever.
    return asyncio.run(asyncio.wait_for(_collect_mp3(text, VOICES[language]), timeout=30))


def play(audio_bytes):
    """Play MP3 or WAV bytes on the laptop's speakers, and wait until it finishes."""
    samples, sample_rate = soundfile.read(io.BytesIO(audio_bytes), dtype="float32")
    sounddevice.play(samples, sample_rate)
    sounddevice.wait()