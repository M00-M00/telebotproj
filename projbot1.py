import requests
from datetime import datetime, date, time
import argparse
import sys
import time

#Message = input("Write Message Here:")


def bot_SendMessage(Bot_message):
    bot_token ='761788216:AAFlQ54dGWnASAtBCwTbgyj2csGK80kd0W4'
    bot_chatId ='-1001146519007'

    send_message = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatId + '&parse_mode=Markdown&text=' + Bot_message

    response = requests.get(send_message)

    return response.json()

Message = sys.argv[1]

bot_SendMessage(Message)




# Time is turned into Datetime object
