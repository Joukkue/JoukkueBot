from __future__ import print_function

def addIdea(chat_id, bot, msg):
    ideaFile = open('ideas.txt', 'a')
    temp = msg['text'].split(" ",1)[1]
    try:
        print(temp , file=ideaFile)
        bot.sendMessage(chat_id, "Idea added")
    except:
        bot.sendMessage(chat_id, "Error adding idea")

        ideaFile.close()

def listIdeas(chat_id, bot):
    ideaFile = open("ideas.txt", 'r')
    text = ""
    try:
        line = "lel"
        while line != "":
            line = ideaFile.readline()
            #line = line.rstrip()
            text += line
        ideaFile.close()

        bot.sendMessage(chat_id, text)

    except:
        bot.sendMessage(chat_id, "Error reading ideas")
