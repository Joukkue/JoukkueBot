
#coding: utf-8
#!usr/bin/python2.7
from __future__ import print_function, unicode_literals
import random, sys, time

import telepot
from telepot.loop import MessageLoop

from code import poll, quote, compare, idea
from resources.archive import *
from code.help import getHelp
from code.uptime import upTime, start_time
from code.treenit import treenit
from code.levels import *
import threading
import datetime
import _thread
import socket
import json

def main():
    pass

if sys.argv[1:]:
    print("JoukkueBot started")
    bot = telepot.Bot(joukkueBot) #Do not change
    target = joukkue
else:
    bot = telepot.Bot(testBot) #Change this if you need to
    target = testground

online = 0


#ADD NEW COMMANDS TO THIS LIST
#MAKE SURE THEY TAKE (bot, msg) AS THEIR PARAMETERS
commands = {
    '/uptime': upTime,
    '/pol': poll.pollMain,
    '/insertquote': quote.addToDataBase,
    '/readquote': quote.findQuote,
	'/listquotes': quote.listQuotes,
    '/treenit': treenit,
    '/addidea': idea.addIdea,
    '/listideas': idea.listIdeas,
    '/help': getHelp,
    '/levels': getLevels,
    '/mylevel': myLevel,
}


def handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print("Message recieved, type " + content_type + ", chat type " +chat_type+ ", chat id ", chat_id)
        print("===========\n{}\n===========".format(msg))
        updateChatDatabase(msg)
        updateUserDatabase(msg)
        if content_type == 'new_chat_member':
            print('username' in msg['new_chat_participant'].keys())
            if 'username' in msg['new_chat_participant'].keys():
                member = msg['new_chat_participant']['username']
                bot.sendMessage(chat_id, 'Tervetuloa norsunluutorniin @' + member + ', voittajien valinta')
            else:
                member = msg['new_chat_participant']['first_name']
                bot.sendMessage(chat_id, 'Tervetuloa norsunluutorniin ' + member + ', voittajien valinta')
        if msg['date'] >= start_time:
            gainExperience(bot, msg)
            if content_type == 'text':
                if str(chat_id) == target:
                    forward_message(msg)
                value = compare.Comparing(msg['text'])
                temp = msg['text'].split(" ")[0].split("@")[0]
                if value.is_tuli() == True:
                    rng = random.randint(0,2)
                    if(rng == 0):
                        bot.sendMessage(chat_id, 'spruit')
                    elif(rng ==1):
                        bot.sendSticker(chat_id, spruit)
                    else:
                        bot.sendMessage(chat_id, "tirsk")
                if value.is_tissit() == True:
                    bot.sendPhoto(chat_id, boobs)
                if value.is_kalja() == True:
                    bot.sendMessage(chat_id, "Sanoiko joku kaljaa?")
                
                #If msg-text starts with "/" checks for any known commands
                if temp[0] == "/":
                    return commandHandler(msg,temp)


            if content_type == 'voice':
                bot.sendMessage(chat_id, 'Lul i have no ears')


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter, bot):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.bot = bot
    def run(self):
        check = 0
        while 1:
            time.sleep(1)
            if datetime.datetime.today().weekday() == 0:
                if check == 0:
                    time.sleep(36000)
                    check = 1
                else:
                    self.bot.sendMessage(joukkue, "Oikein hyvää ja pirteää maanantaita kaikille")
                    time.sleep(86400 * 7 - 1)

#Goes trough list of all commands and check if input matches, runs command
def commandHandler(msg,com):
    for i in commands:
        if com == i:
            asd = commands[i](bot,msg)
            return asd
    return


def udp_server(t_name):
    HOST = '127.0.0.1'
    PORT = 8253

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Server socket created")
    except socket.error as msg:
        print("Server failed to create socket. Error: " + str(msg))
        sys.exit()

    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print("Bind failed. Error: " + str(msg))
        sys.exit()

    while True:
        try:
            d = s.recvfrom(1024)
            reply = d[0].decode()
            addr = d[1]
            message = json.loads(reply)
            if  message:
                bot.sendMessage(testground, message)

        except socket.timeout:
            pass


    print("Socket bind complete")

def forward_message(msg):
    HOST = ''
    PORT = 8251
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))
    addr = ('127.0.0.1', 8250)
    reply = json.dumps(msg)
    s.sendto(reply.encode(), addr)

    s.close()




_thread.start_new_thread(udp_server, ("Server-1",))





if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()
   MessageLoop(bot, handle).run_as_thread()
   thread1 = myThread(1, "Thread-1", 1, bot)
   thread1.start()
   print('The bot is running')

   # Keep the program running.
   while 1:
       online = 1
       if input() == "message":
           text = input("What do you wanna say?\n")
           location = input("What chat?\n").rstrip()
           if location == "testground":
               bot.sendMessage(testground, text)
           elif location == "joukkue":
                bot.sendMessage(joukkue, text)
