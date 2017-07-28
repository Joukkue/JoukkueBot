from datetime import datetime

def timeCheck(my_time):#my_time format "00:00:00"
    time = datetime.time(datetime.now())
    my_datetime = datetime.strptime(my_time, "%H:%M:%S")
    my_datetime = time.replace(hour=my_datetime.time().hour, minute=my_datetime.time().minute, second=my_datetime.time().second, microsecond=0)
    print  my_datetime
    print time
    if (time > my_datetime):
        return True
    else:
        return False