import random


class Player:
    '''
    Player class will create player instances.

    Players have a designated symbol that they place in a specific spot on the board each round.
    All data can be retrieved from the get functions.

    Info that can be provided:
    - name of player (through getName())
    - symbol player has chosen (through getSymbol())
    - placement of the symbol the player has chosen (through getChosenPlacement())
    '''

    def __init__(self) -> None:
        '''
        To create a player, there is nothing to enter.
        Player's have default arguments which can all be retrieved through their respective get functions.
        '''
        self._symbol = "X"
        self._placement = "none"
        self._name = "unnamed"

    def getName(self) -> str:
        return self._name.title()

    def getSymbol(self) -> str:
        return self._symbol.upper()

    def getChosenPlacement(self) -> str:
        return self._placement
    

class Person(Player):
    '''
    Person class will create person instances.

    Persons (people) have a designated symbol that they place in a specific spot on the board each round.
    All data can be retrieved from the get functions, same as parent class, and set through set functions.

    Info that can be provided:
    - name of player (through getName())
    - symbol player has chosen (through getSymbol())
    - placement of the symbol the player has chosen (through getChosenPlacement())

    Info that can be set:
    - symbol person chooses
    - name of person
    - where person wishes to place their symbol
    '''

    def __init__(self) -> None:
        '''
        To create a person, there is nothing to enter.
        All default arguments are the same as the parent class, with the exception of _symbolChoices.
        _symbolChoices are the symbol choices the players have. If their choice of symbol is not in 
        _symbolChoices, there will be an error message prompted through the setSymbol() function.
        All person data will be set through the game and the person's set functions. The person's name
        can be set through the setName() function. The symbol the person chooses can be set through the
        setSymbol() function. The location in which the person wants to place their symbol can be set 
        through the setPlacement() function.
        '''
        super().__init__()
        self._symbolChoices = ['X', 'O']

    def setSymbol(self):
        self._symbol = input("What symbol would you like to play? (X or O) ")
        
        while self._symbol.upper() not in self._symbolChoices:
            print("That symbol is invalid. Please choose again thank youuu.")
            self._symbol = input("What symbol would you like to play? (X or O) ")
    
    def setName(self):
        self._name = input("What is your name? ")

    def setPlacement(self):
        self._placement = str(input(f"{self._name.title()}, where would you like to place your token? "))


class Computer(Player):
    '''
    Computer class will create computer instances.

    Computers have a designated symbol that they place in a specific spot on the board each round. It is
    the symbol the person wishes not to choose.
    All data can be retrieved from the get functions, same as parent class. Only placement can be set.

    Info that can be provided:
    - name of player (through getName())
    - symbol player has chosen (through getSymbol())
    - placement of the symbol the player has chosen (through getChosenPlacement())

    Info that can be set:
    - where computer wishes to place their symbol (randomized)
    '''

    def __init__(self, symbol) -> None:
        '''
        To create a computer, you must enter the symbol it will take. It is whichever the person does
        not wish to take. The name is defaulted to Computer. All other arguments are the same as parent
        class. The location in which the person wants to place their symbol can be set 
        through the setPlacement() function.
        '''
        super().__init__()
        self._symbol = symbol
        self._name = "Computer"

    def setPlacement(self):
        self._placement = str(random.randint(1,9)) # computer placements are randomized in this version
        print(f"Computer chose {self._placement}")


class Board():
    '''
    Board class will create board instances.

    Boards have a specific placements the players can choose.
    All data can be retrieved from the get functions. Only placement can be set.

    Info that can be provided:
    - printing of the board (printBoard())
    - the places the players can pick (getPlacementOptions())
    - the placements that are still left/still open (getBoardPlacements())

    Info that can be set:
    - which spots on the board have been taken (through setBoardPlacements(player))
    '''
    
    def __init__(self) -> None:
        '''
        To create a board there are no arguments to enter. 
        The board placements is defaulted. Printing the board, getting and setting boardplacements are
        all done through functions.
        '''
        self._boardPlacements = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
        self._placementOptions = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # only certain placements players can choose

    def printBoard(self):
        print(f"{self._boardPlacements['1']}|{self._boardPlacements['2']}|{self._boardPlacements['3']}")
        print(f"{self._boardPlacements['4']}|{self._boardPlacements['5']}|{self._boardPlacements['6']}")
        print(f"{self._boardPlacements['7']}|{self._boardPlacements['8']}|{self._boardPlacements['9']}")
    
    def getBoardPlacements(self) -> dict:
        return self._boardPlacements
    
    def getPlacementOptions(self) -> list:
        return self._placementOptions

    def setBoardPlacements(self, player1):
        self._boardPlacements[player1.getChosenPlacement()] = player1.getSymbol()


