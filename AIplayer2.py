# Global variable
import random 

def Freespace(board, move):
  return Board[move] == ''

#G
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

#determines the AI's Letter either it being X or O based of player 1
# Determines where the computer can move on the board
def Ply2Turn(board,computer):
  If Ply2Turn =='X':
    playerturn == 'O'
  else:
    Ply2Turn == 'O'
    
  for row in range(0,9):
    copy = printboard()
    if FreeSpace(copy, row):
      AImove(copy, Ply2Turn, row)
      if winstate(copy, Ply2Turn):
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
  
      
  
  
    
