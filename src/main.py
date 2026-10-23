import random
import math

#initialze list of cards
#for now, only have the values that they represent 
clubs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
hearts = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
spades = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
diamonds = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

userHand1=[]
userHand2 = []
dealerHand=[]


remainingChips = 1000
betAmount = 5 #eventually make this user input, for testing purposes, the value is set to 5

def starterQuestion(betAmount, remainingChips):
    while True:
        if betAmount > remainingChips:
            print("Try again. You can't bet more chips than you have available!")
        elif betAmount <= 0:
            print("You have to bet at least one chip! Try again:")
        else:
            print(f"You have placed a bet of {betAmount} chips")
            print()
            remainingChips = remainingChips - betAmount
            break

#pops two values from the deck and appends to user hand list
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

#pops two values from the deck and appends to dealer hand list
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

#returns string of users hand
def userHandString(userHand):
    handFormatString = ", "
    userHandStr = handFormatString.join(map(str, userHand))
    return userHandStr

def userDealtHandOutput():
    print("You have just been dealt a hand!")
    print(f"Your hand consists of {userHandString(userHand1)}")
    print()

def dealerDealtHandOutput():
    dealerHandStr = str(dealerHand[0])
    print(f"Dealer deals themself two cards. The card showing is worth {dealerHandStr}")

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

#returns true if busts
def bustChecker(handValueCheck, handList):
    bust = False
    bustValue = handValueCheck(handList)

    if bustValue > 21:
        bust = True
        return bust
    else:
        return bust

#returns true if an ace changed values
def aceValueChangeCheck(bustChecker, handList):
    isAce = False

    if (handList.count(11) > 0):
        isAce = True

    if (isAce and bustChecker):
        handList.remove(11)
        handList.append(1)
        return True
    else: 
        return False

def hit(handList = userHand1):
    suitPick = random.randint(1, 4)
    if suitPick == 1:
        cardPull = clubs.pop(random.randint(0, len(clubs) - 1))
        handList.append(cardPull)
    elif suitPick == 2:
        cardPull = hearts.pop(random.randint(0, len(hearts) - 1))
        handList.append(cardPull)
    elif suitPick == 3:
        cardPull = spades.pop(random.randint(0, len(spades) - 1))
        handList.append(cardPull)
    else:
        cardPull = diamonds.pop(random.randint(0, len(diamonds) - 1))
        handList.append(cardPull)

#double downs 
#this is for checking if splitting and doubling down is financially possible
def doubleDownOrSplitPossible(betAmount, remainingChips):
    if betAmount <= remainingChips:
        return True
    else:
        return False

def doubleDownMove(*args):
    splitBool = True if len(args) == 1 else False

    if splitBool:
        global betAmount
        global remainingChips
        remainingChips = remainingChips - betAmount
        betAmount = betAmount * 2
        hit()
    else: #for split hand
        pass

#splits
def splitPossible(userHand1):
    if (doubleDownOrSplitPossible(betAmount, remainingChips) and userHand1[0] == userHand1[1]):
        return True
    else:
        return false

def splitMove():
    userHand2.append(userHand1.pop(1))
    hit(userHand1)
    hit(userHand2)

    print()
    print(f"Hand 1 consists of {userHandString(userHand1)}")
    print(f"Hand 2 consists of {userHandString(userHand1)}")

