import numpy 
import random


class Player():

    def __init__(self, playerNumber: int, properties: list[object]) -> None:
        self.playerNumber = playerNumber
        
        self.properties = properties

    initialMoney = 200 #All players have the same money

class Monopoly():

    def __init__(self, players: list[object]) -> None:
        self.players = players


    def roll_dice() -> int:
        return random.randint(1, 6)

    
    throws = 0

class Board():
    pass

def main(n_players):

    #Creating players
    players = []

    for i in range(n_players):
        players.append(Player(i,[]))

    game = Monopoly(players)









if __name__ == '__main__':
    main(4)

