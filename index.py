from datetime import datetime,timedelta
import webbrowser
import time


print("Enter a song url(youtube link) to play:")
youtube_url = str(input())

print("Enter a Break Interval time(In minutes):")

interval = int(input())

timeV = datetime.now() + timedelta(minutes=interval)
timer = timeV.minute


def takeBreak():
    webbrowser.open(youtube_url)
    timeV = datetime.now() + timedelta(minutes=1)
    timer = timeV.minute
    return timer

while True:
    if(datetime.now().minute == timer):
        timer = takeBreak()
    time.sleep(2)    



