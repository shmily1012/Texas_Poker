'''
Created on May 31, 2018

@author: siyuan
'''
from Log import PRINT
from util import Card
from Dealer import Dealer
from Player import Player
from Rules import Rules
Number = 2
current_num_river_cards = 5


class Game(object):
    '''
    classdocs
    '''

    def __init__(self, me, NumberOfPlayers=Number, current_river_card=[]):
        '''
        Constructor
        '''
        self.NumberOfPlayers = NumberOfPlayers
        self.me = me
        self.players = list()
        me.showCards()
        self.players.append(me)
        
        self.dealer = Dealer()
        self.dealer.dropTargetCard(me.cards_inhand[0])
        self.dealer.dropTargetCard(me.cards_inhand[1])
        self.riverCards = []
        self.current_river_cards = current_river_card
        for card in current_river_card:
            self.dealer.dropTargetCard(card)
        for id in range(1, self.NumberOfPlayers):
            p = Player(id)
            p.receiveCards(self.dealer.sendRandomCard(),
                           self.dealer.sendRandomCard())
            p.showCards()
            self.players.append(p)
        self.getRiverCards()
        
    def showRiverCards(self):
        str = 'River Cards include '
        if len(self.riverCards) == 0:
            PRINT('There is no cards on the table.', 1)
            return
        else:
            for card in self.riverCards:
                str += '{%2d%s} ' % (card.rank, card.suit)
            str += '\n'
            PRINT(str, 1)
#             print str

    def getRiverCards(self): 
        number_of_current_river_cards = len(self.current_river_cards)
        for i in range(5 - number_of_current_river_cards):
            self.riverCards.append(self.dealer.sendRandomCard())
#         self.showRiverCards()
        self.riverCards += self.current_river_cards
        return self.riverCards

    def wehterIAmGoingtoWin(self):
        myscore = self.me.getScore(self.riverCards)
        for player in self.players:
#             print player.playerID
#             print player.cards_inhand
            PRINT("Player %d" % player.playerID)
            if player.getScore(self.riverCards) > myscore:
                PRINT('I lost.')
                return False
        PRINT('I Win.')
        return True

        
if __name__ == "__main__":
    me = Player(0)
    me.receiveCards(Card(2, '+'), Card(3, '+'))
    game = Game(me=me, NumberOfPlayers=5)
    game.wehterIAmGoingtoWin()
