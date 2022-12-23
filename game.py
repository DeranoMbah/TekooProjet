from functions import *
from alpha_beta import *
from variables import *

def start_with_AI():
    global debut
    global globalboard

    #debut du jeu: pose de 4 premiers pions
    if (debut==1):
        for i in range(1,5):
            print("jeu ", i)
            currentPlayer = machinePlayer
            globalboard= deepcopy(computerset(globalboard,i))
            currentPlayer = humanPlayer
            posi = playerInput()
            insertValue(globalboard,currentPlayer, posi)
            #i=i+1

        debut = 0
        
    #fin pose de 4 premiers pions  
    currentPlayer = machinePlayer
    globalboard = deepcopy(computerMove(globalboard))
    if checkWin(globalboard):
        printBoard(globalboard)
        print(currentPlayer + " a gagne!")
        exit()
    currentPlayer = humanPlayer
    printBoard(globalboard)
    globalboard = playerMove(currentPlayer, globalboard)
    if checkWin(globalboard):
        printBoard(globalboard)
        print(currentPlayer + " a gagne!")
        exit()


def start_with_human():
    global debut, globalboard
 

    #debut du jeu: pose de 4 premiers pions
    if (debut==1):
        for i in range(1,5):
            currentPlayer = humanPlayer
            posi = playerInput()
            insertValue(globalboard,currentPlayer, posi)
            currentPlayer = machinePlayer
            globalboard= deepcopy(computerset(globalboard,i))
            #i=i+1
        debut = 0
        
    #fin pose de 4 premiers pions
    currentPlayer = humanPlayer
    globalboard = playerMove(currentPlayer, globalboard)
    if checkWin(globalboard):
        printBoard(globalboard)
        print(currentPlayer + " a gagne!")
        exit()
    currentPlayer = machinePlayer
    globalboard = deepcopy(computerMove(globalboard))
    printBoard(globalboard)

    if checkWin(globalboard):
        printBoard(globalboard)
        print(currentPlayer + " a gagne!")
        exit()


def one_on_one():

    global globalboard

    player_1 = 'X'
    player_2 = 'Y'
    
    global debut
    while 1:

        
        if debut == 1:
            for i in range (1,5):
                currentPlayer = player_1
                pos = playerInput()
                insertValue(globalboard, currentPlayer, pos)
                currentPlayer = player_2
                pos = playerInput()
                insertValue(globalboard, currentPlayer, pos)
            debut = 0
        

        currentPlayer = player_1
        playerMove(currentPlayer, globalboard)
        printBoard(globalboard)
        if checkWin(globalboard):
            print("WINNER: " + currentPlayer + "!")
            exit(0)
        currentPlayer = player_2
        playerMove(currentPlayer, globalboard)
        printBoard(globalboard)
        if checkWin(globalboard):
            print("WINNER: " + currentPlayer + "!")
            exit(0)
