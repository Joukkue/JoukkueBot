#coding: utf-8#!usr/bin/python2.7from __future__ import print_function, unicode_literalsimport random, sysimport telepotfrom telepot.loop import MessageLoopfrom code import poll, quote, compare, ideafrom resources.archive import *from code.help import getHelpfrom code.uptime import upTime, start_timefrom code.treenit import treenitfrom code.levels import gainExperience, getLevelsdef main():    passif sys.argv[1:]:    print("JoukkueBot started")    bot = telepot.Bot(joukkueBot) #Do not changeelse:    bot = telepot.Bot(testBot) #Change this if you need toonline = 0#ADD NEW COMMANDS TO THIS LIST#MAKE SURE THEY TAKE (bot, msg) AS THEIR PARAMETERScommands = {    '/uptime': upTime,    '/pol': poll.pollMain,    '/insertquote': quote.addToDataBase,    '/readquote': quote.findQuote,	'/listquotes': quote.listQuotes,    '/treenit': treenit,    '/addidea': idea.addIdea,    '/listideas': idea.listIdeas,    '/help': getHelp,    '/getlevels': getLevels,}def handle(msg):        content_type, chat_type, chat_id = telepot.glance(msg)        print("Message recieved, type " + content_type + ", chat type " +chat_type+ ", chat id ", chat_id)        print("===========\n{}\n===========".format(msg))        if content_type == 'new_chat_member':            print('username' in msg['new_chat_participant'].keys())            if 'username' in msg['new_chat_participant'].keys():                member = msg['new_chat_participant']['username']                bot.sendMessage(chat_id, 'Tervetuloa norsunluutorniin @' + member + ', voittajien valinta')            else:                member = msg['new_chat_participant']['first_name']                bot.sendMessage(chat_id, 'Tervetuloa norsunluutorniin ' + member + ', voittajien valinta')        if msg['date'] >= start_time:            gainExperience(bot, msg)            if content_type == 'text':                value = compare.Comparing(msg['text'])                temp = msg['text'].split(" ")[0].split("@")[0]                if value.is_tuli() == True:                    rng = random.randint(0,2)                    if(rng == 0):                        bot.sendMessage(chat_id, 'spruit')                    elif(rng ==1):                        bot.sendSticker(chat_id, spruit)                    else:                        bot.sendMessage(chat_id, "tirsk")                if value.is_tissit() == True:                    bot.sendPhoto(chat_id, boobs)                if value.is_kalja() == True:                    bot.sendMessage(chat_id, "Sanoiko joku kaljaa?")                                #If msg-text starts with "/" checks for any known commands                if temp[0] == "/":                    return commandHandler(msg,temp)            if content_type == 'voice':                bot.sendMessage(chat_id, 'Lul i have no ears')#Goes trough list of all commands and check if input matches, runs commanddef commandHandler(msg,com):    for i in commands:        if com == i:            asd = commands[i](bot,msg)            return asd    returnif __name__ == "__main__":   # stuff only to run when not called via 'import' here   main()   MessageLoop(bot, handle).run_as_thread()   print('The bot is running')   # Keep the program running.   while 1:       online = 1       if input() == "message":           text = input("What do you wanna say?\n")           location = input("What chat?\n").rstrip()           if location == "testground":               bot.sendMessage(testground, text)           elif location == "joukkue":                bot.sendMessage(joukkue, text)