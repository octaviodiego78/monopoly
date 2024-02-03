def getSquaresInfo():

    squaresInfo = []

    for i in range(40):

        if i in ([2,7,17,22,33,36,10,30,4,12,29,38]):
            specialSquare = True
        else:
            specialSquare = False

        squaresInfo.append(
            {"squareId":i
            ,"isSpecialSquare":specialSquare
            ,"isOwned":False
            ,"owner":None
            ,"name":""
            ,"price":0
            ,"rent":0
            ,"rentWithHouses":[100,200,300,400,500]
            ,"costPerHouse":0
            ,"houses":0}
            )

    return squaresInfo


def getChanceCards():
    return [-200, -150, -100, -50, 50, 100, 200,]


railroadJSON = {"squareId":1
            ,"isSpecialSquare":1
            ,"isOwned":False
            ,"owner":None
            ,"name":""
            ,"price":0
            ,"rent":0
            ,"rentWithHouses":[100,200,300,400,500]
            ,"costPerHouse":0
            ,"houses":0}
            