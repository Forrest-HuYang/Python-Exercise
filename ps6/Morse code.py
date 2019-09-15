Morse_code = {  'A': '.-',
                'B': '-...',   
                'C': '-.-.',
                'D': '-..',    
                'E': '.',      
                'F': '..-.',
                'G': '--.',    
                'H': '....',   
                'I': '..',
                'J': '.---',   
                'K': '-.-',    
                'L': '.-..',
                'M': '--',   
                'N': '-.',     
                'O': '---',
                'P': '.--.',   
                'Q': '--.-',   
                'R': '.-.', 
                'S': '...',    
                'T': '-',      
                'U': '..-',
                'V': '...-',   
                'W': '.--',    
                'X': '-..-',
                'Y': '-.--',   
                'Z': '--..',
                '0': '-----',  
                '1': '.----',  
                '2': '..---',
                '3': '...--',  
                '4': '....-',  
                '5': '.....',
                '6': '-....',  
                '7': '--...',  
                '8': '---..',
                '9': '----.'}
Morse_decode = {'.-': 'A',
                '-...': 'B',   
                '-.-.': 'C',
                '-..': 'D',    
                '.': 'E',      
                '..-.': 'F',
                '--.': 'G',    
                '....': 'H',   
                '..': 'I',
                '.---': 'J',   
                '-.-': 'K',    
                '.-..': 'L',
                '--': 'M',   
                '-.': 'N',     
                '---': '0',
                '.--.': 'P',   
                '--.-': 'Q',   
                '.-.': 'R', 
                '...': 'S',    
                '-': 'T',      
                '..-': 'U',
                '...-': 'V',   
                '.--': 'W',    
                '-..-': 'X',
                '-.--': 'Y',   
                '--..': 'Z',
                '-----': '0',  
                '.----': '1',  
                '..---': '2',
                '...--': '3',  
                '....-': '4',  
                '.....': '5',
                '-....': '6',  
                '--...': '7',  
                '---..': '8',
                '----.': '9'}

def decode():
    msg = input('Message:')
    msg = msg.split(' ')
    output = []
    for letter in msg:
        if letter in '(!@#$%^&*()_+={}[]|\:;<>?,/\)':
            output.append(letter)
        elif letter == ' ' or letter == '  ' or letter == '' or letter == '   ' or letter == '    ':
            output.append(' ')
        else:
            output.append(Morse_decode[letter])
    output = ''.join(output)
    return output

def convert():
    msg = input('Message:')
    output = []
    for letter in msg:
        if letter.isalpha() or letter.isalnum():
            output.append(Morse_code[letter.upper()])
        elif letter == ' ':
            output.append('  ')
        else:
            output.append(letter)
        output.append(' ')
    output = ''.join(output)
    return output

print (convert())
print (decode())

