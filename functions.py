from variables import *

# Printing de Borad Games

def printBoard(board):
        print(board[1]+ "|" + board[2]+ "|"+ board[3] + "|" + board[4] + "|" +board[5] )
        print("-+-+-+-+-")
        print(board[6]+ "|" + board[7]+ "|"+ board[8] + "|" + board[9] + "|" +board[10] )
        print("-+-+-+-+-")
        print(board[11]+ "|" + board[12]+ "|"+ board[13] + "|" + board[14] + "|" +board[15])
        print("-+-+-+-+-")
        print(board[16]+ "|" + board[17]+ "|"+ board[18] + "|" + board[19] + "|" +board[20])
        print("-+-+-+-+-")
        print(board[21]+ "|" + board[22]+ "|"+ board[23] + "|" + board[24] + "|" +board[25])
        print("\n")


        # Space IS FREE
def espaceFree(position, localboard):
    if localboard[position]==' ':
        return True
    else:
        return False

#       Player Input
def playerInput():

    valid_input = False
    while (not valid_input):
        try:
            while(not valid_input):
                posi=int(input("entrez position B: "))
                if(posi < 1 or posi > 25):
                    print("position invalide, veuillez resaisir la position")
                else:
                    break
        except ValueError as err:
            print("entree invalide, veuillez resaisir la position")
        else:
            return posi
        

#Take player input
def insertValue(localboard, player, position):
    while not espaceFree(position, localboard):
        print("position occupee, veuillez resaisir position: ")
        position = playerInput()
    localboard[position]= player
    printBoard(localboard)
    if checkWin(localboard)== True:
        print(player + " gagne")
        exit()

#Check win    
def checkWin(board):

    def horizontalCheck(board):
        test=False
        for i in [1,2,6,7,11,12,16,17,21,22]:
            if ( board[i] == board[i+1] and board[i] == board[i+2] and board[i] == board[i+3] and board[i] != ' '):
                test= True
        
        for i in [4,5,9,10,14,15,19,20,24,25]:
            if ( board[i] == board[i-1] and board[i] == board[i-2] and board[i] == board[i-3] and board[i] != ' '):
                test= True
       

        return test

    def verticalCheck(board):
        test=False
        for i in range(1,11):
            if ( board[i] == board[i+5] and board[i] == board[i+10] and board[i] == board[i+15] and board[i] != ' '):
                test= True
        
        for i in range(16,26):
            if ( board[i] == board[i-5] and board[i] == board[i-10] and board[i] == board[i-15] and board[i] != ' '):
                test= True
       

        return test

    def crossCheck(board):
        test=False
        for i in [1,2,6]:
            if ( board[i] == board[i+6] and board[i] == board[i+12] and board[i] == board[i+18] and board[i] != ' '):
                test= True

        for i in [24,25,20]:
            if ( board[i] == board[i-6] and board[i] == board[i-12] and board[i] == board[i-18] and board[i] != ' '):
                test= True
        
        for i in [4,5,10]:
            if ( board[i] == board[i+4] and board[i] == board[i+8] and board[i] == board[i+12] and board[i] != ' '):
                test= True

        for i in [16,21,22]:
            if ( board[i] == board[i-4] and board[i] == board[i-8] and board[i] == board[i-12] and board[i] != ' '):
                test= True

        return test

    def rectangleCheck(board):
        test=False
        for i in range(1,5):
            if ( board[i] == board[i+1] and board[i] == board[i+5] and board[i] == board[i+6] and board[i] != ' '):
                test= True

        for i in range(6,10):
            if ( board[i] == board[i+1] and board[i] == board[i+5] and board[i] == board[i+6] and board[i] != ' '):
                test= True

        for i in range(11,15):
            if ( board[i] == board[i+1] and board[i] == board[i+5] and board[i] == board[i+6] and board[i] != ' '):
                test= True

        for i in range(16,20):
            if ( board[i] == board[i+1] and board[i] == board[i+5] and board[i] == board[i+6] and board[i] != ' '):
                test= True


        return test


    if(horizontalCheck(board)==True or verticalCheck(board)==True or crossCheck(board)== True or rectangleCheck(board)):
        return True


#fonction Player Movement
def playerMove(currentPlayer, localboard):


    while(1):
        print("Selectionner le pion a deplacer")
        exPosition = playerInput()
        while(localboard[exPosition] is not currentPlayer):
            print("cette case est vide ou ce jeton ne vous appartiens pas: ")
            exPosition = playerInput()


        keyboard_input = input("Bouger B vers: ")
        keyboard_input = keyboard_input.upper()

        if keyboard_input == 'D': #droit
            newPosition = exPosition + 1
            if not bord_droit(exPosition) and espaceFree(newPosition, localboard):
                localboard[newPosition] = currentPlayer
                break

        elif keyboard_input == 'G': #gauche
            newPosition = exPosition -1
            if not bord_gauche(exPosition) and espaceFree(newPosition, localboard):
                localboard[newPosition] = currentPlayer
                break
        
        elif keyboard_input == 'H': #haut
            newPosition = exPosition - 5
            if not bord_haut(exPosition) and espaceFree(newPosition, localboard):
                localboard[newPosition] = currentPlayer
                break

        elif keyboard_input == 'B': #bas
            newPosition = exPosition + 5
            if not bord_bas(exPosition) and espaceFree(newPosition, localboard):
                localboard[newPosition] = currentPlayer
                break

        elif keyboard_input == 'Q': #cross up left
            newPosition = exPosition - 6
            if not bord_haut(exPosition) and not bord_gauche(exPosition) and espaceFree(newPosition, localboard):
                localboard[newPosition] = currentPlayer
                break

        elif keyboard_input == 'E': #cross up right
            newPosition = exPosition -4
            if not bord_haut(exPosition) and not bord_droit(exPosition) and espaceFree(newPosition, localboard):
                localboard[newPosition] = currentPlayer
                break

        elif keyboard_input == 'Z': #cross down left
            newPosition = exPosition + 4
            if not bord_bas(exPosition) and not bord_gauche(exPosition) and espaceFree(newPosition, localboard):
                localboard[newPosition] = currentPlayer
                break
        
        elif keyboard_input == 'X': #cross down right
            newPosition = exPosition + 6
            if not bord_bas(exPosition) and not bord_droit(exPosition) and espaceFree(newPosition, localboard):
                localboard[newPosition] = currentPlayer
                break

        else:
            print("mouvement invalide")
    
    localboard[exPosition] = ' '
    return localboard



#pion sur le bord haut
def bord_haut(position):
    if position - 5 < 1:
        return True
    return False

#pion sur le bord bas
def bord_bas(position):
    if position + 5 > 25:
        return True
    return False

#pion sur le bord gauche
def bord_gauche(position):
    if position % 5 == 1:
        return True
    return False

#pion sur le bord droit
def bord_droit(position):
    if position % 5 == 0:
        return True
    return False

