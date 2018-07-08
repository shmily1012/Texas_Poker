'''
Created on Jun 1, 2018

@author: Alex
'''
from util import Card
from Log import PRINT
from Log import translate
from Game import Game
from Player import Player
import time
#############################################
Number_Of_Games = 1000
Number_Of_Players = 5
MyCard_1 = Card(14, '-')
MyCard_2 = Card(10, '-')
# CurrentRiverCards = [Card(2, '+'), Card(3, '-'), Card(4, '+'), Card(10, '/'), Card(6, '+')]
CurrentRiverCards = []
# CurrentRiverCards = []
#############################################


def Calculate(number_of_game=Number_Of_Games,
              number_of_players=Number_Of_Players,
              mycardarray=[MyCard_1, MyCard_2],
              current_river_cards=CurrentRiverCards):
    
    start_time = time.time()
    number_of_win_games = 0
    me = Player(0)
    me.receiveCards(mycardarray[0], mycardarray[1])
    parts_time = 0
    for i in range(number_of_game):
        game = Game(me=me, NumberOfPlayers=number_of_players, current_river_card=current_river_cards)
        sub_s_time = time.time()
        if game.wehterIAmGoingtoWin():
            number_of_win_games += 1
        sub_e_time = time.time()
        parts_time += (sub_e_time - sub_s_time)
    rate = (number_of_win_games * 100) / float(number_of_game) 
    
    end_time = time.time()
    time_percentage = (parts_time * 100) / (end_time - start_time)
    PRINT("FOR CARDs %s and %s within %d peoples, the win rate is %.3f Percent.[Calculation took %f seconds.]" % (
        translate(mycardarray[0]), translate(mycardarray[1]), number_of_players, rate, (end_time - start_time)), 3)
    PRINT("parts time is %.3f percent of whole time." % time_percentage, 1)
    return rate

if __name__ == '__main__':
#     for rank in range(2, 15):
#         MyCard_1 = Card(rank, '+')
#         MyCard_2 = Card(rank, '-')

    Calculate()