#function that displays the current time to the LCD
import time
import datetime as dt
from global_config import LCD
from global_config import LCD_CONTROL_BOOL
import threading

class TimeThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        timenow = dt.datetime.now()
        currMin = timenow.minute
        LCD.write_time_to_screen()
        while (True):
            if ((currMin != dt.datetime.now().minute)
                &  (LCD_CONTROL_BOOL == False)):
                LCD.write_time_to_screen()
                currMin = dt.datetime.now().minute
                time.sleep(45)


