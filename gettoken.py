
from pprint import pprint
import telepot
from telepot.loop import *


bot = telepot.Bot('364939368:AAEoiv-I8bQgid0vR2n0SV5W2oG9HdEKANk')
#print(bot.getMe())

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        if msg['text'] == "tuli":
            bot.sendMessage(chat_id, 'spruit')
            bot.sendSticker(chat_id, 'CAADBAADiwAD634eAmMUu4WqWPVmAg')
        if msg['text'] == "tissit":
            bot.sendPhoto(chat_id, 'AgADBAADNKoxGztVqFByX5YFloA7wrFSvRkABBj0S0vREoDK--0AAgI')
        if msg['text'] == "/moi":
            bot.sendMessage(chat_id, "moi")
    if content_type == 'voice':
        bot.sendMessage(chat_id, 'Lul i have no ears')
    if content_type == 'new_chat_member':
        bot.sendMessage(chat_id, 'Tervetuloa norsunluutorniin, voittajien valinta')

MessageLoop(bot, handle).run_as_thread()
print ('The bot is on')
#response = bot.getUpdates()
#pprint(response)
# Keep the program running.
while 1:
    time.sleep(10)
    #bot.sendMessage(-1001059712421L, 'Moi, en ees tullu pakottaa')


#def handle(msg):
#    pprint(msg)

#MessageLoop(bot, handle).run_forever()



##bot.sendMessage(42231217, 'The bot is creepy (:!')