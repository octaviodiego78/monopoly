def getSquaresInfo():

    squaresInfo = []

    for i in range(40):
        squaresInfo.append(
            {"squareId":i
            ,"isStart":0
            ,"isJail":0
            ,"isRailRoad":0
            ,"isMagicCard":0
            ,"isTax":0
            ,"isWaterWork":0
            ,"isOwned":0
            ,"Owner":0
            ,"Name":""
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