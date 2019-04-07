morse_dict = {'.-':     'A',
                 '-...':   'B',
                 '-.-.':   'C',
                 '-..':    'D',
                 '.':      'E',
                 '..-.':   'F',
                 '--.':    'G',
                 '....':   'H',
                 '..':     'I',
                 '.---':  'J',
                 '-.-':    'K',
                 '.-..':   'L',
                 '--':     'M',
                 '-.':     'N',
                 '---':    'O',
                 '.--.':   'P',
                 '--.-':   'Q',
                 '.-.':    'R',
                 '...':    'S',
                 '-':      'T',
                 '..-':     'U',
                 '...-':   'V',
                 '.--':    'W',
                 '-..-':   'X',
                 '-.--':   'Y',
                 '--..':   'Z',
                 '.----':  '1',
                 '..---':  '2',
                 '...--':  '3',
                 '....-':  '4',
                 '.....':  '5',
                 '-....':  '6',
                 '--...':  '7',
                 '---..':  '8',
                 '----.':  '9',
                 '-----':  '0',
                 '--..--': ', ',
                 '.-.-.-': '.',
                 '..--..': '?',
                 '-..-.':  '/',
                 '-....-': '-',
                 '-.--.':  '(',
                 '-.--.-': ')'}

def morse_to_text(morse): 
    words = morse.split('/')
    string = ''
    for i in range(0, len(words)):
        letters = words[i].split(' ')
        for j in range(0, len(letters)):
            string+= morse_dict.get(letters[j], '')
        if len(string) > 0 and string[len(string)-1] != ' ':
            string+= ' '
    return string;
