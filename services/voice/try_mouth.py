# try_mouth.py: hear your laptop speak Hindi and Bengali.

import time

from voice.mouth import play, text_to_mp3

SENTENCES = {
    "hi": "नमस्ते! मैं आपकी डेयरी सहायक हूँ। पशु आहार 1,450 रुपये का है।",
    "bn": "নমস্কার! আমি আপনার ডেয়ারি সহায়ক। গরুর খাবারের দাম 1,450 টাকা।",
}

for language, sentence in SENTENCES.items():
    start = time.perf_counter()
    audio = text_to_mp3(sentence, language)
    print(f"{language}: made {len(audio)} bytes of speech in {time.perf_counter() - start:.1f} s")
    play(audio)