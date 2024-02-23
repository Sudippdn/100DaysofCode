import time
from datetime import datetime
import pytz
import timeit
from playsound import  playsound    

hour = int(input("How many hours? "))
minutes = int(input("How many minutes? "))
seconds = int(input("How many seconds? "))

Clear_and_return = "\033[H"
clear = '\033[2J'

total_second = hour * 60 * 60 + minutes * 60 + seconds

while total_second  > 0:
    
    
    print(clear)
    now = datetime.now()
    Alabama_timeZone = pytz.timezone("US/Central")
    Alabama_current_time = datetime.now(Alabama_timeZone)
    Alabama_time = Alabama_current_time.strftime("%b-%d-%Y   %H:%M:%S")
    current_time = now.strftime("%b-%d-%Y   %H:%M:%S")
    if total_second > 0 and total_second/60 > 0:
        remaining_hours = int(total_second/3600)
        remaining_minutes = int(total_second/60)%60
        remaining_seconds = (total_second%60)  
        print(f'''{Clear_and_return}{remaining_hours:02d}:{remaining_minutes:02d}:{remaining_seconds:02d}
                    \ncurrent time = {current_time}
                    \nAlabama = {Alabama_time}''')
        total_second -= 1
        time.sleep(1)

playsound("alarm.mp3")
playsound("alarm.mp3")
playsound("alarm.mp3")
time.sleep(60)
playsound("alarm.mp3")
playsound("alarm.mp3")
playsound("alarm.mp3")
playsound("alarm.mp3")
time.sleep(100)
playsound("alarm.mp3")
playsound("alarm.mp3")
playsound("alarm.mp3")
playsound("alarm.mp3")

