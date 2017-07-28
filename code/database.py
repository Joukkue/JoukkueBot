#coding: utf-8
import sqlite3
#TODO: Better Error handling

def createTable():
    connection = sqlite3.connect('quotes.db', check_same_thread=False)
    c = connection.cursor()
    #if(checkTableExists()):
    c.execute('''CREATE TABLE IF NOT EXISTS quotes
            (find text, quote text, username text)''')
    connection.commit()
    connection.close()

def addToDataBase(bot, msg):
    print("/addquote was calld")

    chat_id = msg['chat']['id']

    try:
        connection = sqlite3.connect('quotes.db', check_same_thread=False)
        c = connection.cursor()
        find = msg['text'].split(" ")[1]
        quote = msg['reply_to_message']['text']
        username = msg['reply_to_message']['from']['username']
        c.execute("INSERT INTO quotes(find, quote, username) VALUES (?, ?, ?)", (find, quote, username))
        connection.commit()
        connection.close()
        bot.sendMessage(chat_id, "Quote added succesfully")
    except:
        bot.sendMessage(chat_id, "Error adding quote. Please make sure you replied to a message and added a tag for quote")
        connection.close()
    #c.execute("INSERT INTO quotes(quote) VALUES (?)",s)
    #c.execute("INSERT INTO quotes(username) VALUES (?)",r)

def findQuote(bot,msg):
    print("/findquote was calld")

    chat_id = msg['chat']['id']

    try:
        connection = sqlite3.connect('quotes.db', check_same_thread=False)
        t = (msg['text'].split(" ")[1], )
        try:
            c = connection.cursor()
            c.execute("SELECT * FROM quotes WHERE find =?", t)
            found = c.fetchone()
            bot.sendMessage(chat_id, found[1] + "\n-@" + found[2])
            connection.close()
        except:
            bot.sendMessage(chat_id, "No such quote found")
            connection.close()
    except:
        bot.sendMessage(chat_id, "Please add a quote to search for")
        connection.close()


#createTable()

#connection = sqlite3.connect('quotes.db', check_same_thread=False)
#c = connection.cursor()


#addToDataBase("moi", "mitakullu", "@Jollla")

#for row in c.execute('SELECT * FROM quotes'):
    #print (row)

#asd = findQuote("moi")

#print asd[1]


