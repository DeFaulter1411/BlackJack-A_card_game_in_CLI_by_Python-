import sys, random

#Set Up the constants:
HEARTS = chr(9829)      #Character 9829 is (♥)
DIAMONDS = chr(9830)    #Character 9829 is (♦)
SPADES = chr(9824)      #Character 9829 is (♠)
CLUBS = chr(9827)       #Character 9829 is (♣)

BACKSIDE = "backside"


#main function
def main():
    print("""BlackJack,
          
          Rules:
          
          Try to get as close to 21 without going over.
          Kings, Queen, and Jacks are worth 10 points.
          Aces are worth 1 or 11 points.
          Card 2 through 10 are worth their face value.
          (H) it to take another card.
          (S)Stand to stop taking cards.
          On your first play, you can (D)double down to increase your bet but must hit exactly one more time before standing.
          In case of a tie, the best is returned to the player.
          The delaer stop hitting at 17.""")
    
    money =5000
    while True: #Main Game Loop.
        #Check if the player has run out of money:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing!")
            sys.exit()

     #let The Player enter their bet for this round:

    print('Money:', money)
    bet =getBet(money)

    #Give the dealer and player two card from the deck each:
    deck = getDeck()
    dealerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]

    #handle Player Actions:
    print('Bet:', bet)
    while Ture:  #Kepp looping until player stands or busts.
        displayHands(playerHand, dealerHand, False)
        print()

        #Check if the player is ust:
        if gethandValue(playerHadn) > 21:
            break

        #Get theplayer's move, either H,S,or D:
        move = getMove(playerHand, money - bet)


        #Handle the player actions:
        if move == 'D':
            # Player is doubling down, they can increase their bet:
            addditionalBet = getBet(min(bet,(money-bet)))
            bet += additionalBet
            print(f'Bet increased to {bet}')
            print('Bet:',bet)


        if move in ('H', 'D'):
            # hit/doubling down takes another card.
            newCard =deck.pop()
            rank, suit = newCard
            print(f'You drew a {rank} of {suit}')
            playerHand.append(newCard)

            if getHandValue(playerHand) > 21:
                #The POlayer has busted:
                continue
        
        if move in ('S','D'):
            #Stand/doubling down stops the player's turn.
            break
        
