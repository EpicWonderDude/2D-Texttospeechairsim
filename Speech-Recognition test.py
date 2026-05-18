# Speech Recognition test 1
import speech_recognition as sr
# Initialize recognizer
r = sr.Recognizer()
# Use the microphone as source for input.
with sr.Microphone() as source:
