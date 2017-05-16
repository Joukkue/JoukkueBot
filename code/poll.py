	
votes = [0,0]
	
def poll(msg, chat_id, bot):
	global votes
	try:
		temp = msg['text'].split(" ")[1]
		if temp == "new":
			votes = [0,0]
			bot.sendMessage(chat_id, 'New poll')
		elif temp == "yes":
			votes[1] += 1
			bot.sendMessage(chat_id, '+1')
		elif temp == "no":
			votes[0] += 1
			bot.sendMessage(chat_id, '-1')
		elif temp == "result":
			if votes[0] < votes[1]:
				bot.sendMessage(chat_id, 'Voitit pelin')
			elif votes[0] > votes[1]:
				bot.sendMessage(chat_id, 'Havisit pelin')
			else:
				bot.sendMessage(chat_id, 'Tasapeli')
			tot = votes[0] + votes[1]
			bot.sendMessage(chat_id, "Total votes {}".format(tot))
		else:
			bot.sendMessage(chat_id, '/pol [new, yes, no, result]')
	except:
		bot.sendMessage(chat_id, '/pol [new, y, n, result]')