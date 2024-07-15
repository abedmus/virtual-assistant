from gtts import gTTS
from playsound import playsound
import os

def speak(text):
    tts = gTTS(text, lang='en', tld='us')
    filename = "voice"+".mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)
