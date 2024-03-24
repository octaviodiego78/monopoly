import numpy as np
import pandas as pd

def getSquaresInfo():

    squaresInfo = [

        {'squareId': 0, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': None, 'rent': None, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 1, 'isSpecialSquare': False, 'owner': None, 'name': 'Mexico', 'price': 50.0, 'rent': 5.0, 'rentWithHouses': [13.0, 26.0, 39.0, 52.0, 65.0], 'costPerHouse': 10.0, 'houses': 0}
        ,{'squareId': 2, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': None, 'rent': None, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 3, 'isSpecialSquare': False, 'owner': None, 'name': 'EU', 'price': 65.0, 'rent': 7.0, 'rentWithHouses': [17.0, 34.0, 51.0, 68.0, 85.0], 'costPerHouse': 13.0, 'houses': 0}
        ,{'squareId': 4, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': None, 'rent': None, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 5, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': 50, 'rent': 50, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 6, 'isSpecialSquare': False, 'owner': None, 'name': 'Peru', 'price': 80.0, 'rent': 8.0, 'rentWithHouses': [21.0, 42.0, 62.0, 83.0, 104.0], 'costPerHouse': 16.0, 'houses': 0}
        ,{'squareId': 7, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': None, 'rent': None, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 8, 'isSpecialSquare': False, 'owner': None, 'name': 'Argentina', 'price': 90.0, 'rent': 9.0, 'rentWithHouses': [23.0, 47.0, 70.0, 94.0, 117.0], 'costPerHouse': 18.0, 'houses': 0}
        ,{'squareId': 9, 'isSpecialSquare': False, 'owner': None, 'name': 'Brasil', 'price': 105.0, 'rent': 11.0, 'rentWithHouses': [27.0, 55.0, 82.0, 109.0, 137.0], 'costPerHouse': 21.0, 'houses': 0}
        ,{'squareId': 10, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': None, 'rent': None, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 11, 'isSpecialSquare': False, 'owner': None, 'name': 'Spain', 'price': 120.0, 'rent': 12.0, 'rentWithHouses': [31.0, 62.0, 94.0, 125.0, 156.0], 'costPerHouse': 24.0, 'houses': 0}
        ,{'squareId': 12, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': None, 'rent': None, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 13, 'isSpecialSquare': False, 'owner': None, 'name': 'France', 'price': 130.0, 'rent': 13.0, 'rentWithHouses': [34.0, 68.0, 101.0, 135.0, 169.0], 'costPerHouse': 26.0, 'houses': 0}
        ,{'squareId': 14, 'isSpecialSquare': False, 'owner': None, 'name': 'Italy', 'price': 145.0, 'rent': 15.0, 'rentWithHouses': [38.0, 75.0, 113.0, 151.0, 189.0], 'costPerHouse': 29.0, 'houses': 0}
        ,{'squareId': 15, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': 50, 'rent': 50, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 16, 'isSpecialSquare': False, 'owner': None, 'name': 'United Kingdom', 'price': 160.0, 'rent': 16.0, 'rentWithHouses': [42.0, 83.0, 125.0, 166.0, 208.0], 'costPerHouse': 32.0, 'houses': 0}
        ,{'squareId': 17, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': None, 'rent': None, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 18, 'isSpecialSquare': False, 'owner': None, 'name': 'Germany', 'price': 175.0, 'rent': 18.0, 'rentWithHouses': [46.0, 91.0, 137.0, 182.0, 228.0], 'costPerHouse': 35.0, 'houses': 0}
        ,{'squareId': 19, 'isSpecialSquare': False, 'owner': None, 'name': 'Netherlands', 'price': 190.0, 'rent': 19.0, 'rentWithHouses': [49.0, 99.0, 148.0, 198.0, 247.0], 'costPerHouse': 38.0, 'houses': 0}
        ,{'squareId': 20, 'isSpecialSquare': False, 'owner': None, 'name': 'Egipt', 'price': 200.0, 'rent': 20.0, 'rentWithHouses': [52.0, 104.0, 156.0, 208.0, 260.0], 'costPerHouse': 40.0, 'houses': 0}
        ,{'squareId': 21, 'isSpecialSquare': False, 'owner': None, 'name': 'Morocco', 'price': 215.0, 'rent': 22.0, 'rentWithHouses': [56.0, 112.0, 168.0, 224.0, 280.0], 'costPerHouse': 43.0, 'houses': 0}
        ,{'squareId': 22, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': None, 'rent': None, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 23, 'isSpecialSquare': False, 'owner': None, 'name': 'Argelia', 'price': 230.0, 'rent': 23.0, 'rentWithHouses': [60.0, 120.0, 179.0, 239.0, 299.0], 'costPerHouse': 46.0, 'houses': 0}
        ,{'squareId': 24, 'isSpecialSquare': False, 'owner': None, 'name': 'South Africa', 'price': 240.0, 'rent': 24.0, 'rentWithHouses': [62.0, 125.0, 187.0, 250.0, 312.0], 'costPerHouse': 48.0, 'houses': 0}
        ,{'squareId': 25, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': 50, 'rent': 50, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 26, 'isSpecialSquare': False, 'owner': None, 'name': 'Congo', 'price': 255.0, 'rent': 26.0, 'rentWithHouses': [66.0, 133.0, 199.0, 265.0, 332.0], 'costPerHouse': 51.0, 'houses': 0}
        ,{'squareId': 27, 'isSpecialSquare': False, 'owner': None, 'name': 'Madagascar', 'price': 270.0, 'rent': 27.0, 'rentWithHouses': [70.0, 140.0, 211.0, 281.0, 351.0], 'costPerHouse': 54.0, 'houses': 0}
        ,{'squareId': 28, 'isSpecialSquare': False, 'owner': None, 'name': 'Rusia', 'price': 280.0, 'rent': 28.0, 'rentWithHouses': [73.0, 146.0, 218.0, 291.0, 364.0], 'costPerHouse': 56.0, 'houses': 0}
        ,{'squareId': 29, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': None, 'rent': None, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 30, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': None, 'rent': None, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 31, 'isSpecialSquare': False, 'owner': None, 'name': 'India', 'price': 300.0, 'rent': 30.0, 'rentWithHouses': [78.0, 156.0, 234.0, 312.0, 390.0], 'costPerHouse': 60.0, 'houses': 0}
        ,{'squareId': 32, 'isSpecialSquare': False, 'owner': None, 'name': 'Turkey', 'price': 310.0, 'rent': 31.0, 'rentWithHouses': [81.0, 161.0, 242.0, 322.0, 403.0], 'costPerHouse': 62.0, 'houses': 0}
        ,{'squareId': 33, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': None, 'rent': None, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 34, 'isSpecialSquare': False, 'owner': None, 'name': 'China', 'price': 325.0, 'rent': 33.0, 'rentWithHouses': [85.0, 169.0, 254.0, 338.0, 423.0], 'costPerHouse': 65.0, 'houses': 0}
        ,{'squareId': 35, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': 50, 'rent': 50, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 36, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': None, 'rent': None, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 37, 'isSpecialSquare': False, 'owner': None, 'name': 'Japan', 'price': 335.0, 'rent': 34.0, 'rentWithHouses': [87.0, 174.0, 261.0, 348.0, 436.0], 'costPerHouse': 67.0, 'houses': 0}
        ,{'squareId': 38, 'isSpecialSquare': True, 'owner': None, 'name': None, 'price': None, 'rent': None, 'rentWithHouses': None, 'costPerHouse': None, 'houses': 0}
        ,{'squareId': 39, 'isSpecialSquare': False, 'owner': None, 'name': 'Tailand', 'price': 350.0, 'rent': 35.0, 'rentWithHouses': [91.0, 182.0, 273.0, 364.0, 455.0], 'costPerHouse': 70.0, 'houses': 0}
    ]
        

    return squaresInfo


def getChanceCards():
    return [-200, -150, -100, -50, 50, 100, 200,]
