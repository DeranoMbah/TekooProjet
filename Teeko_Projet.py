from binascii import a2b_qp
from copy import deepcopy
from json.encoder import INFINITY
import os
from site import ENABLE_USER_SITE



board ={1:' ',2:' ',3:' ',4:' ',5:' ',
        6:' ',7:' ',8:' ',9:' ',10:' ',
        11:' ',12:' ',13:' ',14:' ',15:' ',
        16:' ',17:' ',18:' ',19:' ',20:' ',
        21:' ',22:' ',23:' ',24:' ',25:' '}

currentPlayer ='B'
machinePlayer='N'
debut=1


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
def espaceFree(position):
    if board[position]==' ':
        return True
    else:
        return False


#Take player input
def insertValue(color, position):
    if espaceFree(position):
        board[position]= color
        printBoard(board)
        if checkWin(board)== True:
           print(color,"gaggne")
           exit()
        return
    else:
        print("Position Invalide")
        position= int(input("entrez une nouvelle position"))
        insertValue(color, position)
        return


#Check for the Win
    
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





#Right Move
def rightMove(exPosition):
    if (exPosition<5 and exPosition>=1):
        return exPosition+1
    elif(exPosition<10 and exPosition>=6):
        return exPosition+1
    elif (exPosition<15 and exPosition>=11):
        return exPosition+1
    elif(exPosition<20 and exPosition>=16 ):
        return exPosition+1
    elif(exPosition<25 and exPosition>=21 ):
        return exPosition+1
    else:
        return False


    
#Left Move
def leftMove(exPosition):
   if (exPosition>1 and exPosition<=5):
            return exPosition-1
   elif(exPosition>6 and exPosition<=10):
            return exPosition-1
   elif (exPosition>11 and exPosition<=15):
            return exPosition-1
   elif(exPosition>16 and exPosition<=20):
            return exPosition-1
   elif(exPosition>21 and exPosition<=25):
            return exPosition-1
   else:
            return False


#Up Move
def upMove(exPosition):
   if (exPosition>5 and exPosition<=25 ):
            return exPosition-5
   else:
            return False


#Down Move
def downMove(exPosition):
   if (exPosition>=1 and exPosition<=20):
            return exPosition+5
   else:
            return False


#crossUP
def crossUpright(exPosition):
    haut=upMove(exPosition)
    if(haut != False):
        return rightMove(haut)
    else:
        return False

def crossUpleft(exPosition):
    haut=upMove(exPosition)
    if(haut != False):
        return leftMove(haut)
    else:
        return False

#crossDown

def crossDownright(exPosition):
    haut=downMove(exPosition)
    if(haut != False):
        return rightMove(haut)
    else:
        return False

def crossDownleft(exPosition):
    haut=downMove(exPosition)
    if(haut != False):
        return leftMove(haut)
    else:
        return False

#General Mouvement
def Movement(exPosition, newPosition):
     if(leftMove(exPosition)==newPosition):
            board[exPosition]=' '
            insertValue(currentPlayer,newPosition)
            print("Movement gauche")
     elif(rightMove(exPosition)== newPosition):
            board[exPosition]=' '
            print("Movement droit")
            insertValue(currentPlayer,newPosition)
     elif(upMove(exPosition)== newPosition):
            board[exPosition]=' '
            print("Movement Haut")
            insertValue(currentPlayer,newPosition)
     elif(downMove(exPosition)== newPosition):
            board[exPosition]=' '
            print("Movement bas")
            insertValue(currentPlayer,newPosition)
     elif(crossUpright(exPosition)==newPosition):
             board[exPosition]=' '
             print("Movement bas")
             insertValue(currentPlayer,newPosition)
     elif(crossUpleft(exPosition)==newPosition):
         board[exPosition]=' '   
         print("Movement bas")
         insertValue(currentPlayer,newPosition)
     elif(crossDownright(exPosition)==newPosition):
         board[exPosition]=' '    
         print("Movement bas")
         insertValue(currentPlayer,newPosition)
     elif(crossDownleft(exPosition)==newPosition):
         board[exPosition]=' '
         print("Movement bas")
         insertValue(currentPlayer,newPosition)
     else:
         print("deplacement pas possible ")