#The typical implementation of user inputs here can be found inside the 'userMovePromptAndAnswer' function
#However most of the 'split' option will be found here
#Split is the most complicated move so an implementation in the normal function would bloat it too much
def split(didHit = False):
    if ((blackJackCheck(userHand1) and blackJackCheck(userHand2))):
        print("You just capped out at 21 for both hands!")
        dealerMove(dealerHand, userHand1)
        dealerMove(dealerHand, userHand1)
    else:
        handNum = 1 if not(blackJackCheck(userHand1)) else 2
        userWhileBool1 = True if (handNum == 1) else False
        userWhileBool2 = True if (handNum == 2) else False

    if (blackJackCheck(userHand1)):
        print()
    elif (blackJackCheck(userHand1):
        
    else:
        pass
    while userWhileBool1:
        print(f"You are on hand 1. What would you like to do? You can hit, stand, or double down.")
        userInput = input("Input H, ST, or DD: ")

        #user hit
        if userInput.upper() == "H":
            print()
            print("You decided to hit!")
            hit(userHand1)

            if (blackJackCheck(userHand1)): #you got capped out at 21
                print(f"Your hand consists of {userHandString(userHand1)}")
                print()
                print("You capped out at 21!")
                dealerMove(dealerHand, userHand1)
            elif (not(bustChecker(handValueCheck, userHand1))): #If you dont bust then ...
                print(f"Your hand consists of {userHandString(userHand1)}")
                print()
                split(True)
            else: #you busted
                print(f"Your hand consists of {userHandString(userHand1)}... YOU BUSTED!")
                userLose(betAmount)
            userWhileBool1 = False

        elif userInput.upper() == "ST":
            print()
            print("You have decided to stand")
            dealerMove(dealerHand, userHand1)
            userWhileBool1 = False

        #user doubled down
        elif userInput.upper() == "DD" and (not didHit):
            if (doubleDownOrSplitPossible(betAmount, remainingChips) == False):
                print("You can't afford to double down!")
                print("Try again!")
                print()
            elif (bustChecker(handValueCheck, userHand1)):
                doubleDownMove(userHand1)
                print("You doubled down!")
                print()
                print(f"Your hand consists of {userHandString(userHand1)}")
                print("You busted!")
                userLose(betAmount)
                userWhileBool1 = False
            else:
                doubleDownMove(userHand1)
                print("You doubled down!")
                print()
                print(f"Your hand consists of {userHandString(userHand1)}")
                dealerMove(dealerHand)
                userWhileBool1 = False
        else:
            print("Not a valid option! Try again!")

        handNum = 2 if not(blackJackCheck(userHand2)) else 1
        userWhileBool2 = True if (handNum == 2) else False

        print()
        while userWhileBool2:
            print(f"Hand 2 consists of {userHandString[userHand2]}")
            print(f"You are on hand 2. What would you like to do? You can hit, stand, or double down.")
            userInput = input("Input H, ST, or DD: ")
            #user hit
            if userInput.upper() == "H":
                print()
                print("You decided to hit!")
                hit(userHand1)

                if (blackJackCheck(userHand2)): #you got black jack
                    print(f"Your hand consists of {userHandString(userHand2)}")
                    print()
                    print("You capped out at 21!")
                    dealerMove(dealerHand, userHand1)
                    userWhileBool2 = False
                elif (not(bustChecker(handValueCheck, userHand2))): #If you dont bust then ...
                    print(f"Your hand consists of {userHandString(userHand1)}")
                    print()
                    userWhileBool2 = False
                    split(True)
                else: #you busted
                    print(f"Your hand consists of {userHandString(userHand2)}... YOU BUSTED!")
                    userLose(betAmount)
                    userWhileBool2 = False
                    
            elif userInput.upper() == "ST":
                print()
                print("You have decided to stand")
                dealerMove(dealerHand, userHand2)
                userWhileBool2 = False

            #user doubled down
            elif userInput.upper() == "DD" and (not didHit):
                if (doubleDownOrSplitPossible(betAmount, remainingChips) == False):
                    print("You can't afford to double down!")
                    print("Try again!")
                    print()
                elif (bustChecker(handValueCheck, userHand2)):
                    doubleDownMove(userHand2)
                    print("You doubled down!")
                    print()
                    print(f"Your hand consists of {userHandString(userHand2)}")
                    print("You busted!")
                    userLose(betAmount)
                    userWhileBool2 = False
                else:
                    doubleDownMove(userHand2)
                    print("You doubled down!")
                    print()
                    print(f"Your hand consists of {userHandString(userHand2)}")
                    dealerMove(dealerHand)
                    userWhileBool2 = False
            else:
                print("Not a valid option! Try again!")


#results
def userWin(remainingChips, betAmount, isBlackJack):
    if (isBlackJack):
        amountWon = betAmount * 3
        remainingChips = remainingChips + amountWon
    else:
        amountWon = betAmount * 2
        remainingChips = remainingChips + amountWon

    print(f"You won this hand of Blackjack, with a bet of {betAmount} chips")
    print(f"That means that you won {math.ceil(amountWon / 2)} chips")

def userLose(betAmount):
    print(f"You lost with a bet of {betAmount}")
def dealerWonOrNot(dealerHand, userHand):
    dealerWon = True if (handValueCheck(dealerHand) > handValueCheck(userHand)) else False
    return dealerWon

def push(dealerHand, userHand):
    pushBool = True if (handValueCheck(dealerHand) == handValueCheck(userHand)) else False
    if pushBool:
        global betAmount
        global remainingChips
        remainingChips = remainingChips + betAmount
        return pushBool
    else:
        return pushBool

        
#what the dealer does after you are done with your hand
def dealerMove(dealerHand, userHand):
    print(f"Dealer reveals his second card... it is worth {dealerHand[1]}")

    while ((handValueCheck(dealerHand) < 17)):
        count = 2
        hit(dealerHand)
        count += 1
        print(f"Dealer reveals card number {count}, it is a {dealerHand[count - 1]}")

    handFormatString = ", "
    dealerHandStr = handFormatString.join(map(str, dealerHand))

    if (bustChecker(handValueCheck, dealerHand)): #dealer busts
        print(f"Dealer has busted with a hand of {dealerHandStr}")
        userWin(remainingChips, betAmount, False)
    else: #dealer doesnt bust
        dealerWon = dealerWonOrNot(dealerHand, userHand1)
        if dealerWon: #dealer outdid you
            print(f"You lost to the dealer who had {dealerHandStr}")
            userLose(betAmount)
        elif (push(dealerHand, userHand) == True): #you tied with dealer
            push(dealerHand, userHand)
            print("You and the dealer tied this hand. You keep your chips.")
        else: #dealer had to stand on 17+
            print("Dealer can draw no more cards! You beat his hand")
            userWin(remainingChips, betAmount, False)

#prompts user and accepts answers
def userMovePromptAndAnswer(didHit = False):
    userWhileBool = True
    #prompt
    if didHit:
        print()
        print("It is now your move! what would you like to do?")
        print("You can hit, stand, split, or surrender!")
    else:
        print()
        print("It is now your move! what would you like to do?")
        print("You can hit, stand, double-down, split, or surrender!")

    userWhileBool = True

    while userWhileBool:
        userInput = input("Input H, ST, DD, SP, or SU: ")
        #user hit
        if userInput.upper() == "H":
            print()
            print("You decided to hit!")
            hit()

            if (blackJackCheck(userHand1)): #you got black jack
                print(f"Your hand consists of {userHandString(userHand1)}")
                print()
                print("You capped out at 21!")
                dealerMove(dealerHand, userHand1)
                userWhileBool = False
            elif (not(bustChecker(handValueCheck, userHand1))): #If you dont bust then ...
                print(f"Your hand consists of {userHandString(userHand1)}")
                print()
                userWhileBool = False
                userMovePromptAndAnswer(True)
            else: #you busted
                print(f"Your hand consists of {userHandString(userHand1)}... YOU BUSTED!")
                userLose(betAmount)
                userWhileBool = False
        #user stood
        elif userInput.upper() == "ST":
            print()
            print("You have decided to stand")
            dealerMove(dealerHand, userHand1)
            userWhileBool = False

        #user doubled down
        elif userInput.upper() == "DD" and (not didHit):
            if (doubleDownOrSplitPossible(betAmount, remainingChips) == False):
                print("You can't afford to double down!")
                print("Try again!")
                print()
            elif (bustChecker(handValueCheck, userHand1)):
                doubleDownMove(userHand1)
                print("You doubled down!")
                print()
                print(f"Your hand consists of {userHandString(userHand1)}")
                print("You busted!")
                userLose(betAmount)
                userWhileBool = False
            else:
                doubleDownMove(userHand1)
                print("You doubled down!")
                print()
                print(f"Your hand consists of {userHandString(userHand1)}")
                dealerMove(dealerHand)
                userWhileBool = False

        #user split
        elif userInput.upper() == "SP":
            if (splitPossible(userHand1)):
                splitMove()
                split()
                userWhileBool = False
            else:
                print("To split, you have to have two hands of the same value!")
                print("Try again")

        #user surrendered
        elif userInput.upper() == "SU" and (not didHit):
            userWhileBool = False
        else:
            print("Not a valid option! Try again!")


def main():
    starterQuestion(betAmount, remainingChips)
    doubleDownMove(betAmount, remainingChips, userHand1)
    userDealHand()
    aceValueChangeCheck(bustChecker(handValueCheck, userHand1), userHand1)
    userHandString(userHand1)
    userDealtHandOutput()
    if (blackJackCheck(userHand1)):
        userWin(remainingChips, betAmount, True)
    else:
        dealerDealHand()
        dealerDealtHandOutput()
        userMovePromptAndAnswer()

main()