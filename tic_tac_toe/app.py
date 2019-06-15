class TicTacToe:
    def __init__(self):
        self.board=[['*','*','*'],['*','*','*'],['*','*','*']]
        self.Player1 = {'mark':'X','turn': True}
        self.Player2 = {'mark':'O', 'turn': False}

    def boardUpdate(self):

        your_turn = input("Where do you want to place your Mark? ex: 0,0 \n")
        #place = [your_turn[0],your_turn[2]]

        if self.Player1['turn'] == True:
            self.board[int(your_turn[0])][int(your_turn[2])] = self.Player1['mark']

            #make player 1 false and then make it players 2 turn
            self.Player1['turn'] = False
            self.Player2['turn'] = True

            #print(self.Player1['turn'], self.Player2['turn'])
            #print(self.board)


        elif self.Player2['turn'] == True:
            self.board[int(your_turn[0])][int(your_turn[2])] = self.Player2['mark']
            self.Player2['turn'] = False
            self.Player1['turn'] = True

            #print(self.Player1['turn'], self.Player2['turn'])
            #print(self.board)


        print(self.board)

    def checkWins(self):
        '''
            This is psudeo code to list the number of ways a player could win

            if all the columns are the same or if all the rows are the same then the player has one

            player can win diagonal way as well
            if 0,0 - 1,1 -1,2 
            or 2,0 - 1,1 - 0,2


        '''
        gameIsDone = False

        if self.board[0][0] == self.board[0][1] and self.board[0][0] == self.board[0][2] and self.board[0][1] == self.board[0][1]:
            print("Game has been won fool!")
            gameIsDone = True
        
        if self.board[1][0] == self.board[1][1] and self.board[1][0] == self.board[1][2] and self.board[1][1] == self.board[1][2]:
            print("Game has been won fool!")
            gameIsDone = True

        if self.board[2][0] == self.board[2][1] and self.board[2][0] == self.board[2][2] and self.board[2][1] == self.board[2][2]:
            print("Game has been won fool!")
            gameIsDone = True

        if self.board[0][1] == self.board[1][1] and self.board[0][1] == self.board[2][1] and self.board[2][1] == self.board[1][1]:
            print("Game has been won fool!")
            gameIsDone = True

        if self.board[0][2] == self.board[1][2] and self.board[0][2] == self.board[2][2] and self.board[1][2] == self.board[2][2]:
            print("Game has been won fool!")
            gameIsDone = True


        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[1][1] == self.board[2][2]:
            print("Game has been won fool!")
            gameIsDone = True

        return gameIsDone
        
    def gameSetup(self):

        while game.checkWins() == False:
            game.boardUpdate()


        
game = TicTacToe()
print(game.board)

myboard = game.board
'''
game.boardUpdate()
game.boardUpdate()
game.boardUpdate()
'''

game.gameSetup()



    
        