import json
import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Card(object):
    def __init__(self, suit: str, value: str):
        if suit not in SUITS:
            raise Exception('Invalid suit')
        self.suit = suit
        if value not in VALUES:
            raise Exception('Invalid value')
        self.value = value

    def __str__(self):
        return f'{self.value} of {self.suit}'


class DeckOfCards(object):
    def __init__(self):
        self.cards = [Card(suit, value) for suit in SUITS for value in VALUES]

    def __str__(self):
        return json.dumps({
            'deck': [str(card) for card in self.cards],
            'length': len(self.cards)
        })

    def deal_single_card(self):
        choose_card = random.randint(0, len(self.cards))
        deal_card = self.cards[choose_card]
        del self.cards[choose_card]
        return deal_card

    def check_deck(self):
        all_cards = self.cards
        if len(all_cards) != 52:
            raise Exception('The deck is not complete')
        else:
            print(f'The cards deck contains {len(all_cards)} cards')
            random.shuffle(all_cards)
            print(str(self))


if __name__ == "__main__":

    my_card = DeckOfCards()
    print(f'The shuffle cards deck is as follow: {my_card.check_deck()}')
    print(f'The shuffle cards deck is as follow: {my_card.check_deck()}')
    print(f'The picked card is: {my_card.deal_single_card()}')

