#coding: utf-8

def getHelp(bot, msg):
    print("/help was calld")

    chat_id = msg['chat']['id']

    helpText = "Use /uptime to see how long the bot has been up\n" \
           "Reply to a message, then use /insertquote and a tag for the quote, to add the selected quote to the database\n" \
           "To read quotes, message /readquote with the tag of the quote you wish to read\n" \
           "Use /treenit to see upcoming practices for Espoo Hwarang Team\n"
    print("Sent message: \n" + helpText)
    bot.sendMessage(chat_id, helpText)

    return helpText