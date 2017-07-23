#coding: utf-8
import sqlite3
connection = sqlite3.connect('quotes.db')
c = connection.cursor()


def createTable():
    c = connection.cursor()
    #if(checkTableExists()):
    c.execute('''CREATE TABLE IF NOT EXISTS quotes
            (find text, quote text, username text)''')
    connection.commit()

def addToDataBase(find, quote, username):
    t = (find, )
    s = (quote, )
    r = ( username, )
    c = connection.cursor()
    c.execute("INSERT INTO quotes(find, quote, username) VALUES (?, ?, ?)", (find, quote, username))
    #c.execute("INSERT INTO quotes(quote) VALUES (?)",s)
    #c.execute("INSERT INTO quotes(username) VALUES (?)",r)
    connection.commit()

def findQuote(quote):
    t = (quote, )
    c.execute("SELECT * FROM quotes WHERE find =?", t)
    return c.fetchone()

createTable()

#addToDataBase("moi", "mitakullu", "@Jollla")

#for row in c.execute('SELECT * FROM quotes'):
    #print (row)

asd = findQuote("moi")

print asd[1]


