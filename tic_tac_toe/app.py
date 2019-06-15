class TicTacToe:
    def __init__(self):
        self.board=[['*','*','*','*','*','*','*','*','*']]
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

            print(self.Player1['turn'], self.Player2['turn'])
            print(self.board)


        elif self.Player2['turn'] == True:
            self.board[int(your_turn[0])][int(your_turn[2])] = self.Player2['mark']
            self.Player2['turn'] = False
            self.Player1['turn'] = True

            print(self.Player1['turn'], self.Player2['turn'])
            print(self.board)


        #print(self.board)

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
game.boardUpdate()
game.boardUpdate()
game.boardUpdate()



    
        