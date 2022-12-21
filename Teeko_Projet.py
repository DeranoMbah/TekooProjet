from binascii import a2b_qp
from copy import deepcopy
from json.encoder import INFINITY
import os
import random
from site import ENABLE_USER_SITE


from variables import *
from functions import *
from alpha_beta import *


   

'''board ={1:' ',2:' ',3:' ',4:' ',5:' ',
        6:' ',7:'B',8:'B',9:' ',10:' ',
        11:'B',12:'N',13:'N',14:'B',15:' ',
        16:' ',17:' ',18:' ',19:' ',20:' ',
        21:'N',22:' ',23:' ',24:'N',25:' '}'''



starter = int(input("Desirer vous etre le premier a jouer: 1. oui   -   2. non"))


while not checkWin(board):
       # Chargement de Coin ou jeuton de jeux par les joeurs
    
    #IA BEGIN
    if starter == 2:
        currentPlayer = humanPlayer

        #debut du jeu: pose de 4 premiers pions
        if (debut==1):
            for i in range(1,5):
                computerset(board,i)
                posi = playerInput()
                insertValue(currentPlayer, posi)
                
                i=i+1
            debut = 0
            
        #fin pose de 4 premiers pions

        printBoard(board)   
        
        currentPlayer = machinePlayer
        computerMove()
        if checkWin(board):
            printBoard(board)
            print(currentPlayer + " a gagne!")
            exit()
        currentPlayer = humanPlayer
        printBoard(board)
        playerMove()
        if checkWin(board):
            printBoard(board)
            print(currentPlayer + " a gagne!")
            exit()

    #PLAYER BEGIN
    else:

        currentPlayer = humanPlayer

        #debut du jeu: pose de 4 premiers pions
        if (debut==1):
            for i in range(1,5):
                posi = playerInput()
                insertValue(currentPlayer, posi)
                computerset(board,i)
                i=i+1
            debut = 0
            
        #fin pose de 4 premiers pions

        printBoard(board)   
        playerMove()
        if checkWin(board):
            printBoard(board)
            print(currentPlayer + " a gagne!")
            exit()
        currentPlayer = machinePlayer
        computerMove()
        printBoard(board)

        if checkWin(board):
            printBoard(board)
            print(currentPlayer + " a gagne!")
            exit()




      