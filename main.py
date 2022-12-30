from art import logo
import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
user_cards = []

def get_card(players):
    random_card = deck[random.randint(0, 13)]
    return players.append(random_card)



def compute_card(player):
    total = sum(user_cards)
    return total

game_continue = True

while game_continue:
    print(f"Your cards: {for}")