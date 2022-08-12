class Represent(object):
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y

    def __repr__(self):
        return "Represent(x={},y=\"{}\")".format(self.x, self.y) 

    def __str__(self):
        return "Representing x as {} and y as {}".format(self.x, self.y)


r = Represent(1, 'Hopper')
print(r)                        # prints __str__
print(r.__repr__)               # prints __repr__

rep = r.__repr__()
print(rep)

r2 = eval(rep)
print(r2)


class Card:
    def __init__(self, suit, pips):
        self.suit = suit
        self.pips = pips

    # def __str__(self):
    #     special_names = {1:'Ace', 11:'Jack', 12:'Queen', 13:'King'}
    #     card_name = special_names.get(self.pips, str(self.pips))
    #     return "%s of %s (S)" %(card_name, self.suit)

    def __repr__(self):
            special_names = {1:'Ace', 11:'Jack', 12:'Queen', 13:'King'}
            card_name = special_names.get(self.pips, str(self.pips))
            return "%s of %s (R)" %(card_name, self.suit)

ace_of_spades = Card('Spades', 1)
four_of_clubs = Card('Clubs', 4)
six_of_hearts = Card('Hearts', 6)

my_hand = [ace_of_spades, four_of_clubs, six_of_hearts]

print(my_hand)
print(ace_of_spades)
print(str(four_of_clubs))
print(repr(four_of_clubs))
print(six_of_hearts.__str__())
print(six_of_hearts.__repr__())

# print(Card.)