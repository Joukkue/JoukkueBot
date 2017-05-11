
from pprint import pprint
import telepot

bot = telepot.Bot('364939368:AAEoiv-I8bQgid0vR2n0SV5W2oG9HdEKANk')
print(bot.getMe())


response = bot.getUpdates()
pprint(response)