#Player Movemement
def playerMove():
    exPosition= int(input("Position du point a deplacer B"))
    newPosition = int(input("entrez la position ou aller B "))
    if(board[exPosition]==currentPlayer):
       Movement(exPosition, newPosition)
    else:
        print("cette case est vide ou ce jeton ne vous appartiens pas")
        playerMove()


#Computer Movement

#DEFINITION ALPHA BETA
def AlphaBeta(board):
   
    profondeurtest = 4
    localboard= deepcopy(board)
    
    
            #DEFINITION DU MAXVALUEA
    def MaxValue(localboard,profondeur, alpha,beta,bestscore):
         global board
         if(checkWin(localboard)==True or profondeur==0):
                return(eval(localboard))

         resultat= - INFINITY
         nextplay= nextBoardList(localboard,'N')
         
         for i in nextplay:
             
             resultat=max(resultat,MinValue(deepcopy(i),profondeur-1,alpha,beta,bestscore))
             if(resultat>=beta): 
                 return resultat

             alpha=max(alpha, resultat)

             if(resultat>bestscore and profondeurtest==profondeur):
                 board=deepcopy(i)
                 bestscore=resultat

             print(bestscore)

         return resultat
    
        #DEFINITION DU MINVALUE
    def MinValue(localboard,profondeur, alpha,beta,bestscore):
        if(checkWin(localboard)==True or profondeur==0):
             return(eval(localboard))

        resultat= + INFINITY
        nextplay= nextBoardList(localboard,'B')
        

        for i in nextplay:
            resultat=min(resultat,MaxValue(deepcopy(i),profondeur-1,alpha,beta,bestscore))
            if(resultat<=alpha):
                return resultat

            beta=min(beta, resultat)

            return resultat

    MaxValue(localboard, profondeurtest, -INFINITY, +INFINITY,-INFINITY)

    





#Definition de la fonction D'evaluation
def eval(board):
    
    scoreboard={1:1,2:8,3:5,4:8,5:1,
                6:8,7:10,8:10,9:10,10:8,
                11:5,12:10,13:20,14:10,15:5,
                16:8,17:10,18:10,19:10,20:8,
                21:1,22:8,23:5,24:8,25:1}

    
    def nombreMovement(localboard,Player):
        i=0;

        for j in range(1,26):
            if (localboard[j]==Player):

                if(crossUpright(j)!=False):
                    if( board[crossUpright(j)]==' '):
                        i=i+1

                if(crossUpleft(j)!=False):
                    if( board[crossUpleft(j)]==' '):
                        i=i+1

                if(crossDownright(j)!=False):
                    if( board[crossDownright(j)]==' '):
                        i=i+1

                if(crossDownleft(j)!=False):
                     if( board[crossDownleft(j)]==' '):
                        i=i+1
            
                if(upMove(j)!=False):
                    if( board[upMove(j)]==' '): 
                        i=i+1
                    
            
                if(downMove(j)!=False):
                    if( localboard[downMove(j)]==' '):
                        i=i+1
                   
                    
                if(rightMove(j)!=False):
                    if( board[rightMove(j)]==' '):
                        i=i+1

                if(leftMove(j)!=False):
                    if( board[leftMove(j)]==' '):
                        i=i+1  

        return i


    def ScoreBoard(localboard):
        scoreOrdinateur=0; scoreJoeur=0; 
        for i in range(1,26):
            if(localboard[i]=='N'):
                scoreOrdinateur=scoreOrdinateur+ scoreboard[i]
            elif(localboard[i]=='B'):
                scoreJoeur=scoreJoeur+ scoreboard[i]

       
        NN=nombreMovement(localboard,'N')
        NB=nombreMovement(localboard,'B')
        

        
        if(scoreOrdinateur>=scoreJoeur and NN>=NB):
            return 0.75
        elif(scoreOrdinateur<=scoreJoeur and NN>=NB):
            return 0.5
        elif(scoreOrdinateur>=scoreJoeur and NN<=NB):
            return -0.5
        elif(scoreOrdinateur<=scoreJoeur and NN<=NB):
            return -0.75
        else:
            return 0

    if(checkWin(board)==True and currentPlayer=='N'):
        return 1
    elif(checkWin(board)==True and currentPlayer=='B'):
        return -1
    else:
        valeur=ScoreBoard(board)
        return valeur


