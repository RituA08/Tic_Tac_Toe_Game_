
#importing tkinter to make interface
import tkinter as tk 
import tkinter.messagebox

#setting up window 
root = tk.Tk()

#setting window dimensions 
root.geometry("270x150")

#making our internal board for the program(not shown to user, used for determining winner) 
myboard = {'1': ' ', '2': ' ', '3':' ', 
'4': ' ', '5': ' ', '6': ' ',
'7': ' ', '8': ' ', '9': ' '}

#defining the first turn and the count 
turn = 'X'
count= 0 

#function that fills the board with moves and calculates winner at the end 
def move(box, row, column, label):

    #defining turn and count as global variables 
    global turn 
    global count 

    #if the picked box already has X or O , display an error message 
    if box['text'] == 'X' or box['text'] == 'O':
        tk.messagebox.showinfo('Error', 'Cannot move there')
    else: 
        # fill the empty gui box with an X or O
        box = tk.Button(root, text=turn, fg='black', bg='white',
                    command=None, height=1, width=7)
        box.grid(row=row, column=column)
        #fill our internal board with the turn 
        myboard[label] = turn
    
    #switch turns 
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

    #update count 
    count += 1 

    #-----------Calculating a winner-------------------
    win = True     

    #if count is 9, the game has ended, all possible boxes have been filled 
    if count == 9:

        #check all rows 
        if myboard['1'] == myboard['2'] == myboard['3'] == 'X':
            tk.messagebox.showinfo('Winner!!!', 'Player X Wins')
        elif myboard['1'] == myboard['2'] == myboard['3'] == 'O':
            tk.messagebox.showinfo('Winner!!!', 'Player O Wins')
        elif myboard['4'] == myboard['5'] == myboard['6'] == 'X':
            tk.messagebox.showinfo('Winner!!!', 'Player X Wins')
        elif myboard['4'] == myboard['5'] == myboard['6'] == '0':
            tk.messagebox.showinfo('Winner!!!', 'Player O Wins')
        elif myboard['7'] == myboard['8'] == myboard['9'] == 'X':
            tk.messagebox.showinfo('Winner!!!', 'Player X Wins')
        elif myboard['7'] == myboard['8'] == myboard['9'] == 'O':
            tk.messagebox.showinfo('Winner!!!', 'Player O Wins')
        else:
            win = False 

        #if no winner is found yet, check the columns 
        if win is False:
            if myboard['1'] == myboard['4'] == myboard['7'] == 'X':
                tk.messagebox.showinfo('Winner!!!', 'Player X Wins')
                win = True 
            elif myboard['1'] == myboard['4'] == myboard['7'] == 'O':
                tk.messagebox.showinfo('Winner!!!', 'Player O Wins')
                win = True 
            elif myboard['2'] == myboard['5'] == myboard['8'] == 'X':
                tk.messagebox.showinfo('Winner!!!', 'Player X Wins')
                win = True 
            elif myboard['2'] == myboard['5'] == myboard['8'] == '0':
                tk.messagebox.showinfo('Winner!!!', 'Player O Wins')
                win = True 
            elif myboard['3'] == myboard['6'] == myboard['9'] == 'X':
                tk.messagebox.showinfo('Winner!!!', 'Player X Wins')
                win = True 
            elif myboard['3'] == myboard['6'] == myboard['9'] == '0':
                tk.messagebox.showinfo('Winner!!!', 'Player O Wins')
                win = True 

        #if no winner is found, check the diagonals 
        if win is False:
            if myboard['1'] == myboard['5'] == myboard['9'] == 'X':
                tk.messagebox.showinfo('Winner!!!', 'Player X Wins')
                win = True 
            elif myboard['1'] == myboard['5'] == myboard['9'] == 'O':
                tk.messagebox.showinfo('Winner!!!', 'Player O Wins')
                win = True 
            elif myboard['3'] == myboard['5'] == myboard['7'] == 'X':
                tk.messagebox.showinfo('Winner!!!', 'Player X Wins')
                win = True 
            elif myboard['3'] == myboard['5'] == myboard['7'] == '0':
                tk.messagebox.showinfo('Winner!!!', 'Player O Wins')
                win = True 

        #if still no winner is found, declare a tie 
        if win is False:
            tk.messagebox.showinfo('No Win!', 'Its a tie!')

        return 

#Displaying our gui tictactoe squares 
box1 = tk.Button(root, text='', fg='black', bg='white',
                    command=lambda: move(box1, box1.grid_info()['row'],box1.grid_info()['column'], label='1'), height=1, width=7)
box1.grid(row=2, column=0)

box2 = tk.Button(root, text='', fg='black', bg='white',
                    command=lambda: move(box2, box2.grid_info()['row'],box2.grid_info()['column'],label='2'), height=1, width=7)
box2.grid(row=2, column=1)
 
box3 = tk.Button(root, text='', fg='black', bg='white',
                    command=lambda: move(box3, box3.grid_info()['row'],box3.grid_info()['column'],label='3'), height=1, width=7)
box3.grid(row=2, column=2)
 
box4 = tk.Button(root, text='', fg='black', bg='white',
                    command=lambda: move(box4, box4.grid_info()['row'],box4.grid_info()['column'],label='4'), height=1, width=7)
box4.grid(row=3, column=0)
 
box5 = tk.Button(root, text='', fg='black', bg='white',
                    command=lambda: move(box5, box5.grid_info()['row'],box5.grid_info()['column'],label='5'), height=1, width=7)
box5.grid(row=3, column=1)
 
box6 = tk.Button(root, text='', fg='black', bg='white',
                    command=lambda: move(box6, box6.grid_info()['row'],box6.grid_info()['column'],label='6'), height=1, width=7)
box6.grid(row=3, column=2)
 
box7 = tk.Button(root, text='', fg='black', bg='white',
                    command=lambda: move(box7, box7.grid_info()['row'],box7.grid_info()['column'],label='7'), height=1, width=7)
box7.grid(row=4, column=0)
 
box8 = tk.Button(root, text='', fg='black', bg='white',
                    command=lambda: move(box8, box8.grid_info()['row'],box8.grid_info()['column'],label='8'), height=1, width=7)
box8.grid(row=4, column=1)
 
box9 = tk.Button(root, text='', fg='black', bg='white',
                    command=lambda: move(box9, box9.grid_info()['row'],box9.grid_info()['column'],label='9'), height=1, width=7)
box9.grid(row=4, column=2)

root.mainloop()