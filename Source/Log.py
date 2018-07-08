'''
Created on May 31, 2018

@author: Alex
'''
import time
from util import Card

debug_mode = 0
path = '../Log/'


def translate(card):
#         str_rank = ''
    str_suit = ''
    if card.rank < 11:
        str_rank = '%d' % card.rank
    elif card.rank == 11:
        str_rank = 'J'
    elif card.rank == 12:
        str_rank = 'Q'
    elif card.rank == 13:
        str_rank = 'K'
    elif card.rank == 14:
        str_rank = 'A'
    # spades,diamonds,clubs,hearts    
    if card.suit == '+':
        str_suit = 'spades'
    elif card.suit == '-':
        str_suit = 'diamonds'
    elif card.suit == '*':
        str_suit = 'clubs'
    elif card.suit == '/':
        str_suit = 'hearts'
    return "%2s(%s)" % (str_rank, str_suit)


class PRINT(object):
    '''
    classdocs
    '''
    filename = '../Log/game.log'

    def __init__(self, input, level=debug_mode):
        '''
        Constructor
        '''
        if level == 0:
            pass
        elif level == 1:
            print input
        elif level == 2:
            str = time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime())
            str += '%s\n' % input
            fi = open(self.filename, 'a')
            fi.write(str)
            fi.close()
        elif level == 3:
            print input
            str = time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime())
            str += '%s\n' % input
            fi = open(self.filename, 'a')
            fi.write(str)
            fi.close()


if __name__ == "__main__":
    PRINT("hello world!", 3)
