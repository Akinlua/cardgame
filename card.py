
from  random import shuffle
class Card:

    def __init__(self, value, name):
        self.value=value
        self.name=name

    def __repr__(self):
        """Should print out 1 of cards"""
        return f"{self.name}{self.value}"

class Deck:
    def __init__(self):
        names=["♦","♤","♧","🖤"]
        letter=["d","s","c","h"]
        values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
        self.g=[Card(value, name) for name in names for value in values]
        self.general_market=[]
        for i in self.g:
            self.general_market.append(str(i))
        self.general= [Card(value, let) for let in letter for value in values]
        self.elements = {self.general[x]:self.general_market[x] for x in range(len(self.general))}
        
    def __repr__(self):
        """return Deck of no of cards in General Market"""
        return f"Deck of {self.count()}  "
    def count(self):
	    return len(self.general_market)
    def shuffle(self):
        """Shuffle the Genral Market"""
        if self.count() < 52:
            raise ValueError("The general market is full")
        shuffle(self.general_market)
        return self
    def deal(self, amt):
        """to take out of the deck of General Market, and make sure the remains in General market is not lost"""
        actual= min(int(amt),self.count())
        if self.count()<=0:
            raise ValueError("There is nothing general market, you can not take anything from it")
        to_take=self.general_market[-actual:]
        self.general_market= self.general_market[:-actual]
        return to_take
    


card= Card("1","Heart")
d=Deck()

print(d.general_market)

