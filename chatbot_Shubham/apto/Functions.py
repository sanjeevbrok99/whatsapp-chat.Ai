from django.conf import settings
import requests

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


#phonenumber="918968258994"
#message="Hello there"
#ans=sendWhatsappmessage(phonenumber,message)