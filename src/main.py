import random

clubs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
hearts = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
spades = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
diamonds = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

userHand1=[]
dealerHand=[]

def starterInitAndQuestion():
    global remainingChips
    remainingChips = 1000
    global betAmount
    betAmount = 5  
    while True:
        if betAmount > remainingChips:
            print("Try again. You can't bet more chips than you have available!")
        elif betAmount <= 0:
            print("You have to bet at least one chip! Try again:")
        else:
            print("You have placed a bet of " + str(betAmount) + " chips.\n")
            remainingChips = remainingChips - betAmount
            break

def userDealHand():
    for x in range(2):
        suitPick = random.randint(1, 4)
        if suitPick == 1:
            cardPull = clubs.pop(random.randint(0, len(clubs)-1))
            userHand1.append(cardPull)
        elif suitPick == 2:
            cardPull = hearts.pop(random.randint(0,len(hearts)-1))
            userHand1.append(cardPull)
        elif suitPick == 3:
            cardPull = spades.pop(random.randint(0,len(spades)-1))
            userHand1.append(cardPull)
        else:
            cardPull = diamonds.pop(random.randint(0,len(diamonds)-1))
            userHand1.append(cardPull)
    
def userHandString(userHand1):
    handFormatString = ", "
    userHandStr = handFormatString.join(map(str, userHand1))
    return userHandStr

def userDealtHandResponse():
    print("You have just been dealt a hand!")
    print("Your hand consists of " + userHandString(userHand1))
    print()


def dealerDealHand():
    for x in range(2):
        suitPick = random.randint(1, 4)
        if suitPick == 1:
            cardPull = clubs.pop(random.randint(0,len(clubs)-1))
            dealerHand.append(cardPull)
        elif suitPick == 2:
            cardPull = hearts.pop(random.randint(0,len(hearts)-1))
            dealerHand.append(cardPull)
        elif suitPick == 3:
            cardPull = spades.pop(random.randint(0,len(spades)-1))
            dealerHand.append(cardPull)
        else:
            cardPull = diamonds.pop(random.randint(0,len(diamonds)-1))
            dealerHand.append(cardPull)

def dealerDealtHandResponse():
    dealerHandStr = str(dealerHand[0])
    print("Dealer deals themself two cards. The card showing is worth " + dealerHandStr)

def handValueCheck(handList):
    valueOfHand = 0
    for value in handList:
        valueOfHand += value
    return valueOfHand

def blackJackCheck(handList):
    if handValueCheck(handList) == 21:
        return True
    else:
        return False

def bustChecker(handValueCheck, userOrDealer):
    user = True
    bust = False
    bustValue = 0

    if userOrDealer == 0:
        pass
    else:
        user = False

    if user == True:
        handValueCheck(userHand1)
        for x in userHand1:
            bustValue += x
    else:
        handValueCheck(dealerHand)
        for x in dealerHand:
            bustValue += x

    if bustValue > 21:
        bust = True
        return bust
    else:
        return bust

def aceValueChangeCheck(bustChecker, userOrDealer):
    isAce = False

    if userOrDealer == 0:
        if userHand1.count(11) > 0:
            isAce = True        
    else:
        if dealerHand.count(11) > 0:
            isAce = True

    if isAce == True and bustChecker == True:
        if userOrDealer == 0:
            userHand1.remove(11)
            userHand1.append(1)
        else:
            dealerHand.remove(11)
            dealerHand.append(1)

def hit(handDealer = userHand1):
    user = True

    suitPick = random.randint(1, 4)
    if suitPick == 1:
        cardPull = clubs.pop(random.randint(0, len(clubs) - 1))
        handDealer.append(cardPull)
    elif suitPick == 2:
        cardPull = hearts.pop(random.randint(0, len(hearts) - 1))
        handDealer.append(cardPull)
    elif suitPick == 3:
        cardPull = spades.pop(random.randint(0, len(spades) - 1))
        handDealer.append(cardPull)
    else:
        cardPull = diamonds.pop(random.randint(0, len(diamonds) - 1))
        handDealer.append(cardPull)

def doubleDown(betAmount, remainingChips):
    if betAmount <= remainingChips:
        print("You doubled down!")
        remainingChips = remainingChips - betAmount
        betAmount = betAmount * 2
        hit()
        return True
    else:
        return False

def split(userHand):
    if userHand1[0] == userHand1[1]:
        hit()
        hit()
        userHand2 = []
        userHand2.append(userHand1.pop(1)); userHand2.append(userHand1.pop(2))
    else:
        print("You cannot split! Try another input!")
        pass

def userMovePrompt():
    print("\nIt is now your move! what would you like to do?")
    print("You can hit, stand, double-down, split, or surrender!")
    #Remember to *maybe* implement cases here based on possible moves
    #Have to unless different implementation is possible
    #Though it seems like it'd be simpler to use cases here....

def userMoveAnswer():
    userWhileBool = True
    while userWhileBool:
        userInput = input("Input H, ST, DD, SP, or SU: ")
        if userInput.upper() == "H":
            print("You decided to hit!")
            hit()
            if ((aceValueChangeCheck(bustChecker, 0)) and (bustChecker(handValueCheck, 0))):
                print("Your hand consists of " + userHandString())
                print()

            userWhileBool = False
        elif userInput.upper() == "ST":
            print("You have decided to stand")
            userWhileBool = False
            bustChecker(handValueCheck, 0)
        elif userInput.upper() == "DD":
            doubleDown(betAmount, remainingChips)
            userWhileBool = False
        elif userInput.upper() == "SP":
            userWhileBool = False
        elif userInput.upper() == "SU":
            userWhileBool = False
        else:
            print("Not a valid option! Try again!")

def userWin(remainingChips):
    amountWon = betAmount * 2
    remainingChips = remainingChips + amountWon

    print("You won this hand of Blackjack, with a bet of " + str(betAmount) + " chips.")
    print("That means that you won " + str(amountWon) +" chips")


def main():
    starterInitAndQuestion()
    userDealHand()
    aceValueChangeCheck(bustChecker, 0)
    userHandString(userHand1)
    userDealtHandResponse()
    if (blackJackCheck(userHand1)):
        userWin(remainingChips)
    else:
        pass 
    dealerDealHand()
    dealerDealtHandResponse()
    userMovePrompt()
    userMoveAnswer()

main()