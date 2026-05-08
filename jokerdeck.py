from carddeck import CardDeck
from playingcard import PlayingCard

class Game:
    def ID(self):
        print("I am a game")


class JokerDeck(CardDeck, Game):
    def _create_deck(self):
        super()._create_deck()
        for joker_number in 1, 2:
            card = PlayingCard(
                f"Joker{joker_number}",
                "*** JOKER ***"
            )
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(j.cards)
    j.ID()
    print(f"{JokerDeck.mro() = }")
