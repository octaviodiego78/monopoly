import numpy 
import random
from typing import List
from utils.__init__ import getSquaresInfo, getChanceCards

"""Move money, position, and jail attributes into _init_ in the Player class: These should be instance attributes, not class attributes. Class attributes are shared across all instances of the class, which isn't what you want for individual players.
Change Properties class name to Property: It's a common practice to use singular names for classes.
Integrate the Property class with the Monopoly class: You mentioned that Property does not exist inside the Monopoly class, but you want to relate it to the players. We can create a list of properties as a class attribute in Monopoly and assign owners as Player objects.
Correcting turn and round methods: I'll adjust the methods to make them more consistent and efficient."""


class Player():

    def __init__(self, playerNumber: int, properties: list[object]) -> None:
        self.playerNumber = playerNumber      
        self.properties = properties

        self.money = 2500  #All players have the same money when starting
        self.position = 0
        self.jail = False
        self.railroads = 0

class Property():
    def __init__(self, **kwargs) -> None:
        for k,v in kwargs.items():
            setattr(self, k, v)

class Monopoly():
   
    def __init__(self, players: List[object]) -> None:
        self.players = players

    class Property():
     def __init__(self, **kwargs) -> None:
        for k,v in kwargs.items():
            setattr(self, k, v)

    rounds = 1
    chanceCards = getChanceCards()
    
    properties = [Property(**pm) for pm in getSquaresInfo()] #Create a list of Property objects
                                                                #Each object recieves a dict and create a Property object setting the k,v of the dict 
                                                                # as attributes of the said object
 
    print(properties[0].owner)

    def roll_dice(self) -> int:
        return random.randint(1, 6)
    
    def binaryChoice():
        return random.choice([True, False])
    
    def housesChoice(n):
        return random.randint(1, n)


    def turn(self,player: Player):

        if player.jail == True:
            print(f"Player{player.playerNumber} in jail")
            player.jail = False
        
        else:
            #Roll dice
            dice = self.roll_dice()
        
            lastPosition = player.position #Last position
            player.position = (player.position + dice) % 40 #New position

            #Give player $200 if they complete a round
            if player.position < lastPosition:
                player.money +=  200

            #print(f"Player {player.playerNumber} - Dice {dice} - Last Position {lastPosition} - Position {player.position} - Money {player.money}")

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


            #Mutate position and money of player
            currentProperty = self.properties[player.currentPosition] #does properties need a self because it's created inside a method from monopoly class?

            if player.position in (5,15,25,35): #If position is a railroad
                
                if currentProperty.owner != player: #If the owner of the railroad is not the player
                    if currentProperty.owner == None:  #if no one is the owner
                        if player.money > currentProperty.price and self.binaryChoice(): #option to buy it
                            currentProperty.owner = player
                            player.money -= currentProperty.price
                            player.railroads += 1
                    else:
                        rentToPay =  currentProperty.owner.railroads*50
                        currentProperty.owner += rentToPay
                        player -= rentToPay
            
            else:
                if currentProperty.owner == player: 
                    #Simulating the player decision to add a house or many  to the property
                        #For properties with less than 5 house
                        #Only is your simulated descition to buy a house is True
                        #If you have enough money for houses
                    propertyHouses = currentProperty.houses
                    if (5 - propertyHouses) > 0 and (player.money > ((5 - propertyHouses)*currentProperty.costPerHouse)) and self.binaryChoice: 

                        housesToAdd = self.housesChoice(5 - propertyHouses) #Decide houses to add
                        currentProperty.houses += housesToAdd               #Update amount of houses on property
                        player.money -= currentProperty.costPerHouse * housesToAdd  #Pay for the houses
                        currentProperty.rent = currentProperty.rentWithHouses[currentProperty.houses -1]    #Set rent to the price with n houses

                else:
                    if currentProperty.owner == None:
                        if self.binaryChoice():
                            player.money -=  currentProperty.price #Pay for the property 
                            currentProperty.owner = player #Update property owner

                    else:
                        #Paying rent to the owner
                        player.money -= currentProperty.rent
                        currentProperty.owner.money += currentProperty.rent
                    
    



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
    monopoly = Monopoly(players)
  
    #while min([p.money for p in game.players]) > 0:
    for i in range(1):

        monopoly.round(players)


    


if __name__ == '__main__':
    main(1)




