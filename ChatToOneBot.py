import requests
import json

APIToken = input("Enter Bot API Token: ")
urlAPI = "https://api.telegram.org/bot"+APIToken+"/getUpdates"
res=requests.get(urlAPI)
response=json.loads(res.text)
target=response['result'][-1]['message']
fromuser=target['from']['first_name']
currUpdid=response['result'][-1]['update_id']
print(fromuser,'says: ',target['text'])
while True:
    res=requests.get(urlAPI)
    response=json.loads(res.text)
    fromuser=target['from']['first_name']
    target=response['result'][-1]['message']
    if currUpdid!=response['result'][-1]['update_id']:
        fromuser=target['from']['first_name']
        print(fromuser,'says: ',target['text'])
        currUpdid=response['result'][-1]['update_id']
        msg=input("Msg: ")
        chatid=fromuser=target['chat']['id']
        actualurl=r'https://api.telegram.org/bot' + APIToken +'/sendMessage?text='+msg+r'&chat_id='+str(chatid)
        sendres=requests.get(actualurl)




