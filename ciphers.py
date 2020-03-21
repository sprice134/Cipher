import random, string
def randomAlphabet(incomingList):#Creates a randomized alphabet any time I need
    for i in range(26):
        tempLocation = random.randint(0,25)
        tempLetter = incomingList[tempLocation]
        incomingList[tempLocation] = incomingList[i]
        incomingList[i] = tempLetter
    return incomingList

def handleMessage(message):
    alphabet = getAlphabet()
    for i in range(len(message)):
        if (message[i] not in (alphabet)):
            message = message.replace(message[i], " ")  
    return message

def getAlphabet():
    letterAlphabet = list(string.ascii_uppercase)#Creates alphabet
    LetterAlphabet = list(string.ascii_lowercase)
    additionalCharecters = ['!','"'," ",',','#','.', "'"]
    for i in range(0,10):
        additionalCharecters.append(str(i))
    alphabet = [*LetterAlphabet, *letterAlphabet, *additionalCharecters]
    return alphabet

def getAtBashAlphabet():
    alphabet = getAlphabet()
    convertedAlphabet = []
    for i in range(len(alphabet)):
        convertedAlphabet.append(alphabet[-i-1])
    return convertedAlphabet
def getCaesarAlphabet(shifts):
    alphabet = getAlphabet()
    if shifts > 0:
        newAlphabet = alphabet
        for i in range(shifts):
            movingLetter = newAlphabet[0]
            newAlphabet = newAlphabet[1:]
            newAlphabet.append(movingLetter)
    return newAlphabet

def caesarEncrypt(message, shifts):
    convertedAlphabet = getCaesarAlphabet(shifts)
    alphabet = getAlphabet()
    newText = ''
    for i in range(len(message)):
        newText += convertedAlphabet[alphabet.index(message[i])]
    return newText

def caesarDecrypt(message, shifts):#alphabet is organized, string is what you want decrypted, shifts is rotations on caeser cipher used
    convertedAlphabet = getCaesarAlphabet(shifts)
    alphabet = getAlphabet()
    newText = ''
    for i in range(len(message)):
        newText += alphabet[convertedAlphabet.index(message[i])]
    return newText

def atBashEncrypt(message):
    alphabet = getAlphabet()
    convertedAlphabet = getAtBashAlphabet()
    newText = ''
    for i in range(len(message)):
        newText += alphabet[convertedAlphabet.index(message[i])]
    return newText

def atBashDecrypt(message):
    alphabet = getAlphabet()
    convertedAlphabet = getAtBashAlphabet()
    newText = ""
    for i in range(len(message)):
        newText += convertedAlphabet[alphabet.index(message[i])]
    return newText
    
def caesarAtBashEncrypt(plainText):
    message = handleMessage(plainText)
    encryptedMessage = caesarEncrypt(atBashEncrypt(caesarEncrypt(message, len(message))), (len(message)*2))
    return encryptedMessage

def caesarAtBashDecrypt(encryptedText):
    message = caesarDecrypt(atBashDecrypt(caesarDecrypt(encryptedText, (len(encryptedText)*2))), len(encryptedText))
    return message

def boxShiftUpEncrypt(message, key):
    box = []
    counter = 0
    for i in range(len(key)):
        box.append([])
    for i in range(len(message)):
        pass
    return box
    
def mainMethod():
    plainText = "I came, I saw, I conquered!"
    e = caesarAtBashEncrypt(plainText)
    e1 = caesarAtBashDecrypt(e)
    print(plainText)
    print(e)
    print(e1)
    print(boxShiftUpEncrypt("hello", "pie"))




mainMethod()

