#quick note: all ciphers below do follow the rules of their origin, 
#That being said, they cannot be decrypted with anything other than this program 
#What makes these special is it contains charecters, and both capital and lower case
#so any substitution cipher would inherently be using a different alphabet than this one

import random, string, math
#math.ceil(4.2) -> 5
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

def buildBox(message, key):
    box = [[]]
    counter = 0
    for i in range(len(key)):
        box[0].append([])
    for i in range(len(message)):
        column = (i % len(key))
        #print("" + str(counter) + "  " + str(column) + " " + str(message[i]))
        box[counter][column].append(message[i])
        if (column == (len(key)-1)):
            counter += 1
            box.append([])
            for j in range(len(key)):
                box[counter].append([])
    x = len(key) - ((len(message)%len(key)))
    for i in range(x):
        print(i)
        box[counter][len(key)-i-1].append(' ')
    return box

def destroyBox(box, key):#At some point, go back and delete the extra spaces from the message
    message = ''
    for i in range(len(box)):
        for j in box[i]:
            message += str(j)
    weirdMessage = message
    message = ''
    message += weirdMessage[2]
    counter = 0
    for i in range(len(weirdMessage)):
        if i > 1:
            if counter == 5:
                message += weirdMessage[i]
                counter = 0
            counter +=1
    return message

def printBox(box):
    for i in range(len(box)):
        print(box[i])

def columnaryTransferEncrypt():#Shifts everything horizontally 
    pass
    
def mainMethod():
    plainText = "I came, I saw, I conquered!"
    x = buildBox(plainText, "Lemon")
    printBox(x)
    y = destroyBox(x, "lemon")
    print(y)



mainMethod()

