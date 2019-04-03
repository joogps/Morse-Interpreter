# https://www.geeksforgeeks.org/morse-code-translator-python/
# https://www.geeksforgeeks.org/python-program-to-swap-keys-and-values-in-dictionary/

morse = ''

time_press = 0
time_space = 0

time_treshold = 100

morse_to_text = {'.-':     ['A'],
                 '-...':   ['B'],
                 '-.-.':   ['C'],
                 '-..':    ['D'],
                 '.':      ['E'],
                 '..-.':   ['F'],
                 '--.':    ['G'],
                 '....':   ['H'],
                 '..':     ['I'],
                 '.---':   ['J'],
                 '-.-':    ['K'],
                 '.-..':   ['L'],
                 '--':     ['M'],
                 '-.':     ['N'],
                 '---':    ['O'],
                 '.--.':   ['P'],
                 '--.-':   ['Q'],
                 '.-.':    ['R'],
                 '...':    ['S'],
                 '-':      ['T'],
                 '..-':    ['U'],
                 '...-':   ['V'],
                 '.--':    ['W'],
                 '-..-':   ['X'],
                 '-.--':   ['Y'],
                 '--..':   ['Z'],
                 '.----':  ['1'],
                 '..---':  ['2'],
                 '...--':  ['3'],
                 '....-':  ['4'],
                 '.....':  ['5'],
                 '-....':  ['6'],
                 '--...':  ['7'],
                 '---..':  ['8'],
                 '----.':  ['9'],
                 '-----':  ['0'],
                 '--..--': [', '],
                 '.-.-.-': ['.'],
                 '..--..': ['?'],
                 '-..-.':  ['/'],
                 '-....-': ['-'],
                 '-.--.':  ['('],
                 '-.--.-': [')']}

import time
import random

while True:
    state = 1 # here's your input. define it using whathever you want. 1 = on, 0 = off
    
    try:
        if state == 1 & time_press == 0:
                if int(round(time.time() * 1000)) - time_space > time_treshold:
                    morse+= '/'
                else:
                    morse+= ' '
                    
                time_press = int(round(time.time() * 1000))
        else:
            if time_press > 0:
                if int(round(time.time() * 1000)) - time_press > time_treshold:
                    morse+= '-'
                else:
                    morse+= '.'

                time_press = 0
    except:
        continue


