from morse_to_text import *

import time
import RPi.GPIO as GPIO

morse = ''

time_press = 0
time_nopress = 0

# If the user holds the button for more than 200 milliseconds, a dash is inserted at the morse string instead of a dot
time_place_dash = 200

# If the user doesn't press the button by 500 milliseconds, a letter break (space) is inserted at the morse string
time_next_letter = 500

# If the user doesn't press the button by 1500 milliseconds, a word break (slash) is inserted at the morse string
time_next_word = 1500

# I will be using the GPIO pin 4 (in BCM mode) to get the digital signal
pin = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    print(morse, morse_to_text(morse))
    
    signal = GPIO.input(pin)
    
    try:
        if signal == 1 and time_press == 0:
                time_press = round(time.time() * 1000)
                time_nopress = 0
        elif signal == 0:
            if time_press > 0:
                if round(time.time() * 1000) - time_press > time_place_dash:
                    morse+= '-'
                else:
                    morse+= '.'

                time_press = 0
                time_nopress = round(time.time() * 1000)
            elif morse[len(morse)-1] != '/' :
                if round(time.time() * 1000) - time_nopress > time_next_word:
                    if morse[len(morse)-1] == ' ':
                        morse = morse[:-1]
                    morse+= '/'
                elif round(time.time() * 1000) - time_nopress > time_next_letter and morse[len(morse)-1] !=  ' ':
                    morse+= ' '
    except:
        continue
