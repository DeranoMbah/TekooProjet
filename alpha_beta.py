
from functions import *
#from Teeko_Projet import currentPlayer
from json.encoder import INFINITY
from copy import deepcopy




#DEFINITION ALPHA BETA
def AlphaBeta(board, pose):
    global scoreprofondeur
    global newscoreprofondeur
    profondeurtest = 3
    localboard= deepcopy(board)
    newscoreprofondeur= profondeurtest
    scoreprofondeur = profondeurtest
    
    def nextset(localboard,currentPlayer):
        next=[]
        for i in range(1,26):
            localvalue=deepcopy(board)
            if(localboard[i]==' '):
                localvalue[i]=currentPlayer
                next=next+[deepcopy(localvalue)]
             
        return next


    
            #DEFINITION DU MAXVALUEA
    def MaxValue(localboard,profondeur, alpha,beta,bestscore):
         global board
         global newscoreprofondeur
         if(checkWin(localboard)==True or profondeur==0):

             return(eval(localboard,profondeur))

         resultat= - INFINITY
         if(pose==True):
            nextplay= nextset(deepcopy(localboard),'N')
         else:
            nextplay= nextBoardList(localboard,'N')
         
         for i in nextplay:
             resultat=max(resultat,MinValue(deepcopy(i),profondeur-1,alpha,beta,bestscore))
             if(resultat>=beta): 
                 return resultat

             alpha=max(alpha, resultat)

             if(resultat>bestscore and profondeurtest==profondeur):
                 board=deepcopy(i)
                 bestscore=resultat

             if(resultat==1 and bestscore==1 and profondeurtest==profondeur and newscoreprofondeur>scoreprofondeur):
                 board=deepcopy(i)
                 bestscore=resultat
                 newscoreprofondeur=scoreprofondeur


             print(newscoreprofondeur," ",scoreprofondeur," ",bestscore)
                    
                
             #print(bestscore)

         return resultat
    
        #DEFINITION DU MINVALUE
    def MinValue(localboard,profondeur, alpha,beta,bestscore):
        if(checkWin(localboard)==True or profondeur==0):
            return(eval(localboard,profondeur))

        resultat= + INFINITY
        if(pose==True):
            nextplay= nextset(deepcopy(localboard),'B')
        else:
            nextplay= nextBoardList(localboard,'B')
        

        for i in nextplay:
            resultat=min(resultat,MaxValue(deepcopy(i),profondeur-1,alpha,beta,bestscore))
            if(resultat<=alpha):
                return resultat

            beta=min(beta, resultat)

            return resultat

    MaxValue(localboard, profondeurtest, -INFINITY, +INFINITY,-INFINITY)




#Definition de la fonction D'evaluation
def eval(board, profondeur):
    global scoreprofondeur
    
    scoreboard={1:1,2:8,3:5,4:8,5:1,
                6:8,7:10,8:15,9:10,10:8,
                11:5,12:15,13:20,14:15,15:5,
                16:8,17:10,18:15,19:10,20:8,
                21:1,22:8,23:5,24:8,25:1}

    
    def nombreMovement(localboard,Player):
        i=0

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
        scoreprofondeur=3-profondeur
        return 1
    elif(checkWin(board)==True and currentPlayer=='B'):
        return -1
    else:
        valeur=ScoreBoard(board)
        return valeur
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


#POSE DES PIONS ORDINATEUR
def computerset(localboard,compteur):
    global board
    scoreboard={1:1,2:8,3:5,4:8,5:1,
                6:8,7:10,8:15,9:10,10:8,
                11:5,12:15,13:20,14:15,15:5,
                16:8,17:10,18:15,19:10,20:8,
                21:1,22:8,23:5,24:8,25:1}
    global machinePlayer
    position=0
    score=0
    if(compteur !=4):
        for i in range(1,26):
            if (espaceFree(i) and scoreboard[i]>score):
                score=scoreboard[i]
                position=i
            
        localboard[position]= machinePlayer
        printBoard(localboard)
    elif(compteur==4):
        "STAND BEY"
        AlphaBeta(board,True)
        printBoard(board)


#DETECTION DES PROCHAIN ETAT DE JEUX
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




# Definition de COMPUTER MOVE
def computerMove(): 

    global board
    AlphaBeta(board,False)

    if(checkWin(board)== True):
        printBoard(board)
        print(string(currentPlayer) + " a gange")
