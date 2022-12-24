import random

#global grid numbers
num=[1,2,3,4,5,6,7,8,9]

def main():
    #HEADING    
    print(format('*** WELCOME TO TIC TAC TOE!! ***','>50s'))
    print()
    #PLAY AGAIN LOOP
    while (1):
        #MENU
        menu(1)

        #CHOICE OF GAME VERSION
        while (1):
            #SINGLE,DUAL OR EXIT
            game=input('Enter game choice: ').strip()
            game.replace(' ','')
            if game.isdigit() == True and (int(game) >= 0 and int(game) <= 2):
                game=int(game)
                break
            else:
                print('Invalid Entry!\n')
                
        #1 PLAYER
        if game == 1:
            while (1):
                print('\n\t\t***************** 1 PLAYER GAME *****************')
                print()
                #MENU
                menu(2)
                
                #EASY,MEDIUM, DIFFICULT
                while (1):
                    level=input('Enter difficulty level: ').strip()
                    level.replace(' ','')
                    if level.isdigit() == True and (int(level) >= 0 and int(level) <= 3):
                        level=int(level)
                        break
                    else:
                        print('Invalid Entry!')

                #EASY
                if level == 1:
                    while (1):
                        print('\nLEVEL: EASY')
                        print('------------',end='')
                        player_1(1)
                        play_again=input('\nEnter \'Y\' to *play again*; \'M\' to display *Single Player menu*; otherwise press any key: ')
                        if (play_again != 'Y' and play_again != 'y') or (play_again == 'M' and play_again == 'm'):
                            game_end=True
                            print(format('X '*6,'>45s'))
                            print()
                            break
                        else:
                            print(format('X '*6,'>45s'))

                #MEDIUM
                elif level == 2:
                    while (1):
                        print('\nLEVEL: MEDIUM')
                        print('--------------',end='')
                        player_1(2)
                        play_again=input('\nEnter \'Y\' to *play again*; \'M\' to display *Single Player menu*; otherwise press any key: ')
                        if (play_again != 'Y' and play_again != 'y') or (play_again == 'M' and play_again == 'm'):
                            game_end=True
                            print(format('X '*6,'>45s'))
                            print()
                            break
                        else:
                            print(format('X '*6,'>45s'))

                #DIFFICULT
                elif level == 3:
                    while(1):
                        print('\nLEVEL: DIFFICULT')
                        print('-----------------')
                        player_1(3)
                        play_again=input('\nEnter \'Y\' to *play again*; \'M\' to display *Single Player menu*; otherwise press any key: ')
                        if (play_again != 'Y' and play_again != 'y') or (play_again == 'M' and play_again == 'm'):
                            game_end=True
                            print(format('X '*6,'>45s'))
                            print()
                            break
                        else:
                            print(format('X '*6,'>45s'))
                    
                #EXITING 1 PLAYER GAME MENU
                else:
                    print(format('X '*6,'>45s'))
                    print()
                    break

                if game_end == True and play_again != 'M' and play_again != 'm':
                    break
            
        #2PLAYER
        elif game == 2:
            while (1):
                print('\n\t\t***************** 2 PLAYER GAME *****************')
                print()
                #MENU
                menu(3)
                
                #SINGLE, TOURNAMENT MODE
                while (1):
                    mode=input('Enter mode: ').strip()
                    mode.replace(' ','')
                    if mode.isdigit() == True and (int(mode) >= 0 and int(mode) <= 2):
                        mode=int(mode)
                        break
                    else:
                        print('Invalid Entry!\n')

                #SINGLE MODE
                if mode == 1:
                    while (1):
                        print('\nMODE: SINGLE')
                        print('------------')
                        winner=[]
                        player1,sym1,player2,sym2=name_symbol()
                        player_2(winner,player1,sym1,player2,sym2) 
                        play_again=input('\nEnter \'Y\' to *play again*; \'M\' to display *Dual Player menu*; otherwise press any key: ')
                        if (play_again != 'Y' and play_again != 'y') or (play_again == 'M' and play_again == 'm'):
                            game_end=True
                            print(format('X '*6,'>45s'))
                            print()
                            break
                        else:
                            print(format('X '*6,'>45s'))

                #TOURNAMENT MODE
                elif mode == 2:
                    while (1):
                        print('\nMODE: TOURNAMENT')
                        print('----------------')
                        tournament()
                        print(format('X '*6,'>45s'))
                        play_again=input('\nEnter \'Y\' to *play again*; \'M\' to display *Dual Player menu*; otherwise press any key: ')
                        if (play_again != 'Y' and play_again != 'y') or (play_again == 'M' and play_again == 'm'):
                            game_end=True
                            print(format('X '*6,'>45s'))
                            print()
                            break
                        else:
                            print(format('X '*6,'>45s'))
                            print()
                            
                #EXITING 2 PLAYER GAME MENU
                else:
                    print(format('X '*6,'>45s'))
                    print()
                    break

                if game_end == True and play_again != 'M' and play_again != 'm':
                    break
        else:
            print('\n',format('*** THANK YOU FOR PLAYING!! ***','>50s'))
            break           
#END OF MAIN()
        
def menu(num):
    if num == 1:
        print('\tMAIN MENU')
        print('-----------------------')
        print('TO EXIT            : PRESS 0')
        print('SINGLE PLAYER GAME : PRESS 1')
        print('DUAL PLAYER GAME   : PRESS 2')
        print('-----------------------')
    elif num ==2:
        print('   DIFFICULTY LEVEL')
        print('-----------------------')
        print('TO EXIT    : PRESS 0')
        print('EASY       : PRESS 1')
        print('MEDIUM     : PRESS 2')
        print('DIFFICULT  : PRESS 3')
        print('-----------------------')
    elif num == 3:
        print('   DUAL PLAYER MENU')
        print('-----------------------')
        print('TO EXIT     : PRESS 0')
        print('SINGLE GAME : PRESS 1')
        print('TOURNAMENT  : PRESS 2')
        print('-----------------------')   
#END OF MENU()
        
def printgrid(ind, symbol):
    for i in range(1,10):
        if i == ind:
            num.insert(i-1,symbol)
            num.remove(i)
            break
    print('\n   GRID')
    print('-----------')
    print('',num[0],'|',num[1],'|',num[2])
    print('-----------')
    print('',num[3],'|',num[4],'|',num[5])
    print('-----------')
    print('',num[6],'|',num[7],'|',num[8])
    print()
#END OF PRINTGRID()
      
def grid_initial():
    j=1
    for i in range(0,len(num)):
        num[i]=j
        j+=1
#END OF GRID_INITIAL()
              
