
import requests
import json

URL = 'https://www.way2sms.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, '0VXHJEEYMNLRPG271MU5LCADC4XWA3V8', 'H45FXRPYBBU6S9GC', 'prod', '9004652865', 'active-sender-id', 'pppp' )

# print response if you want
response = json.loads(response.text)
print (response.get('code'))