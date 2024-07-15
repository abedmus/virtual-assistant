from ai import respond
from tts import speak

while True:
    print("Listening...")
    message = input()
    if message.strip():
        response = respond(message)
        speak(response)
