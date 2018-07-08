'''
Created on May 31, 2018

@author: siyuan
'''
# from util import Card
from Log import PRINT
from Dealer import Dealer
from Rules import Rules
# from Poker import Poker


class Player(object):
    '''
    classdocs
    '''

    def __init__(self, playerID):
        '''
        each player must have a ID (1~7)
        '''
        self.playerID = playerID
        self.cards_inhand = []

    def receiveCards(self, card1, card2):
        self.cards_inhand.append(card1)
        self.cards_inhand.append(card2)
        if len(self.cards_inhand) != 2:
            PRINT("The number of the cards must be 2.", 1)
            exit(-1)
    
    def showCards(self):
        PRINT("player %d has {%2d%s} and {%2d%s}." % (self.playerID,
                                                    self.cards_inhand[0].rank,
                                                    self.cards_inhand[0].suit,
                                                    self.cards_inhand[1].rank,
                                                    self.cards_inhand[1].suit))
    
    def getScore(self, riverCards):
        score = 0x0
        self.all_available_cards = riverCards + self.cards_inhand
#         print self.all_available_cards
        rule = Rules(self.all_available_cards)
        if rule.checkStraightFlush():
            return rule.getStraightFlushScore()
        if rule.checkFourOfAKind():
            return rule.getFourOfAKindScore()
        if rule.checkFullHouse():
            return rule.getFullHouseScore()
        if rule.checkFlush():
            return rule.getFlushScore()
        if rule.checkStaight():
            return rule.getStaightScore()
        if rule.checkThreeOfAKind():
            return rule.getThreeOfAKindScore()
        if rule.checkTwoPairs():
            return rule.getTwoPairsScore()
        if rule.checkAPair():
            return rule.getAPairScore()
        if rule.checkHighCard():
            return rule.getHighCardScore()
        PRINT("In getScore function, cannot find the right format. Wrong.", 1)
        exit(-1)


if __name__ == "__main__":
#     poker = Poker()
    dealer = Dealer()
    player1 = Player(1)
    player2 = Player(2)
    
    card1 = dealer.sendRandomCard()
    card2 = dealer.sendRandomCard()
    player1.receiveCards(card1, card2)
    card1 = dealer.sendRandomCard()
    card2 = dealer.sendRandomCard()
    player2.receiveCards(card1, card2)
    player1.showCards()
    player2.showCards()
