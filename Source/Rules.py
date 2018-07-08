'''
Created on May 31, 2018

@author: Alex
'''
from Dealer import Dealer
from Log import PRINT


class Rules(object):
    '''
    Ranking
    1. Straight Flush    2+3+4+5+6+
    2. Four of a Kind    2+2-2*2/3+
    3. Full House        2+2-2*3+3-
    4. Flush                2+5+8+9+10+
    5. Straight            2+3-4+5*6/
    6. Three of a Kind    2+2-2*4+5-
    7. Two Pairs            2+2-3+3*4/
    8. One Pair            2+2*4-5+7/
    9. High Card            2+3-7*8/13+
    
    '''
    full_staight_array_temp = [x for x in range(2, 15)]
    full_staight_array = sorted(full_staight_array_temp, reverse=True)
    full_staight_array.append(14)

    def __init__(self, allSevenCardsArray):
        '''
        Constructor
        '''
        self.cards = allSevenCardsArray
        if len(self.cards) != 7:
            PRINT("The total number of cards is wrong.", 1)
            exit(-1)

    def checkStraightFlush(self):
        '''
        #1
        '''
        results = False
        if self.checkFlush() == False:
            return False
#         print self.sorted_rank_array
        a = 0
        for j in range(4):
            
            if self.sorted_rank_array[a] - self.sorted_rank_array[a + 1] != 1:
                results = False
                break
            else:
                results = True
                a += 1
        if results == True:
            PRINT("This is Staight.")
        
        return results
        pass

    def getStraightFlushScore(self):
        score = 0x90000000
        score |= self.sorted_rank_array[0] << (4 * 5)

#         print 'score=0x%x' % score
        return score

    def checkFourOfAKind(self):
        '''
        #2
        '''
        results = False
        temp_rank_array = []
        for card in self.cards:
            temp_rank_array.append(card.rank)
        v = {x:temp_rank_array.count(x) for x in temp_rank_array}
#         print v
        rest_of_four_A_kind = []
        for key, value in v.iteritems():
            if value == 4:
                PRINT("This is Four Of a Kind.")
                self.value_of_four_of_a_kind = key   
                results = True
            else:
                rest_of_four_A_kind.append(key)
        if results == True:
            self.sorted_rest_of_four_A_kind = sorted(rest_of_four_A_kind, reverse=True)
        return results

    def getFourOfAKindScore(self):
        score = 0x80000000
        score |= self.value_of_four_of_a_kind << (5 * 4)
        score |= self.sorted_rest_of_four_A_kind[0] << (2 * 4)
#         print 'Score is 0x%x' % score
        return score

    def checkFullHouse(self):
        '''
        #3
        '''
        results = False
        temp_rank_array = []
        for card in self.cards:
            temp_rank_array.append(card.rank)
        v = {x:temp_rank_array.count(x) for x in temp_rank_array}
#         print v
        value_of_three_of_a_kind = []
        value_of_pairs = []
        value_of_singles = []
        for key, value in v.iteritems():
            if value == 4:
                results = False
                break
            if value == 3:
                value_of_three_of_a_kind.append(key)
            elif value == 2:
                value_of_pairs.append(key)
            else:    
                value_of_singles.append(key)
        if len(value_of_three_of_a_kind) == 1 and len(value_of_pairs) >= 1:
            results = True
        elif len(value_of_three_of_a_kind) == 2:
            results = True
        else:
            results = False
        if results == True:
            self.sorted_value_of_three_of_a_kind = sorted(value_of_three_of_a_kind, reverse=True)
            self.sorted_value_of_pairs = sorted(value_of_pairs, reverse=True)
        return results

    def getFullHouseScore(self):
        score = 0x70000000
        if len(self.sorted_value_of_three_of_a_kind) == 2:
            score |= self.sorted_value_of_three_of_a_kind[0] << (5 * 4)
            score |= self.sorted_value_of_three_of_a_kind[1] << (4 * 4)
        elif len(self.sorted_value_of_three_of_a_kind) == 1 and len(self.sorted_value_of_pairs) >= 1:
            score |= self.sorted_value_of_three_of_a_kind[0] << (5 * 4)
            score |= self.sorted_value_of_pairs[0] << (4 * 4) 
