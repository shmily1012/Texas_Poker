'''
Created on May 31, 2018

@author: Alex
'''
from util import Card
import random
from Log import PRINT
from Poker import Poker


class Dealer(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.poker = Poker()
        self.current_rvier_cards = []
    
    def sendRandomCard(self):
        total_len = len(self.poker)
#         print 'total num of cards is', total_len
        id = random.randrange(total_len)
        temp_card = self.poker[id]
        self.poker.removeFromCards(temp_card)
#         print 'send this card:', temp_card
        return temp_card

    def dropTargetCard(self, card):
        self.poker.removeFromCards(card)
    

    
if __name__ == "__main__":
#     poker = Poker()
    dealer = Dealer()
    
#     card = dealer.sendRandomCard()
#     card = dealer.sendRandomCard()
#     card = dealer.sendRandomCard()
#     card = dealer.sendRandomCard()
#     card = dealer.sendRandomCard()
#     card = dealer.sendRandomCard()
#     for i in range(52):
#         card = dealer.sendRandomCard()
#         for c in dealer.poker:
#             print c
