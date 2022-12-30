import random
from art import logo

playerIn = True
dealerIn = True
playerContinue = True
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
playerHand = []
dealerHand = []

print(logo)
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)


# calculate the total of each card
def computeCard(turn):
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total


def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]


for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

while playerContinue:
    while playerIn or dealerIn:
        print(f"Dealer had {revealDealerHand()} and X")
        print(f"You have {playerHand} for a total of {computeCard(playerHand)}")
        if playerIn:
            stayOrHit = input("1: Stay\n2: Hit\n")
        if computeCard(dealerHand) > 17:
            dealerIn = False
        else:
            dealCard(dealerHand)
        if stayOrHit == '1':
            playerIn = False
        else:
            dealCard(playerHand)
        if computeCard(playerHand) >=21:
            break
        elif computeCard(dealerHand) >= 21:
            break

    if computeCard(playerHand) == 21:
        print(f"\nYou have {playerHand} for a total of {computeCard(playerHand)} and the dealer has {dealerHand} for a total of {computeCard(dealerHand)}")
        print("Blackjack! You win:")
    elif computeCard(dealerHand) == 21:
        print(f"\nYou have {playerHand} for a total of {computeCard(playerHand)} and the dealer has {dealerHand} for a total of {computeCard(dealerHand)}")
        print("Blackjack! Dealer wins!")
    elif computeCard(playerHand) > 21:
        print(f"\nYou have {playerHand} for a total of {computeCard(playerHand)} and the dealer has {dealerHand} for a total of {computeCard(dealerHand)}")
        print("You bust! Dealer Wins")
    elif computeCard(dealerHand) > 21:
        print(f"\nYou have {playerHand} for a total of {computeCard(playerHand)} and the dealer has {dealerHand} for a total of {computeCard(dealerHand)}")
        print("Dealer busts! You win!")
    elif 21 - computeCard(dealerHand) < 21 - computeCard(playerHand):
        print(f"\nYou have {playerHand} for a total of {computeCard(playerHand)} and the dealer has {dealerHand} for a total of {computeCard(dealerHand)}")
        print("Dealer wins!")
    elif 21 - computeCard(dealerHand) > 21 - computeCard(playerHand):
        print(f"\nYou have {playerHand} for a total of {computeCard(playerHand)} and the dealer has {dealerHand} for a total of {computeCard(dealerHand)}")
        print("Player wins!")
    elif computeCard(dealerHand) == computeCard(playerHand):
        print(f"\nYou have {playerHand} for a total of {computeCard(playerHand)} and the dealer has {dealerHand} for a total of {computeCard(dealerHand)}")
        print("PUSH")
    user_choice = input("Do you still want to play? press 1 for 'yes' or press 2 for 'no' ")
    if user_choice == '2':
        playerContinue = False
        print("Thanks for playing!")
    else:
        dealerHand = []
        playerHand = []
        for _ in range(2):
            dealCard(dealerHand)
            dealCard(playerHand)