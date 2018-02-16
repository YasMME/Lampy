#Class for the Set Alarm Thread
#Thread waits for the Toggle Button, and then allows the alarm to be
#set using the push buttons

from global_config import *
import RPi.GPIO as GPIO
from inputs.button import Button
from inputs.set_alarm_mode import SetAlarmMode

global TOGGLE_FLAG
def callback_toggle(channel):
    global TOGGLE_FLAG
    print TOGGLE_FLAG 
    if (TOGGLE_FLAG == True):
        LCD_CONTROL_BOOL = True
        LCD.write_msg_to_screen("Set Alarm Mode")
        time.sleep(2)
        LCD.write_msg_to_screen("Alarm: %s" 
        % DAY_NIGHT_ALARM.get_morning_alarm())
        LCD_CONTROL_BOOL = False

def callback_hour(channel):
    if (TOGGLE_FLAG):
        DAY_NIGHT_ALARM.increment_both_hour()
        LCD.write_msg_to_screen("Alarm: %s" 
            % DAY_NIGHT_ALARM.get_morning_alarm())
    
def callback_min(channel):
    if (TOGGLE_FLAG):
        DAY_NIGHT_ALARM.increment_both_min()
        LCD.write_msg_to_screen("Alarm: %s"
            % DAY_NIGHT_ALARM.get_morning_alarm())

class SetAlarmThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        alarmToggle = Button(11) 
        hourButton = Button(29)
        minButton = Button(31)

        #callback for the toggle button
        GPIO.add_event_detect(alarmToggle.get_pin()
            , GPIO.RISING
            , callback = callback_toggle
            , bouncetime=750)
        #callback for the hour button
        GPIO.add_event_detect(hourButton.get_pin()
            , GPIO.BOTH
            , callback = callback_hour
            , bouncetime=750)
        #callback for the minute button
        GPIO.add_event_detect(minButton.get_pin()
            , GPIO.BOTH
            , callback = callback_min
            , bouncetime=750)
