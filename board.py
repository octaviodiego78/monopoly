import numpy 
import random
from typing import List
from utils.__init__ import getSquaresInfo, getChanceCards


class Player():

    def __init__(self, playerNumber: int, properties: list[object]) -> None:
        self.playerNumber = playerNumber      
        self.properties = properties

    money = 2500 #All players have the same money when starting
    position = 0
    jail = False

class Properties():
    def __init__(self, **kwargs) -> None:
        for k,v in kwargs.items():
            setattr(self, k, v)

class Monopoly():
   
    def __init__(self, players: List[object]) -> None:
        self.players = players

    rounds = 1
    chanceCards = getChanceCards()
    properties = [Properties(**pm) for pm in getSquaresInfo()]

    print(vars(properties[0]))


    
    def roll_dice(self) -> int:
        return random.randint(1, 6)


    def turn(self,player: object):

        if player.jail == True:
            print(f"Player{player.playerNumber} in jail")
            player.jail = False
        
        else:
            #Roll dice
            dice = self.roll_dice() #why do i need to use self to call function inside the same class?
        
            lastPosition = player.position #Last position
            player.position = (player.position + dice) % 40 #New position

            #Give player $200 if they complete a round
            if player.position < lastPosition:
                player.money +=  200

            print(f"Player {player.playerNumber} - Dice {dice} - Last Position {lastPosition} - Position {player.position} - Money {player.money}")

            #Jail ------------------------------->
            if player.position == 10:
                player.jail = True

            elif player.position == 30:
                player.jail = True
                player.position = 10

            #Chance Cards ----------------------->
            if player.position in (2,7,17,22,33,36):
                print("Chance carrd or chest")
                player.money += random.choice(self.chanceCards)

            #Taxes ------------------------------>
            if player.position == 4:
                print("taxes")
                player.money -= 200

            if player.position in (12,29):
                print("taxes")
                player.money -= 150

            if player.position == 38:
                print("taxes")
                player.money -= 100

            #Railroads
            


            #Mutate position and money of player
            ...

    def round(self,players: List[object]):
        #Make a turn for all players
        #print(f"Round: {self.rounds}")
        for p in players:
            self.turn(p)
        self.rounds += 1




    

def main(n_players):

    #Creating players
    players = []

    for i in range(n_players):
        players.append(Player(i,[]))

    #Monopoly creating
    game = Monopoly(players)


    #Games goes on until someone gets out of money
    playerWithLessMoney = min([p.money for p in game.players])
    
    #while playerWithLessMoney > 0:
    for i in range(1):

        game.round(players)
        playerWithLessMoney = min([p.money for p in game.players])


    


if __name__ == '__main__':
    main(1)




