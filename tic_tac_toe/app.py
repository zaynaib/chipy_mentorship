class TicTacToe:
    def __init__(self):
        self.board=[['*','*','*','*','*','*','*','*','*']]
        #self.player = None

    def playerSetup(self):
        num = input('Are you Player number 1 or number 2?')
        mark = ''
        turn = None
        name = None
        if int(num) == 1:
            self.player.name = 'Player1'
            self.player.mark = 'X'
            self.player.turn = True
        else:
            self.player.name = 'Player2'
            self.player.mark = 'O'
            self.player.turn = False

    def boardUpdate(self,board,player):
        your_turn = input("Where do you want to place your Mark? ex: 0,0")
        place = [your_turn[0],your_turn[2]]

        if self.player.name == 'Player1':
            self.board[place] = 'X'
        else:
            self.board[place] = 'O'

        if self.player.turn == True:
            self.player.turn = False
        else:
            self.player.turn = True

    def checkWins(self,board,player):
        '''
            This is psudeo code to list the number of ways a player could win

            if all the columns are the same or if all the rows are the same then the player has one

            player can win diagonal way as well
            if 0,0 - 1,1 -1,2 
            or 2,0 - 1,1 - 0,2


        '''
game = TicTacToe()
print(game.board)

print(game.playerSetup())

    
        