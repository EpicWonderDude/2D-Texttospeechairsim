# Speech Recognition test 1
import speech_recognition as sr
# Initialize recognizer
r = sr.Recognizer()
# Use the microphone as source for input.
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize your voice")