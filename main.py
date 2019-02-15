from prints_function import prints
from rcolors import colors

import requests
import json
import urllib
import os
import time

prints(colors.blue,'\nEnter Your API KEY ',end='')
token = input()
LINK = 'https://api.telegram.org/bot{}/'.format(token)

def StatusResponse(response):
    if response.status_code==200:
        prints(colors.lightgreen,'SUCCESSFULL RESPONSE\n')
    else:
        prints(colors.red,'SOMETHING IS WRONG !!\n')

def getResponse(link):
    try:
        response = requests.get(link)
        response.raise_for_status()
        StatusResponse(response)
        return response
    except Exception as e:
    	prints(colors.red,e)


def getJsonFromURL(link):
    response = getResponse(link)
    JsonFormat = getJson(response)
    return JsonFormat

def getJson(response):
    JsonFormat = json.loads(response.text)
    return JsonFormat

def getUpdates(offset=None):
    link = LINK+'getUpdates?timeout=100'
    if offset:
        link+='&offset={}'.format(offset)
    JsonData = getJsonFromURL(link)
    return JsonData

def sendMessage(chat_id,text):
    text = urllib.parse.quote_plus(text)
    link = LINK + 'sendMessage?text={}&chat_id={}'.format(text,chat_id)
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
        prints(colors.red,e)
        return ChatID
    else:
        return ChatID,Message

def code():
    try:
        chatid,message = getLastIdMessage()
        sendMessage(chatid,message[::-1])
    except Exception as e:
        prints(colors.red,e)
        chatid = getLastIdMessage()
        sendMessage(chatid,'Somthing is Wrong')

def main():
    os.system('clear')
    latestupdateid = None
    while True:
        prints(colors.yellow,'Running Smoothly\n')
        updates = getUpdates(latestupdateid)
        if (len(updates['result'])>0):
            prints(colors.cyan,'New Message Arrived\n')
            latestupdateid = getLatestId(updates)+1
            code()
        time.sleep(1)
        

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        prints(colors.lightred,'\nExiting')
