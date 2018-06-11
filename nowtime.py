import datetime

def getNow():
    now = datetime.datetime.now()
    return now

def getJst():
    now = getNow()
    jst = now + datetime.timedelta(hours=9)
    return jst