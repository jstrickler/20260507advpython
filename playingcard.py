class PlayingCard:
    def __init__(self, rank: str, suit: str):
        self._rank: str|None = None
        self._suit: str|None = None
        self.rank = rank
        self.suit = suit

    @property
    def rank(self):  # getter property
        return self._rank

    @rank.setter
    def rank(self, rank_value: str): # setter property
        if isinstance(rank_value, str):
            self._rank = rank_value
        else:
            raise TypeError("rank must be a str")

    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, value):
        if isinstance(value, str):
            self._suit = value
        else:
            raise TypeError("suit must be a string")

    def __str__(self):
        return f"{self.rank}-{self.suit}"

    def __repr__(self):
        return f"PlayingCard('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = PlayingCard("8", "Diamonds")
    print(c1)
    print(str(c1))
    print(repr(c1))
    print(f"{c1 = }")   # repr()
     
    print(c1.rank)  # .rank is a PROPERTY not a METHOD
    print(type(PlayingCard.rank))
    try:
        c1.rank = 1234
    except TypeError as err:
        print(err)
    else:
        print(c1.rank)
