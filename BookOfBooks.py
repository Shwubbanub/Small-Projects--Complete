from colorama import Fore as col
import os
import keyboard

try :
    OpenFile = open(os.getcwd()+"\\Data\\RefFile","r")
    OpenFile.close()
except FileNotFoundError :
    os.mkdir(os.getcwd()+"\\Data")
    OpenFile = open(os.getcwd()+"\\Data\\RefFile","w")
    OpenFile.write("Reference point for file creation.")
    OpenFile.close()

SimpleChars = []
for c in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_ " :
    SimpleChars.append(c)

def Input(prompt="", existing = None):

    Clear()
    user_input = []
    EditingCharacter = 0
    EditingCharacterModifier = 0
    EditingCharacter = len(user_input)+EditingCharacterModifier-1

    if existing != None :
        for c in existing :
            user_input.append(c)
        user_input.insert(len(user_input),col.MAGENTA+"_")
        print(prompt+"".join(user_input))
    else :
        user_input.insert(EditingCharacter,col.MAGENTA+"_")
        print(prompt, end='', flush=True)

    while True:
        EditingCharacter = len(user_input)+EditingCharacterModifier-1
        event = keyboard.read_event()

        user_input.remove(col.MAGENTA+"_")
        user_input.insert(EditingCharacter,col.MAGENTA+"_")

        if event.event_type == keyboard.KEY_DOWN:
            key = event.name

            if key == "left" and EditingCharacter + EditingCharacterModifier - 1 >= 0-(len(user_input)-1) :
                EditingCharacterModifier -= 1
                EditingCharacter = len(user_input)+EditingCharacterModifier-1
                user_input.remove(col.MAGENTA+"_")
                user_input.insert(EditingCharacter,col.MAGENTA+"_")
                Clear()
                print(prompt+"".join(user_input))

            elif key == "right" and EditingCharacter + EditingCharacterModifier + 1 <= len(user_input)-1 :
                EditingCharacterModifier += 1
                EditingCharacter = len(user_input)+EditingCharacterModifier-1
                user_input.remove(col.MAGENTA+"_")
                user_input.insert(EditingCharacter,col.MAGENTA+"_")
                Clear()
                print(prompt+"".join(user_input))

            elif key == 'enter':
                if (not keyboard.is_pressed("shift")) and (not keyboard.is_pressed("right shift")) :
                    print()
                    break
                else :
                    user_input.insert(EditingCharacter,"\n")
                    Clear()
                    print(prompt+"".join(user_input))

            elif key == 'backspace':
                if EditingCharacter > 0 :
                    user_input.pop(EditingCharacter-1)
                    Clear()
                    print(prompt+"".join(user_input))

            elif len(key) == 1:
                user_input.insert(EditingCharacter,key)
                Clear()
                print(prompt+"".join(user_input))
            elif key == "space" :
                user_input.insert(EditingCharacter," ")
                Clear()
                print(prompt+"".join(user_input))

    if col.MAGENTA+"_" in user_input :
        user_input.remove(col.MAGENTA+"_")
    return ''.join(user_input)

def WaitFor(key,Repeats = 1) :
    for c in range(Repeats) :
        while not keyboard.is_pressed(key) :
            pass
        while keyboard.is_pressed(key) :
                keyboard.read_event()

def Read(FilePath,Line = None) :
    if Line == None :
        OpenFile = open(FilePath,"r")
        ReadData = OpenFile.read()
        OpenFile.close()
        return ReadData
    else :
        OpenFile = open(FilePath,"r")
        try :
            ReadData = str(OpenFile.readlines()[Line])
        except IndexError :
            ReadData = None
        OpenFile.close()
        if ReadData != None :
            ReadData = ReadData.replace("\n","")
        return ReadData

def Write(FilePath,Content,clr = False) :
    if not clr :
        OpenFile = open(FilePath,"r")
        Prefix = OpenFile.read()
        OpenFile.close()

        OpenFile = open(FilePath,"w")
        OpenFile.write(Prefix+Content)
        OpenFile.close
    else :
        OpenFile = open(FilePath,"w")
        OpenFile.write(Content)
        OpenFile.close()

def Clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

Clear()

