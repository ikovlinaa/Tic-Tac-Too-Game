#TikTacToo(X-O-X) Game

winner = [0]

board = [[" "," "," "]  #Empty game board
         ,[" "," "," "]
         ,[" "," "," "]]

def print_normal_board(board): #Drawing the start table
  print("",board[0][0]+"1","|",board[0][1]+"2", "|",board[0][2]+"3")
  print("---+---+---")
  print("",board[1][0]+"4","|",board[1][1]+"5", "|",board[1][2]+"6")
  print("---+---+---")
  print("",board[2][0]+"7","|",board[2][1]+"8", "|",board[2][2],"9")


def print_board(board,number,x_y): #Drawing the game table
  if number == 1:
    board[0][0] = x_y
  elif number == 2:
    board[0][1] = x_y
  elif number == 3:
    board[0][2] = x_y
  elif number == 4:
    board[1][0] = x_y
  elif number == 5:
    board[1][1] = x_y
  elif number == 6:
    board[1][2] = x_y
  elif number == 7:
    board[2][0] = x_y
  elif number == 8:
    board[2][1] = x_y
  elif number == 9:
    board[2][2] = x_y

  print("",board[0][0],"|",board[0][1], "|",board[0][2])
  print("---+---+---")
  print("",board[1][0],"|",board[1][1], "|",board[1][2])
  print("---+---+---")
  print("",board[2][0],"|",board[2][1], "|",board[2][2])


def finish_the_game1(board,x_or_y): #Ending the game when someone wins horizontally with x/o
  if board[0][0] == x_or_y and board[0][1] == x_or_y and board[0][2] == x_or_y:
    print(x_or_y.upper()," Won!")
    winner[0] = 1
  elif board[1][0] == x_or_y and board[1][1] == x_or_y and board[1][2] == x_or_y:
    print(x_or_y.upper()," Won!")
    winner[0] = 1
  elif board[2][0] == x_or_y and board[2][1] == x_or_y and board[2][2] == x_or_y:
    print(x_or_y.upper()," Won!")
    winner[0] = 1

def finish_the_game2(board,x_or_y): #Ending the game when someone wins vertically with x/o 
  if board[0][0] == x_or_y and board[1][0] == x_or_y and board[2][0] == x_or_y:
    print(x_or_y.upper()," Won!")
    winner[0] = 1
  elif board[0][1] == x_or_y and board[1][1] == x_or_y and board[2][2] == x_or_y:
    print(x_or_y.upper()," Won!")
    winner[0] = 1
  elif board[0][2] == x_or_y and board[1][2] == x_or_y and board[2][2] == x_or_y:
    print(x_or_y.upper()," Won!")    
    winner[0] = 1


def finish_the_game3(board,x_or_y): #Ending the game when someone wins diagonally with x/o
  if board[0][0] == x_or_y and board[1][1] == x_or_y and board[2][2] == x_or_y:
    print(x_or_y.upper()," Won!")
    winner[0] = 1
  elif board[0][2] == x_or_y and board[1][1] == x_or_y and board[2][0] == x_or_y:
    print(x_or_y.upper()," Won!")
    winner[0] = 1



def finish_the_game(board):
  finish_the_game1(board,"x")
  finish_the_game1(board,"y")
  finish_the_game2(board,"x")
  finish_the_game2(board,"y")
  finish_the_game3(board,"x")
  finish_the_game3(board,"y")

def play_game(board): #The function to play the game
  print_normal_board(board)
  while winner[0] != 1:
    x_turn = int(input("X: Enter the number : "))
    print("\n")
    print_board(board,x_turn,"x")
    finish_the_game(board)
    if winner[0] == 1:
      break
    y_turn = int(input("Y: Enter the number : "))
    print("\n")
    print_board(board,y_turn,"y")
    finish_the_game(board)
    if winner[0] == 1:
      break

play_game(board)

#Coded By Emir ÇİÇEK
