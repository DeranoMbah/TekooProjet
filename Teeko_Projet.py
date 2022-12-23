from binascii import a2b_qp
from copy import deepcopy
from json.encoder import INFINITY
import os
import random
from site import ENABLE_USER_SITE


from variables import *
from functions import *
from alpha_beta import *
from game import *


   

'''globalboard ={1:' ',2:' ',3:' ',4:' ',5:' ',
        6:' ',7:'B',8:'B',9:' ',10:' ',
        11:'B',12:'N',13:'N',14:'B',15:' ',
        16:' ',17:' ',18:' ',19:' ',20:' ',
        21:'N',22:' ',23:' ',24:'N',25:' '}'''

while(1):
    if not is_game_on:
        print_menu()
        choice = valid_choice()

        if choice == 1:
            print_commandes()
        
        else :
            O = os.system('cls')
            if O > 0:
                os.system('clear')
            
            is_game_on = True

        
    if is_game_on:
        
        if choice == 2:
    
            starter = valid_starter()

            while is_game_on:
                if starter == 2:
                    start_with_AI()
                else:
                    start_with_human()
        
        else:
            one_on_one()


      