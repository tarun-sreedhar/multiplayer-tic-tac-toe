# Tic Tac Toe

import random

class Game(object):
    # constructor to initialize the board
    def __init__(self,board,isPlaying,player1,player2):
        self.board = board
        self.players = [player1,player2]
        self.isPlaying = isPlaying
    def drawBoard(self):
    # This function prints out the board

    # "board" is a list of 10 strings representing the board (ignore index 0)
      print('   |   |')
      print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
      print('   |   |')
      print('-----------')
      print('   |   |')
      print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
      print('   |   |')
      print('-----------')
      print('   |   |')
      print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
      print('   |   |')
      
    def getPlayerMove(self, player):
    # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(int(move)):
            print()
            print(player.getName() + ': What is your next move? (1-9)')
            move = input()
        return int(move)

    def makeMove(self, letter, move):
        self.board[move] = letter

    def isWinner(self,le):
      bo = self.board  
      # Given a board and a player's letter, this function returns True if that player has won.
      # We use bo instead of board and le instead of letter so we don't have to type as much.
      return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
             (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
             (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
             (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
             (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
             (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
             (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
             (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True

    def isSpaceFree(self,move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

class Player(object):
    def __init__(self,name,letter,turn):
        self.name = name
        self.letter = letter
        self.turn = turn
    def getName(self):
        return self.name
    def getLetter(self):
        return self.letter



print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    print("What is the name of player 1?")
    p1 = input()
    print("What is the name of player 2?")
    p2 = input()
    turn = random.randint(1, 2)
    letter = ''
    print('Player '+str(turn)+' has been randomly selected to go first. Please pick a letter. (X or O)')
    while not (letter == 'X' or letter == 'O'):
        letter = input().upper()
    letter2 = 'X'
    if (letter == 'X'):
        letter2 = 'O'
    if (turn == 1):
    # player1 goes first
       player1 = Player(p1,letter,1)
       player2 = Player(p2,letter2,2)
    else:
    # player2 goes first
       player1=Player(p1,letter2,2)
       player2=Player(p2,letter,1)
    theGame = Game(theBoard,True,player1,player2)
    while theGame.isPlaying:
        if turn == 1:
            # Player 1's turn.
            theGame.drawBoard()
            move = theGame.getPlayerMove(player1)
            theGame.makeMove(player1.getLetter(), move)

            if theGame.isWinner(player1.getLetter()):
                theGame.drawBoard()
                print('Hooray! '+player1.getName()+' has won the game!')
                theGame.isPlaying=False
            else:
                if theGame.isBoardFull():
                    theGame.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 2

        else:
            if turn == 2:
                # Player 2's turn.
                theGame.drawBoard()
                move = theGame.getPlayerMove(player2)
                theGame.makeMove(player2.getLetter(), move)

                if theGame.isWinner(player2.getLetter()):
                    theGame.drawBoard()
                    print('Hooray! '+player2.getName()+' has won the game!')
                    theGame.isPlaying = False
                else:
                    if theGame.isBoardFull():
                        theGame.drawBoard()
                        print('The game is a tie!')
                        break
                    else:
                        turn = 1

    if not theGame.playAgain():
        break
