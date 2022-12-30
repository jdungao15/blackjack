from art import logo
import random

random_choice = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "K", "Q", "J"]
deck = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "A": 11,
    "K": 10,
    "Q": 10,
    "J": 10
}
user_cards = {}


def get_card():
    card_face = random_choice[random.randint(0, 13)]
    random_card = deck[card_face]
    if random_card >= 10:
        if card_face == 'A':
            user_cards[card_face] = random_card
        elif card_face == 'K':
            user_cards[card_face] = random_card
        elif card_face == 'Q':
            user_cards[card_face] = random_card
        elif card_face == 'J':
            user_cards[card_face] = random_card
        else:
            user_cards[card_face] = random_card
    user_cards[card_face] = random_card
