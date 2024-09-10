import os

#define variables
command = ""
splitCommand = []
filePath = os.getcwd()
displayedUserEnvironment = ""
fileReference = ""

#we will use this to generate a bunch of commands just below the constructor
#dont need to global these as they should never be edited as that would fuck the syntax
class OOPcommand:
    def __init__(cmd, name, arguments):
        cmd.name = name
        cmd.arguments = arguments

#defining commands as a class for organising purposes, this could never go wrong... right?
echo = OOPcommand("echo", 2)
quit = OOPcommand("quit", 1)
make = OOPcommand("make", 2)
cat = OOPcommand("cat", 2)

# keep these handy
#
# global command
# global splitCommand

#this takes the command input
def getCommand():
    global command
    global splitCommand
    global filePath
    global displayedUserEnvironment
    global fileReference

    #this generates the bit at the front which you expect from a terminal (working directory)
    displayedUserEnvironment = "PyShell [" + filePath + "]$: "

    #this displays the last bit of code and gets the input of the user
    command = input(displayedUserEnvironment)

#splits the input, now we can look at it bit by bit
def parse():
    global command
    global splitCommand
    global fileReference

    #split commmand string into list
    splitCommand = command.split()

    #get the 2nd arg and make a fileReference for make/cat commands so we can navigate directories :D
    try:
        fileReference = filePath + splitCommand[1]
    except IndexError:
        fileReference = filePath

#this command will let you print text!
#its a bit fucking useless, but will be better when i add the scripting feature (linebyline)
def echoCMD():
    global command
    global splitCommand

    #validity check
    if len(splitCommand) < echo.arguments:
        print("Syntax Error: command \"echo\" must take 1 argument (output)")
        return 1

    #if its valid we can run it
    splitCommand.pop(0)
    shellOut = " ".join(splitCommand)
    print(shellOut)
    return 0

#this is a bit fucking obvious, no?
def quitCMD():
    exit()

#this will make a file
def makeCMD():
    if len(splitCommand) < make.arguments:
        print("Syntax Error: command \"make\" must take 1 argument (filename)")
        return 1
    
    #if its valid we make the file ig
    f = open(splitCommand[1], "w")
    f.close()

#dump file contents, this doesnt have any security so we pray to god it doesnt fuck up
def catCMD():
    if len(splitCommand) < cat.arguments:
        print("Syntax Error: command \"cat\" must take 1 argument (filename)")
        return 1
    
    f = open(splitCommand[1], "r")
    print(f.read())
    f.close()

#we will use this to call a function depending on the command
def interpret():
    global command
    global splitCommand

    if splitCommand[0] == echo.name:
        echoCMD()

    elif splitCommand[0] == quit.name:
        quitCMD()

    elif splitCommand[0] == make.name:
        makeCMD()

    elif splitCommand[0] == cat.name:
        catCMD()

    else:
        print("Command not recognised.")

def shellLoop():
    getCommand()
    parse()
    interpret()

while True:
    shellLoop()