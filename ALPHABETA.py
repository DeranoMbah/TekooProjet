
from Teeko_Projet import *

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
        
        movementpossibleN=int(nombreMovement(localboard,'N'))
        movementpossibleB=int(nombreMovement(localboard,'B'))
        

        if(scoreOrdinateur==scoreJoeur and movementpossibleB==movementpossibleN):
            return 0
        elif(scoreOrdinateur<scoreJoeur and movementpossibleN<movementpossibleB):
            return -0.75
        elif(scoreOrdinateur<scoreJoeur and movementpossibleN>=movementpossibleB):
            return -0.5
        elif(scoreOrdinateur>scoreJoeur and movementpossibleN<movementpossibleB):
            return 0.5
        elif(scoreOrdinateur>scoreJoeur and movementpossibleN>=movementpossibleB):
            return 0.75
      

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
