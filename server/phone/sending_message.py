import requests
import json
from server import settings


# get request
def sendPostRequest(phoneNo, textMessage):
  req_params = {
  'apikey':settings.WAY2SMS['api_key'],
  'secret':settings.WAY2SMS['secret_key'],
  'usetype':settings.WAY2SMS['use_type'],
  'phone': phoneNo,
  'message':textMessage,
  'senderid':settings.WAY2SMS['sender_id']
  }
  return requests.post(settings.WAY2SMS['url'], req_params)

# get response
def send_otp(to, otp):
    response = sendPostRequest(to, otp)
    response = json.loads(response.text)
    if response.get('code') == "200 OK":
        return 
    return response.get('code')