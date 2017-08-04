from __future__ import print_function
from os import path


ideas_dir = path.join(path.dirname(path.dirname(path.abspath(__file__))), 'ideas.txt')

def addIdea(bot, msg):

    chat_id = msg['chat']['id']

    ideaFile = open(ideas_dir, 'a')
    
    try:
        temp = msg['text'].split(" ",1)[1]
        print(temp , file=ideaFile)
        bot.sendMessage(chat_id, "Idea added")
    except IndexError:
        bot.sendMessage(chat_id, "Use: /addIdea *idea*")
    except:
        bot.sendMessage(chat_id, "Error adding idea")

        ideaFile.close()

def listIdeas(bot, msg):

    chat_id = msg['chat']['id']

    text = ""
    try:
        ideaFile = open(ideas_dir, 'r')
        
        for line in ideaFile:
            text += line
        ideaFile.close()

        if len(text) > 0:
            bot.sendMessage(chat_id, text)
        else:
            bot.sendMessage(chat_id, "No ideas found")

    except:
        bot.sendMessage(chat_id, "Error reading ideas")
