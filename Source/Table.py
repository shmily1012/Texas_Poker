'''
Created on Jun 3, 2018

@author: Alex
'''
from Calculate import Calculate
from Log import path
from util import Card

if __name__ == '__main__':
    ranks = [n for n in range(2, 15)]
    same_suit = ['+', '+']
    diff_suits = ['+', '-']
    number_of_players = 2
    
    fi = open('%stable.csv' % path, 'w')
    fi.write("Same Suit,")
    for rank in ranks:
        fi.write("%d," % rank)
    fi.write("\n")
    for card1 in ranks:
        fi.write('%d,' % card1)
        for card2 in ranks:
            if card1 == card2:
                str = 'N/A,'
            else:
                str = '%.3f,' % Calculate(number_of_players=number_of_players,
                                          mycardarray=[Card(card1, same_suit[0]), Card(card2, same_suit[1])],
                                          )
            fi.write('%s' % str)
        fi.write('\n')
    fi.write("Diff Suits,")
    for rank in ranks:
        fi.write("%d," % rank)
    fi.write("\n")
    for card1 in ranks:
        fi.write('%d,' % card1)
        for card2 in ranks:
            str = '%.3f,' % Calculate(number_of_players=number_of_players,
                                          mycardarray=[Card(card1, diff_suits[0]), Card(card2, diff_suits[1])],
                                          )
            fi.write('%s' % str)
        fi.write('\n')
    fi.close()
    pass
