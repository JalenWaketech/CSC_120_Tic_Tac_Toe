# Global variable
import random 

def Freespace(board, move):
  return Board[move] == ''

#Where on the board the AI moved and placing down the letter
def AImove(board, letter, move):
  board[move] = letter

# Does a valid move from the lsit on the past board
#returns None if there are no valid moves
def RandomMove(board, mlist):
  pMoves = []
  for i in mlist:
    if row in mlist:
     if Freespace(board, row):
      pMoves.append(row)

# Determines where the computer can move on the board
def Ply2Turn(board, letter):
  letter = 'O'
    
  for row in range(0,9):
    copy = printboard()
    if FreeSpace(copy, row):
      AImove(copy, letter, row)
      if winstate(copy, letter):
        return row
   
  #Blocking Player 1 moves
  for row in range(0,9):
    copy = printboard(board)
    if FreeSpace(copy, row):
      AImove(copy, playerturn, row)
      if winstate(copy, playerturn):
        return row
      
  #AI player corner moves
  Cmove = RandomMove(board, [0, 2, 6, 8])
  if Cmove != None:
    return Cmove
      
  #AI player takes middle square if the position is free on the board
  if FreeSpace(board, 4):
    return 4
  
  #AI player side moves
  return RandomMove(board, [1, 3, 5, 7])
  
      
  
  
    
