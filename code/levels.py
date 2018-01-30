import os
import sqlite3

db_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'joukkue.db')

def gainExperience(bot, msg):
    connection = sqlite3.connect(db_dir, check_same_thread=False)
    c = connection.cursor()
    username = msg['from']['username']
    chat = msg['chat']['id']
    c.execute("SELECT user FROM Levels WHERE user =? and chat=?", (username, chat))
    exist = c.fetchone()
    if not exist:
        c.execute("INSERT INTO Levels(user, chat, level, experience) VALUES (?, ?, 0, 0)", (username, chat))
    c.execute("SELECT experience FROM Levels WHERE user =? and chat=?", (username, chat))
    newExp = c.fetchone()[0] + 10
    c.execute("SELECT level FROM Levels WHERE user =? and chat=?", (username, chat))
    currentLevel = c.fetchone()[0]

    if newExp >= 100 * currentLevel:
        c.execute("SELECT level FROM Levels WHERE user =? and chat=?", (username, chat))
        newLevel = c.fetchone()[0] + 1
        c.execute("UPDATE Levels SET level =? WHERE user =? AND chat=?", (newLevel, username, chat))
        c.execute("UPDATE Levels SET experience =? WHERE user =? AND chat=?", (0, username, chat))
        connection.commit()
        connection.close()
    else:
        c.execute("UPDATE Levels SET experience =? WHERE user =? AND chat=?", (newExp, username, chat))
        connection.commit()
        connection.close()

def getLevels(bot, msg):
    print("getLevels called")
    connection = sqlite3.connect(db_dir, check_same_thread=False)
    c = connection.cursor()
    chat = msg['chat']['id']
    c.execute("SELECT level, experience, user FROM Levels WHERE chat=? ORDER BY level DESC, experience DESC " , (chat,) )
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
    c.execute("SELECT user, level, experience FROM Levels WHERE chat=? AND user =? ORDER BY level DESC, experience DESC ", (chat, username))
    user = c.fetchone()
    message = "User, level, experience\n" \
              "----------------------------\n"
    message += "{:s} {:5d} {:7d}\n".format(user[0], user[1], user[2])
    print("Message sent: \n"
          + message)
    bot.sendMessage(chat, message)
    connection.close()



def main():
    initializeTable()


def initializeTable():
    connection = sqlite3.connect(db_dir, check_same_thread=False)
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Levels
            (user text, chat text, level integer, experience integer)''')
    connection.commit()
    connection.close()

main()