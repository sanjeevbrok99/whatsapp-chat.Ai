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
os.environ['_BARD_API_KEY']="ZAg7RrKFc0wJsb_x6oyIqJLL--PDSWnnlzKklbeb9hpIToVDN0cKmxxpPliSvLzYxsAFEA."
# from .Functions import generate_response
api_key = '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'
openai.api_key = api_key

from .Functions import*


# Create your views here.
def homepage(request):
    return render(request,'Base.html')

# @csrf_exempt
# def whatsapp_webhook (request):
#     if request.method =='GET':
#         VERIFY_TOKEN = '24f8f399'
#         mode = request.GET ['hub.mode']
#         token = request.GET ['hub.verify_token']
#         challenge = request.GET ['hub. challenge']
#         if mode == 'subscribe' and token == VERIFY_TOKEN:
#             return HttpResponse (challenge, status=200)
#         else:
#             return HttpResponse ('error', status=403)

        

#     if request.method == 'POST':
#         # Extract the incoming message details
#         payload = request.body.decode('utf-8')
#         incoming_message = json.loads(payload)
        
#         # Process the incoming message and prepare a response
#         # Add your own logic here to handle the incoming messages and generate the appropriate response
#         response_message = "Hello, you sent: " + incoming_message['message']
        
#         # Send the response message back to the user
#         send_response(incoming_message['sender'], response_message)
        
#         # Return a successful response
#         return HttpResponse(status=200)
    
    
#     def send_response(recipient, message):
#         access_token = 'EAANqcotxjXQBALx3aOkMBddWZBTeXaoK8U5yoHQXzAOOPEF4I9GUYG8SQ98U7EE7jMXKZCawKEtWPPF3SJ4OlV0uVBrlZCUCFi2sOz7oa6sCWKNGlZBS06NWpiwWG4pZC637Mz9RJfnhA4ZC2AT9Czpd3ftacYBZCmk3oWaDT6sQPqnOu5lsRR2W5Q7nZAgutcAjdyRGJbstRwZDZD'
#         base_url = 'https://graph.facebook.com/v17.0/115701801584874/messages'
#         url = f'{base_url}?access_token={access_token}'
    
#         payload = {
#             'recipient': {
#                 'phone_number': recipient
#             },
#             'message': {
#                 'text': message
#             }
#         }
    
#         response = requests.post(url, json=payload)
#         response.raise_for_status()

    
    # if request.method =='POST':
    #     data = json. loads (request. body)
    #     if 'object' in data and 'entry' in data:
    #         if data['object'] =='whatsapp_business_account':
    #             try:
    #                 for entry in data['entry']:
    #                     phoneNumber = entry [' changes ' ] [0] ['value ' ] ['metadata'] ['display_phone_number']
    #                     phoneId = entry [' changes ' ] [0] ['value' ] ['metadata '] ['phone_number_id']
    #                     profileName = entry [' changes ' ] [0] ['value'] ['contacts '] [0] ['profile' ] ['name' ]
    #                     whatsAppId = entry [' changes ' ] [0] [' value'] [' contacts '] [0] ['wa id']
    #                     fromId = entry [' changes ' ] [0] ['value'] ['messages '] [0] [' from']
    #                     messageId = entry [' changes ' ] [0] ['value ' ] ['messages '] [0] [' id']
    #                     timestamp = entry [' changes ' ] [0] ['value ' ] ['messages ' ] [0] [' timestamp' ]
    #                     text = entry [' changes ' ] [0] [' value ' ] ['messages ' ] [0] [' text ' ] [' body' ]

    #                     phoneNumber = "918968258994"
    #                     message = 'RE: {} was received'. format (text)
    #                     sendWhatsappmessage (phoneNumber, message)
    #             except:
    #                 pass
    #     return HttpResponse('success',status=200)        



 #another function for webhook confirmation

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == 'GET':
        # WhatsApp verification token provided by WhatsApp
        verification_token = '24f8f399'
        
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
                            if "image " in text or "photo"in text or "pic" in text:
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




    # Handle the incoming WhatsApp messages
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

    #                     phonenumber = "918968258994"
    #                     message = 'RE: {} was received'.format(text)
    #                     sendWhatsappmessage(phonenumber, message)
                        
    #             except:
    #                 pass
    #     return HttpResponse('success', status=200)
    

    



                
