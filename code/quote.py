from __future__ import print_function

def addquote(chat_id, bot, msg):
    quoteFile = open('quotes.txt', 'a')
    print(msg['reply_to_message']['text'], file = quoteFile)
    bot.sendMessage(chat_id, "Quote added")
    quoteFile.close()

def readquote(chat_id, bot, msg):

    quoteFile = open("quotes.txt", 'r')

    try:
        temp = msg['text'].split(" ")[1]

        for i in range(0,3):
            text = quoteFile.readline()
            check = text.split(" ")[0]
            quote = text.split(" ")[1]
            if check == temp:
                bot.sendMessage(chat_id, quote)

    except:
        bot.sendMessage(chat_id, "No such message")

    quoteFile.close()