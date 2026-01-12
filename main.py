# Main Speak and Get Audio taken from Tech with Tim YT Chanel
# https://www.youtube.com/watch?v=zqEoTxkh95M

import os, time
import playsound3
import pyaudio
import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
from gtts import gTTS

import pokemonSearch, weather


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
if "weather" in  text.lower():
    speak("Which City would you like to look at?")
    input = get_audio()
    result = weather.get_weather(input)
    speak(f"\nCurrent time: {result['time']}")
    speak(f"Current temperature: {result['temperature']:.2f}°C")
    if result["is_day"] == 1:
        speak(f"Currently There is daylight")
    else:
        speak(f"Currently There is no daylight")
    speak(f"Current precipitation: {result['precipitation']}")
    speak(f"Current wind speed: {result['wind_speed']:.2f} mph")
    speak(f"Current wind direction: {result['wind_direction']:.2f}")
    speak(f"Current weather code: {result['weather_code']}")