def win_check(number,symbol1,symbol2):
    if number == 1:
        if   num[1-1] == num[2-1] == num[3-1] or num[4-1] == num[5-1] == num[6-1] or num[7-1] == num[8-1] == num[9-1] or num[1-1] == num[4-1] == num[7-1] or num[2-1] == num[5-1] == num[8-1] or num[3-1] == num[6-1] == num[9-1] or num[1-1] == num[5-1] == num[9-1] or num[3-1] == num[5-1] == num[7-1]:
            return True
        
    elif number == 2:
        if num[1-1] == num[2-1] == symbol2 or num[6-1] == num[9-1] == symbol2 or num[5-1] == num[7-1] == symbol2:
            if num[3-1] != symbol1 and num[3-1] != symbol2:
                printgrid(3,symbol2)
                return True
        if num[4-1] == num[5-1] == symbol2 or num[3-1] == num[9-1] == symbol2:
            if num[6-1] != symbol1 and num[6-1] != symbol2:
                printgrid(6,symbol2)
                return True
        if num[7-1] == num[8-1] == symbol2 or num[3-1] == num[6-1] == symbol2 or num[1-1] == num[5-1] == symbol2:
            if num[9-1] != symbol1 and num[9-1] != symbol2:
                printgrid(9,symbol2)
                return True
        if num[2-1] == num[3-1] == symbol2 or num[4-1] == num[7-1] == symbol2 or num[5-1] == num[9-1] == symbol2:
            if num[1-1] != symbol1 and num[1-1] != symbol2:
                printgrid(1,symbol2)
                return True
        if num[5-1] == num[6-1] == symbol2 or num[1-1] == num[7-1] == symbol2:
            if num[4-1] != symbol1 and num[4-1] != symbol2:
                printgrid(4,symbol2)
                return True
        if num[8-1] == num[9-1] == symbol2 or num[1-1] == num[4-1] == symbol2 or num[3-1] == num[5-1] == symbol2:
            if num[7-1] != symbol1 and num[7-1] != symbol2:
                printgrid(7,symbol2)
                return True
        if num[5-1] == num[8-1] == symbol2 or num[1-1] == num[3-1] == symbol2:
            if num[2-1] != symbol1 and num[2-1] != symbol2:
                printgrid(2,symbol2)
                return True
        if num[4-1] == num[6-1] == symbol2 or num[2-1] == num[8-1] == symbol2 or num[1-1] == num[9-1] == symbol2 or num[3-1] == num[7-1] == symbol2:
            if num[5-1] != symbol1 and num[5-1] != symbol2:
                printgrid(5,symbol2)
                return True
        if num[2-1] == num[5-1] == symbol2 or num[7-1] == num[9-1] == symbol2:
            if num[8-1] != symbol1 and num[8-1] != symbol2:
                printgrid(8,symbol2)
                return True
        
    elif number == 3:
        if num[1-1] == num[2-1] == symbol1 or num[6-1] == num[9-1] == symbol1 or num[5-1] == num[7-1] == symbol1:
            if num[3-1] != symbol1 and num[3-1] != symbol2:
                printgrid(3,symbol2)
                return True
        if num[4-1] == num[5-1] == symbol1 or num[3-1] == num[9-1] == symbol1:
            if num[6-1] != symbol1 and num[6-1] != symbol2:
                printgrid(6,symbol2)
                return True
        if num[7-1] == num[8-1] == symbol1 or num[3-1] == num[6-1] == symbol1 or num[1-1] == num[5-1] == symbol1:
            if num[9-1] != symbol1 and num[9-1] != symbol2:
                printgrid(9,symbol2)
                return True
        if num[2-1] == num[3-1] == symbol1 or num[4-1] == num[7-1] == symbol1 or num[5-1] == num[9-1] == symbol1:
            if num[1-1] != symbol1 and num[1-1] != symbol2:
                printgrid(1,symbol2)
                return True
        if num[5-1] == num[6-1] == symbol1 or num[1-1] == num[7-1] == symbol1:
            if num[4-1] != symbol1 and num[4-1] != symbol2:
                printgrid(4,symbol2)
                return True
        if num[8-1] == num[9-1] == symbol1 or num[1-1] == num[4-1] == symbol1 or num[3-1] == num[5-1] == symbol1:
            if num[7-1] != symbol1 and num[7-1] != symbol2:
                printgrid(7,symbol2)
                return True
        if num[5-1] == num[8-1] == symbol1 or num[1-1] == num[3-1] == symbol1:
            if num[2-1] != symbol1 and num[2-1] != symbol2:
                printgrid(2,symbol2)
                return True
        if num[4-1] == num[6-1] == symbol1 or num[2-1] == num[8-1] == symbol1 or num[1-1] == num[9-1] == symbol1 or num[3-1] == num[7-1] == symbol1:
            if num[5-1] != symbol1 and num[5-1] != symbol2:
                printgrid(5,symbol2)
                return True
        if num[2-1] == num[5-1] == symbol1 or num[7-1] == num[9-1] == symbol1:
            if num[8-1] != symbol1 and num[8-1] != symbol2:
                printgrid(8,symbol2)
                return True
#END OF WIN_CHECK()
    
