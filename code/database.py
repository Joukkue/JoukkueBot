#coding: utf-8
import sqlite3
#TODO: Error handling

def createTable():
    connection = sqlite3.connect('quotes.db', check_same_thread=False)
    c = connection.cursor()
    #if(checkTableExists()):
    c.execute('''CREATE TABLE IF NOT EXISTS quotes
            (find text, quote text, username text)''')
    connection.commit()
    connection.close()

def addToDataBase(find, quote, username):
    connection = sqlite3.connect('quotes.db', check_same_thread=False)
    c = connection.cursor()
    c.execute("INSERT INTO quotes(find, quote, username) VALUES (?, ?, ?)", (find, quote, username))
    #c.execute("INSERT INTO quotes(quote) VALUES (?)",s)
    #c.execute("INSERT INTO quotes(username) VALUES (?)",r)
    connection.commit()
    connection.close()

def findQuote(quote, chat_id, bot):
    connection = sqlite3.connect('quotes.db', check_same_thread=False)
    t = (quote, )
    c = connection.cursor()
    c.execute("SELECT * FROM quotes WHERE find =?", t)
    found = c.fetchone()
    bot.sendMessage(chat_id, found[1] + "\n-@" + found[2])
    connection.close()

#createTable()

#connection = sqlite3.connect('quotes.db', check_same_thread=False)
#c = connection.cursor()


#addToDataBase("moi", "mitakullu", "@Jollla")

#for row in c.execute('SELECT * FROM quotes'):
    #print (row)

#asd = findQuote("moi")

#print asd[1]


