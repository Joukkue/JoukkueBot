#coding: utf-8#!usr/bin/python2.7from __future__ import print_functionfrom __future__ import unicode_literalsimport telepotimport timeimport randomfrom code.archive import *from code.poll import *from code.compare import *from code.uptime import upTimefrom telepot.loop import MessageLoopfrom code.treenit import treenitfrom code.idea import  addIdea, listIdeasfrom code.database import createTable, addToDataBase, findQuotefrom code.help import helpbot = telepot.Bot(joukkueBot)response = bot.getUpdates()#print(bot.getMe())#response = bot.getUpdates()# etsitaan uusille filuille id:t#print(response)start_time = time.time()createTable()online = 0#ADD NEW COMMANDS TO THIS LIST#MAKE SURE THEY TAKE (bot, msg) AS THEIR PARAMETERScommands = {    '/uptime': upTime,    '/pol': poll,    '/insertquote': addToDataBase,    '/readquote': findQuote,    '/treenit': treenit,    '/addIdea': addIdea,    '/listIdeas': listIdeas,    '/help': help}def handle(msg):        content_type, chat_type, chat_id = telepot.glance(msg)        print("Message recieved, type " + content_type + ", chat type " +chat_type+ ", chat id ", chat_id)        #print(msg)        if content_type == 'new_chat_member':            member = msg['new_chat_participant']['username']            bot.sendMessage(chat_id, 'Tervetuloa norsunluutorniin @' + member + ', voittajien valinta')        if msg['date'] >= start_time:            if content_type == 'text':                value = Comparing(msg['text'])                temp = msg['text'].split(" ")[0].split("@")[0]                if value.is_tuli() == True:                    rng = random.randint(0,2)                    if(rng == 0):                        bot.sendMessage(chat_id, 'spruit')                    elif(rng ==1):                        bot.sendSticker(chat_id, spruit)                    else:                        bot.sendMessage(chat_id, "tirsk")                if value.is_tissit() == True:                    bot.sendPhoto(chat_id, boobs)                if value.is_kalja() == True:                    bot.sendMessage(chat_id, "Sanoiko joku kaljaa?")                                #If msg-text starts with "/" checks for any known commands                if temp[0] == "/":                    for i in commands:                        if temp == i:                            commands[i](bot, msg)                            break            if content_type == 'voice':                bot.sendMessage(chat_id, 'Lul i have no ears')MessageLoop(bot, handle).run_as_thread()print ('The bot is running')# Keep the program running.while 1:    online = 1    time.sleep(10)    #bot.sendMessage(-1001059712421L, 'Moi, en ees tullu pakottaa')#def handle(msg):#pprint(msg)#MessageLoop(bot, handle).run_forever()##bot.sendMessage(42231217, 'The bot is creepy (:!')