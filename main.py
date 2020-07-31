from clear import clear
from prints import prints as print
from colors import colors as color

import requests,json,urllib,os,time

clear()
print(color.orange,'\nEnter Your API KEY : ',end='')
token = input()
LINK = f'https://api.telegram.org/bot{token}/'
clear()


class Bot:
    def getJsonFromURL(self,link):
        try:
            response = requests.get(link)
            response.raise_for_status()
            JsonFormat = json.loads(response.text)
            return JsonFormat
        except Exception as e:
            if response.status_code == 409:
                print(color.red,"Webhook with this bot detected, Do you want to delete that webhook ?[N/y]")
                will_delete = input()
                if will_delete.upper() == "Y" or "YES":
                    print("OK Deleting webhook")

                else:
                    print("Exiting")
            print(color.red,e)


    def getUpdates(self,offset=None):
        link = f'{LINK}getUpdates?timeout=100'
        if offset:
            link+='&offset={}'.format(offset)
        JsonData = self.getJsonFromURL(link)
        return JsonData

    def sendMessage(self,chat_id,text):
        text = urllib.parse.quote_plus(text)
        link = f'{LINK}sendMessage?text={text}&chat_id={chat_id}'
        response = requests.get(link)
        return response

    def getLatestId(self,updates):
        update_ids=[]
        for update in updates['result']:
            update_ids.append(int(update['update_id']))
        return max(update_ids)

    def getLastIdMessage(self):
        JsonData = self.getUpdates()
        LengthOfMessages = len(JsonData['result'])
        LastMessage = LengthOfMessages-1
        ChatID=None
        Message=None
        print(JsonData['result'][LastMessage]['message'])
        try:
            ChatID  =  JsonData['result'][LastMessage]['message']['chat']['id']
            Message =  JsonData['result'][LastMessage]['message']['text']
        except Exception as e:
            print(color.red,e)
            return ChatID
        else:
            return ChatID,Message
    def code(self):
        try:
            chatid,message = self.getLastIdMessage()
            self.sendMessage(chatid,message[::-1])
        except Exception as e:
            print(color.red,e)
            chatid = self.getLastIdMessage()
            self.sendMessage(chatid,'Somthing is Wrong')
        return
def main():
    bot = Bot()
    latestupdateid = None
    while True:
        print(color.yellow,'Running Smoothly\n')
        updates = bot.getUpdates(latestupdateid)
        if (len(updates['result'])>0):
            print(color.cyan,'New Message Arrived\n')
            latestupdateid = bot.getLatestId(updates)+1
            l=bot.code()
            print(l,'OK')
        print("sleeping")
        time.sleep(2)





if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(color.lightred,'\nExiting')
