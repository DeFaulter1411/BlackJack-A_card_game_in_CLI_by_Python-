import sys, random

# Set up constants:
HEARTS = chr(9829)     # ♥
DIAMONDS = chr(9830)   # ♦
SPADES = chr(9824)     # ♠
CLUBS = chr(9827)      # ♣
BACKSIDE = "backside"


def main():
    print("""
Welcome to BlackJack!

Rules:
Try to get as close to 21 without going over.
Kings, Queens, and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet but must hit exactly one more time before standing.
In case of a tie, the bet is returned to the player.
The dealer stops hitting at 17.
""")

    money = 5000
    while True:  # Main game loop
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            sys.exit()

        print('Money:', money)
        bet = getBet(money)

        # Deal initial cards
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print('Bet:', bet)

        # Player's turn
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            if getHandValue(playerHand) > 21:
                break

            move = getMove(playerHand, money - bet)

            if move == 'D':
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f'Bet increased to {bet}')
                print('Bet:', bet)

            if move in ('H', 'D'):
                newCard = deck.pop()
                rank, suit = newCard
                print(f'You drew a {rank} of {suit}')
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    break

            if move in ('S', 'D'):
                break

        # Dealer's turn
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break

                input('Press Enter to continue...')
                print('\n')

        # Show results
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        if dealerValue > 21:
            print(f'Dealer busts! You win ${bet}')
            money += bet
        elif playerValue > 21 or playerValue < dealerValue:
            print("You lost!")
            money -= bet
        elif playerValue > dealerValue:
            print(f'You won ${bet}!')
            money += bet
        else:
            print("It's a tie, the bet is returned to you.")

        input('Press Enter to continue...')
        print('\n\n')


def getBet(maxBet):
    """Ask the player how much they want to bet for this round."""
    while True:
        print(f'How much do you bet? (1-{maxBet}, or QUIT)')
        bet = input("> ").strip().upper()

        if bet == 'QUIT':
            print("Thanks for playing!")
            sys.exit()

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet
        else:
            print(f"Bet must be between 1 and {maxBet}. Try again.")


def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards."""
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        displayCards([BACKSIDE] + dealerHand[1:])

    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    """Return the value of the cards."""
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(cards):
    """Display all cards in a list."""
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += ' ___ '
        if card == BACKSIDE:
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '|_##|'
        else:
            rank, suit = card
            rows[1] += f'|{rank.ljust(2)} |'
            rows[2] += f'| {suit} |'
            rows[3] += f'|_{rank.rjust(2, "_")}|'

    for row in rows:
        print(row)


def getMove(playerHand, money):
    """Ask the player for their move."""
    while True:
        moves = ['(H)it', '(S)tand']
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S', 'D'):
            return move


if __name__ == '__main__':
    main()
