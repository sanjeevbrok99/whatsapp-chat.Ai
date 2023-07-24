from django.conf import settings
import requests
import openai
from bardapi import Bard
import os
os.environ['_BARD_API_KEY']="ZAg7RrKFc0wJsb_x6oyIqJLL--PDSWnnlzKklbeb9hpIToVDN0cKmxxpPliSvLzYxsAFEA."
api_key = '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'
openai.api_key = api_key

def sendWhatsappmessage(phonenumber, message):
    headers = {"Authorization": settings.WHATSAPP_TOKEN}
    payload = {
        "messaging_product": "whatsapp",
        "to": phonenumber,
        "type": "text",
        "text": {"body": message}
    }
    response = requests.post(settings.WHATSAPP_URL, headers=headers, json=payload)
    ans = response.json()
    return ans

import openai

def generate_response(text):
    # Use OpenAI API to generate a response based on user_message
    # Replace this with your actual AI model or logic
    print(text)
    input_text = (text)
    print(input_text)
    print(Bard().get_answer(input_text)['content'])
    return(Bard().get_answer(input_text)['content'])
    
   
    
# def generate_response(text):
#     # Use OpenAI API to generate a response based on user_message
#     # Replace this with your actual AI model or logic
#     print(text)
#     response = openai.Completion.create(
#         model="text-davinci-003",  # You can choose other engines based on your preference and subscription level
#         prompt=text,
#         temperature=0.6,
#         max_tokens=150,  # Adjust the number of tokens based on your desired response length
#     )
#     print(response)
#     return response['choices'][0]['text'].strip()

# Call the function with a text prompt

# Example usage:
# user_input = "Tell me a joke."
# response = generate_response(user_input)
# print(response)


#phonenumber="918968258994"
#message="Hello there"
#ans=sendWhatsappmessage(phonenumber,message)