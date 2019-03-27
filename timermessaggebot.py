import requests
from datetime import datetime, date, time
import argparse
import sys
import time
import config



#Function to send a message to a channel

def bot_SendMessage(Bot_message):
    token = config.bot_token
    chatId = config.chatId

    send_message = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatId + '&parse_mode=Markdown&text=' + Bot_message

    response = requests.get(send_message)

    return response.json()


# Getting schedule and formatting it to date time object, then sorting by the soonest post

t_now = datetime.now()

schedules = []

for x in config.Schedule:

    t = x[0]
    p = x[1]
    time1 = datetime(2019, t[0], t[1], t[2], t[3])
    Time = (time1 - t_now).total_seconds()
    d = [Time, p]
    schedules += [d]





def getKey(item):
    return item[0]




sorted_schedule= sorted(schedules, key=getKey)



# Start of the program


def main():

    for x in sorted_schedule:
        print('waiting ' + str(x[0])[:-6] +'s before send a post.')
        time.sleep(int(x[0]))
        bot_SendMessage(x[1])
    print("All posts are sent")
    sys.exit()





if __name__ == '__main__':
    main()
