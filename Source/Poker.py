'''
Created on May 30, 2018

@author: Alex
'''
from random import choice
from util import Card



class Poker(object):
    '''
    Poker should include those Attributes
    1. ranks    for example 2,3,...,J,Q,K,A
    2. suits    for example spades,diamonds,clubs,hearts
    '''
    ranks = [n for n in range(2, 15)]
#     suits = 'spades diamonds clubs hearts'.split()
    suits = '+ - * /'.split()

    rank_value = dict(J=11, Q=12, K=13, A=14)

    def __init__(self):
        '''
        Constructor
        '''
        self._cards = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def getRanksValue(self, temp_card):
        rank_value = self.ranks.index(temp_card.rank)
        return rank_value

    def removeFromCards(self, card):
        self._cards.remove(card)
        pass
    def inputMyCards(self):
        pass


if __name__ == '__main__':
    poker = Poker()
#     for card in sorted(poker, key=poker.getRanksValue):
#         print card
    
#         print card
    myfirstCard = Card(14, '+')
    mysecondCard = Card(2, '/')
    
    playerA_cards = []
    playerB_cards = []
    river_cards = []
    playerA_cards.append(Card(14, '+'))
    playerA_cards.append(Card(14, '-'))
    playerB_cards.append(Card(2, '+'))
    playerB_cards.append(Card(3, '-'))
    river_cards.append(poker[10])
    river_cards.append(poker[11])
    river_cards.append(poker[15])
    river_cards.append(poker[17])
    river_cards.append(poker[19])
    
    print playerA_cards
    print playerB_cards
    print river_cards
    
