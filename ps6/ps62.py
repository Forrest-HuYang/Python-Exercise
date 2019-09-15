import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    valid
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a    object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        '''A = string.ascii_uppercase
        B = string.ascii_lowercase
        upperdict = []
        lowerdict = []
        for i in range (26):
            upperdict.append(A[i])
            lowerdict.append(B[i])

        msg = list(self.message_text)
        for i in range(len(msg)):
           
            if msg[i].isalpha() :
                if lowerdict.index(msg[i].lower()) + 1 > shift:
                    msg[i] = chr( ord(msg[i]) - shift )
                elif lowerdict.index(msg[i].lower()) + 1 <= shift:
                    msg[i] = chr( ord(msg[i]) + 26 - shift )'''
        msg = list(self.message_text)
        for i in range(len(msg)):
            if msg[i].isalpha() :
                if  msg[i].islower():
                    msg[i] = chr( ( ord(msg[i])-ord('a') + 26 - shift ) % 26 + ord('a') )
                else :
                    msg[i] = chr( ( ord(msg[i])-ord('A') + 26 - shift ) % 26 + ord('A') )


        shit = ''.join(msg)  
        return shit

    def code_message(self,shift):
        msg = list(self.message_text)
        for i in range(len(msg)):
            if msg[i].isalpha() :
                if  msg[i].islower():
                    msg[i] = chr( ( ord(msg[i])-ord('a') + shift ) % 26 + ord('a') )
                else :
                    msg[i] = chr( ( ord(msg[i])-ord('A') + shift ) % 26 + ord('A') )
        msg = ''.join(msg)
        return msg

    def get_shift(self):
        m = 0
        shiftss = 0
        
        for i in range(26):
            ss = self.apply_shift(i)
            msg = ss.split(' ')
            valid_words = 0

            for word in range(len(msg)):
                if msg[word] in self.valid_words:
                    valid_words += 1
                    

            if valid_words >= m:
                m = valid_words
                shiftss = i
        return self.apply_shift(shiftss)


        


msg = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj'
a = Message(msg)
print(a.get_shift())

#print('the code is ',a.get_shift())