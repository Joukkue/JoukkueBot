from __future__ import print_function

counter = -1

def fileLength(file):
    stack = open(file, "r")
    global  counter
    line = "lel"
    while line!="":
        line = stack.readline()
        line = line.rstrip()
        counter += 1
    stack.close()

def addquote(chat_id, bot, msg):
    global counter
    quoteFile = open('quotes.txt', 'a')
    try:
        print(msg['text'].split(" ")[1] + ";<;"+ msg['reply_to_message']['from']['username'] +";<;"+ msg['reply_to_message']['text'] , file = quoteFile)
        #TODO: No telegran nick == no quote, should be fixed
        bot.sendMessage(chat_id, "Quote added")
        counter += 1
    except:
        bot.sendMessage(chat_id, "Error adding quote")

    quoteFile.close()

def readquote(chat_id, bot, msg):

    quoteFile = open("quotes.txt", 'r')

    try:
        temp = msg['text'].split(" ")[1]

        for i in range(counter):
            text = quoteFile.readline()
            #text = text.rstrip()
            check = text.split(";<;")[0]
            who = text.split(";<;")[1]
            quote = text.split(";<;")[2] #TODO: Miten oikeesti menee?
            if check == temp:
                bot.sendMessage(chat_id, quote + "by @" + who)

    except:
        bot.sendMessage(chat_id, "No such message")

    quoteFile.close()