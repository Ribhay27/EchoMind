# app/model.py

import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an empathetic therapist assistant."},
            {"role": "user", "content": f"Summarize the emotional state in this journal entry: '{text}'"}
        ],
        temperature=0.7 #Level of creativity-im open to changing this 
    )
    return response['choices'][0]['message']['content']
