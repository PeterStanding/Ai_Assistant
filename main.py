# Main Speak and Get Audio taken from Tech with Tim YT Chanel
# https://www.youtube.com/watch?v=zqEoTxkh95M

import os, time
import playsound3
import pyaudio
import speech_recognition as sr
from gtts import gTTS

def speak(audio):
    tts = gTTS(text=audio, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound3.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

text = get_audio()
if "hello" in text:
    speak("Hello, I am your AI Assistant.")
if "test" in text:
    speak("Test Was Successful!")