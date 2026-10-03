import random

clubs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
hearts = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
spades = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
diamonds = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

userHand1=[]
dealerHand=[]

def starterQuestion():
    global remainingChips
    remainingChips = 1000
    global betQuestion
    betQuestion = 5  # int(input("How many chips do you want to bet?: "))
    while True:
        if betQuestion > remainingChips:
            print("Try again. You can't bet more chips than you have available!")
        elif betQuestion <= 0:
            print("You have to bet at least one chip! Try again:")
        else:
            print(f"You have placed a bet of {betQuestion} chips. \n")
            remainingChips = remainingChips - betQuestion
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
    userHandStr = ", ".join(map(str, userHand1))


    print("You have just been dealt a hand!")
    print("Your hand consists of " + userHandStr + "\n")

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
    dealerHandStr = str(dealerHand[0])
    print("Dealer deals themself two cards. The card showing is worth " + dealerHandStr)

def handValueCheck(hand):
    valueNum = 0
    for value in hand:
        valueNum += value
    return valueNum

def blackJackCheck(hand):
    if handValueCheck(hand) == 21:
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
            pass
    else:
        if dealerHand.count(11) > 0:
            isAce = True
        else:
            pass

    if isAce == True and bustChecker == True:
        if userOrDealer == 0:
            userHand1.remove(11)
            userHand1.append(1)
        else:
            dealerHand.remove(11)
            dealerHand.append(1)
    else:
        pass

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

def doubleDown(betQuestion, remainingChips):
    if betQuestion <= remainingChips:
        print("You doubled down!")
        remainingChips = remainingChips - betQuestion
        betQuestion = betQuestion * 2
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

def userMove():
    print("\nIt is now your move! what would you like to do?")
    print("You can hit, stand, double-down, split, or surrender!")

    userWhileBool = True
    while userWhileBool:
        userInput = input("Input H, ST, DD, SP, or SU: ")
        if userInput.upper() == "H":
            print("You decided to hit!")
            hit()
            bustChecker(handValueCheck, 0)
            userWhileBool = False
        elif userInput.upper() == "ST":
            print("You have decided to stand")
            userWhileBool = False
            bustChecker(handValueCheck, 0)
        elif userInput.upper() == "DD":
            doubleDown(betQuestion, remainingChips)
            userWhileBool = False
        elif userInput.upper() == "SP":
            userWhileBool = False
        elif userInput.upper() == "SU":
            userWhileBool = False
        else:
            print("Not a valid option! Try again!")

    if bustChecker(handValueCheck,0) == True:
        print("You busted!")
        print("You lost your bet of " + str(betQuestion))
    else:
        pass

def main():
    starterQuestion()
    userDealHand()
    dealerDealHand()
    userMove()

main()


