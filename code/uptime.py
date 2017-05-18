import time


start_time = time.time()

def upTime(chat_id, bot):
    running_time_seconds = time.time() - start_time
    running_time_minutes = running_time_seconds / 60
    if running_time_seconds < 1000: #TODO:  paremmat luvut
        bot.sendMessage(chat_id, " %.2f seconds " % running_time_seconds)
    elif running_time_seconds < 10000:
        bot.sendMessage(chat_id, " %.2f minutes " % running_time_minutes)