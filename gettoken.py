
from pprint import pprint
import telepot
from telepot.loop import *


bot = telepot.Bot('364939368:AAEoiv-I8bQgid0vR2n0SV5W2oG9HdEKANk')
#print(bot.getMe())

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['Please dont disturb me right now :('])

MessageLoop(bot, handle).run_as_thread()
print ('The bot is on')

# Keep the program running.
while 1:
    time.sleep(10)


#def handle(msg):
#    pprint(msg)

#MessageLoop(bot, handle).run_forever()

#response = bot.getUpdates()
#pprint(response)

##bot.sendMessage(42231217, 'The bot is creepy (:!')