from __future__ import print_functionimport telepotimport timefrom code.archive import *from code.poll import *from code.compare import *from code.uptime import upTimefrom code.quote import addquote, readquote, fileLengthfrom telepot.loop import MessageLoopbot = telepot.Bot(testBot)response = bot.getUpdates()#print(bot.getMe())#response = bot.getUpdates()# etsitaan uusille filuille id:t#print(response)start_time = time.time()fileLength()online = 0def handle(msg):	content_type, chat_type, chat_id = telepot.glance(msg)	print(content_type, chat_type, chat_id)	if online != 0:		if content_type == 'text':			value = comparing(msg['text'])			temp = msg['text'].split(" ")[0]			if value.is_tuli() == True:				bot.sendMessage(chat_id, 'spruit')				bot.sendSticker(chat_id, spruit)			if value.is_tissit() == True:				bot.sendPhoto(chat_id, testBoobs)			if msg['text'] == "/uptime":				upTime(chat_id, bot)			if msg['text'].split(" ")[0] == "/pol":				poll(msg, chat_id, bot)			if temp == "/insertquote":				addquote(chat_id, bot, msg)			if temp == "/readquote":				readquote(chat_id, bot, msg)		if content_type == 'voice':			bot.sendMessage(chat_id, 'Lul i have no ears')		if content_type == 'new_chat_member':			bot.sendMessage(chat_id, 'Tervetuloa norsunluutorniin, voittajien valinta')MessageLoop(bot, handle).run_as_thread()print ('The bot is on')# Keep the program running.while 1:    if online == 0:        time.sleep(1)        online = 1    time.sleep(10)    #bot.sendMessage(-1001059712421L, 'Moi, en ees tullu pakottaa')#def handle(msg):#pprint(msg)#MessageLoop(bot, handle).run_forever()##bot.sendMessage(42231217, 'The bot is creepy (:!')