import random
from math import ceil

#initialze list of cards
#for now, only have the values that they represent 
clubs =    [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
hearts =   [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
spades =   [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
diamonds = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


userHand1 = []
userHand2 = []
dealerHand= []
handFormatString = ", "

remainingChips = 1000
betAmount = 0


#by default the chips are removed, so any maninpulation beyond this should keep that in mind
def starterQuestion():
    global betAmount
    global remainingChips
    
    while True:
        betAmount = int(input("How many chips would you like to bet?: "))
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
        suitOfCardSelect = random.randint(1, 4)
        if suitOfCardSelect == 1:
            cardPull = clubs.pop(random.randint(0, len(clubs)-1))
            userHand1.append(cardPull)
        elif suitOfCardSelect == 2:
            cardPull = hearts.pop(random.randint(0, len(hearts)-1))
            userHand1.append(cardPull)
        elif suitOfCardSelect == 3:
            cardPull = spades.pop(random.randint(0, len(spades)-1))
            userHand1.append(cardPull)
        else:
            cardPull = diamonds.pop(random.randint(0, len(diamonds)-1))
            userHand1.append(cardPull)

#pops two values from the deck and appends to dealer hand list
def dealerDealHand():
    for x in range(2):
        suitOfCardSelect = random.randint(1, 4)
        if suitOfCardSelect == 1:
            cardPull = clubs.pop(random.randint(0, len(clubs)-1))
            dealerHand.append(cardPull)
        elif suitOfCardSelect == 2:
            cardPull = hearts.pop(random.randint(0, len(hearts)-1))
            dealerHand.append(cardPull)
        elif suitOfCardSelect == 3:
            cardPull = spades.pop(random.randint(0, len(spades)-1))
            dealerHand.append(cardPull)
        else:
            cardPull = diamonds.pop(random.randint(0, len(diamonds)-1))
            dealerHand.append(cardPull)

#returns string of users hand
def handString(userHand):
    HandStr = handFormatString.join(map(str, userHand))
    return HandStr

def userDealtHandOutput():
    print("You have just been dealt a hand!")
    print(f"Your hand consists of {handString(userHand1)}")
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
def bustChecker(handList):
    bust = False
    valueToCheck = handValueCheck(handList)

    if valueToCheck > 21:
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
    suitOfCardSelect = random.randint(1, 4)
    if suitOfCardSelect == 1:
        cardPull = clubs.pop(random.randint(0, len(clubs) - 1))
        handList.append(cardPull)
    elif suitOfCardSelect == 2:
        cardPull = hearts.pop(random.randint(0, len(hearts) - 1))
        handList.append(cardPull)
    elif suitOfCardSelect == 3:
        cardPull = spades.pop(random.randint(0, len(spades) - 1))
        handList.append(cardPull)
    else:
        cardPull = diamonds.pop(random.randint(0, len(diamonds) - 1))
        handList.append(cardPull)

    aceValueChangeCheck(bustChecker(handList), handList)

#double downs 
#this is for checking if splitting and doubling down is financially possible
def doubleDownOrSplitPossible(betAmount, remainingChips):
    if betAmount <= remainingChips:
        return True
    else:
        return False

def doubleDownMove(userHand, didSplit = False):
    global remainingChips
    global betAmount
    if (didSplit and (userHand == userHand1)):
        global betAmount1
        betAmount1 = betAmount
        remainingChips -= betAmount1
        betAmount1 *= 2
        hit(userHand)
    elif (didSplit and (userHand == userHand2)):
        global betAmount2
        betAmount2 = betAmount
        remainingChips -= betAmount2
        betAmount2 *= 2
        hit(userHand)
    else:
        remainingChips = remainingChips - betAmount
        betAmount = betAmount * 2
        hit()
#splits section

#returns if split is possible
def splitPossible(userHand1):
    if (doubleDownOrSplitPossible(betAmount, remainingChips) and userHand1[0] == userHand1[1]):
        return True
    else:
        return False

#Splits hand
def splitMove():
    userHand2.append(userHand1.pop(1))
    hit(userHand1)
    hit(userHand2)

    print()
    print(f"Hand 1 consists of {handString(userHand1)}")
    print(f"Hand 2 consists of {handString(userHand2)}")

def splitInput(splitHand, didHit = False):
    if splitHand == userHand1:
        splitHand = userHand1
        handNum = 1
    else:
        splitHand = userHand2
        handNum = 2

    userContinue = True
    print(f"You are on hand {handNum}. What would you like to do? You can hit, stand, or double down.")
    
    while userContinue:
        userInput = input("Input H, ST, or DD: ")
        if userInput.upper() == "H": #user hit
            print()
            print("You decided to hit!")
            hit(splitHand)
            if (blackJackCheck(splitHand)): #you got capped out at 21
                print(f"Your hand consists of {handString(splitHand)}")
                print()
                print("You capped out at 21!")
                userContinue = False
            elif (not(bustChecker(splitHand))): #If you dont bust then ...
                print(f"Your hand consists of {handString(splitHand)}")
                print()
                splitInput(splitHand)
                userContinue = False
            else: #you busted
                print(f"Your hand {handNum} consists of {handString(splitHand)}... YOU BUSTED!")
                userContinue = False

        elif userInput.upper() == "ST":
            print()
            print(f"You have decided to stand on hand {handNum}")
            userContinue = False

        #user doubled down
        elif userInput.upper() == "DD" and (not didHit):
            if (doubleDownOrSplitPossible(betAmount, remainingChips) == False):
                print("You can't afford to double down!")
                print("Try again!")
                print()
            elif (bustChecker(splitHand)):
                doubleDownMove(splitHand, True)
                print("You doubled down!")
                print()
                print(f"Your hand consists of {handString(splitHand)}")
                print("You busted!")
                userContinue = False
            else:
                doubleDownMove(splitHand, True)
                print("You doubled down!")
                print()
                print(f"Your hand {handNum} consists of {handString(splitHand)}... YOU BUSTED!")
                userContinue = False
        else:
            print("Not a valid option! Try again!")

#The typical implementation of user inputs here can be found inside the 'userMovePromptAndAnswer' function
#However most of the 'split' option will be found here
#Split is the most complicated move so an implementation in the normal function would bloat it too much
def split(betAmount):
    global betAmount1
    global betAmount2
    betAmount1 = betAmount
    betAmount2 = betAmount
    doneSplitting = False
    userContinueHand1 = True if not(blackJackCheck(userHand1)) else False
    userContinueHand2 = True if not(blackJackCheck(userHand2)) else False
    if (not (userContinueHand1 and userContinueHand2)):
        print("You just capped out at 21 for both hands!")
        dealerMove(dealerHand, userHand1, betAmount)
        dealerMove(dealerHand, userHand2, betAmount)
        doneSplitting = True        

    #hand 1
    while userContinueHand1:
        splitInput(userHand1)
        userContinueHand1 = False
       
    #hand 2
    while userContinueHand2:
        splitInput(userHand2)
        userContinueHand2 = False
        
    if (not doneSplitting): #unless they capped out at 21 for both hands then...
        doneSplitting = True
        print()
        print("You have concluded your split hands!")
        print(f"Hand one consists of {handString(userHand1)}")
        print(f"Hand two consists of {handString(userHand2)}")
        print ("For hand one...", end = "")
        dealerMove(dealerHand, userHand1, betAmount1)
        print()
        print ("For hand two...", end = "")
        dealerMove(dealerHand, userHand2, betAmount2, True)

#results sections
def userWin(remainingChips, betAmount, isBlackJack):
    if (isBlackJack):
        amountWon = betAmount * 3
        remainingChips = remainingChips + amountWon
    else:
        amountWon = betAmount * 2
        remainingChips = remainingChips + amountWon

    print(f"You won this hand of Blackjack, with a bet of {betAmount} chips")
    print(f"That means that you won {ceil(amountWon / 2)} chips")

def userLose(betAmount):
    print(f"You lost with a bet of {betAmount}")

def dealerWonOrNot(dealerHand, userHand):
    dealerWon = True if (handValueCheck(dealerHand) > handValueCheck(userHand)) else False
    return dealerWon

#aka tiebreaker, returns true if possible and adds chips back
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
def dealerMove(dealerHand, userHand, betAmount, doneRevealing = False):
    if doneRevealing:
        pass
    else:
        print(f"Dealer reveals his second card... it is worth {dealerHand[1]}")

    while ((handValueCheck(dealerHand) < 17)):
        count = 2
        hit(dealerHand)
        count += 1
        print(f"Dealer reveals card number {count}, it is a {dealerHand[count - 1]}")

    
    dealerHandStr = handFormatString.join(map(str, dealerHand))

    if (bustChecker(dealerHand)): #dealer busts
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

def surrender(remainingChips):
    userLose(betAmount);
    surrenderBet = ceil(betAmount / 2)
    remainingChips += surrenderBet

    return surrenderBet

#prompts user and accepts answers
#basically the parent function for user input
def userMovePromptAndAnswer(didHit = False):
    userContinue = True
    #prompt that checks whether or not they hit
    #they shouldn't be able to do some things if they already hit!!
    if didHit:
        print()
        print("It is now your move! what would you like to do?")
        print("You can hit, stand, split, or surrender!")
    else:
        print()
        print("It is now your move! what would you like to do?")
        print("You can hit, stand, double-down, split, or surrender!")

    userContinue = True

    while userContinue:

        userInput = input("Input H, ST, DD, SP, or SU: ")

        if userInput.upper() == "H":  #user hit
            print()
            print("You decided to hit!")
            hit()
            if (blackJackCheck(userHand1)): #you got black jack
                print(f"Your hand consists of {handString(userHand1)}")
                print()
                print("You capped out at 21!")
                dealerMove(dealerHand, userHand1, betAmount)
                userContinue = False
            elif (not(bustChecker(userHand1))): #If you dont bust then ...
                print(f"Your hand consists of {handString(userHand1)}")
                print()
                userContinue = False
                userMovePromptAndAnswer(True)
            else: #you busted
                print(f"Your hand consists of {handString(userHand1)}... YOU BUSTED!")
                userLose(betAmount)
                userContinue = False

        #user stood
        elif userInput.upper() == "ST":
            print()
            print("You have decided to stand")
            dealerMove(dealerHand, userHand1, betAmount)
            userContinue = False

        #user doubled down
        #note they can't double down if they already hit
        elif userInput.upper() == "DD" and (not didHit):
            if (doubleDownOrSplitPossible(betAmount, remainingChips) == False):
                print("You can't afford to double down!")
                print("Try again!")
                print()
            elif (bustChecker(userHand1)):
                doubleDownMove(userHand1)
                print("You doubled down!")
                print()
                print(f"Your hand consists of {handString(userHand1)}")
                print("You busted!")
                userLose(betAmount)
                userContinue = False
            else:
                doubleDownMove(remainingChips)
                print("You doubled down!")
                print()
                print(f"Your hand consists of {handString(userHand1)}")
                dealerMove(dealerHand, userHand1, betAmount)
                userContinue = False

        #user split
        #they can't split if they already hit
        elif (userInput.upper() == "SP" and (not didHit)):
            if (splitPossible(userHand1)):
                splitMove()
                split(betAmount)
                userContinue = False
            else:
                print("To split, you have to have two hands of the same value!")
                print("Try again")

        #user surrendered
        elif userInput.upper() == "SU" and (not didHit):
            print()
            print("You chose to surrender and lose this hand!")
            print("You get half your chips back!")
            print()
            print(f"But get back {surrender(remainingChips)}")

            userContinue = False
        else:
            print("Not a valid option! Try again!")

def continuePrompt():
    print()
    print("Would you like play another game of Blackjack?: ")
    response = input("Y for yes, else for no")

    if response.upper() == "Y":
        return True
    else:
        return False

def reinitialize():
        global clubs
        global hearts
        global spades
        global diamonds

        clubs =    [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        hearts =   [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        spades =   [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        diamonds = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        global userHand1
        global userHand2
        global dealerHand
        userHand1 = []
        userHand2 = []
        dealerHand= []
        
def main():
    starterQuestion()
    userDealHand()
    aceValueChangeCheck(bustChecker(userHand1), userHand1)
    handString(userHand1)
    userDealtHandOutput()
    if (blackJackCheck(userHand1)):
        userWin(remainingChips, betAmount, True)
    else:
        dealerDealHand()
        dealerDealtHandOutput()
        userMovePromptAndAnswer()

    if continuePrompt():
        reinitialize()
        main()

main()