#         print 'Score is 0x%x' % score
        return score

    def checkFlush(self):
        '''
        #4
        '''
        results = False
        temp_array = []
        temp_rank_array = []
        
        for card in self.cards:
            temp_array.append(card.suit)
#         print temp_array
        
        d = {x:temp_array.count(x) for x in temp_array}
#         print d
        for key, value in d.iteritems():
            if value >= 5:
                PRINT("This is Flush!")
                self.flush_suit = key
                results = True
                break
        if results == True:
            for card in self.cards:
                if card.suit == self.flush_suit:
                    temp_rank_array.append(card.rank)
        
            self.sorted_rank_array = sorted(temp_rank_array, reverse=True)
#             print "self.sorted_rank_array=", self.sorted_rank_array
        return results        

    def getFlushScore(self):
        score = 0x60000000
        count = len(self.sorted_rank_array) - 1
#         print 'len=', len(self.sorted_rank_array)
        for rank in self.sorted_rank_array:
            hex_rank = hex(rank)
#             print '%s' % hex_rank
            score |= (int(hex_rank, 16) << (4 * count))
            count -= 1
#         print 'score=0x%x' % score
        return score

    def checkStaight(self):
        '''
        #5
        '''

        temp_array = []
#         temp_suits_array = []
        for card in self.cards:
            if card.rank not in temp_array:
                temp_array.append(card.rank)
        if len(temp_array) < 5:
            return False
        new_array = sorted(temp_array, reverse=True)
#         print 'new_array=', new_array
#         new_array = [13, 13, 12, 11, 10, 9, 7]
        for i in range(len(temp_array) - 5 + 1):
#             end = 7-3+i
            five_items = new_array[i: (7 - 3 + i + 1)]
            results = False
#             print 'five_items=', five_items
            a = 0
            for j in range(4):
                
                if five_items[a] - five_items[a + 1] != 1:
                    results = False
                    break
                else:
                    results = True
                    a += 1
                    
            if results == True:
                self.sorted_rank_array = five_items
                PRINT("This is Staight.")
#                 self.staight_suits_array = temp_suits_array
                break
        # One special Case 'A 2 3 4 5'
        if results == False:
#             print 'five_items=', five_items
            if new_array[0] == 14 and new_array[-1] == 2 and new_array[-2] == 3 and new_array[-3] == 4 and new_array[-4] == 5:
                self.sorted_rank_array = [5]
#                 print 'special Case'
                results = True
            
        return results

    def getStaightScore(self):
        score = 0x50000000
        score |= self.sorted_rank_array[0] << (4 * 3)

#         print 'score=0x%x' % score
        return score

    def checkThreeOfAKind(self):
        '''
        #6
        '''
        results = False
        temp_rank_array = []
        for card in self.cards:
            temp_rank_array.append(card.rank)
        v = {x:temp_rank_array.count(x) for x in temp_rank_array}
#         print v
        value_of_three_of_a_kind = []
        rest_of_three_of_a_kind = []
        for key, value in v.iteritems():
            if value == 3:
                PRINT("This is Three Of a Kind.")
#                 if self.value_of_three_of_a_kind < key:
                value_of_three_of_a_kind.append(key)
                results = True
            if value == 1:    
                rest_of_three_of_a_kind.append(key)
        if results == True:
            self.sorted_value_of_three_of_a_kind = sorted(value_of_three_of_a_kind, reverse=True)
            self.sorted_rest_of_three_of_a_kind = sorted(rest_of_three_of_a_kind, reverse=True)
        return results

    def getThreeOfAKindScore(self):
        score = 0x40000000
#         sorted_pair_value_array = sorted(self.pair_value_array, reverse=True)
        score |= self.sorted_value_of_three_of_a_kind[0] << (5 * 4)
        final_rest_of_three_of_a_kind = self.sorted_rest_of_three_of_a_kind[:2]
        count = len(final_rest_of_three_of_a_kind) - 1
