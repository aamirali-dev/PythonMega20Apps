import random


class PlayingCard:
    def __init__(self, suit, rank):
        self.suit = suit.lower()
        self.rank = rank.lower()

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __repr__(self):
        return f'PlayingCard(suit={self.suit}, rank={self.rank})'


class CardDeck:
    _SUITS = ['spades', 'diamonds', 'clubs', 'hearts']
    _RANKS = [str(i) for i in range(2, 11)] + ['ace', 'jack', 'king', 'queen']

    def __init__(self, deck=None):
        if deck is None:
            self._deck = []
        else:
            self._deck = list(filter(lambda card: type(card) == PlayingCard, deck))
        if (self._deck is None) or len(self._deck) < 1:
            for suit in self._SUITS:
                for rank in self._RANKS:
                    self._deck.append(PlayingCard(suit, rank))

    def __contains__(self, item):
        return item in self._deck

    def __len__(self):
        return len(self._deck)

    def __getitem__(self, indices):
        if type(indices) == slice:
            return CardDeck(self._deck[indices])
        elif type(indices) == int:
            return self._deck[indices]
        else:
            raise IndexError('index must be slice or int')

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        if self._i >= len(self._deck):
            self._i = 0
            raise StopIteration()
        self._i += 1
        return self._deck[self._i - 1]

    def __add__(self, other):
        if type(other) == PlayingCard:
            return CardDeck([*self, other])
        return CardDeck([*self, *other])

    def draw(self, n=1):
        if n == 1:
            idx = random.choice(range(0, len(self._deck)))
            return self._deck.pop(idx)
        else:
            drawn_cards = []
            for _ in range(n):
                idx = random.randrange(len(self))
                drawn_cards.append(self._deck.pop(idx))
            return CardDeck(drawn_cards)

    def __repr__(self):
        return f'CardDeck(cards={self._deck})'

    def __mul__(self, other):
        if type(other) == int:
            cd = CardDeck([*self])
            for _ in range(0, other-1):
                cd += self
            return cd
        return NotImplemented()

    def __rmul__(self, other):
        return self * other

    def __delitem__(self, key):
        del self._deck[key]


cd = CardDeck()
cd2 = CardDeck([PlayingCard('diamonds', '2')])
cd3 = CardDeck(['Andrew', PlayingCard('clubs', '7')])
cd4 = CardDeck(['Andrew', 'Lisa'])
print(len(cd))
print(len(cd2))
print(len(cd3))
print(len(cd4))
print(cd[1])
print(cd[2])
print(cd[-10:])
print(PlayingCard('spades', '3') in cd)
print(cd2 + PlayingCard('spades', '6'))
print(cd2 + cd3)
print(cd2 * 2)
print(cd.draw(1))
print(len(cd))
print(cd.draw(3))
print(len(cd))
print(2 * cd2)

# for card in 2 * cd2:
#     print(card)

