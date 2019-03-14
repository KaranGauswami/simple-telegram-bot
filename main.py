from clear import clear
from prints import prints as print
from colors import colors as color

import requests,json,urllib,os,time

clear()
print(color.orange,'\nEnter Your API KEY : ',end='')
token = input()
LINK = f'https://api.telegram.org/bot{token}/'
clear()

def main():    
    latestupdateid = None
    while True:
        print(color.yellow,'Running Smoothly\n')
        updates = getUpdates(latestupdateid)
        if (len(updates['result'])>0):
            print(color.cyan,'New Message Arrived\n')
            latestupdateid = getLatestId(updates)+1
            code()
        time.sleep(1)
        
def getJsonFromURL(link):
    try:
        response = requests.get(link)
        response.raise_for_status()
        JsonFormat = json.loads(response.text)
        return JsonFormat
    except Exception as e:
        print(color.red,e)


def getUpdates(offset=None):
    link = f'{LINK}getUpdates?timeout=100'
    if offset:
        link+='&offset={}'.format(offset)
    JsonData = getJsonFromURL(link)
    return JsonData

def sendMessage(chat_id,text):
    text = urllib.parse.quote_plus(text)
    link = f'{LINK}sendMessage?text={text}&chat_id={chat_id}'
    response = requests.get(link)
    return response

def getLatestId(updates):
    update_ids=[]
    for update in updates['result']:
        update_ids.append(int(update['update_id']))
    return max(update_ids)

def getLastIdMessage():
    JsonData = getUpdates()
    LengthOfMessages = len(JsonData['result'])
    LastMessage = LengthOfMessages-1
    ChatID=None
    Message=None
    try:
        ChatID  =  JsonData['result'][LastMessage]['message']['chat']['id']
        Message =  JsonData['result'][LastMessage]['message']['text']
    except Exception as e:
        print(color.red,e)
        return ChatID
    else:
        return ChatID,Message

def code():
    try:
        chatid,message = getLastIdMessage()
        sendMessage(chatid,message[::-1])
    except Exception as e:
        print(color.red,e)
        chatid = getLastIdMessage()
        sendMessage(chatid,'Somthing is Wrong')

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(color.lightred,'\nExiting')
