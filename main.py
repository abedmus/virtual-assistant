import os
import google.generativeai as genai
from gtts import gTTS
from playsound import playsound

API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=str(API_KEY))

model = genai.GenerativeModel('gemini-1.5-flash')

def respond(message):
    response = model.generate_content(message)
    return response.text

def speak(text):
    tts = gTTS(text, lang='en', tld='us')
    filename = "voice"+".mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

while True:
    print("Listening...")
    message = input()
    if message.strip():
        response = respond(message)
        print(response)
        speak(response)
