import random
from playingcard import PlayingCard

class CardDeck:
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    SUITS = "Clubs Diamonds Hearts Spades".split()

    def __init__(self):
        self._create_deck()

    def _create_deck(self):
        self._cards: list = []
        for suit in self.SUITS: # self. is inheritance-friendly
            for rank in self.RANKS:
                card = PlayingCard(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self) -> None:
        random.shuffle(self._cards)


    def draw(self) -> PlayingCard:
        return self._cards.pop()

    @classmethod
    def get_suits(cls):
        return cls.SUITS
    
    def __len__(self):  # responds to len(obj)
        return len(self._cards)

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    d1.shuffle()
    print(d1.cards)
    for _ in range(5):
        card = d1.draw()
        print(card)
    print(d1.get_suits())
    print(CardDeck.get_suits())
    print(len(d1))