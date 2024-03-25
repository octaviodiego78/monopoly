import numpy 
import random
from typing import List
from utils.__init__ import getSquaresInfo, getChanceCards
import pandas as pd
import time






class Player():

    def __init__(self, playerNumber: int, properties: list[object]) -> None:
        self.playerNumber = playerNumber      
        self.properties = properties
        self.money = 2500  
        self.land_value = 0
        self.position = 0
        self.jail = False
        self.railroads = 0
        self.houses = 0
        self.rent_to_charge = 0

class Property():
    def __init__(self, **kwargs) -> None:
        for k,v in kwargs.items():
            setattr(self, k, v)

class Monopoly():
   
    def __init__(self, players: List[Player]) -> None:
        self.players = players
        self.results = pd.DataFrame(
            columns = ["player_number"
                        ,"last_position"
                        ,"dice"
                        ,"current_position"
                        ,"jail"
                        ,"is_special_position"
                        ,"money"
                        ,"properties"
                        ,"networth"
                        ,"owned_properties_price"
                        ,"owned_properties_houses"
                        ,"rent_to_charge"
                        ,"percentage_of_owned_properties"
                        ,"railroads_owned"
                        ,"properties_available"
                        ,"buy"
                        ,"money2"
                        ,"properties2"
                        ,"networth2"
                        ,"owned_properties_price2"
                        ,"owned_properties_houses2"
                        ,"rent_to_charge2"
                        ,"percentage_of_owned_properties2"
                        ,"railroads_owned2"
                        ,"properties_available2"])


    rounds = 1
    chanceCards = getChanceCards()
    
    properties = [Property(**pm) for pm in getSquaresInfo()] #Create a list of Property objects
                                                                #Each object recieves a dict and create a Property object setting the k,v of the dict 
                                                                # as attributes of the said object
 

    def roll_dice(self) -> int:
        return random.randint(1, 6)
    
    def binaryChoice(self):
        return random.choice([True, False])
    
    def housesChoice(self,n):
        return random.randint(1, n)


    def turn(self,player: Player):

        choice = self.binaryChoice() 
        lastPosition = player.position


        if player.jail == True:
            player.jail = False

            dice = 0
            player.position = (player.position + dice) % 40 #New position
            qt = [player.playerNumber #Player number
                ,lastPosition #Last position
                , dice #Dice
                , player.position #New position
                , player.jail #Jail
                , self.properties[player.position].isSpecialSquare #Special position
                , player.money #Money
                , len(player.properties) #Number of properties owned
                , player.money + sum([p.price for p in player.properties]) #networth
                , sum([p.price for p in player.properties]) #Owned Properties price 
                , sum([p.houses for p in player.properties]) #Owned properties Houses
                , sum([p.rent for p in player.properties]) #Rent to charge
                , round(len(player.properties) / 28,2) #Percentage of properties owned
                , player.railroads #Railroads owned
                , round(len([p for p in self.properties if p.owner == None and p.isSpecialSquare == False]) / 27,2) #Percentage of properties avaible 
                ]

        else:
            #Roll dice
            dice = self.roll_dice()      
            player.position = (player.position + dice) % 40 #New position

            qt = [player.playerNumber #Player number
                ,lastPosition #Last position
                , dice #Dice
                , player.position #New position
                , player.jail #Jail
                , self.properties[player.position].isSpecialSquare #Special position
                , player.money #Money
                , len(player.properties) #Number of properties owned
                , player.money + sum([p.price for p in player.properties]) #networth
                , sum([p.price for p in player.properties]) #Owned Properties price 
                , sum([p.houses for p in player.properties]) #Owned properties Houses
                , sum([p.rent for p in player.properties]) #Rent to charge
                , round(len(player.properties) / 28,2) #Percentage of properties owned
                , player.railroads #Railroads owned
                , round(len([p for p in self.properties if p.owner == None and p.isSpecialSquare == False]) / 27,2) #Percentage of properties avaible 
                ]

            #Give player $200 if they complete a round
            if player.position < lastPosition:
                player.money +=  200


            if self.properties[player.position].isSpecialSquare == True: #Special squares logic
                #Jail ------------------------------->
                if player.position == 10:
                    player.jail = True

                elif player.position == 30:
                    player.jail = True
                    player.position = 10

                #Chance Cards ----------------------->
                if player.position in (2,7,17,22,33,36):
                    player.money += random.choice(self.chanceCards)

                #Taxes ------------------------------>
                if player.position == 4:
                    player.money -= 200

                if player.position in (12,29):
                    player.money -= 150

                if player.position == 38:
                    player.money -= 100

            else:

                #Mutate position of player
                currentProperty = self.properties[player.position] 

                if player.position in (5,15,25,35): #If position is a railroad
                    
                    if currentProperty.owner != player: #If the owner of the railroad is not the player
                        if currentProperty.owner == None:  #if no one is the owner
                            if player.money > currentProperty.price and choice: 
                                currentProperty.owner = player
                                player.money -= currentProperty.price
                                player.railroads += 1
                        else:
                            rentToPay =  currentProperty.owner.railroads*50
                            currentProperty.owner.money += rentToPay
                            player.money -= rentToPay
                
                else:
                    if currentProperty.owner == player: #Simulating the player decision to add a house or many  to the property    
                            #For properties with less than 5 house
                            #Only is your simulated descition to buy a house is True
                            #If you have enough money for houses
                        propertyHouses = currentProperty.houses
                        if (5 - propertyHouses) > 0 and (player.money > currentProperty.costPerHouse) and choice: 

                            
                            currentProperty.houses += 1               #Update amount of houses on property
                            player.money -= currentProperty.costPerHouse  #Pay for the houses
                            currentProperty.rent = currentProperty.rentWithHouses[currentProperty.houses -1]    #Set rent to the price with n houses

                    else: 
                        if currentProperty.owner == None:  #buying the property
                            if choice: 
                                player.money -=  currentProperty.price #Pay for the property 
                                currentProperty.owner = player #Update property owner
                                player.properties.append(currentProperty) #Add property to player's properties


                        else: #Paying rent to the owner
                            rentToPay = currentProperty.rent
                            player.money -= rentToPay
                            currentProperty.owner.money += rentToPay
    
        qt1 = [
                 player.money #Money
                , len(player.properties) #Number of properties
                , player.money + sum([p.price for p in player.properties]) #networth
                , sum([p.price for p in player.properties]) #Owned Properties price 
                , sum([p.houses for p in player.properties]) # Owned Houses
                , sum([p.rent for p in player.properties]) #Rent to charge
                , round(len(player.properties) / 28,2) #Percentage of properties owned
                , player.railroads #Railroads owned
                , round(len([p for p in self.properties if p.owner == None and p.isSpecialSquare == False]) / 27,2) #Percentage of properties avaible 
                ]
  
        return qt + [choice] + qt1

    def round(self,players: List[Player]):
        #Make a turn for all players
        for p in players:
            self.results.loc[len(self.results)] = self.turn(p)
        self.rounds += 1



def main(n_players):

    #Creating players
    players = []

    for i in range(n_players):
        players.append(Player(i,[]))

    #Monopoly creating
    monopoly = Monopoly(players)
    
    
    while min([p.money for p in monopoly.players]) > 0:

        monopoly.round(players)

    winner = monopoly.results.tail(3).groupby('player_number').max()['money'].sort_values(ascending=False).index[0]
    return monopoly.results.loc[(monopoly.results['player_number'] == winner) & (monopoly.results["is_special_position"] == False)]



if __name__ == '__main__':
    df = pd.DataFrame(
            columns = ["player_number","last_position","dice","current_position","jail","is_special_position","money","properties","networth"
                       ,"owned_properties_price","owned_properties_houses","rent_to_charge","percentage_of_owned_properties","railroads_owned"
                       ,"properties_available","buy","money2","properties2","networth2","owned_properties_price2","owned_properties_houses2"
                       ,"rent_to_charge2","percentage_of_owned_properties2","railroads_owned2","properties_available2"])
    start = time.time()
    for _ in range(3000):
        df = pd.concat([df, main(3)], axis=0)
    print(time.time() - start)
    print(len(df))
    df.to_csv("results.csv")





