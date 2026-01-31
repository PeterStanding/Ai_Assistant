# Main Speak and Get Audio taken from Tech with Tim YT Chanel
# https://www.youtube.com/watch?v=zqEoTxkh95M

import os, time
import playsound3
import pyaudio
import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
from gtts import gTTS
import ollama
import pokemonSearch, weather, qr_code, reminders, expenses, games

#Arrays used for looping in the Main Logic
months = ["January", "February", "March", "April", "May", "June",
          "July", "August","September", "October", "November", "December"]
games = ["Guess Number"]

#Speak for the Assistant to respond to the user
def speak(audio):
    tts = gTTS(text=audio, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound3.playsound(filename)
#Gets the Audio input from the User to input into the system
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
#Searches Ollama for the question asked and returns the output,
# ready for the text and speech
def search_ollama(question):
    client = ollama.Client()

    model = "gemma3"
    response = client.generate(model=model, prompt=question)
    return response.response
    print("Response from Ollama:")
    print(response.response)

exit_conditions = ("bye","quit","exit","stop")
while True:
    #Gets user Input from Microphone
    text = get_audio()

    #Exit condition for the Assistant
    if text.lower() in exit_conditions:
        break
    if "qrcode" in text.lower():
        speak("Which website would you like a QR Code for?")
        loc = get_audio()
        speak("What would you like it to be Saved as?")
        fName = get_audio()
        qr_code.generateQR(loc, fName)
        speak("QR Code has been generated and Saved as:", fName)
    if "ollama" in text.lower():
        speak("What would you like to search Ollama?")
        q = get_audio()
        res = search_ollama(q)
        speak(res)
    if "hello" in text.lower():
        speak("Hello, I am Orion your AI Assistant.")
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
    if "reminder" in  text.lower():
        speak("What would you like to be reminded about?")
        input = get_audio()
        if "add" in input.lower():
            speak("What would you like to add?")
            rem = get_audio()
            speak("When would you like to set it for?")
            date = get_audio()
            reminders.add_reminder(date, rem)
            speak("Perfect, the Reminder has been set")
        elif "remove" in input.lower():
            speak("Which reminder would you like to remove?")
            rem = get_audio()
            reminders.delete_reminder(rem)
            speak("Reminder has been removed")
        elif "today" in input.lower():
            today = reminders.reminders_today()
            speak("All reminders for today")
            for t in today:
                speak(t)
        elif input in months:
            total = reminders.reminders_month(input)
            speak(f"All reminders for {input}")
            for t in total:
                speak(t)
    if "expenses" in text.lower():
        speak("What would you like todo with the expenses?")
        todo = get_audio()
        if "add" in todo.lower():
            speak("Which Expense would you like to add?")
            expense = get_audio()
            speak("How much is it worth?")
            cost = get_audio()
            expense.add_expense(expense, cost)
            speak("Completed, Expense has been added")
        if "delete" in  todo.lower():
            speak("Which Expense would you like to Remove?")
            expense = get_audio()
            expense.delete_expense(expense)
            speak("Completed, Expense has been removed")
        if "total" in todo.lower():
            t = expenses.total_remaining()
            speak(f"Total Remaining per month: {t}")
    if "game" in text.lower():
        speak("What game would you like to play?")
        for g in games:
            speak(g)
        game_choice = get_audio()
        if "guess number" in game_choice.lower():
            speak("I shall think of a random number between 1 and What?")
            higher = get_audio()
            games.guess_number(higher)