import os
import sqlite3

db_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'joukkue.db')

def gainExperience(bot, msg):
    connection = sqlite3.connect(db_dir, check_same_thread=False)
    c = connection.cursor()
    username = msg['from']['id']
    chat = msg['chat']['id']
    c.execute("SELECT user FROM Levels LEFT OUTER JOIN Users ON Levels.userid = Users.userid WHERE Levels.userid =? and chat=? ", (username, chat))
    exist = c.fetchone()
    if not exist:
        c.execute("INSERT INTO Levels(userid, chat, level, experience) VALUES (?, ?, 0, 0)", (username, chat))
    c.execute("SELECT experience FROM Levels LEFT OUTER JOIN Users ON Levels.userid = Users.userid WHERE Levels.userid =? and chat=?", (username, chat))
    newExp = c.fetchone()[0] + 10
    c.execute("SELECT level FROM Levels LEFT OUTER JOIN Users ON Levels.userid = Users.userid WHERE Levels.userid =? and chat=?", (username, chat))
    currentLevel = c.fetchone()[0]

    if newExp >= 100 * currentLevel:
        c.execute("SELECT level FROM Levels LEFT OUTER JOIN Users ON Levels.userid = Users.userid WHERE Levels.userid =? and chat=?", (username, chat))
        newLevel = c.fetchone()[0] + 1
        c.execute("UPDATE Levels SET level =? WHERE userid =? AND chat=?", (newLevel, username, chat))
        c.execute("UPDATE Levels SET experience =? WHERE userid =? AND chat=?", (0, username, chat))
        connection.commit()
        connection.close()
    else:
        c.execute("UPDATE Levels SET experience =? WHERE userid =? AND chat=?", (newExp, username, chat))
        connection.commit()
        connection.close()

def getLevels(bot, msg):
    print("getLevels called")
    connection = sqlite3.connect(db_dir, check_same_thread=False)
    c = connection.cursor()
    chat = msg['chat']['id']
    c.execute("SELECT level, experience, user FROM Levels LEFT OUTER JOIN Users ON Levels.userid = Users.userid WHERE chat=? ORDER BY level DESC, experience DESC " , (chat,) )
    users = c.fetchall()
    message = "Level, experience, user\n" \
              "----------------------------\n"
    for i in users:
        message += " {:5d} {:7d}    {:s}\n".format(i[0], i[1],i[2])

    print("Message sent: \n"
          + message)
    bot.sendMessage(chat, message)
    connection.close()


def myLevel(bot, msg):
    print("myLevel called")
    connection = sqlite3.connect(db_dir, check_same_thread=False)
    c = connection.cursor()
    username = msg['from']['username']
    chat = msg['chat']['id']
    c.execute("SELECT user, level, experience FROM Levels LEFT OUTER JOIN Users ON Levels.userid = Users.userid WHERE chat=? AND user =? ORDER BY level DESC, experience DESC ", (chat, username))
    user = c.fetchone()
    message = "User, level, experience\n" \
              "----------------------------\n"
    message += "{:s} {:5d} {:7d}\n".format(user[0], user[1], user[2])
    print("Message sent: \n"
          + message)
    bot.sendMessage(chat, message)
    connection.close()

def updateChatDatabase(msg):
    connection = sqlite3.connect(db_dir, check_same_thread=False)
    c = connection.cursor()
    c.execute("SELECT chatid FROM Chats WHERE chatid =?", (msg['chat']['id'],))
    exist = c.fetchone()
    if not exist:
        c.execute("INSERT INTO Chats (name, chatid)VALUES (?, ?)", (msg['chat']['title'], msg['chat']['id']))
    else:
        if not exist[0] == msg['chat']['title']:
            c.execute("UPDATE Chats SET name =? WHERE chatid =?", (msg['chat']['title'], msg['chat']['id'] ) )

    connection.commit()
    connection.close()


def updateUserDatabase(msg):
    connection = sqlite3.connect(db_dir, check_same_thread=False)
    c = connection.cursor()
    c.execute("SELECT userid FROM Users WHERE userid =?", (msg['from']['id'],))
    exist = c.fetchone()
    if not exist:
        try:
            c.execute("INSERT INTO Users (user, userid)VALUES (?, ?)", (msg['from']['username'], msg['from']['id']))
        except:
            c.execute("INSERT INTO Users (user, userid)VALUES (?, ?)", (msg['from']['first_name'], msg['from']['id']))
    else:
        if not exist[0] == msg['from']['username']:
            try:
                c.execute("UPDATE Users SET user =? WHERE userid =?", (msg['from']['username'], msg['from']['id'] ) )
            except:
                c.execute("UPDATE Users SET user =? WHERE userid =?", (msg['from']['first_name'], msg['from']['id']))

    connection.commit()
    connection.close()


def main():
    initializeTable()


def initializeTable():
    connection = sqlite3.connect(db_dir, check_same_thread=False)
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Levels
            (userid text, chat text, level integer, experience integer)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Chats
                (name text, chatid text)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Users
              (user text, userid text)''')
    connection.commit()
    connection.close()

main()