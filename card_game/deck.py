import random

class Card(object):
    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite
    def __repr__(self):
        return '%s%s' %(self.rank, self.suite)

class Deck(object):
    def __init__(self):
        # Composition
        self.cards = []
        for suite in ['S', 'H', 'C', 'D']:
            for rank in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K']:
                self.cards.append(Card(rank, suite))
    def __repr__(self):
        return ','.join(str(card) for card in self.cards)
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self, num_hands, cards_per_hand=13):
        pass

class Hand(object):
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        pass
    def discard_card(self, card):
        pass

class DealerHand(Hand):
    pass

d = Deck()
print d
d.shuffle()
print d