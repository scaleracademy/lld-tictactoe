from player import Player
from cell import Cell
class Game:
    def __init__(self) -> None:
        self.players = []
        self.moves = []
        self.grid = [["_"]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.grid[i][j] = Cell(i+1, j+1)

        self.row = {}
        self.col = {}
        self.pdig = {}
        self.ndig = {}

    def printGrid(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j].player:
                    value = self.grid[i][j].player
                    print(value.symbol, end=" ")
                else:
                    print("_", end=" ")
            print()
    
    def getPlayerDetails(self):
        for i in range(2):
            player = Player()
            player.name  = input("Enter your name: ")
            player.symbol = input("Which symbol would you choose? X or O: ")
            self.players.append(player)

        self.row = {1: {val:0 for val in self.players}, 2: {val:0 for val in self.players}, 3: {val:0 for val in self.players}}
        self.col = {1: {val:0 for val in self.players}, 2: {val:0 for val in self.players}, 3: {val:0 for val in self.players}}
        self.pdig = {val:0 for val in self.players}
        self.ndig = {val:0 for val in self.players}

    def printPlayerDetails(self):
        print("Players who are playing are:")
        for i in range(2):
            print("Player{}".format(i+1), end=": ")
            player = self.players[i]
            print(player.name, player.symbol)

    def startTheGame(self):
        playerTurn = 0
        moves = 9
        while moves:
            print("Player{} make a move".format(playerTurn+1), end="")
            print()
            x, y = map(int, input("Enter the cell where you want to place in 3X3 grid (space seperated x(0,1,2) & y(0,1,2))").split())
            
            cell = self.grid[x][y]
            if cell.player:
                print("Invalid Move, try again with a valid place(x & y)")
                continue
            else:
                cell.player = self.players[playerTurn]
            player = self.players[playerTurn]
            self.row[x+1][player] += 1
            
            self.col[y+1][player] += 1
            
            if (x==y): self.pdig[player] += 1
            
            if (x+y == 2): self.ndig[player] += 1

            validation = self.gameCompletionValidation(x+1, y+1, player)
            if validation:
                self.printGrid()
                print("{} won the match".format(validation.name))
                return
            playerTurn = (playerTurn+1)%2
            self.printGrid()
            moves-=1

        print("Game Over!!! It's a draw.")
        return 

    
    def gameCompletionValidation(self, x, y, player):

        if self.row[x][player] == 3 or \
           self.col[y][player] == 3 or \
           self.pdig[player] == 3 or \
           self.ndig[player] == 3:
                return player 
        else:
            return False
        