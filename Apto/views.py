from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core.mail import send_mail
import json
from django.http import HttpResponse
import openai
from bardapi import Bard
import os
os.environ['_BARD_API_KEY']='BARD_API_KEY'
# from .Functions import generate_response

openai.api_key = 'api_key'

from .Functions import*


# Create your views here.
def homepage(request):
    return render(request,'Base.html')




@csrf_exempt
def whatsapp_webhook(request):
    if request.method == 'GET':
        # WhatsApp verification token provided by WhatsApp
        verification_token='verification_key'
        
        # Extract the query parameters from the request
        params = request.GET
        token = params.get('token', '')
        challenge = params.get('hub.challenge', '')
        return HttpResponse(challenge)

        if token == verification_token:
            # Respond with the challenge to verify the webhook
            return HttpResponse(challenge)
        else:
            # Invalid verification token
            return HttpResponse("Invalid token", status=403)

       



    if request.method == 'POST':
            data = json.loads(request.body)
            if 'object' in data and 'entry' in data:
                if data['object'] == 'whatsapp_business_account':
                    try:
                        for entry in data['entry']:
                            phonenumber = entry['changes'][0]['value']['metadata']['display_phone_number']
                            phoneId = entry['changes'][0]['value']['metadata']['phone_number_id']
                            profileName = entry['changes'][0]['value']['contacts'][0]['profile']['name']
                            whatsAppId = entry['changes'][0]['value']['contacts'][0]['wa_id']
                            fromId = entry['changes'][0]['value']['messages'][0]['from']
                            messageId = entry['changes'][0]['value']['messages'][0]['id']
                            timestamp = entry['changes'][0]['value']['messages'][0]['timestamp']
                            text = entry['changes'][0]['value']['messages'][0]['text']['body']
                            if "image" in text or "photo"in text or "pic" in text:
                                message = generate_image(text)
                                print( message)
                            else:
                                message = generate_response(text)
                                print( message)

                        # Send the response back using WhatsApp API or any other appropriate method
                            phonenumber = "918968258994"  # Replace with the recipient's phone number
                            sendWhatsappmessage(phonenumber, message)
                        
                    except:
                        pass
    return HttpResponse('success', status=200)
# input_text = "what is google bard?"

# print(Bard().get_answer(input_text)['content'])
    # if request.method == 'POST':
    #     data = json.loads(request.body)
    #     if 'object' in data and 'entry' in data:
    #         if data['object'] == 'whatsapp_business_account':
    #             try:
    #                 for entry in data['entry']:
    #                     phonenumber = entry['changes'][0]['value']['metadata']['display_phone_number']
    #                     phoneId = entry['changes'][0]['value']['metadata']['phone_number_id']
    #                     profileName = entry['changes'][0]['value']['contacts'][0]['profile']['name']
    #                     whatsAppId = entry['changes'][0]['value']['contacts'][0]['wa_id']
    #                     fromId = entry['changes'][0]['value']['messages'][0]['from']
    #                     messageId = entry['changes'][0]['value']['messages'][0]['id']
    #                     timestamp = entry['changes'][0]['value']['messages'][0]['timestamp']
    #                     text = entry['changes'][0]['value']['messages'][0]['text']['body']

    #                     # Use OpenAI to generate a response
    #                     print(text)

    #                     message = generate_response(text)
    #                     print( message)

    #                     # Send the response back using WhatsApp API or any other appropriate method
    #                     phonenumber = "918968258994"  # Replace with the recipient's phone number
    #                     sendWhatsappmessage(phonenumber, message)
    #             except:
    #                 pass
    #     return HttpResponse('success', status=200)




   