import playsound3, random
import speech_recognition as sr
from gtts import gTTS

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

def guess_number(higher):
    answer = random.randint(1, higher)
    speak("Guess a number between 1 and " + str(higher))
    while True:
        guess = get_audio()
        if int(guess) == answer:
            speak("Congratulations, you guessed it!")
            break
        elif int(guess) > answer:
            speak("Sorry, you've guessed too high")
        elif int(guess) < answer:
            speak("Sorry, you've guessed too low")