logo = col.GREEN+"""\n██████╗  ██████╗  ██████╗ ██╗  ██╗ ██████╗ ███████╗██████╗  ██████╗  ██████╗ ██╗  ██╗███████╗   ██████╗ ██╗   ██╗
██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝██╔═══██╗██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝██╔════╝   ██╔══██╗╚██╗ ██╔╝
██████╔╝██║   ██║██║   ██║█████╔╝ ██║   ██║█████╗  ██████╔╝██║   ██║██║   ██║█████╔╝ ███████╗   ██████╔╝ ╚████╔╝ 
██╔══██╗██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔══╝  ██╔══██╗██║   ██║██║   ██║██╔═██╗ ╚════██║   ██╔═══╝   ╚██╔╝  
██████╔╝╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     ██████╔╝╚██████╔╝╚██████╔╝██║  ██╗███████║██╗██║        ██║   
╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚═╝        ╚═╝   """+col.RESET

def Logo() :
    print(logo)

def SelectMenu(Options, Returns, Prefix = "") :
    selected = 0
    loop = True

    while loop :
        Clear()
        print(Prefix)

        for c in Options :
            if c == Options[selected] :
                Col = col.BLUE
            else :
                Col = col.LIGHTBLACK_EX
            print(Col+c)
        print(col.MAGENTA+"\n"+Options[selected])

        key = keyboard.read_key()
        while keyboard.is_pressed(key) :
            keyboard.read_event()
        
        if key != "" :
            if key == "down" :
                if selected+1 < len(Options) :
                    selected += 1
            elif key == "up" :
                if selected-1 >= 0 :
                    selected -= 1
            elif key == "enter" :
                Clear()
                print(Prefix)
                return Returns[selected]

def MainMenu() :
    Clear()
    Logo()

thirdloop = True

