import google.generativeai as genai
import os

KEY = os.getenv('GeminiAPIKey')
genai.configure(api_key=KEY)

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 100,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings,
)

chat = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["You are a virtual customer service representative. Use your knowledge base to best respond to customer queries."
                  ]
    }
    ,
    {
        "role": "model",
        "parts": ["Certainly!"]
    }
])

def respond(message):
    response = chat.send_message(message, stream=True)
    for chunk in response:
        print(chunk.text, end='')
    print()
    return response.text