class Game():
    '''
    Game class will create game instances.

    Games play out the game.

    Info that can be provided:
    - getting the players (getPlayers())
    - playing the game (playRounds(board))
    - getting the instructions for the game (getInstructions())
    - getting the winners of the game (getWinners(board))

    Info that can be set:
    - wthe players of the game (setPlayers())
    '''

    def __init__(self) -> None:
        '''
        To create a game, there are no arguments to enter.
        How to win is defaulted, the list of players, the number of rounds, the winner, the
        status of the match are all used in functions.
        '''
        self._winningInstances = [
            ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], 
            ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
            ['1', '5', '9'], ['3', '5', '7']
        ]
        self._listOfPlayers = []
        self._roundCounter = 0
        self._winner = "undecided"
        self._tie = True 

    def getInstructions(self):
        print('''
                    Welcome!!!!!!
                    ~How to Play~
To choose which part of the board, please use this template:
                       |1|2|3|
                       |4|5|6|
                       |7|8|9|

                      Objective:
Get three of your respective symbol in a row, column or diagonal,
        while obstructing the other from being able to. 
                     For example:
                       |X| |O|
                       |X|X|O|
                       |O| |X|
                 In this case, X wins.
            ''')

    def setPlayers(self):
        whoVsWho = int(input("Would you like to play versus a computer (1) or someone else (2)? Please enter 1 or 2 "))
        while whoVsWho not in [1, 2]:
            print("Please enter either 1 (versus computer) or 2 (verson another human)")
            whoVsWho = int(input("Would you like to play versus a computer (1) or someone else (2)? Please enter 1 or 2 "))
        
        if whoVsWho == 1:
            person1 = Person()
            person1.setName()
            person1.setSymbol()

            # deciding which symbol the computer gets
            if person1.getSymbol() == "X":
                computerSymbol = "O"
            else:
                computerSymbol = "X"
            
            self._listOfPlayers.append(person1)
            self._listOfPlayers.append(Computer(computerSymbol))
        
        else: 
            
            # two players so loops twice
            for x in range(1, 3):
                person1 = Person()
                person1.setName()
                person1.setSymbol()
                self._listOfPlayers.append(person1)
            
            while self._listOfPlayers[0].getSymbol() == self._listOfPlayers[1].getSymbol():
                print("Symbol is taken. Please choose again.")
                self._listOfPlayers[1].setSymbol()

    def getPlayers(self) -> list:
        return self._listOfPlayers

    def playRounds(self, board1):
        
        # nine tiles on board therefore can go through nine rounds (1 round = 1 person turn)
        while self._roundCounter < 9:
        
            for player in self._listOfPlayers:
                self._roundCounter += 1
                board1.printBoard()
                player.setPlacement()
                
                while board1.getBoardPlacements()[player.getChosenPlacement()] != ' ':
                    print("Sorry that placement is already taken. Please choose another.")
                    player.setPlacement()
                board1.setBoardPlacements(player)
                
                counter = 0 # counts the iterations and indexs the list
                for instanceSet in self._winningInstances:
                    instanceSet = [player.getSymbol() if z == player.getChosenPlacement() else z for z in instanceSet]
                    self._winningInstances[counter] = instanceSet
                    counter += 1
                    
                    # determining if any players have won
                    if instanceSet == ['X', 'X', 'X']:
                        self._winner = 'X'
                        self._tie = False
                        break
                    elif instanceSet == ['O', 'O', 'O']:
                        self._winner = 'O'
                        self._tie = False
                        break
                    else:
                        continue 
                
                # if no break, the loop will loop infinitely since nested loop breaks, the whole thing must
                if self._tie == False:
                    break
                elif self._roundCounter == 9:
                    break
            
            # if no break, the loop will loop infinitely
            if self._tie == False:
                break
                
    def getWinners(self, board1):
        board1.printBoard()
        if self._tie == False:
            winner = [print(f"Game end. Winner is {player.getName()}!") if player.getSymbol() == self._winner else player for player in self._listOfPlayers]
        else:
            print("Game ends. It's a tie :P")
                

def main():
    '''
    Main function running the game.
    '''
    game1 = Game()
    board1 = Board()
    game1.getInstructions()
    game1.setPlayers()
    game1.playRounds(board1)
    game1.getWinners(board1)

main()

                        

    