#DECTION DES PROCHAIN ETAT DE JEUX
def nextBoardList(localboard,currentPlayer):
    nextPositionList=[ ]
    i=0
    def computerVirtualMove(exposition,newPosition,Virtualboard):
        Virtualboard[newPosition]=Virtualboard[exposition]
        Virtualboard[exposition]=' '
        Test = Virtualboard
        return Test
     
    for j in range(1,26):
        #Test des mouvement possible
        if (localboard[j]==currentPlayer):

            if(crossUpright(j)!=False):
                if( board[crossUpright(j)]==' '):
                    nextPositionList=nextPositionList+[[j,crossUpright(j)]]
                    i=i+1

            if(crossUpleft(j)!=False):
                if( board[crossUpleft(j)]==' '):
                    nextPositionList=nextPositionList+[[j,crossUpleft(j)]]
                    i=i+1

            if(crossDownright(j)!=False):
                if( board[crossDownright(j)]==' '):
                    nextPositionList=nextPositionList+[[j,crossDownright(j)]]
                    i=i+1

            if(crossDownleft(j)!=False):
                 if( board[crossDownleft(j)]==' '):
                    nextPositionList=nextPositionList+[[j,crossDownleft(j)]]
                    i=i+1
            
            if(upMove(j)!=False):
                if( board[upMove(j)]==' '): 
                    nextPositionList=nextPositionList+[[j,upMove(j)]]
                    i=i+1
                    
            
            if(downMove(j)!=False):
                if( localboard[downMove(j)]==' '):
                    nextPositionList=nextPositionList+[[j,downMove(j)]]
                    i=i+1
                   
                    
            if(rightMove(j)!=False):
                if( board[rightMove(j)]==' '):
                    nextPositionList=nextPositionList+[[j,rightMove(j)]]
                    i=i+1

            if(leftMove(j)!=False):
                if( board[leftMove(j)]==' '):
                    nextPositionList=nextPositionList+[[j,leftMove(j)]]
                    i=i+1      
                    
    nextplay=[]   
    for k in range (0,i):
        testboard= deepcopy(localboard)
        testboard=computerVirtualMove(nextPositionList[k][0],nextPositionList[k][1],testboard)
        nextplay= nextplay+[testboard]

    return nextplay


def computerMove(): 
    '''exPosition= int(input("Position du point a deplacer N"))
    newPosition = int(input("entrez la position ou aller N "))
    if(board[exPosition]==machinePlayer):
        Movement(exPosition, newPosition)
    else:
        print("cette case est vide ou ce jeton ne vous appartiens pas")
        computerMove()'''
  
    global board
    AlphaBeta(board)

    if(checkWin(board)== True):
        printBoard(board)
        print("ordinateur a gange")
   

'''board ={1:' ',2:'B',3:' ',4:' ',5:' ',
        6:' ',7:' ',8:' ',9:' ',10:' ',
        11:' ',12:' ',13:' ',14:' ',15:' ',
        16:' ',17:' ',18:' ',19:' ',20:' ',
        21:' ',22:' ',23:' ',24:' ',25:' '}'''

#Test Programme


while not checkWin(board):
   
       # Chargement de Coin ou jeuton de jeux par les joeurs
   if (debut==1):
        for i in range(1,5):
            posi=int(input("entrez poition B"))
            insertValue(currentPlayer, posi)
            posi=int(input("entrez poition N"))
            insertValue(machinePlayer, posi)
            i=i+1
        debut=0
   
   printBoard(board)   
   playerMove()
   if(currentPlayer=='B'):
        currentPlayer='N'
   else:
        currentPlayer='B'
   computerMove()
   if(currentPlayer=='N'):
        currentPlayer='B'
   else:
        currentPlayer='N'
      
    