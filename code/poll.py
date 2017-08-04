from os import path
import sqlite3

db_dir = path.join(path.dirname(path.dirname(path.abspath(__file__))), 'resources\joukkue.db')

def main():
	initializeDatabase()


def pollMain(bot, msg):
	chat_id = msg['chat']['id']
	print("/poll called")
	print(msg['text'].lstrip("/pol "))
	
	
	try:
		pass
		#TODO Create interpreter for user input
	except:
		pass
	finally:
		pass
		
		
#TODO
'''
Add following funktions
 - new_poll
 - remove_poll
 - vote
 - show_polls
 - show_poll
 
 Sample commads
 - /pol new; name; desc; (endTime)
'''

def createPoll(name, desc, endTime=None, **kwargs):
	
	
	try:
		connection = sqlite3.connect(db_dir, check_same_thread=False)
		c = connectio.cursor()
		
	except:
		pass
	finally:
		connection.close()
		
	


#Returns list of sender: id, first name, last name, username
#Missing parts are replaced with empty string
def identify(msg):
	sender = msg['from']
	
	identity = []
	information = ['id', 'first_name', 'last_name', 'username']
	
	for i in information:
		try:
			identity.append(sender[i])
		except KeyError:
			identity.append("")
	
	return identity

	
#Initializes required tables to joukkue.db if not found
def initializeDatabase():
	connection = sqlite3.connect(db_dir, check_same_thread=False)
	c = connection.cursor()
	c.execute('''
		CREATE TABLE IF NOT EXISTS Polls(
			name TEXT NOT NULL, 
			description TEXT NOT NULL,
			endTime INT,
			active INT DEFAULT 1,
			PRIMARY KEY(name)
		)''')
	c.execute('''
		CREATE TABLE IF NOT EXISTS PollOptions(
			number INT NOT NULL,
			description TEXT NOT NULL,
			pollName TEXT NOT NULL,
			PRIMARY KEY  (number, pollName)
			FOREIGN KEY (pollName) REFERENCES Polls(name)
		)''')
	
	c.execute('''
		CREATE TABLE IF NOT EXISTS PollEntries(
			id INT NOT NULL,
			participName TEXT NOT NULL,
			participUsername TEXT,
			answer TEXT,
			pollName TEXT NOT NULL,
			option INT NOT NULL,
			PRIMARY KEY (id, pollName),
			FOREIGN KEY (pollname, option) REFERENCES PollOptions(pollName, number)
		)''')
	connection.commit()
	connection.close()

main()

