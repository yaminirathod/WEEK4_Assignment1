import datetime

def currentDateTimeDisplay():
    currenttime = datetime.datetime.now()
    # currentday = datetime.datetime.day()
    # currentyear = datetime.date.today().year

    print('Current Date & Time : {}'.format(currenttime.strftime("%Y/%m/%d %H:%M:%S")))
    # print(currentday)
    # print(currentyear)