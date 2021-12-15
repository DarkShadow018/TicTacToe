import numpy

board = numpy.zeros((3, 3)).astype(int) #astype(int) coz each player will be considered as an integer

def play_turn(): #custom Function for players turn

   x = int(input(f"What is player {turn}'s x position?")) #taking x position from both the players
   y = int(input(f"What is player {turn}'s y position?")) #taking y position from both the players

   try:
       if board[y, x] == 0: #default board input
           board[y, x] = turn #taking input in the specific position

       else:
           play_turn() #taking input in the specific position

   except IndexError:
       play_turn() #if the player didnt provided with any position then it will terminate the program

def check_win(): #custom function to check who won the game

    if any(numpy.sum(board, 1) == 3) or any(numpy.sum(board, 0) == 3) or sum(numpy.diag(board)) == 3 or sum(numpy.diag(board[::-1])) == 3:
        return True #checking for player 1(1)                     at this point we are checking diagonally and here we are slicing the board

    if any(numpy.sum(board, 1) == -3) or any(numpy.sum(board, 0) == -3) or sum(numpy.diag(board)) == -3 or sum(numpy.diag(board[::-1])) == -3:
        return True #checking for player 2(-1)                    at this point we are checking diagonally and here we are slicing the board
    return False #if the no input is provided by the player then it will return nothing

turn = 1 #player 1 turn
move = 9 #total number of moves

while move > 0: #loop to take input and print at specific position
    print(board) #printing the game board
    play_turn() #using the custom function for player turn
    if check_win(): #using the custom function to check who won the game
        print(f"Player {turn} won the game")
        break
    turn = turn * -1 #for "player 1" and for "player -1"
    move = move -1 #for python indexing . . . [0, 1, 2]