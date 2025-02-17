from colorama import Fore as colour
from random import randint as random
import pyperclip

CharacterNumber = 0
CharacterToNumberKey = {}
NumberToCharacterKey = {}

KeyGenerationList = []
KeyEquivilentList = []
KeyEquivilent = 0

CYAN = colour.CYAN
GREY = colour.LIGHTBLACK_EX
YELLOW = colour.YELLOW
GREEN = colour.GREEN
RED = colour.RED
RESET = colour.RESET
BLUE = colour.BLUE

EncryptedMessageList = []
EncryptedMessage = ""

for c in "`1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>? " :
    CharacterToNumberKey.update({c:CharacterNumber})
    NumberToCharacterKey.update({CharacterNumber:c})
    CharacterNumber += 1

def Encode(Message, Key, Fuzz) :

    PlaceHolder = None
    Loop = False
    KeyEquivilent = 0

    if Key == None :
        for c in range(random(50,400)) :
            KeyGenerationList.append(str(NumberToCharacterKey[random(0,len(NumberToCharacterKey)-1)]))
        Key = "".join(KeyGenerationList)
        print(f"{CYAN}<Key_Generated>{BLUE}[{YELLOW}{Key}{BLUE}]")

    for c in Key :
        KeyEquivilentList.append(CharacterToNumberKey[c])
    for c in KeyEquivilentList :
        KeyEquivilent += c

    for c in Message :
        EncryptedMessageList.append(str(CharacterToNumberKey[c]*KeyEquivilent))
        if Fuzz != None :
            for c in range(random(Fuzz,Fuzz*2)) :
                Loop = True
                while Loop :
                    PlaceHolder = NumberToCharacterKey[random(0,len(NumberToCharacterKey)-1)]
                    try :
                        PlaceHolder = int(PlaceHolder)
                    except ValueError :
                        EncryptedMessageList.append(str(PlaceHolder))
                        Loop = False
    EncryptedMessage = "".join(EncryptedMessageList)
    print(f"{CYAN}<Encrypted_Message>{BLUE}[{GREEN}{EncryptedMessage}{BLUE}]{RESET}")
    pyperclip.copy(EncryptedMessage)
    

def Decode(Message, Key) :
    LetterBuilder = []
    Letters = []
    DecodedLetters = []
    KeyEquivilent = 0

    for c in Key :
        KeyEquivilentList.append(CharacterToNumberKey[c])
    for c in KeyEquivilentList :
        KeyEquivilent += c
    

    for c in Message :
        try :
            c = int(c)
            LetterBuilder.append(str(c))
        except ValueError :
            if "".join(LetterBuilder) != "" :
                Letters.append("".join(LetterBuilder))
                LetterBuilder.clear()
    
    for c in Letters :
        c = int(c)
        DecodedLetters.append(str(NumberToCharacterKey[c/KeyEquivilent]))
    
    Decoded = "".join(DecodedLetters)
    print(f"{CYAN}<Decoded_Message>{BLUE}[{GREEN}{Decoded}{BLUE}]{RESET}")
    pyperclip.copy(Decoded)
    
    
while True :

    ModeOfOperation = input(f"{CYAN}[Mode]\n1-Encode|2-Decode\n{GREY}")

    if ModeOfOperation == 1 or ModeOfOperation == "1" or ModeOfOperation == "Encode" or ModeOfOperation == "encode" :
        ModeOfOperation = "Encode"
    elif ModeOfOperation == 2 or ModeOfOperation == "2" or ModeOfOperation == "Decode" or ModeOfOperation == "decode" :
        ModeOfOperation = "Decode"

    if ModeOfOperation == "Encode" :
        try :
            Message = str(input(f"{CYAN}[Message]{GREY}"))
            
        except ValueError :
            print(f"{RED}!ValueError! : Value assigned null")
            Message = None
        if Message == "" :
            print(f"{RED}!NullSet!")
            print(f"{RED}!Override! : ValueError")
            Message = None

        try:
            Key = str(input(f"{CYAN}[Key]\n(Auto-Generated If Null)\n{GREY}"))
            
        except ValueError :
            print(f"{RED}!ValueError! : Value assigned null")
            Key = None
        if Key == "" :
            print(f"{RED}!NullSet!")
            print(f"{RED}!Override! : Value randomised")
            Key = None

        Fuzz = ""

        try:
            Fuzz = input(f"{CYAN}[Fuzz]\n(Auto-Generated If Null)\n{GREY}")
            Fuzz = int(Fuzz)
            
        except ValueError :
            if Fuzz != "" :
                Fuzz = None
                print(f"{RED}!ValueError!")
        if Fuzz == "" :
            print(f"{RED}!NullSet!")
        if Fuzz == None or Fuzz == "" :
            Fuzz = random(10,500)
            print(f"{RED}!Override! : Value randomised")

        Encode(Message,Key,Fuzz)

    elif ModeOfOperation == "Decode" :
        try :
            Message = str(input(f"{CYAN}[Message]{GREY}"))
            
        except ValueError :
            print(f"{RED}!ValueError! : Value assigned null")
            Message = None

        try:
            Key = str(input(f"{CYAN}[Key]{GREY}"))
            
        except ValueError :
            print(f"{RED}!ValueError! : Value assigned null")
            Key = None
        
        Decode(Message,Key)

    elif ModeOfOperation == "" :
        print(f"{RED}!ValueError! : NullSet")

    else :
        print(f"{RED}!ValidityError!")
    
    ContinueLoop = input(f"{CYAN}[Rerun?]{GREY}")

    if ContinueLoop == "y" or ContinueLoop == "Y" or ContinueLoop == "Yes" or ContinueLoop == "yes" or ContinueLoop == 1 or ContinueLoop == 1 :
        KeyGenerationList = []
        KeyEquivilentList = []
        KeyEquivilent = 0

        CYAN = colour.CYAN
        GREY = colour.LIGHTBLACK_EX
        YELLOW = colour.YELLOW
        GREEN = colour.GREEN
        RED = colour.RED
        RESET = colour.RESET
        BLUE = colour.BLUE

        EncryptedMessageList = []
        EncryptedMessage = ""
    else :
        break

print(f"{RED}-Fin-{RESET}")

while True :
    pass