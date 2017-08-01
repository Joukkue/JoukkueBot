from os import path

poll_dir = path.join(path.dirname(path.dirname(path.abspath(__file__))), 'polls.txt')
	
def poll(bot, msg):

	chat_id = msg['chat']['id']
	
	try:
		poll_file = open(poll_dir, 'a')
	except OSError:
		bot.sendMessage("Couldn't access polls data")
		
	print(identify(msg))
	
	try:
		pass
		#TODO Create interpreter for user input
	except:
		pass
	finally:
		poll_file.close()
		
		
#TODO
"""
Add following funktions
 - new_poll
 - remove_poll
 - vote
 - show_polls
 - show_poll
"""
		
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



