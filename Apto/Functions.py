from django.conf import settings
import requests
import openai
from bardapi import Bard
import os
from django.conf import settings
from decouple import config

os.environ['_BARD_API_KEY']='BARD_API_KEY'
Api_key=config('api_key')
openai.api_key =Api_key

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

# def generate_response(text):
#     # Use OpenAI API to generate a response based on user_message
#     # Replace this with your actual AI model or logic
    
#     input_text = (text)
#     print(input_text)
#     print(Bard().get_answer(input_text)['content'])
#     return(Bard().get_answer(input_text)['content'])
    
   
    
def generate_response(text):
    # Use OpenAI API to generate a response based on user_message
    # Replace this with your actual AI model or logic
    print(text)
    response = openai.Completion.create(
        model="text-davinci-003",  # You can choose other engines based on your preference and subscription level
        prompt=text,
        temperature=0.6,
        max_tokens=1000,  # Adjust the number of tokens based on your desired response length
    )
    print(response)
    return response['choices'][0]['text'].strip()

import openai

def generate_image(text):
    prompt = text
    
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size='512x512',
    )
    
    image_url = response['data'][0]['url']
    return image_url


# Call the function with a text prompt

# Example usage:
# user_input = "Tell me a joke."
# response = generate_response(user_input)
# print(response)


#phonenumber="918968258994"
#message="Hello there"
#ans=sendWhatsappmessage(phonenumber,message)