#         print 'len=', len(self.sorted_rest_of_three_of_a_kind)
        for rank in final_rest_of_three_of_a_kind:
            hex_rank = hex(rank)
#             print '%s' % hex_rank
            score |= (int(hex_rank, 16) << (4 * count))
            count -= 1

#         print 'score=0x%x' % score
        return score

    def getNumberOfPairs(self):
        '''
        For CheckAPair() and CheckTwoPairs()
        '''
        temp_rank_array = []
        for card in self.cards:
            temp_rank_array.append(card.rank)
        v = {x:temp_rank_array.count(x) for x in temp_rank_array}
#         print v
        number_of_pairs = 0
        self.pair_value_array = []
        
        self.rank_rest_of_pair = []
        for key, value in v.iteritems():
            if value == 2:
#                 PRINT("This is Three Of a Kind.")
                number_of_pairs += 1
                self.pair_value_array.append(key)
            elif value == 1:
                self.rank_rest_of_pair.append(key)
        return number_of_pairs

    def checkTwoPairs(self):
        '''
        #7
        '''
        results = False
        if self.getNumberOfPairs() >= 2:
            results = True
        return results

    def getTwoPairsScore(self):
        score = 0x30000000
        sorted_pair_value_array = sorted(self.pair_value_array, reverse=True)
        score |= sorted_pair_value_array[0] << (5 * 4)
        score |= sorted_pair_value_array[1] << (4 * 4)
        
        self.sorted_rank_rest_of_pair = sorted(self.rank_rest_of_pair, reverse=True)
        hex_rank = hex(self.sorted_rank_rest_of_pair[0])
        score |= int(hex_rank, 16)
#         print 'Score is 0x%x' % score
        return score

    def checkAPair(self):
        '''
        #8
        '''
        results = False
        if self.getNumberOfPairs() == 1:
            results = True
        return results

    def getAPairScore(self):
        score = 0x20000000
        score |= self.pair_value_array[0] << (5 * 4)
#         print 'self.rank_rest_of_pair=', self.rank_rest_of_pair
        if len(self.rank_rest_of_pair) == 5:
            self.sorted_rank_rest_of_pair = sorted(self.rank_rest_of_pair, reverse=True)
            highest_three_cards = self.sorted_rank_rest_of_pair[:3]
            count = len(highest_three_cards) - 1

            for rank in highest_three_cards:
                hex_rank = hex(rank)
#                 print '%s' % hex_rank
                score |= (int(hex_rank, 16) << (4 * count))
                count -= 1
            pass
        else:
            PRINT('in getAPairScore, the len of rank_rest_of_pair is wrong', 1)
            exit(-1)
#         print 'Score is 0x%x' % score
        return score

    def checkHighCard(self):
        '''
        #9
        '''
        temp_rank_array = []
        for card in self.cards:
            temp_rank_array.append(card.rank)
        v = {x:temp_rank_array.count(x) for x in temp_rank_array}
#         print v
#         number_of_pairs = 0
        for key, value in v.iteritems():
            if value != 1:
                return False
        
        self.sorted_rank_array = sorted(temp_rank_array, reverse=True)
        self.sorted_final_cards = self.sorted_rank_array[:5]
        return True

    def getHighCardScore(self):
        score = 0x10000000
        count = 4
#         print 'len=', len(self.sorted_final_cards)
        for rank in self.sorted_final_cards:
            hex_rank = hex(rank)
#             print '%s' % hex_rank
            score |= (int(hex_rank, 16) << (4 * count))
            count -= 1

#         print 'score=0x%x' % score
        return score


if __name__ == "__main__":
    check = False
    while check == False:
        dealer = Dealer()
        cards = []
        for i in range(7):
            cards.append(dealer.sendRandomCard())
        rule = Rules(cards)
#         if rule.checkFlush():
#             check = rule.checkFlush
#             print 'Yes'
#         else:
#             print 'No'
#         check = rule.checkStaight()
        check = rule.checkStraightFlush()
    rule.getStraightFlushScore()
    
#     print rule.value_of_three_of_a_kind
#     print rule.pair_value_array