def player_1(level):
    #grid numbers
    grid_initial()
    
    #names
    while (1):
        player=input('\nPlayer, please enter your name: ').title()
        if player.isalpha() != True:
            print('Invalid name entry!')
        else:
            break

    player_symbol=random.randint(0,1)
    if player_symbol == 1:
        print('\nYou are player O')
        print('Computer is player X')
        sym1='O' #user1
        sym2='X' #computer
    else:
        print('\nYou are player X')
        print('Computer is player O')
        sym1='X' #user1
        sym2='O' #computer

    #initial grid and heading
    printgrid(0,'')
    
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #1st turn check
    turn=random.randint(1,2)
    
    #Easy level
    if level == 1:
        #Computer turn
        if turn == 1:
            #GAME START
            print('*****************Computer','('+sym2+')','wins the toss!\n')
            for i in range(1,10):

                #odd turns of computer
                if i==1 or i==3 or i==5 or i==7 or i==9:
                    print('TURN: Computer')
                    
                    ret=win_check(2,sym1,sym2)
                    if ret != True:
                        while (1):
                            index=random.randint(1,9)-1
                            if num[index] != sym1 and num[index] != sym2:
                                printgrid(index+1,sym2)
                                break
                    else:
                        print('*****************COMPUTER WON!')
                        break
                        
                    if i == 9:
                        print('*****************IT\'S A DRAW!')

                #even turns of player
                else:
                    print('TURN:',player)
                    check=1
                
                    #Start: while checker loop
                    while check !=0 :
                        #Choice entry
                        while (1):
                            choice=input(str(player)+'('+sym1+'), please enter a box number: ').strip()
                            choice.replace(' ','')
                            if choice.isdigit() != True or (int(choice) < 1 or int(choice) > 9):
                                print('Invalid entry\n')
                            else:
                                choice=int(choice)
                                break
                            
                        #choice of symbol placement 
                        if num[choice-1] == choice:
                            printgrid(choice,sym1)
                            check=0
                            
                        else:
                            print('The place is already filled\n')
                    if win_check(1,0,0) == True:
                        print('*****************'+player,'WON!')
                        break
                    
        #Player turn
        elif turn == 2:
        
            #GAME START
            print('*****************'+player,'('+sym1+')','wins the toss!\n')
            for i in range(1,10):

                #odd turns of player
                if i==1 or i==3 or i==5 or i==7 or i==9:
                    print('TURN:',player)
                    check=1
                
                    #Start: while checker loop
                    while check !=0 :
                        #Choice entry
                        while (1):
                            choice=input(str(player)+'('+sym1+'), please enter a box number: ').strip()
                            choice.replace(' ','')
                            if choice.isdigit() != True or (int(choice) < 1 or int(choice) > 9):
                                print('Invalid entry\n')
                            else:
                                choice=int(choice)
                                break
                            
                        #choice of symbol placement 
                        if num[choice-1] == choice:
                            printgrid(choice,sym1)
                            check=0
                            
                        else:
                            print('The place is already filled\n')
                    if win_check(1,0,0) == True:
                        print('*****************'+player,'WON!')
                        break
                        
                    if i == 9:
                        print('*****************IT\'S A DRAW!')

                #even turns of computer
                else:
                    print('TURN: Computer')
                    
                    ret=win_check(2,sym1,sym2)
                    if ret != True:
                        while (1):
                            index=random.randint(1,9)-1
                            if num[index] != sym1 and num[index] != sym2:
                                printgrid(index+1,sym2)
                                break
                    else:
                        print('*****************COMPUTER WON!')
                        break

    #Medium level
    if level == 2:
        #Computer turn
        if turn == 1:
            #GAME START
            print('*****************Computer','('+sym2+')','wins the toss!\n')
            for i in range(1,10):

                #odd turns of computer
                if i==1 or i==3 or i==7 or i==9:
                    print('TURN: Computer')
                    
                    ret=win_check(2,sym1,sym2)
                    if ret != True:
                        while (1):
                            index=random.randint(1,9)-1
                            if num[index] != sym1 and num[index] != sym2:
                                printgrid(index+1,sym2)
                                break
                    else:
                        print('*****************COMPUTER WON!')
                        break
                        
                    if i == 9:
                        print('*****************IT\'S A DRAW!')

                #to stop user from winning during its 3rd turn
                elif i==5:
                    print('TURN: Computer')
                    
                    ret1=win_check(2,sym1,sym2)
                    if ret1 != True:
                        ret2=win_check(3,sym1,sym2)
                        if ret2 != True:
                            while (1):
                                index=random.randint(1,9)-1
                                if num[index] != sym1 and num[index] != sym2:
                                    printgrid(index+1,sym2)
                                    break
                    else:
                        print('*****************COMPUTER WON!')
                        break 

                #even turns of player
                else:
                    print('TURN:',player)
                    check=1
                
                    #Start: while checker loop
                    while check !=0 :
                        #Choice entry
                        while (1):
                            choice=input(str(player)+'('+sym1+'), please enter a box number: ').strip()
                            choice.replace(' ','')
                            if choice.isdigit() != True or (int(choice) < 1 or int(choice) > 9):
                                print('Invalid entry\n')
                            else:
                                choice=int(choice)
                                break
                            
                        #choice of symbol placement 
                        if num[choice-1] == choice:
                            printgrid(choice,sym1)
                            check=0
                            
                        else:
                            print('The place is already filled\n')
                    if win_check(1,0,0) == True:
                        print('*****************'+player,'WON!')
                        break
                    
        #Player turn
        elif turn == 2:
        
            #GAME START
            print('*****************'+player,'('+sym1+')','wins the toss!\n')
            for i in range(1,10):

                #odd turns of player
                if i==1 or i==3 or i==5 or i==7 or i==9:
                    print('TURN:',player)
                    check=1
                
                    #Start: while checker loop
                    while check !=0 :
                        #Choice entry
                        while (1):
                            choice=input(str(player)+'('+sym1+'), please enter a box number: ').strip()
                            choice.replace(' ','')
                            if choice.isdigit() != True or (int(choice) < 1 or int(choice) > 9):
                                print('Invalid entry\n')
                            else:
                                choice=int(choice)
                                break
                            
                        #choice of symbol placement 
                        if num[choice-1] == choice:
                            printgrid(choice,sym1)
                            check=0
                            
                        else:
                            print('The place is already filled\n')
                    if win_check(1,0,0) == True:
                        print('*****************'+player,'WON!')
                        break
                        
                    if i == 9:
                        print('*****************IT\'S A DRAW!')

                #even turns of computer
                elif i==2 or i==6 or i==8:
                    print('TURN: Computer')
                    
                    ret=win_check(2,sym1,sym2)
                    if ret != True:
                        while (1):
                            index=random.randint(1,9)-1
                            if num[index] != sym1 and num[index] != sym2:
                                printgrid(index+1,sym2)
                                break
                    else:
                        print('*****************COMPUTER WON!')
                        break

                #stopping user from winning during its 3rd turn
                elif i==4:
                    print('TURN: Computer')
                    
                    ret=win_check(3,sym1,sym2)
                    if ret != True:
                        while (1):
                            index=random.randint(1,9)-1
                            if num[index] != sym1 and num[index] != sym2:
                                printgrid(index+1,sym2)
                                break
                    
                    
    #Difficult level
    if level == 3:
        
        #Computer turn
        if turn == 1:
            #GAME START
            print('*****************Computer','('+sym2+')','wins the toss!\n')
            for i in range(1,10):

                #odd turns of computer
                if i==1 or i==3 or i==5 or i==7 or i==9:
                    print('TURN: Computer')
            #1
                    if i == 1:
                        #grid printing
                        printgrid(5,sym2)
            #3  
                    elif i == 3:
                        if num[3-1] != sym1:
                            #grid printing
                            printgrid(3,sym2)                        
                        elif num[1-0] != sym1:
                            #grid printing
                            printgrid(1,sym2)

            #5        
                    elif i == 5:
                        #turn 3 of computer is checked
                        if num[3-1] == sym2:
                            #turn i=4 of user is checked
                            if num[7-1] != sym1:                                
                                #grid printing
                                printgrid(7,sym2)
                                print('*****************COMPUTER WON!')
                                break
                            elif num[8-1] == sym1:
                                printgrid(9,sym2)
                            elif num[9-1] == sym1:
                                printgrid(8,sym2)
                            elif num[1-1] != sym1:           
                                #grid printing
                                printgrid(1,sym2)                                
                            else:
                                #grid printing
                                printgrid(4,sym2)
                                
                        elif num[1-1] == sym2:
                            if num[9-1] != sym1:                                
                                #grid printing
                                printgrid(9,sym2)
                                print('*****************COMPUTER WON!')
                                break                                
                            else:                                
                                #grid printing
                                printgrid(6,sym2)
                        
           #7                 
                    elif i == 7:
                        #turn 3,5 of computer is checked
                        if num[3-1] == sym2 and num[9-1] == sym2 and num[8-1] == sym1:
                            if num[1-1] != sym1:
                                #grid printing
                                printgrid(1,sym2)
                                print('*****************COMPUTER WON!')
                                break                                
                            else:                                
                                #grid printing
                                printgrid(6,sym2)
                                print('*****************COMPUTER WON!')
                                break
                            
                        elif num[3-1] == sym2 and num[8-1] == sym2 and num[9-1] == sym1:
                            if num[2-1] != sym1:
                                #grid printing
                                printgrid(2,sym2)
                                print('*****************COMPUTER WON!')
                                break                                
                            else:                                
                                #grid printing
                                printgrid(4,sym2)
                                                        
                        elif num[3-1] == sym2 and num[1-1] == sym2:
                            #turn i=6 of user is checked
                            if num[9-1] != sym1:
                                #grid printing
                                printgrid(9,sym2)
                                print('*****************COMPUTER WON!')
                                break                                
                            elif num[2-1] != sym1:                                
                                #grid printing
                                printgrid(2,sym2)
                                print('*****************COMPUTER WON!')
                                break
                            else:
                                #grid printing
                                printgrid(8,sym2)
                            
                                
                        elif num[3-1] == sym2 and num[4-1] == sym2:
                            if num[6-1] != sym1:                                
                                #grid printing
                                printgrid(6,sym2)
                                print('*****************COMPUTER WON!')
                                break                                
                            else:
                                #grid printing
                                printgrid(9,sym2)

                        elif num[1-1] == sym2 and num[6-1] == sym2:
                            if num[4-1] != sym1:
                                #grid printing
                                printgrid(4,sym2)
                                print('*****************COMPUTER WON!')
                                break                                
                            else:
                                #grid printing
                                printgrid(8,sym2)
                                
           #9                 
                    elif i == 9:
                        #turn 3,5,7 of computer is checked
                        if num[3-1] == sym2 and num[8-1] == sym2 and num[9-1] == sym1 and num[4-1] == sym2 and num[2-1] == sym1 :
                            if num[6-1] != sym1:
                                printgrid(6,sym2)
                                print('*****************COMPUTER WON!')
                                break 
                            else:
                                printgrid(1,sym2)
                                print('*****************IT\'S A DRAW!')
                                break
                            
                        elif num[3-1] == sym2 and num[1-1] == sym2 and num[8-1] == sym2:
                            if num[4-1] != sym1:
                                printgrid(4,sym2)
                                print('*****************IT\'S A DRAW!')
                                break
                            else:
                                printgrid(6,sym2)
                                print('*****************IT\'S A DRAW!')
                                break
                            
                        elif num[1-1] == sym2 and num[6-1] == sym2 and num[8-1] == sym2:
                            if num[2-1] != sym1:
                                printgrid(2,sym2)
                                print('*****************COMPUTER WON!')
                                break 
                            else:
                                printgrid(7,sym2)
                                print('*****************IT\'S A DRAW!')
                                break
                                
                        if (num[3-1] == sym2 and num[4-1] == sym2 and num[9-1] == sym2) or (num[1-1] == sym2 and num[6-1] == sym2 and num[7-1] == sym2):
                            #turn i=8 of user is checked
                            if num[2-1] != sym1:
                                #grid printing
                                printgrid(2,sym2)

                                print('*****************IT\'S A DRAW!')
                                break
                                
                            else:
                                #grid printing
                                printgrid(8,sym2)
                                
                                print('*****************IT\'S A DRAW!')
                                break
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      #2,4,6,8
                    #start: even turns of player
                elif i==2 or i==4 or i==6 or i==8:
                    print('TURN:',player)
                    check=1
                
                    #Start: while checker loop
                    while check !=0 :
                        #Choice entry
                        while (1):
                            choice=input(str(player)+'('+sym1+'), please enter a box number: ').strip()
                            choice.replace(' ','')
                            if choice.isdigit() != True or (int(choice) < 1 or int(choice) > 9):
                                print('Invalid entry\n')
                            else:
                                choice=int(choice)
                                break
                            
                        #choice of symbol placement
                        if num[choice-1] == choice:
                            printgrid(choice,sym1)
                            check=0
                            
                        else:
                            print('The place is already filled\n')
                            
                    #close: while checker ends

            #GAME END
            
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       #Player turn
        else:
            #GAME START
            print('*****************'+player,'('+sym1+')', 'wins the toss!\n')

            for i in range(1,10):

    #1,3,5,7,9
                #start: odd turns of player
                if i==1 or i==3 or i==5 or i==7 or i==9:
                    print('TURN:',player)
                    check=1
                
                    #Start: while checker loop
                    while check !=0 :
                        #Choice entry
                        while (1):
                            choice=input(str(player)+'('+sym1+'), please enter a box number: ').strip()
                            choice.replace(' ','')
                            if choice.isdigit() != True or (int(choice) < 1 or int(choice) > 9):
                                print('Invalid entry\n')
                            else:
                                choice=int(choice)
                                break
                            
                        #choice of symbol placement 
                        if num[choice-1] == choice:
                            printgrid(choice,sym1)
                            check=0
                            
                        else:
                            print('The place is already filled\n')
                            
                    if i == 9:
                        print('*****************IT\'S A DRAW!')

                    #close: while checker ends
                #close: odd turns of 1st player
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------              
                #start: even turns of computer
         #2
                elif i == 2:
                    print('TURN: Computer')
                    if num[5-1] == sym1:
                        printgrid(3,sym2)
                    else:
                        printgrid(5,sym2)
         #4           
                elif i == 4:
                    print('TURN: Computer')

                    #player 1st entry not at mid
                    if num[5-1] == sym2 and num[1-1] == sym1 and num[3-1] == sym1:
                        printgrid(2,sym2)
                        
                    elif num[5-1] == sym2 and num[1-1] == sym1 and num[7-1] == sym1:
                        printgrid(4,sym2)
                        
                    elif num[5-1] == sym2 and num[9-1] == sym1 and num[3-1] == sym1:
                        printgrid(6,sym2)
                        
                    elif num[5-1] == sym2 and num[9-1] == sym1 and num[7-1] == sym1:
                        printgrid(8,sym2)
                        
                    elif num[5-1] == sym2 and num[1-1] == sym1 and num[2-1] == sym1:
                        printgrid(3,sym2)
                        
                    elif num[5-1] == sym2 and num[2-1] == sym1 and num[3-1] == sym1:
                        printgrid(1,sym2)
                        
                    elif num[5-1] == sym2 and num[3-1] == sym1 and num[6-1] == sym1:
                        printgrid(9,sym2)
                        
                    elif num[5-1] == sym2 and num[6-1] == sym1 and num[9-1] == sym1:
                        printgrid(3,sym2)
                        
                    elif num[5-1] == sym2 and num[9-1] == sym1 and num[8-1] == sym1:
                        printgrid(7,sym2)
                        
                    elif num[5-1] == sym2 and num[8-1] == sym1 and num[7-1] == sym1:
                        printgrid(9,sym2)
                        
                    elif num[5-1] == sym2 and num[1-1] == sym1 and num[4-1] == sym1:
                        printgrid(7,sym2)
                        
                    elif num[5-1] == sym2 and num[4-1] == sym1 and num[7-1] == sym1:
                        printgrid(1,sym2)
                    
                    elif num[5-1] == sym2 and num[1-1] == sym1 and num[9-1] == sym1:
                        printgrid(6,sym2)
                        
                    elif num[5-1] == sym2 and num[3-1] == sym1 and num[7-1] == sym1:
                        printgrid(4,sym2)
                        
                    elif num[5-1] == sym2 and ( (num[2-1] == sym1 and num[8-1] == sym1) or (num[4-1] == sym1 and num[6-1] == sym1) ):
                        printgrid(3,sym2)
                        
                    elif num[5-1] == sym2 and ( (num[2-1] == sym1 and num[4-1] == sym1) or (num[2-1] == sym1 and num[7-1] == sym1) or (num[4-1] == sym1 and num[3-1] == sym1) ):
                        printgrid(1,sym2)
                        
                    elif num[5-1] == sym2 and ( (num[2-1] == sym1 and num[6-1] == sym1)  or (num[2-1] == sym1 and num[9-1] == sym1) or (num[1-1] == sym1 and num[6-1] == sym1) ):
                        printgrid(3,sym2)
                        
                    elif num[5-1] == sym2 and ( (num[8-1] == sym1 and num[4-1] == sym1)  or (num[8-1] == sym1 and num[1-1] == sym1) or (num[4-1] == sym1 and num[9-1] == sym1) ):
                        printgrid(7,sym2)
                        
                    elif num[5-1] == sym2 and ( (num[8-1] == sym1 and num[6-1] == sym1)  or (num[8-1] == sym1 and num[3-1] == sym1) or (num[6-1] == sym1 and num[7-1] == sym1) ):
                        printgrid(9,sym2)

                    #player 1st entry at mid    
                    elif num[3-1] == sym2 and num[1-1] == sym1:
                        printgrid(9,sym2)
                        
                    elif num[3-1] == sym2 and num[9-1] == sym1:
                        printgrid(1,sym2)
                        
                    elif num[3-1] == sym2 and num[2-1] == sym1:
                        printgrid(8,sym2)
                        
                    elif num[3-1] == sym2 and num[8-1] == sym1:
                        printgrid(2,sym2)
                        
                    elif num[3-1] == sym2 and num[4-1] == sym1:
                        printgrid(6,sym2)
                        
                    elif num[3-1] == sym2 and num[6-1] == sym1:
                        printgrid(4,sym2)
                        
                    elif num[3-1] == sym2 and num[7-1] == sym1:
                        printgrid(1,sym2)
         #6               
                elif i == 6:
                    print('TURN: Computer')

                    #player 1st entry not at mid
                    if num[5-1] == sym2 and num[1-1] == sym1 and num[3-1] == sym1 and num[2-1] == sym2:
                        if num[8-1] != sym1:
                            printgrid(8,sym2)
                            print('*****************COMPUTER WON!')
                            break                        
                        else:
                            printgrid(7,sym2)
                        
                    elif num[5-1] == sym2 and num[1-1] == sym1 and num[7-1] == sym1 and num[4-1] == sym2:
                        if num[6-1] != sym1:
                            printgrid(6,sym2)
                            print('*****************COMPUTER WON!')
                            break                        
                        else:
                            printgrid(3,sym2)

                    elif num[5-1] == sym2 and num[9-1] == sym1 and num[3-1] == sym1 and num[6-1] == sym2:
                        if num[4-1] != sym1:
                            printgrid(4,sym2)
                            print('*****************COMPUTER WON!')
                            break                        
                        else:
                            printgrid(1,sym2)

                    elif num[5-1] == sym2 and num[9-1] == sym1 and num[7-1] == sym1 and num[8-1] == sym2:
                        if num[2-1] != sym1:
                            printgrid(2,sym2)
                            print('*****************COMPUTER WON!')
                            break                        
                        else:
                            printgrid(1,sym2)

                    elif num[5-1] == sym2 and  num[1-1] == sym1 and num[2-1] == sym1 and num[3-1] == sym2:
                        if num[7-1] != sym1:
                            printgrid(7,sym2)
                            print('*****************COMPUTER WON!')
                            break                        
                        else:
                            printgrid(4,sym2)

                    elif num[5-1] == sym2 and num[2-1] == sym1 and num[3-1] == sym1 and num[1-1] == sym2:
                        if num[9-1] != sym1:
                            printgrid(9,sym2)
                            print('*****************COMPUTER WON!')
                            break                        
                        else:
                            printgrid(6,sym2)

                    elif num[5-1] == sym2 and num[3-1] == sym1 and num[6-1] == sym1 and num[9-1] == sym2:
                        if num[1-1] != sym1:
                            printgrid(1,sym2)
                            print('*****************COMPUTER WON!')
                            break                        
                        else:
                            printgrid(2,sym2)
                        
                    elif num[5-1] == sym2 and num[6-1] == sym1 and num[9-1] == sym1 and num[3-1] == sym2:
                        if num[7-1] != sym1:
                            printgrid(7,sym2)
                            print('*****************COMPUTER WON!')
                            break                        
                        else:
                            printgrid(8,sym2)
                        
                    elif num[5-1] == sym2 and num[9-1] == sym1 and num[8-1] == sym1 and num[7-1] == sym2:
                        if num[3-1] != sym1:
                            printgrid(3,sym2)
                            print('*****************COMPUTER WON!')
                            break                        
                        else:
                            printgrid(6,sym2)

                    elif num[5-1] == sym2 and num[7-1] == sym1 and num[8-1] == sym1 and num[9-1] == sym2:
                        if num[1-1] != sym1:
                            printgrid(1,sym2)
                            print('*****************COMPUTER WON!')
                            break                        
                        else:
                            printgrid(4,sym2)

                    elif num[5-1] == sym2 and num[1-1] == sym1 and num[4-1] == sym1 and num[7-1] == sym2:
                        if num[3-1] != sym1:
                            printgrid(3,sym2)
                            print('*****************COMPUTER WON!')
                            break                        
                        else:
                            printgrid(2,sym2)
                        
                    elif num[5-1] == sym2 and num[4-1] == sym1 and num[7-1] == sym1 and num[1-1] == sym2:
                        if num[9-1] != sym1:
                            printgrid(9,sym2)
                            print('*****************COMPUTER WON!')
                            break                        
                        else:
                            printgrid(8,sym2)

                    elif num[5-1] == sym2 and num[1-1] == sym1 and num[9-1] == sym1 and num[6-1] == sym2:
                        if num[4-1] != sym1:
                            printgrid(4,sym2)
                            print('*****************COMPUTER WON!')
                            break                        
                        else:
                            printgrid(7,sym2)

                    elif num[5-1] == sym2 and num[3-1] == sym1 and num[7-1] == sym1 and num[4-1] == sym2:
                        if num[6-1] != sym1:
                            printgrid(6,sym2)
                            print('*****************COMPUTER WON!')
                            break                        
                        else:
                            printgrid(9,sym2)

                    elif num[5-1] == sym2 and ( (num[2-1] == sym1 and num[8-1] == sym1) or (num[4-1] == sym1 and num[6-1] == sym1)) and num[3-1] == sym2:
                        if num[2-1] == sym1 and num[8-1] == sym1:
                            
                            if num[7-1] != sym1:
                                printgrid(7,sym2)
                                print('*****************COMPUTER WON!')
                                break                        
                            else:
                                printgrid(9,sym2)
                                
                        elif num[4-1] == sym1 and num[6-1] == sym1:
                            
                            if num[7-1] != sym1:
                                printgrid(7,sym2)
                                print('*****************COMPUTER WON!')
                                break                        
                            else:
                                printgrid(1,sym2)
                                
                    elif num[5-1] == sym2 and ( (num[2-1] == sym1 and num[4-1] == sym1) or (num[2-1] == sym1 and num[7-1] == sym1)) and num[1-1] == sym2:
                        if num[9-1] != sym1:
                            printgrid(9,sym2)                            
                            print('*****************COMPUTER WON!')
                            break                    
                        else:
                            printgrid(8,sym2)

                    elif num[5-1] == sym2 and ( (num[2-1] == sym1 and num[6-1] == sym1) or (num[2-1] == sym1 and num[9-1] == sym1)) and num[3-1] == sym2:
                        if num[7-1] != sym1:
                            printgrid(7,sym2)                            
                            print('*****************COMPUTER WON!')
                            break                    
                        else:
                            printgrid(8,sym2)

                    elif num[5-1] == sym2 and ( (num[8-1] == sym1 and num[4-1] == sym1) or (num[8-1] == sym1 and num[1-1] == sym1)) and num[7-1] == sym2:
                        if num[3-1] != sym1:
                            printgrid(3,sym2)                            
                            print('*****************COMPUTER WON!')
                            break                    
                        else:
                            printgrid(2,sym2)

                    elif num[5-1] == sym2 and ( (num[8-1] == sym1 and num[6-1] == sym1) or (num[8-1] == sym1 and num[3-1] == sym1)) and num[9-1] == sym2:
                        if num[1-1] != sym1:
                            printgrid(1,sym2)                            
                            print('*****************COMPUTER WON!')
                            break                    
                        else:
                            printgrid(2,sym2)

                    elif num[5-1] == sym2 and num[4-1] == sym1 and num[9-1] == sym1 and num[7-1] == sym2:
                        if num[3-1] != sym1:
                            printgrid(3,sym2)                            
                            print('*****************COMPUTER WON!')
                            break
                    
                        else:
                            printgrid(6,sym2)
                            
                    elif num[5-1] == sym2 and num[4-1] == sym1 and num[3-1] == sym1 and num[1-1] == sym2:
                        if num[9-1] != sym1:
                            printgrid(9,sym2)                            
                            print('*****************COMPUTER WON!')
                            break                    
                        else:
                            printgrid(6,sym2)
                            
                    elif num[5-1] == sym2 and num[1-1] == sym1 and num[6-1] == sym1 and num[3-1] == sym2:
                        if num[7-1] != sym1:
                            printgrid(7,sym2)                            
                            print('*****************COMPUTER WON!')
                            break                    
                        else:
                            printgrid(4,sym2)
                            
                    elif num[5-1] == sym2 and num[6-1] == sym1 and num[7-1] == sym1 and num[9-1] == sym2:
                        if num[1-1] != sym1:
                            printgrid(1,sym2)                            
                            print('*****************COMPUTER WON!')
                            break                    
                        else:
                            printgrid(4,sym2)
                            
                    #player 1st entry at mid
                    elif num[3-1] == sym2 and num[1-1] == sym1 and num[9-1] == sym2:
                        if num[6-1] != sym1:
                            printgrid(6,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(4,sym2)
                            
                    elif num[3-1] == sym2 and num[9-1] == sym1 and num[1-1] == sym2:
                        if num[2-1] != sym1:
                            printgrid(2,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(8,sym2)
                            
                    elif num[3-1] == sym2 and num[2-1] == sym1 and num[8-1] == sym2:
                        if num[1-1] == sym1:
                            printgrid(9,sym2)                            
                        elif num[9-1] == sym1:
                            printgrid(1,sym2)                            
                        elif num[4-1] == sym1:
                            printgrid(6,sym2)                            
                        elif num[6-1] == sym1:
                            printgrid(4,sym2)                            
                        else:
                            printgrid(9,sym2)
                            
                    elif num[3-1] == sym2 and num[8-1] == sym1 and num[2-1] == sym2:
                        if num[1-1] != sym1:
                            printgrid(1,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(9,sym2)
                            
                    elif num[3-1] == sym2 and num[4-1] == sym1 and num[6-1] == sym2:
                        if num[9-1] != sym1:
                            printgrid(9,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(1,sym2)
                            
                    elif num[3-1] == sym2 and num[6-1] == sym1 and num[4-1] == sym2:
                        if num[1-1] == sym1:
                            printgrid(9,sym2)                            
                        elif num[9-1] == sym1:
                            printgrid(1,sym2)                            
                        elif num[2-1] == sym1:
                            printgrid(8,sym2)                            
                        elif num[8-1] == sym1:
                            printgrid(2,sym2)                            
                        else:
                            printgrid(9,sym2)
                            
                    elif num[3-1] == sym2 and num[7-1] == sym1 and num[1-1] == sym2:
                        if num[2-1] != sym1:
                            printgrid(2,sym2)
                            print('*****************COMPUTER WON!')
                            break                        
                        else:
                            printgrid(8,sym2)
         #8                   
                elif i == 8:
                    print('TURN: Computer')

                    #player 1st entry not at mid
                    if num[5-1] == sym2 and num[1-1] == sym1 and num[3-1] == sym1 and num[2-1] == sym2 and num[8-1] == sym1 and num[7-1] == sym2:
                        if num[6-1] != sym1:
                            printgrid(6,sym2)                            
                        else:
                            printgrid(9,sym2)
                        
                    elif num[5-1] == sym2 and num[1-1] == sym1 and num[7-1] == sym1 and num[4-1] == sym2 and num[6-1] == sym1 and num[3-1] == sym2:
                        if num[8-1] != sym1:
                            printgrid(8,sym2)                            
                        else:
                            printgrid(9,sym2)

                    elif num[5-1] == sym2 and num[9-1] == sym1 and num[3-1] == sym1 and num[6-1] == sym2 and num[4-1] == sym1 and num[1-1] == sym2:
                        if num[7-1] != sym1:
                            printgrid(7,sym2)                            
                        else:
                            printgrid(8,sym2)

                    elif num[5-1] == sym2 and num[9-1] == sym1 and num[7-1] == sym1 and num[8-1] == sym2 and num[2-1] == sym1 and num[1-1] == sym2:
                        if num[3-1] != sym1:
                            printgrid(3,sym2)                            
                        else:
                            printgrid(6,sym2)

                    elif num[5-1] == sym2 and num[1-1] == sym1 and num[2-1] == sym1 and num[3-1] == sym2 and num[7-1] == sym1 and num[4-1] == sym2:
                        if num[6-1] != sym1:
                            printgrid(6,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(9,sym2)

                    elif num[5-1] == sym2 and num[2-1] == sym1 and num[3-1] == sym1 and num[1-1] == sym2 and num[9-1] == sym1 and num[6-1] == sym2:
                        if num[4-1] != sym1:
                            printgrid(4,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(7,sym2)

                    elif num[5-1] == sym2 and num[3-1] == sym1 and num[6-1] == sym1 and num[9-1] == sym2 and num[1-1] == sym1 and num[2-1] == sym2:
                        if num[8-1] != sym1:
                            printgrid(8,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(7,sym2)
                        
                    elif num[5-1] == sym2 and num[6-1] == sym1 and num[9-1] == sym1 and num[3-1] == sym2 and num[7-1] == sym1 and num[8-1] == sym2:
                        if num[2-1] != sym1:
                            printgrid(2,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(1,sym2)
                        
                    elif num[5-1] == sym2 and num[9-1] == sym1 and num[8-1] == sym1 and num[7-1] == sym2 and num[3-1] == sym1 and num[6-1] == sym2:
                        if num[4-1] != sym1:
                            printgrid(4,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(1,sym2)

                    elif num[5-1] == sym2 and num[7-1] == sym1 and num[8-1] == sym1 and num[9-1] == sym2 and num[1-1] == sym1 and num[4-1] == sym2:
                        if num[6-1] != sym1:
                            printgrid(6,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(3,sym2)

                    elif num[5-1] == sym2 and num[1-1] == sym1 and num[4-1] == sym1 and num[7-1] == sym2 and num[3-1] == sym1 and num[2-1] == sym2:
                        
                        if num[8-1] != sym1:
                            printgrid(8,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(9,sym2)
                        
                    elif num[5-1] == sym2 and num[4-1] == sym1 and num[7-1] == sym1 and num[1-1] == sym2 and num[9-1] == sym1 and num[8-1] == sym2:
                        if num[2-1] != sym1:
                            printgrid(2,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(3,sym2)
                    
                    elif num[5-1] == sym2 and num[1-1] == sym1 and num[9-1] == sym1 and num[6-1] == sym2 and num[4-1] == sym1 and num[7-1] == sym2:
                        if num[3-1] != sym1:
                            printgrid(3,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(2,sym2)

                    elif num[5-1] == sym2 and num[3-1] == sym1 and num[7-1] == sym1 and num[4-1] == sym2 and num[6-1] == sym1 and num[9-1] == sym2:
                        if num[1-1] != sym1:
                            printgrid(1,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(2,sym2)

                    elif num[5-1] == sym2 and ( (num[2-1] == sym1 and num[8-1] == sym1) or (num[4-1] == sym1 and num[6-1] == sym1) ) and num[7-1] == sym1 and num[3-1] == sym2:
                        if num[2-1] == sym1 and num[8-1] == sym1 and num[9-1] == sym2:
                            if num[1-1] != sym1:
                                printgrid(1,sym2)
                                print('*****************COMPUTER WON!')
                                break                                
                            else:
                                printgrid(6,sym2)
                                print('*****************COMPUTER WON!')
                                break
                            
                        elif num[4-1] == sym1 and num[6-1] == sym1 and num[1-1] == sym2:
                            if num[2-1] != sym1:
                                printgrid(2,sym2)
                                print('*****************COMPUTER WON!')
                                break                                
                            else:
                                printgrid(9,sym2)
                                print('*****************COMPUTER WON!')
                                break
                          
                    elif num[5-1] == sym2 and ( (num[2-1] == sym1 and num[4-1] == sym1) or (num[2-1] == sym1 and num[7-1] == sym1) ) and num[1-1] == sym2 and num[9-1] == sym1 and num[8-1] == sym2:
                        if num[6-1] != sym1:
                            printgrid(6,sym2)                        
                        else:
                            printgrid(3,sym2)

                    elif num[5-1] == sym2 and ( (num[2-1] == sym1 and num[6-1] == sym1) or (num[2-1] == sym1 and num[9-1] == sym1) ) and num[3-1] == sym2 and num[7-1] == sym1 and num[8-1] == sym2:
                        if num[4-1] != sym1:
                            printgrid(4,sym2)                            
                        else:
                            printgrid(1,sym2)

                    elif num[5-1] == sym2 and ( (num[8-1] == sym1 and num[4-1] == sym1) or (num[8-1] == sym1 and num[1-1] == sym1) ) and num[7-1] == sym2 and num[3-1] == sym1 and num[2-1] == sym2:
                        if num[9-1] != sym1:
                            printgrid(9,sym2)                            
                        else:
                            printgrid(6,sym2)

                    elif num[5-1] == sym2 and  ( (num[8-1] == sym1 and num[6-1] == sym1) or (num[8-1] == sym1 and num[3-1] == sym1) ) and num[9-1] == sym2 and num[1-1] == sym1 and num[2-1] == sym2:
                        if num[7-1] != sym1:
                            printgrid(7,sym2)                            
                        else:
                            printgrid(4,sym2)
                            
                    elif num[5-1] == sym2 and num[4-1] == sym1 and num[9-1] == sym1 and num[7-1] == sym2 and num[3-1] == sym1 and num[6-1] == sym2:
                        if num[1-1] != sym1:
                            printgrid(1,sym2)                            
                        else:
                            printgrid(2,sym2)
                            
                    elif num[5-1] == sym2 and num[4-1] == sym1 and num[3-1] == sym1 and num[1-1] == sym2 and num[9-1] == sym1 and num[6-1] == sym2:
                        if num[7-1] != sym1:
                            printgrid(7,sym2)                            
                        else:
                            printgrid(8,sym2)
                            
                    elif num[5-1] == sym2 and num[1-1] == sym1 and num[6-1] == sym1 and num[3-1] == sym2 and num[7-1] == sym1 and num[4-1] == sym2:
                        if num[8-1] != sym1:
                            printgrid(8,sym2)                            
                        else:
                            printgrid(9,sym2)
                            
                    elif num[5-1] == sym2 and num[6-1] == sym1 and num[7-1] == sym1 and num[9-1] == sym2 and num[1-1] == sym1 and num[4-1] == sym2:
                        if num[2-1] != sym1:
                            printgrid(2,sym2)                            
                        else:
                            printgrid(3,sym2)
                    
                    #player 1st entry at mid
                    elif num[3-1] == sym2 and num[1-1] == sym1 and num[9-1] == sym2 and num[4-1] == sym2:
                        if num[8-1] != sym1:
                            printgrid(8,sym2)                            
                        else:
                            printgrid(2,sym2)
                            
                    elif num[3-1] == sym2 and num[9-1] == sym1 and num[1-1] == sym2 and num[8-1] == sym2:
                        if num[6-1] != sym1:
                            printgrid(6,sym2)                            
                        else:
                            printgrid(4,sym2)
                            
                    elif num[3-1] == sym2 and num[2-1] == sym1 and num[8-1] == sym2 and num[1-1] == sym1 and num[9-1] == sym2:
                        if num[6-1] != sym1:
                            printgrid(6,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(7,sym2)
                            print('*****************COMPUTER WON!')
                            break
                            
                    elif num[3-1] == sym2 and num[2-1] == sym1 and num[8-1] == sym2 and num[9-1] == sym1 and num[1-1] == sym2:
                        if num[4-1] != sym1:
                            printgrid(4,sym2)                            
                        else:
                            printgrid(6,sym2)
                            
                    elif num[3-1] == sym2 and num[2-1] == sym1 and num[8-1] == sym2 and num[4-1] == sym1 and num[6-1] == sym2:
                        if num[9-1] != sym1:
                            printgrid(9,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(1,sym2)
                            
                    elif num[3-1] == sym2 and num[2-1] == sym1 and num[8-1] == sym2 and num[6-1] == sym1 and num[4-1] == sym2:
                        if num[1-1] != sym1:
                            printgrid(1,sym2)                            
                        else:
                            printgrid(9,sym2)
                            
                    elif num[3-1] == sym2 and num[2-1] == sym1 and num[8-1] == sym2 and num[7-1] == sym1 and num[9-1] == sym2:
                        if num[6-1] != sym1:
                            printgrid(6,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(4,sym2)
                            
                    elif num[3-1] == sym2 and num[8-1] == sym1 and num[2-1] == sym2 and num[9-1] == sym2:
                        if num[6-1] != sym1:
                            printgrid(6,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(4,sym2)
                        
                    elif num[3-1] == sym2 and num[4-1] == sym1 and num[6-1] == sym2 and num[1-1] == sym2:
                        if num[2-1] != sym1:
                            printgrid(2,sym2)
                            print('*****************COMPUTER WON!')
                            break                            
                        else:
                            printgrid(8,sym2)
                            
                    elif num[3-1] == sym2 and num[6-1] == sym1 and num[4-1] == sym2 and num[1-1] == sym1 and num[9-1] == sym2:
                        if num[2-1] != sym1:
                            printgrid(2,sym2)                            
                        else:
                            printgrid(8,sym2)
                            
                    elif num[3-1] == sym2 and num[6-1] == sym1 and num[4-1] == sym2 and num[9-1] == sym1 and num[1-1] == sym2:
                        if num[2-1] != sym1:
                            printgrid(2,sym2)                            
                            print('*****************COMPUTER WON!')
                            break
                        else:
                            printgrid(7,sym2)
                            print('*****************COMPUTER WON!')
                            break
                            
                    elif num[3-1] == sym2 and num[6-1] == sym1 and num[4-1] == sym2 and num[2-1] == sym1 and num[8-1] == sym2:
                        if num[1-1] != sym1:
                            printgrid(1,sym2)
                        else:
                            printgrid(9,sym2)
                            
                    elif num[3-1] == sym2 and num[6-1] == sym1 and num[4-1] == sym2 and num[8-1] == sym1 and num[2-1] == sym2:
                        if num[1-1] != sym1:
                            printgrid(1,sym2)
                            print('*****************COMPUTER WON!')
                            break
                        else:
                            printgrid(9,sym2)
                            
                    elif num[3-1] == sym2 and num[6-1] == sym1 and num[4-1] == sym2 and num[7-1] == sym1 and num[9-1] == sym2:
                        if num[2-1] != sym1:
                            printgrid(2,sym2)
                        else:
                            printgrid(8,sym2)
               
                    elif num[3-1] == sym2 and num[7-1] == sym1 and num[1-1] == sym2 and num[8-1] == sym2:
                        if num[4-1] != sym1:
                            printgrid(4,sym2)                        
                        else:
                            printgrid(6,sym2)

            #close: for loops
            #GAME OVER
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        print(format('X '*6,'>45s'))
    #end: while loop
#END OF PLAYER1()
        
def name_symbol():
    #symbol selection
    player_symbol=random.randint(0,1)
    if player_symbol == 1:
        sym1='O' #user1
        sym2='X' #user2
    else:
        sym1='X' #user1
        sym2='O' #user2
            
    #names
    while (1):
        player1=input('\nPlayer 1, please enter your name: ').strip()
        player1=player1.title()
        if player1.isalpha() != True:
            print('Invalid name entry!')
        else:
            print('You are player',sym1)
            break
    while (1):
        player2=input('\nPlayer 2, please enter your name: ').strip()
        player2=player2.title()
        if player2.isalpha() != True:
            print('Invalid name entry!')
        else:
            print('You are player',sym2)
            break
    return player1,sym1,player2,sym2
#END OF NAME_SYMBOL()

def player_2(winner,player1,sym1,player2,sym2):
    #grid numbers
    grid_initial()

    #initial grid
    printgrid(0,'')       
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #1st turn check
    turn=random.randint(1,2)

    #player1 turn
    if turn==1:
        #GAME START
        print('*****************'+player1,'('+sym1+')', 'wins the toss!\n')
        for i in range(1,10):

            #odd turns of 1st player
            if i==1 or i==3 or i==5 or i==7 or i==9:
                print('TURN:',player1)
                check=1
                                
                #Start: inner while checker loop
                while check !=0 :
                    #Choice1 entry
                    while (1):
                        choice1=input(str(player1)+'('+sym1+'), please enter a box number: ').strip()
                        choice1.replace(' ','')
                        if choice1.isdigit() != True or (int(choice1) < 1 or int(choice1) > 9):
                            print('Invalid entry\n')
                        else:
                            choice1=int(choice1)
                            break
                        
                    #choice of symbol placement
                    if num[choice1-1] == choice1:
                        printgrid(choice1,sym1)
                        check=0
                            
                    else:
                        print('The place is already filled\n')
                            
                #checking
                if win_check(1,0,0) == True:
                    print('*****************'+player1,'WON!')
                    winner.append(1)
                    break
                if i == 9:
                    print('*****************IT\'S A DRAW!')
                    winner.append(0)
                    
                #close checker
            #close: odd turns of 1st player
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #start: even turns of 2nd player
            elif i==2 or i==4 or i==6 or i==8:
                print('TURN:',player2)
                check=1
                
                #Start: while checker loop
                while check !=0 :
                    #Choice1 entry
                    while (1):
                        choice2=input(str(player2)+'('+sym2+'), please enter a box number: ').strip()
                        choice2.replace(' ','')
                        if choice2.isdigit() != True or (int(choice2) < 1 or int(choice2) > 9):
                            print('Invalid entry\n')
                        else:
                            choice2=int(choice2)
                            break
                        
                    #choice of symbol placement
                    if num[choice2-1] == choice2:
                        printgrid(choice2,sym2)
                        check=0
                        
                    else:
                        print('The place is already filled\n')                           
                        
                #checking
                if win_check(1,0,0) == True:
                    print('*****************'+player2,'WON!')
                    winner.append(2)
                    break
                
                #close: checker
            #close: even turns of 2nd player
                                
        #GAME END
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------              
    #player2 turn
    elif turn==2:
        #GAME START
        print('*****************'+player2,'('+sym2+')','wins the toss!\n')
        for i in range(1,10):

            #start: odd turns of 2nd player
            if i==1 or i==3 or i==5 or i==7 or i==9:
                print('TURN:',player2)
                check=1

                #start: while checker loop
                while check != 0:
                    #Choice1 entry
                    while (1):
                        choice2=input(str(player2)+'('+sym2+'), please enter a box number: ').strip()
                        choice2.replace(' ','')
                        if choice2.isdigit() != True or (int(choice2) < 1 or int(choice2) > 9):
                            print('Invalid entry\n')
                        else:
                            choice2=int(choice2)
                            break
                        
                    #choice of symbol placement
                    if num[choice2-1] == choice2:
                        printgrid(choice2,sym2)
                        check=0
                            
                    else:
                        print('The place is already filled\n')   
                #checking
                if win_check(1,0,0) == True:
                    print('*****************'+player2,'WON!')
                    winner.append(2)
                    break
                if i == 9:
                    print('*****************IT\'S A DRAW!')
                    winner.append(0)

                #close: checker
            #close: odd turns of 2nd player
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #start: even turns of 1st player
            elif i==2 or i==4 or i==6 or i==8:
                print('TURN:',player1)
                check=1
                            
                #Start: inner while checker loop
                while check !=0 :
                    #Choice1 entry
                    while (1):
                        choice1=input(str(player1)+'('+sym1+'), please enter a box number: ').strip()
                        choice1.replace(' ','')
                        if choice1.isdigit() != True or (int(choice1) < 1 or int(choice1) > 9):
                            print('Invalid entry\n')
                        else:
                            choice1=int(choice1)
                            break
                    
                    #choice of symbol placement
                    if num[choice1-1] == choice1:
                        printgrid(choice1,sym1)
                        check=0
                        
                    else:
                        print('The place is already filled\n')
                        
                #checking
                if win_check(1,0,0) == True:
                    print('*****************'+player1,'WON!')
                    winner.append(1)
                    break
               
                #close choice and checking
            #close: even turns of 1st player
        
        #GAME END
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    print(format('X '*6,'>45s'))
    
    #end: while loop
#END OF PLAYER2()

def tournament():
    winner=[]
    while (1):
        #TOTAL MATCHES
        matches=input('Number of matches: ').strip()
        matches.replace(' ','')
        if matches.isdigit() == True:
            matches=int(matches)
            break
        else:
            print('Invalid Entry!')
            
    player1,sym1,player2,sym2=name_symbol()
    i=1
    while i <= matches:
        print('\nMATCH:',str(i)+'/'+str(matches))
        print('-------------')
        player_2(winner,player1,sym1,player2,sym2)
        if i == matches and winner.count(1) == winner.count(2):
            matches+=1
            print('\n*****************KNOCK OUT ROUND!')
        i+=1
            
        
    #RESULTS
    print('\nRESULT')
    print('------')
    if winner.count(1) > ( winner.count(2) ):
        print(player1,'won the tournament with score',str(winner.count(1))+'/'+str(matches)+'!')
    elif winner.count(2) > ( winner.count(1) ):
        print(player2,'won the tournament with score',str(winner.count(2))+'/'+str(matches)+'!')
#END OF TOURNAMENT()

main()
