#coding: utf-8
import os
import sqlite3

db_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'joukkue.db')

def createTable():
    connection = sqlite3.connect(db_dir, check_same_thread=False)
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS quotes
            (find text, quote text, username text)''')
    connection.commit()
    connection.close()

def addToDataBase(bot, msg):
    print("/addquote was calld")

    chat_id = msg['chat']['id']

    try:
        connection = sqlite3.connect(db_dir, check_same_thread=False)
        c = connection.cursor()
        find = msg['text'].split(" ")[1]
        quote = msg['reply_to_message']['text']
        username = msg['reply_to_message']['from']['username']
        try:
            c.execute("INSERT INTO quotes(find, quote, username) VALUES (?, ?, ?)", (find, quote, username))
            connection.commit()
            connection.close()
            bot.sendMessage(chat_id, "Quote added succesfully")
        except:
            bot.sendMessage(chat_id, "Quote with the tag " + find + " already exists")
            connection.commit()
            connection.close()


    except:
        bot.sendMessage(chat_id, "Error adding quote. Please make sure you replied to a message and added a tag for quote")
        connection.close()

def findQuote(bot,msg):
    print("/findquote was calld")

    chat_id = msg['chat']['id']

    try:
        connection = sqlite3.connect(db_dir, check_same_thread=False)
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

def listQuotes(bot, msg):
    print("/listquotes was calld")

    chat_id = msg['chat']['id']
    try:
        connection = sqlite3.connect("/storage/emulated/0/qpython/projects/JoukkueBot-master/joukkue.db", check_same_thread=False)
        c = connection.cursor()
        text = ""
        for row in c.execute('SELECT find FROM quotes'):
            text += row[0]
            text += "\n"
        bot.sendMessage(chat_id, text)
    except:
        bot.sendMessage(chat_id, "Error listing quotes")
