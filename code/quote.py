#coding: utf-8
import os
import sqlite3

db_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'joukkue.db')


def main():
	initializeTable()


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
            c.execute("INSERT INTO Quotes(find, quote, username) VALUES (?, ?, ?)", (find, quote, username))
            connection.commit()
            connection.close()
            print("Sent message: \n" + "Quote added succesfully")
            bot.sendMessage(chat_id, "Quote added succesfully")
        except:
            print("Sent message: \n" +  "Quote with the tag " + find + " already exists")
            bot.sendMessage(chat_id, "Quote with the tag " + find + " already exists")
            connection.commit()
            connection.close()


    except:
        print("Sent message: \n" + "Error adding quote. Please make sure you replied to a message and added a tag for quote")
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
            c.execute("SELECT * FROM Quotes WHERE find =?", t)
            found = c.fetchone()
            print("Sent message: \n" +  found[1] + "\n-@" + found[2])
            bot.sendMessage(chat_id, found[1] + "\n-@" + found[2])
            connection.close()
        except:
            print("Sent message: \n" + "No such quote found")
            bot.sendMessage(chat_id, "No such quote found")
            connection.close()
    except:
        print("Sent message: \n" + "Please add a quote to search for")
        bot.sendMessage(chat_id, "Please add a quote to search for")
        connection.close()

def listQuotes(bot, msg):
    print("/listquotes was calld")

    chat_id = msg['chat']['id']
    try:
        connection = sqlite3.connect(db_dir, check_same_thread=False)
        c = connection.cursor()
        text = ""
        for row in c.execute('SELECT find FROM Quotes'):
            text += row[0]
            text += "\n"
        print("Sent message: \n" + text)
        bot.sendMessage(chat_id, text)
    except:
        print("Sent message: \n" + "Error listing quotes")
        bot.sendMessage(chat_id, "Error listing quotes")

#Initializes required table to joukkue.db if not found
def initializeTable():
    connection = sqlite3.connect(db_dir, check_same_thread=False)
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Quotes
            (find text, quote text, username text)''')
    connection.commit()
    connection.close()
	

main()

