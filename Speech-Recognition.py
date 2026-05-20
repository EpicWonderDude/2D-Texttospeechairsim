// Run this:
// python -m pip install sounddevice soundfile speechrecognition numpy

import sounddevice as sd
import numpy as np
import wave
import speech_recognition as sr

# Settings
duration = 5  # seconds
sample_rate = 44100

print("Talk")

# Record audio
audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype='int16'
)

sd.wait()

print("Time over, thanks")

# Save recording temporarily
filename = "temp.wav"

with wave.open(filename, 'wb') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)  # int16 = 2 bytes
    wf.setframerate(sample_rate)
    wf.writeframes(audio.tobytes())

# Speech recognition
r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_text = r.record(source)

try:
    print("Text:", r.recognize_google(audio_text))
except Exception as e:
    print("Sorry, I did not get that")
    print(e)