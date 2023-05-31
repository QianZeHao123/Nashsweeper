from flask import Blueprint
from .nashsweeper_core_engine.CoreCalcOptForGame import CoreCalc
import random
import numpy

bp = Blueprint('GetGameData', __name__, url_prefix='/api/GetGameData')


@bp.route('/')
def GetGamedata():
    NE_num = 0
    while NE_num == 0:
        test_strategy_matrix = [random.randint(0, 100) for _ in range(128)]
        strategy_matrix = test_strategy_matrix
        regP1, regP2 = CoreCalc.regCalc(strategy_matrix)
        # calculate the regret value of regP1 and regP2
        # print(regP1)
        # print(regP2)
        # output the nash equilibrium list and best response of player 1 and player 2
        NE, BRP1, BRP2 = CoreCalc.BRNElst(regP1, regP2)
        NE_num = len(NE)

    strategy_matrix = numpy.array(strategy_matrix).reshape(64, 2)
    strategy_matrix = strategy_matrix.tolist()

    print('strategy data:')
    print(strategy_matrix)
    print('Nash Equilibrium List: ')
    print(NE)
    print('Best Response of Player 1: ')
    print(BRP1)
    print('Best Response of Player 2: ')
    print(BRP2)

    GameData = {
        'Checkerboard': strategy_matrix,
        'NE': [int(_) for _ in NE],
        'BRP1': [int(_) for _ in BRP1],
        'BRP2': [int(_) for _ in BRP2]
    }
    # return test_strategy_matrix, NE, BRP1, BRP2
    return GameData
