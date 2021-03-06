
#creating the empty squares in the board
myboard = {'1': ' ', '2': ' ', '3':' ', 
'4': ' ', '5': ' ', '6': ' ',
'7': ' ', '8': ' ', '9': ' '}

#creating our tic tac toe board
def boardvisual(myboard):
    print(myboard['1'] + '|' + myboard['2'] + '|' + myboard['3'])
    print('-+-+-')
    print(myboard['4'] + '|' + myboard['5'] + '|' + myboard['6'])
    print('-+-+-')
    print(myboard['7'] + '|' + myboard['8'] + '|' + myboard['9'])

boardvisual(myboard)

win = False  
#main function to play the game
def play(win):

    turn = 'X'
    count = 0 

    for i in range(9):
        
        if win == False:
            print('its {} turn'.format(turn))
            print('Where would you like to move?')

            move = input()

            if myboard[move] != 'X' and myboard[move] != 'O':
                myboard[move] = turn 
                boardvisual(myboard)
            else:
                print('cannot move to that place')
                move = input()

            if turn == 'X':
                turn = 'O'
            else: 
                turn = 'X'
        
            count += 1 

        if count >= 5:
            #check the rows  
            if myboard['1'] == myboard['2'] == myboard['3'] == 'X':
                print('player X has won')
                win = True 
            elif myboard['1'] == myboard['2'] == myboard['3'] == 'O':
                print('player O has won')
                win = True 
            elif myboard['4'] == myboard['5'] == myboard['6'] == 'X':
                print('player X has won')
                win = True 
            elif myboard['4'] == myboard['5'] == myboard['6'] == '0':
                print('player O has won')
                win = True 
            elif myboard['7'] == myboard['8'] == myboard['9'] == 'X':
                print('player X has won')
                win = True 
            elif myboard['7'] == myboard['8'] == myboard['9'] == 'O':
                print('player O has won')
                win = True 

            #if no winner is found, check the columns 
            if win == False:
                if myboard['1'] == myboard['4'] == myboard['7'] == 'X':
                    print('player X has won')
                    win = True 
                elif myboard['1'] == myboard['4'] == myboard['7'] == 'O':
                    print('player O has won')
                    win = True
                elif myboard['2'] == myboard['5'] == myboard['8'] == 'X':
                    print('player X has won')
                    win = True
                elif myboard['2'] == myboard['5'] == myboard['8'] == '0':
                    print('player O has won')
                    win = True
                elif myboard['3'] == myboard['6'] == myboard['9'] == 'X':
                    print('player X has won')
                    win = True
                elif myboard['3'] == myboard['6'] == myboard['9'] == '0':
                    print('player O has won')
                    win = True

            #if winner is still false check the diagonals 
            if win == False:
                if myboard['1'] == myboard['5'] == myboard['9'] == 'X':
                    print('player X has won')
                    win = True 
                elif myboard['1'] == myboard['5'] == myboard['9'] == 'O':
                    print('player O has won')
                    win = True 
                elif myboard['3'] == myboard['5'] == myboard['7'] == 'X':
                    print('player X has won')
                    win = True 
                elif myboard['3'] == myboard['5'] == myboard['7'] == '0':
                    print('player O has won')
                    win = True 

            #if still no winner is found, declare a tie 
            if win == False and count == 9:
                print('its a tie!')

play(win)
