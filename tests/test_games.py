import pytest 
from unittest import mock
import builtins
from Rock_Paper_Scissors.game import Game
from Rock_Paper_Scissors.Rock_Paper_Scissors import *

@pytest.fixture
def play():
    game=Game()
    return game

def test_str(play):
    actual =play.__str__()
    expected='you are in Rock paper scissors game'
    assert actual == expected
def test_rper(play):
    actual =play.__repr__()
    expected='Game'
    assert actual == expected

def test_result1(play):
    actual =play.result2('R','R')
    expected=0
    assert actual == expected
def test_result2(play):
    actual =play.result2('R','S')
    expected=10
    assert actual == expected
def test_result3(play):
    actual =play.result2('R','P')
    expected=-10
    assert actual == expected


def test_one(play):
    play.set_player(1)
    assert play.get_player()==1

def test_two(play):
    list=['R','S','P']
    assert play.random() in list

def test_three(play):
    list=[0,10,-10]
    assert play.result("R") in list

def test_four(play):
    assert play.result2("R","S")==10



## test in Rock_Paper_Scissors.py
def test_five():
    assert Welcoming()=="""
     ###########################################################################
                                                    
        Welcome to our Rock_Paper_Scissors game 

        The principle of this game is that the rock smashes the scissors 
        and the scissors cut the paper and the paper covers the rock
        Whoever makes the strongest move wins the game
        rock > scissors, scissors > paper, paper > rock

        This game requires two player and It consists of three rounds,
        and whoever gets the highest total wins the game

        Rock represent by "R"
        paper represent by "P"
        scissors represent by "S"

        You have to enter a character and then press the enter key.

        hint: you can play with computer or with your partner
    ##############################################################################
    """

# def test_function():
#     with mock.patch.object(builtins, 'input', lambda: ['walaa',"r","r","r"]):
#         assert tow_player(0) == "**** Draw *****"|f"***** {name} is Winner ********"|f"****** {name} you lost *********"