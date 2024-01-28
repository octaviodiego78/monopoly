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
            ,"ownerId":0
            ,"name":""
            ,"color":""
            ,"price":0
            ,"rent":0
            ,"costPerHouse":0
            ,"costPerHotel":0
            ,"rentPerHouse":0
            ,"rentPerHotel":0
            ,"houses":0
            ,"hotel":0}
            )

    return squaresInfo


def getChanceCards():
    return [-200, -150, -100, -50, 50, 100, 200,]