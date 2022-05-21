import random
from sys import exit

ticTacSize = 3

isCPU = False

ticTacArr = [['-']*ticTacSize for _ in range(ticTacSize)]

stragedies = {'random': 'getInputFromCPUBasedOnRandomStragedy',
                'score': 'getInputFromCPUBasedOnScoreStragedy'
            }
currentStragedy = 'score'


def printTicTacFormat():
    index = 0
    print("enter the below index for getting the position")
    for i in range(ticTacSize):
        print()
        for j in range(ticTacSize):
            print(index, end=" ")
            index += 1

def printTicTac():
    print("current game status")
    # print(ticTacArr)

    for i in range(ticTacSize):
        print("\t".join(ticTacArr[i] ))

def isValid(pos):

    i, j = pos//ticTacSize, pos%ticTacSize
    return 0 <= i < ticTacSize and 0 <= j < ticTacSize and ticTacArr[i][j] == '-'

def updateTicTac(pos, sym):
    print(pos)
    if isValid(pos):
        i, j = pos//ticTacSize, pos%ticTacSize
        ticTacArr[i][j] = sym

def gameStatus(noOfConsecutiveSymsToCheck=ticTacSize):
    xSymToCheck = 'X'*noOfConsecutiveSymsToCheck
    oSymToCheck = 'O'*noOfConsecutiveSymsToCheck
    # check rowise
    for i in range(ticTacSize):
        if xSymToCheck in ''.join(ticTacArr[i]):
            return 'X won'

        elif oSymToCheck in ''.join(ticTacArr[i]):
            return 'O won'
    sld = ''
    srd = ''
    # check columwise
    for j in range(ticTacSize):
        s = ''
        sld += ticTacArr[j][j]
        srd += ticTacArr[j][ticTacSize-1-j]
        for i in range(ticTacSize):
            s += ticTacArr[i][j]
        if xSymToCheck in s or xSymToCheck in sld or xSymToCheck in srd:
            return 'X won'

        elif oSymToCheck in s or oSymToCheck in sld or oSymToCheck in srd:
            return 'O won'
    isDraw = True
    for i in range(ticTacSize):
        if '-' in ticTacArr[i]:
            isDraw = False
    return "Match drawn" if isDraw else None


def inputForPlayer(p):
    print("turn of {}, X denotes in the game {}".format(p, p))
    pos = input("enter input for {} : ".format(p))
    try:
        pos = int(pos)

        isValidPos = isValid(pos)
    except:
        isValidPos = False
    
    while not isValidPos:
        print("invalid position, please enter again")
        pos = input("enter input for {} : ".format(p))
        try:
            pos = int(pos)

            isValidPos = isValid(pos)
        except:
            isValidPos = False
    updateTicTac(pos, ticTaxSymbols[p])

    printTicTac()
    status = gameStatus()
    if status: 
        print(gameStatus())
        exit()

def getValidPos():
    valid_pos = []
    for i in range(0,ticTacSize*ticTacSize - 1):
        if isValid(i):
            valid_pos.append(i)
    return valid_pos

def getScoreForPos(pos, sym):
    if not isValid(pos):
        return float('-inf')
    i, j = pos//ticTacSize, pos%ticTacSize
    score = 0    
    if i == ticTacSize//2 or j == ticTacSize//2:
        score += 20
    
    updateTicTac(pos, sym)

    status = gameStatus()
    if not status:
        score += 0
    elif status == sym + ' won':
        score += 100000
    elif ' won' in status:
        score -= 100000
    elif status:
        score += 1000
    


    i, j = pos//ticTacSize, pos%ticTacSize
    ticTacArr[i][j] = '-'

    return score



def getRandomPos():
    # print(getValidPos(), random.choice(getValidPos()))
    return random.choice(getValidPos())

def getPosBasedOnScoreStragedy(p):
    validPoss = getValidPos()
    sym = ticTaxSymbols[p]
    bestPos = validPoss[0]
    bestScore = 0
    for pos in validPoss:
        score = getScoreForPos(pos, sym)
        print("score", pos, score, sym)
        if score > bestScore:
            bestPos = pos
            bestScore = score
    return bestPos

def getInputFromCPUBasedOnScoreStragedy(p):
    pos = getPosBasedOnScoreStragedy(p)
    updatePosForPerson(pos, p)

def getInputFromCPUBasedOnRandomStragedy(p):
    pos = getRandomPos()
    print(pos)
    updatePosForPerson(pos, p)

def updatePosForPerson(pos, p):
    print("input by {} is {}".format(p, pos))
    updateTicTac(pos, ticTaxSymbols[p])

    printTicTac()
    status = gameStatus()
    if status: 
        print(gameStatus())
        exit()

p1 = input("enter name of p1:")
isCPU = input("do you want to play against Computer enter y / n")
isCPU = (isCPU == 'y')
if isCPU:
    p2 = 'cpu'
else:
    p2 = input("enter name of p2:")

ticTaxSymbols = {'X': p1, 'O': p2, p1: 'X', p2: 'O'}

should_exit = input("enter n to exit, anything else to continue the game")

while (should_exit != 'n'):
    printTicTacFormat()

    printTicTac()
    inputForPlayer(p1)
    if isCPU:
        stragedyFunc = stragedies[currentStragedy]
        print("current stragedy for CPU : {}".format(currentStragedy) )
        # eval(stragedyFunc +'("{}")'.format(p2))
        globals()[stragedyFunc](p2)
    else:
        inputForPlayer(p2)
    


    should_exit = input("enter n to exit, anything else to continue the game")


exit()

