# Main Speak and Get Audio taken from Tech with Tim YT Chanel
# https://www.youtube.com/watch?v=zqEoTxkh95M

import os, time
import playsound3
import pyaudio
import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
from gtts import gTTS

import pokemonSearch


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
            #print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

text = get_audio()

if "hello" in text.lower():
    speak("Hello, I am your AI Assistant.")
if "test" in text.lower():
    speak("Test Was Successful!")
if "pokémon" in text.lower():
    speak("Which Pokémon would you like?")
    input = get_audio()
    result = pokemonSearch.get_pokemon_info(input)
    speak(f"Name: {result["name"].capitalize()}")
    speak(f"Dex No: {result["id"]}")
    speak(f"Types: {', '.join(result['types'])}")