while thirdloop :
    MainMenu()
    action = SelectMenu(["[New entry]","[Read entry]","[Edit entry]","[View entries]","[Search entries]","[Exit]"],["new","read","edit","list","search","exit"],logo+"\n")

    if action == "exit" :
        thirdloop = False

    elif action == "new" :
        Title = Input(logo+"\n\n"+col.CYAN+"Title: "+col.YELLOW)
        TitleList = []
        for c in Title :
            if c in SimpleChars :
                TitleList.append(c)
        for c in range(len(TitleList)) :
            if TitleList[c] == " " :
                TitleList[c] = "_"
        ScoredTitle = "".join(TitleList)
        Author = Input(logo+"\n\n"+col.CYAN+"Author: "+col.YELLOW)
        Note = Input(logo+"\n\n"+col.CYAN+"Notes: "+col.YELLOW)
        Write(os.getcwd()+"\\data\\"+ScoredTitle,Title+"\n"+Author+"\n\n"+Note,True)
        WaitFor("enter")

    elif action == "list" :
        BookList = os.listdir(os.getcwd()+"\\data")
        BookList.remove('RefFile')
        BookTitles = []
        for c in BookList :
            try :
                BookTitles.append(str(len(BookTitles)+1)+".["+Read(os.getcwd()+"\\data\\"+c,0)+"]\n"+" "*len(str(len(BookTitles))+".")+"{"+Read(os.getcwd()+"\\data\\"+c,1)+"}")
            except :
                None
        if BookTitles != [] :
            SearchingFor = SelectMenu(BookTitles,BookList,logo+"\n")
            SearchList = []
            for c in SearchingFor :
                if c in SimpleChars :
                    SearchList.append(c)
            for c in range(len(SearchList)) :
                if SearchList[c] == " " :
                    SearchList[c] = "_"
            SearchingFor = "".join(SearchList)
            print("\n"+col.GREEN+Read(os.getcwd()+"\\data\\"+SearchingFor))
            WaitFor("enter")
        else :
            print(col.RED+"No entries")
            WaitFor("enter")
    
    elif action == "read" :
        SearchingFor = Input(logo+"\n\n"+col.CYAN+"Title: "+col.YELLOW)
        SearchList = []
        for c in SearchingFor :
            if c in SimpleChars :
                SearchList.append(c)
        for c in range(len(SearchList)) :
            if SearchList[c] == " " :
                SearchList[c] = "_"
        SearchingFor = "".join(SearchList)
        try :
            print("\n"+col.GREEN+Read(os.getcwd()+"\\data\\"+SearchingFor))
            WaitFor("enter",2)
        except FileNotFoundError :
            print(col.RED+'File "'+SearchingFor+'" does not exist')
            WaitFor("enter",2)
    
    elif action == "edit" :
        BookList = os.listdir(os.getcwd()+"\\data")
        BookList.remove("RefFile")
        BookTitles = []
        for c in BookList :
            try :
                BookTitles.append(str(len(BookTitles)+1)+".["+Read(os.getcwd()+"\\data\\"+c,0)+"]\n"+" "*len(str(len(BookTitles))+".")+"{"+Read(os.getcwd()+"\\data\\"+c,1)+"}")
            except :
                None
        if BookTitles != [] :
            Editing = SelectMenu(BookTitles,BookList,logo+"\n")
            action = SelectMenu(["[Edit]","[Delete]"],["edit","delete"],logo+"\n")
            if action == "delete" :
                action = SelectMenu(["[Confirm delete]","[Cancel delete]"],["confirm","cancel"],logo+"\n")
                if action == "confirm" :
                    os.remove(os.getcwd()+"\\data\\"+Editing)
                    print(col.RED+"Deleted")
                    WaitFor("enter")
                elif action == "cancel" :
                    print(col.RED+"Cancelled")
                    WaitFor("enter")
            elif action == "edit" :
                loop = True
                while loop :
                    Write(os.getcwd()+"\\data\\"+Editing,Input(logo+col.YELLOW+"\n\n",Read(os.getcwd()+"\\data\\"+Editing)),True)
                    WaitFor("enter")
                    action = SelectMenu(["[Done]","[Continue editing]"],["done","continue"],logo+"\n\n"+col.YELLOW+Read(os.getcwd()+"\\data\\"+Editing)+"\n")
                    if action == "done" :
                        loop = False
        else :
            print(col.RED+"No entries")
            WaitFor("enter")
   
    elif action == "search" :
        contents = []
        loop = True

        while loop :
            Clear()
            print(logo+"\n")

            BookList = os.listdir(os.getcwd()+"\\data")
            BookList.remove("RefFile")
            BookTitles = []
            for c in BookList :
                try :
                    if "".join(contents) in str(len(BookTitles)+1)+".["+Read(os.getcwd()+"\\data\\"+c,0)+"]\n"+" "*len(str(len(BookTitles))+".")+"{"+Read(os.getcwd()+"\\data\\"+c,1)+"}" :
                        BookTitles.append(str(len(BookTitles)+1)+".["+Read(os.getcwd()+"\\data\\"+c,0)+"]\n"+" "*len(str(len(BookTitles))+".")+"{"+Read(os.getcwd()+"\\data\\"+c,1)+"}")
                except :
                    None
            if BookList != ["RefFile"] :
                for c in BookTitles :
                    print(col.LIGHTMAGENTA_EX+c)
            else :
                print(col.RED+"No entries")
                loop = False
            
            print(col.YELLOW+"".join(contents)+"_"+"\n")

            key = keyboard.read_event()
            key = key.name
            if key != "right shift" and key != "shift" :
                while keyboard.is_pressed(key) :
                    keyboard.read_event()

            if len(key) == 1 :
                contents.append(key)
            elif key == "space" :
                contents.append(" ")
            elif key == "backspace" :
                contents.pop()
            elif key == "enter" :
                if keyboard.is_pressed("right shift") or keyboard.is_pressed("shift"):
                    contents.append("\n")
                else :
                    loop = False
        
        if BookTitles != [] :
            SearchingFor = SelectMenu(BookTitles,BookList,logo+"\n")
            SearchList = []
            for c in SearchingFor :
                if c in SimpleChars :
                    SearchList.append(c)
            for c in range(len(SearchList)) :
                if SearchList[c] == " " :
                    SearchList[c] = "_"
            SearchingFor = "".join(SearchList)
            print("\n"+col.GREEN+Read(os.getcwd()+"\\data\\"+SearchingFor))
            WaitFor("enter")